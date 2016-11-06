from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as tf
from sklearn.naive_bayes import MultinomialNB as NB

class dankMemeClassifier():
	def __init__(self, labels_train, data_train):
		names = open(data_train).read()
		
		
		namesList = names.split('|')
		
		self.count_vect = CV(input=u'content')
		train_counts = self.count_vect.fit_transform(namesList)
		self.transformer = tf(use_idf = False).fit(train_counts)
		

		tfidf = self.transformer.fit_transform(train_counts)


		a = open(labels_train).read()
		lb = a.split(',')
		
		lb = lb[:len(lb)-1]

		self.clf = NB().fit(tfidf,lb)
	
	def classify(self, newpoint):
		new = self.count_vect.transform(newpoint)
		new_tfidf = self.transformer.transform(new)
		pred = self.clf.predict(new_tfidf)
		return pred


c = dankMemeClassifier('training_labels.txt','training_points.txt')

print c.classify(['the'])
