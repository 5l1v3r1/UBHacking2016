from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as tf
from sklearn.naive_bayes import MultinomialNB as NB

names = open('articles.txt').read()

namesList = names.split('\n')


namesList = namesList[:len(namesList)-1]

count_vect = CV(input=u'content')

train_counts = count_vect.fit_transform(namesList)


#returns a matrix based on the file

transformer = tf(use_idf = False).fit(train_counts)


tfidf = transformer.fit_transform(train_counts)




#tfidf = transformer.transform(train_counts)


a = open('training_labels.txt').read()

labels_train = a.split(',')

clf = NB().fit(tfidf,labels_train)


docs = ['A South Korean Man Adopted by Americans Prepares for Deportation']

new = count_vect.transform(docs)

new_tfidf = transformer.transform(new)

pred = clf.predict(new_tfidf)

print pred
