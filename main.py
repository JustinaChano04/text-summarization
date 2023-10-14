import requests
import json
import config


if __name__ == "__main__":
    method = "post"
    url = "http://eventregistry.org/api/v1/article/getArticles"
    headers = {
        'Content-Type': 'application/json',
    }
    body = {
        "keyword": "Finance, Market, Technology",
        "articleCount": 5,
        "apiKey": config.api_key
    }

    r = requests.request(method, url, headers=headers, data=json.dumps(body))
    if r.status_code == 200:
        x = r.json()
        print(x)
        with open('response.json', 'w') as outf:
            json.dump(x, outf)


   