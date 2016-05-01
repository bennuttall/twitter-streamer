from twython import TwythonStreamer

# Twitter application authentication
consumer_key        = 'ABCDEFGHIJKLKMNOPQRSTUVWXYZ'
consumer_secret     = '1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ'
access_token        = 'ZYXWVUTSRQPONMLKJIHFEDCBA'
access_token_secret = '0987654321ZYXWVUTSRQPONMLKJIHFEDCBA'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data)

# Create streamer
stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
term = "#yolo"
stream.statuses.filter(track=term)
