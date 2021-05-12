exclude_words= ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'al', 'del', 'lo', 'le',
                'y', 'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con',
                'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 
                'estoy', 'voy', 'porque', 'he', 'son', 'solo', 'tengo', 'muy', '.', '-', 
                '|', 'd', 'no', 'si', 'yo', 'ha', "?"]


top_words = []

top_words = {}
tweet_topic = open('./data_tweets.txt', encoding='utf-8')
for line in tweet_topic:
    words = line.strip().lower().split()
    for word in words:
        if word not in exclude_words:
            top_words[word] = top_words.get(word, 0) + 1

most_used_words = sorted(top_words, key=top_words.get, reverse=True)

count_u = 0
for word in most_used_words:
    if count_u < 10 and word.startswith('@'):
        print(top_words[word], word)
        count_u += 1

print('*'*40)

count = 0
for word in most_used_words:
    if count < 30:
        print(top_words[word], word)
        count += 1