import datetime
from bot import tweet_post
import config as cfg
from telethon import TelegramClient
import time


def main():
    client = TelegramClient(cfg.tg['channel'], cfg.tg['api_id'], cfg.tg['api_hash'])
    client.connect()
    delay = cfg.util['delay']

    # Ensure you're authorized
    if not client.is_user_authorized():
        client.send_code_request(cfg.tg['phone'])
        client.sign_in(cfg.tg['phone'], input('Enter the code: '))

    channel = client.get_entity(cfg.tg['channel'])

    start_time = datetime.datetime.strptime(cfg.util['start'], cfg.util['format'])
    end_time = datetime.datetime.strptime(cfg.util['end'], cfg.util['format'])

    messages = client.get_message_history(channel, offset_date=end_time)
    sended_posts = []
    with open('sended_posts.txt', 'r') as file:
        sended_posts = file.read().splitlines()
    for message in messages:
        if message.date > start_time and str(message.id) not in sended_posts:
            try:
                #tweet_post(message.id, message.message)
                with open('sended_posts.txt', 'a') as file:
                    file.write(str(message.id) + '\n')
                time.sleep(delay)
            except AttributeError:
                print("no attribute")

if __name__ == '__main__':
    main()