import credentials
import tweepy

auth = tweepy.OAuthHandler(credentials.API_Key, credentials.API_Secret_Key)
auth.set_access_token(credentials.Acces_token, credentials.Acces_token_secret)

api = tweepy.API(auth)

# #Para imprimir tu timeline en consola
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*60}')

id = None
count = 0
while count <= 3000:
    tweets = api.search(q='#CoheteChino', lang='es', tweet_mode='extended', max_id=id)
    for tweet in tweets:
        if tweet.full_text.startswith('RT'):
            count += 1
            continue
        f = open('./data_tweets.txt', 'a', encoding='utf-8')
        f.write(tweet.full_text + '\n')
        f.close
        count += 1
    id = tweet.id
    print(count)