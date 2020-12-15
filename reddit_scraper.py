import praw
from psaw import PushshiftAPI
import pandas as pd

user_agent = "python:twoHorrorStory:v1.0 (by u/savaldesr)"
r = praw.Reddit(...)
api = PushshiftAPI(r)

gen = api.search_submissions(subreddit='Showerthoughts', filter=['title', 'selftext', 'score'], score='>1000')
results = []
for subm in gen:
    if subm.selftext != '[removed]' and subm.over_18 is False:
        results.append({'title': subm.title, 'score': subm.score})

df = pd.DataFrame(results)
df['title'].str.encode('ascii', 'ignore').str.decode('ascii')
df = df['title']
df = df.sample(frac=1)
df.reset_index()
df.to_json('showerthoughts1.json', orient='values')
