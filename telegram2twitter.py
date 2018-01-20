#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import logging
import settings as cfg
import tweepy


from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

# Enable logging
logging.basicConfig(filename="telegram_bot.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def make_twitter_api():
    auth = tweepy.OAuthHandler(cfg.twitter["consumer_key"], cfg.twitter["consumer_secret"])
    auth.set_access_token(cfg.twitter["access_token"], cfg.twitter["access_token_secret"])
    return tweepy.API(auth)


def slice_text(text):
    text = text[0:130]
    regs = [r"\n([^\n]*)$", r"\:\s([^:]*)$", r"\.\s([^.]*)$", r"\s([^\s]*)$"]

    for r in regs:
        text = re.sub(r, "", text)
        if len(text) < 130:
            break

    return text.strip() + "\n\nRead more:"


def tweet_post(id, text, username=None):
    channel = cfg.telegram["channel"]
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
    updater = Updater(token=cfg.telegram["token"])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text, tweet_post_update, channel_post_updates=True))

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