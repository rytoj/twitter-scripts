from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from config import *


class StdOutListener(StreamListener):
    def __init__(self, debug=False):
        self.debug = debug

    def on_data(self, raw_json):
        decoded_json = json.loads(raw_json)
        retweeted = decoded_json.get('is_quote_status')
        reply = decoded_json.get('in_reply_to_screen_name')
        user = decoded_json.get('user').get('name')
        user_id = decoded_json.get('user').get('id_str')
        if self.debug:
            if retweeted:
                print("Retweet...")
                print("User: {}".format(user))
                print(decoded_json.get('text'))
                print(decoded_json.get('filter_level'))
                print("-----------")
            if reply:
                print("Reply...")
                print("User: {}".format(user))
                print(decoded_json.get('text'))
                print(decoded_json.get('filter_level'))
                print("-----------")
            if user_id in FOLLOW_IDS:
                print("!!!!!!ORIGINAL!!!!!!!!")
                print("User: {}".format(user))
                print(decoded_json.get('text'))
                print(decoded_json.get('filter_level'))
                print("-----------")
        else:
            if user_id in FOLLOW_IDS:
                print("User: {}".format(user))
                print(decoded_json.get('text'))
                print("-----------")
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener(debug=False)
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, l)
    stream.filter(follow=["254853566"])
