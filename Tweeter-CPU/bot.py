import tweepy
import time
import credentials

auth=tweepy.OAuthHandler(credentials.a1,credentials.a2)

auth.set_access_token(credentials.b1,credentials.b2)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()
api=tweepy.API(auth)

# print(user)
myfile=open('verne.txt','r')
file_lines=myfile.readlines()
myfile.close()
count=0
filenames = ['1.jpeg']
media_ids = []
for filename in filenames:
     res = api.media_upload(filename)
     media_ids.append(res.media_id)

for line in file_lines:
    try:
        print(line)
        if line != '\n':
            api.update_status(line,media_ids=media_ids)
            print("Sucess " + str(count+1))
            time.sleep(60)
        else:
            print('unsucess')
    except tweepy.error.TweepError as e:
        print(e)
    # print(user.screen_name)
