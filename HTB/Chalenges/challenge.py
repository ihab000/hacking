import re, hashlib, requests
p = re.compile("<h3 align='center'>(.*)</h3>")
url = "http://docker.hackthebox.eu:32832/"
s = requests.Session()
while True:
    r = s.get(url)
    md5 = hashlib.md5(str.encode(p.search(r.text).group(1))).hexdigest()
    data = {'hash':md5}
    r = s.post(url,data)
    print(r.text)
