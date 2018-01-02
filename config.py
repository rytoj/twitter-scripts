# -*- coding: utf-8 -*-
import json
import os
tw_consumer_key = "TWITTER_CONSUMER_KEY"
tw_consumer_secret = "TWITTER_CONSUMER_SECRET"
tw_access_token = "TWITTER_ACCESS_KEY"
tw_access_token_secret = "TWITTER_ACCESS_SECRET"
twitter_user_id = "TWITTER_FOLLOW_IDS"

try:
    CONSUMER_KEY = os.environ[tw_consumer_key]
    CONSUMER_SECRET = os.environ[tw_consumer_secret]
    ACCESS_KEY = os.environ[tw_access_token]
    ACCESS_SECRET = os.environ[tw_access_token_secret]
    FOLLOW_IDS = os.environ[twitter_user_id]
except KeyError:
    with open("config.json") as f:
        keys = json.load(f)
        CONSUMER_KEY = keys[tw_consumer_key]
        CONSUMER_SECRET = keys[tw_consumer_secret]
        ACCESS_KEY = keys[tw_access_token]
        ACCESS_SECRET = keys[tw_access_token_secret]
        FOLLOW_IDS = keys[twitter_user_id]