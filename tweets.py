from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

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

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    myStream = tweepy.Stream(auth, l)
    myStream.filter(track=['$NVDA', '$AMD', 'nvidia', 'amd'])

# if __name__ == '__main__':
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth)
#     results = api.search(q="NVDA")
#     for r in results:
#         print("-----------------------")
#         print(r.text)
#     print("-----------------------")