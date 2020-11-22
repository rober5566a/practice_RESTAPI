import requests
import json

if __name__ == "__main__":
    resouce = requests.get(
        'https://api.stackexchange.com//2.2/questions?order=desc&sort=activity&site=stackoverflow')
    # print(resouce.json()['items'])

    for questions in resouce.json()['items']:
        if questions['answer_count'] == 0:
            print(questions['title'])
            print(questions['link'])
        else:
            print("skipped")
