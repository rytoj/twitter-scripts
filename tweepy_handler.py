# -*- coding: utf-8 -*-

import tweepy

from config import *


class Twitter:
    def __init__(self):
        # create an OAuthHandler instance
        # Twitter requires all requests to use OAuth for authentication
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        # Construct the API instance
        self.api = tweepy.API(self.auth)  # create an API object

    def print_followers(self, username):
        """
        Print all followers
        :param username: Username
        :return: get list of username followers
        """
        followers = _get_usernames(user=username, api=self.api)
        for follower in followers:
            print(follower)

    def print_tweets(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

    def user_info(self, username):
        """
        :param username: twitter user name
        :return: twitter user object
        """
        user_data = self.api.get_user(username)
        print("User screen name: {}".format(user_data.screen_name))
        print("Follower count: {}".format(user_data.followers_count))

    def search_by_hash(self, tag, items=10):
        """
        Get selected hash tags, by default display 10 items
        :param tag: tag to search
        :param items: items to display
        :return: print elements
        """
        print("Number of tweets extracted: {}.\n".format(items))
        for tweet in tweepy.Cursor(self.api.search, q=tag).items(items):
            print('Tweet by: @{} \n{}\n-------'.format(tweet.user.screen_name, tweet.text))


def _get_usernames(user, api):
    """
    :param api: twitter API instance
    :param user: Username
    :return: get yield of username followers
    """
    user = api.get_user(user)
    for friend in user.friends():
        yield friend.screen_name


def _run_as_standalone_script():
    """Runs program as standalone script."""

    twitter = Twitter()
    # twitter.print_followers('La1kas')
    # twitter.user_info('La1kas')
    # twitter.print_tweets()
    twitter.search_by_hash(tag="bitcoin")


if __name__ == '__main__':
    _run_as_standalone_script()
