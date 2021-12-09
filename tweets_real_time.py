import tweepy
import json
import credentials



class Tweets_Listener(tweepy.StreamListener):

    def on_conect(self):
        print("En líena")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print("Error", status_code)


auth = tweepy.OAuthHandler(credentials.API_Key, credentials.API_Secret_Key)
auth.set_access_token(credentials.Acces_token, credentials.Acces_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = Tweets_Listener()
streaming_Api = tweepy.Stream(auth=api.auth, listener=stream)

streaming_Api.filter(
    #Sirve para seguir cuentas especificas
    #follow=[""]
    #Para Trackear palabras clave
    track=["Tabacundo"]
    #Para filtrar por ubicacion usar https://boundingbox.klokantech.com CSVRaw
    #locations=[-80.9740173817,-5.0365472107,-75.3490173817,1.6364188301]
)