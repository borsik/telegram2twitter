# Telegram2Twitter

Simple telegram bot for tweeting channel posts


### Prerequsites
First, you'll need a Telegram Bot Token, you can get it via @BotFather ([more info here](https://core.telegram.org/bots)).

Also, setting this up will need an Application-only authentication token from Twitter ([more info here](https://dev.twitter.com/oauth/application-only)). Optionally, you can provide a user access token and secret.

You can get this by creating a Twitter App [here](https://apps.twitter.com/).

Bear in mind that if you don't have added a mobile phone to your Twitter account you'll get this:

>You must add your mobile phone to your Twitter profile before creating an application. Please read https://support.twitter.com/articles/110250-adding-your-mobile-number-to-your-account-via-web for more information.

For client.py you need to obtain api_hash, api_id and phone, more [here](https://my.telegram.org/auth). Don't forget to set start and end dates


### Installing

```
# clone this thing
# create your virtualenv, activate it, etc
# virtualenv -p python3 venv
# . venv/bin/activate
pip install -r requirements.txt
# fill config.py (see prerequisites)
python bot.py
```


### Based on

- [python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot)
- [tweepy](https://github.com/tweepy/tweepy)
- [Telethon](https://github.com/LonamiWebs/Telethon)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Innopolis University
* My mama
* And my dealer

If you find some bugs or monkey code, feel free to create an issue