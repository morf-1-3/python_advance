#ecercise 1
#exercise 2
#exercise 3
#exercise 4
# import urllib
# import urllib.request
# import requests
# import os

# PATH = os.path.abspath(__file__+"/..")
# PATH_FILE = PATH + "/site.html"


# URL = "https://rozetka.com.ua/"
# # text = requests.request("GET",URL).text
# # print(PATH_FILE)


# # with open(PATH_FILE,"w",encoding="utf-8") as file:
# #     file.write(text)


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# }
# request = urllib.request.Request(URL,headers = headers)

# response = urllib.request.urlopen(request)

# text = response.read().decode("utf-8")
# with open(PATH_FILE,"w",encoding="utf-8") as file:
#     file.write(text)


#Exercise 5

import urllib
import urllib.request

import requests
import os
import json

URL = "https://jsonplaceholder.typicode.com/posts/1"
PATH = os.path.abspath(__file__+"/..")
PATH_FILE = PATH + "/site.html"
data = json.dumps({
    "userId": 10,
    "id": 99,
    "title": "hi",
    "body": "by"
  }).encode("utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# # data = urllib.parse.urlencode({"key1": "value1", "key2": "value2"}).encode("utf-8")
# request = urllib.request.Request(URL,headers=headers,method="POST")
# response = urllib.request.urlopen(request,data=data)
# # text =response.read().decode("utf-8")
# text =response.getcode()
# print(text)
response = requests.request("PUT",URL,data=data)
print(response)




