from twython import Twython
import json

appKey=""
appSecret=""
oauthToken=""
oauthTSecret=""



twitter = Twython(appKey,appSecret,oauthToken,oauthTSecret)

timeline = twitter.get_home_timeline()

#print json.dumps(timeline)

data  = twitter.search(q='#websummit', result_type='mixed',count=100)

statuses = data['statuses']

for post in statuses:
	print post['id_str'] + ':' + post['text']

print len(data['statuses'])