import requests

session1 = requests.session()

# login
response = session1.get(url="https://httpbin.org/cookies/set?foo=bar", allow_redirects=False)
print(response.cookies.get_dict())
