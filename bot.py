#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import logging
import config as cfg
import tweepy


from telegram.ext import Updater
from telegram.ext import MessageHandler

# Enable logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler("telegram2twitter.log")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def make_twitter_api():
    auth = tweepy.OAuthHandler(cfg.tweeter["consumer_key"], cfg.tweeter["consumer_secret"])
    auth.set_access_token(cfg.tweeter["access_token"], cfg.tweeter["access_token_secret"])
    return tweepy.API(auth)


def slice_text(text):
    text = text[0:130]
    regs = [r"\n([^\n]*)$", r"\:\s([^:]*)$", r"\.\s([^.]*)$", r"\s([^\s]*)$"]

    for r in regs:
        text = re.sub(r, "", text)
        if len(text) < 130:
            break

    return text.strip() + "\n\n𝐑𝐞𝐚𝐝 𝐦𝐨𝐫𝐞:"


def tweet_post(id, text, username=None):
    channel = cfg.tg["channel"]
    twitter_api = make_twitter_api()
    if username is None or username == channel:
        link = "https://telegram.me/%s/%d " % (channel, id)
        post = "%s %s" % (slice_text(text), link)
        # print(tweet)
        try:
            twitter_api.update_status(post)
        except tweepy.TweepError as e:
            print(e.reason)


def tweet_post_update(bot, update):
    username = update.channel_post.chat.username
    id = update.channel_post.message_id
    text = update.channel_post.text
    tweet_post(id, text, username)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=cfg.tg["token"])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add message handler
    dp.add_handler(MessageHandler(None, tweet_post_update, channel_post_updates=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot# S
    updater.start_polling()
    logger.info("Bot started")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()