from twython import TwythonStreamer


appKey=""
appSecret=""
oauthToken=""
oauthTSecret=""

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)

stream = MyStreamer(appKey,appSecret,oauthToken,oauthTSecret)

stream.statuses.filter(track = '#websummit')