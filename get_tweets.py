

# #Obtener mi información
# data = api.me()
# print (json.dumps(data._json, indent=2))

# #Obtener información de otro usuario
# data = api.get_user("nike")
# print (json.dumps(data._json, indent=2))

#Obtener los followers de un usuario
# data = api.followers(screen_name="nike")
# print (len(data))
# for user inrm data:
#     print (json.dumps(user._json, indent=2))

# #Cursos en una clase de tweepy que me permite obtener mas elemenos sin paginacion
# for user in tweepy.Cursor(api.followers, screen_name="nike").items(100):
#     print (json.dumps(user._json, indent=2))

# #Llamando a los friends
# for user in tweepy.Cursor(api.friends, screen_name="nike").items(100):
#     print (json.dumps(user._json, indent=2))

# #Obtener un Timeline
# for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(1):
#     print (json.dumps(tweet._json, indent=2))

# # Buscar Tweets
# for tweet in tweepy.Cursor(api.search, q="mundial de clubes", tweet_mode="extended").items(10):
#     #print (json.dumps(tweet._json, indent=2))    #Imprimir el objeto compelto
#     print (json.dumps(tweet._json["full_text"]))  #Imprimir solo el texto del tweet

#Publicar en Twitter
#api.update_status("Hi Tweepy")

#Retuitear un Tweet
#Necesitamos tener el id del tweet, se puede sacar desde la pagina de twitter.
# utimo_tweet_id = '1393983995998883841'
# api.retweet(utimo_tweet_id)

# #Dar like a un tweet
# data = api.me()
# json_data = json.dumps(data._json, indent=4)
# id_las_tweet = data._json['status']['id']
# print(id_las_tweet)

# api.create_favorite(id_las_tweet)
# api.destroy_favorite(id_las_tweet) #Quitar like

# #Reply Tweet
# data = api.me()
# # json_data = json.dumps(data._json, indent=4)
# id_las_tweet = data._json['status']['id']
# print(id_las_tweet)
# api.update_status("hi there", in_reply_to_status_id=id_las_tweet)

# #Twittear fotos
# #primero subimos la imagen a twitter
# data_img = api.media_upload("./picture.jpg")
# print (data_img)

# #Luego posteamos la id de la foto con id status
# api.update_status("foto", media_ids=[""])

 #Seguir a una cuenta
# api.create_friendship("nike")
# #Dejar de Seguir a una cuenta
# api.destroy_friendship("nike")
# #Bloquear
# api.create_blok("nike")
# #Desbloquear
# api.destroy_block("nike")