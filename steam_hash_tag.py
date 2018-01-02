# -*- coding: utf-8 -*-
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from config import *


class StdOutListener(StreamListener):
    """
    A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, raw_data):
        """
        :param raw_data: json data
        """
        raw_data = json.loads(raw_data)
        twitter_text = raw_data.get('text')
        print(twitter_text)

    def on_error(self, status):
        print(status)


def _run_as_standalone_script():
    """Runs program as standalone script."""
    track_hash_tag(hash_tag="bitcoin")


def track_hash_tag(hash_tag):
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, listener)
    stream.filter(track=hash_tag)


if __name__ == '__main__':
    _run_as_standalone_script()

