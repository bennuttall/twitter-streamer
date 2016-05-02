# Twitter Streamer

How to use TwythonStreamer to take action when a particular term is tweeted.

## Install

Open a Terminal window and enter the following:

```bash
sudo pip3 install twython
sudo pip install twython
```

## API keys

Get your API keys from [apps.twitter.com](https://apps.twitter.com/) (full instructions in [Tweeting Babbage](https://www.raspberrypi.org/learning/tweeting-babbage/worksheet/))

## Python Code

```python
from twython import TwythonStreamer

consumer_key        = 'ABCDEFGHIJKLKMNOPQRSTUVWXYZ'
consumer_secret     = '1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ'
access_token        = 'ZYXWVUTSRQPONMLKJIHFEDCBA'
access_token_secret = '0987654321ZYXWVUTSRQPONMLKJIHFEDCBA'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
term = "#yolo"
stream.statuses.filter(track=term)
```
