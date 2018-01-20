import datetime
from telegram2twitter import tweet_post
import settings as cfg
from telethon import TelegramClient
import time
from telethon.errors import SessionPasswordNeededError
from getpass import getpass
import logging


logging.basicConfig(filename="telegram_bot.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    logger.info("Client started")
    client = TelegramClient(cfg.telegram['channel'], cfg.telegram['api_id'], cfg.telegram['api_hash'])
    client.connect()
    delay = cfg.util['delay']

    # Ensure you're authorized
    if not client.is_user_authorized():
        try:
            client.send_code_request(cfg.telegram['phone'])
            client.sign_in(cfg.telegram['phone'], input('Enter the code: '))
        # Two-step verification may be enabled
        except SessionPasswordNeededError:
            pw = getpass('Two step verification is enabled. '
                         'Please enter your password: ')
            client.sign_in(password=pw)

    channel = client.get_entity(cfg.telegram['channel'])

    start_time = datetime.datetime.strptime(cfg.util['start'], cfg.util['format'])
    end_time = datetime.datetime.strptime(cfg.util['end'], cfg.util['format'])

    messages = client.get_message_history(channel, offset_date=end_time)
    with open('sended_posts.txt', 'r') as file:
        sended_posts = file.read().splitlines()
    for message in messages:
        if message.date > start_time and str(message.id) not in sended_posts:
            try:
                tweet_post(message.id, message.message)
                logger.info("Tweet with message_id " + message.id + "sent")
                with open('sended_posts.txt', 'a') as file:
                    file.write(str(message.id) + '\n')
                time.sleep(delay)
            except AttributeError:
                logger.error("Message with id " + message.id + " has no message attribute")
    logger.info("Client finished")

if __name__ == '__main__':
    main()