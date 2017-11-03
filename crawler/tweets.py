from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
from datetime import date, datetime
import time
# import dateutil.parser

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        # print obj.isoformat()
        # r = dateutil.parser.parse(obj.isoformat())
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

consumer_key="N4G6GT86uWNo7uQTfbRPvp5lZ"
consumer_secret="03Ed9nfUiAc5A7oLNZmzwpadZEUzUAOlPoZ3Z4sgfnwgJHhVBf"
access_token="146893662-w6kGYqUlgVVnOQopPMirpiTUjORIYAfVjGjdJr2M"
access_token_secret="XOOpHt1E20uW6nyQRlgb4LOxrrVrJB33CzYClUepSSds9"

class StdOutListener(StreamListener):
    def on_data(self, data):
        with open("data1.txt", "a") as myfile:
            myfile.write(data)
            print(data)
        return True

    def on_error(self, status):
        print("ERROR")
        print(status)
        if status == 420:
            return False

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
    for follower in limit_handled(tweepy.Cursor(api.followers).items()):
        if follower.friends_count < 300:
            print follower.screen_name

# if __name__ == '__main__':
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     myStream = tweepy.Stream(auth, l)
#     myStream.filter(track=['$NVDA', '$AMD', 'nvidia', 'amd'])

if __name__ == '__main__':
    # Maximum number of tweets we want to collect
    maxTweets = 1000000

    # The twitter Search API allows up to 100 tweets per query
    tweetsPerQry = 100

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    # api.rate_limit_status()['resources']['search']

    filename = "data/tweets" + time.strftime("%Y%m%d-%H%M%S") + ".txt"

    with open(filename, "a") as myfile:
        for tweet in limit_handled(tweepy.Cursor(api.search, q='"nvda"', lang="en", rpp=tweetsPerQry, result_type="recent").items(maxTweets)):
            res = {}
            res["text"] = tweet.text
            res["id"] = tweet.id
            res["date"] = tweet.created_at
            r = json.dumps(res, default=json_serial)
            print r
            myfile.write(json.dumps(res, default=json_serial))
