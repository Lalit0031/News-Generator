import requests
import json

url = "https://free-news.p.rapidapi.com/v1/search"

# taking input from user
input_value = input("Enter topic of News you wants to Know : ")
querystring = {"q": input_value, "lang": "en"}

# using news api for getting news
headers = {
    'x-rapidapi-host': "free-news.p.rapidapi.com",
    'x-rapidapi-key': "eda1fe6afbmshe91568662693b5fp14f531jsn20ce82f2552e"
}

# Requesting api to give us the required news
response = requests.request("GET", url, headers=headers, params=querystring)

data = response.text

parsed = json.loads(data)
adic = parsed["articles"]
i = 0
j = 0

# finding of max index
try:
    while 1:
        if adic[i] is not None:
            i += 1
        else:
            break
except:
    pass

# printing list item by item
while j < i:
    # converting list to dictionary
    sdic = dict(adic[j])
    print(j + 1, ") ", json.dumps(sdic["summary"], indent=4), "\n")
    j += 1
