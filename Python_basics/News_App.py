import requests
import json
import time
def Yesterday_Date():
    date = time.strftime("%Y-%m-%d")
    ystrd_date = int(date[8:]) - 1
    if ystrd_date < 10:
        return f'{date[:8]}0{str(ystrd_date)}'
    else:
        return f'{date[:8]}{str(ystrd_date)}'
date = Yesterday_Date()
while True:
    query = input("What type of news are you interested in?\n")
    url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-02&sortBy=publishedAt&apiKey=b908fc2d6f254587939f492e7e033371"
    r = requests.get(url)
    dic = json.loads(r.text)
    articles = dic['articles']
    print(f"Here are some news related to {query.capitalize()} published on {date}")
    for index, article in enumerate(articles, start = 1):
        if article['publishedAt'].startswith(date):
            print(f"{index} - {article['title']}")
        else:
            break
    answer = input(f'''If you are interested in seeing some other types of news
Press 1
If not
Press 0\n''')
    if answer == '0':
        break
#answer = input('''If you want to know more about the above mentioned news
#Press the number before that news or 0 to exit : - ''')
#print(answer)
#for i, article in enumerate(articles, start = 1):
#    if answer == 0:
#        break
#    elif article['publishedAt'].startswith(date) and answer == i:
#        print(f'''This news is published by {article['source']['name']}and its author is {article['author']}
#        {article['description']}
#        For more information you can just visit {article['url']}''')
#    else:
#        break
