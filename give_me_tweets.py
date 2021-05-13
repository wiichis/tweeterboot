import credentials
import tweepy
import schedule

auth = tweepy.OAuthHandler(credentials.API_Key, credentials.API_Secret_Key)
auth.set_access_token(credentials.Acces_token, credentials.Acces_token_secret)

api = tweepy.API(auth)

# #Para imprimir tu timeline en consola
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*60}')

def get_tweets():
    id = None
    count = 0
    while count <= 1000:
        tweets = api.search(q='#Bitcoin', lang='es', tweet_mode='extended', max_id=id)
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
    
def run():
    get_tweets()

if __name__=='__main__':
    schedule.every(6).minutes.do(run)
    

    while True:
        schedule.run_pending()