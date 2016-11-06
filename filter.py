from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as tf
from sklearn.naive_bayes import MultinomialNB as NB
from sklearn.neural_network import MLPClassifier as MLP



class dankMemeClassifier():
	def __init__(self, labels_train, data_train):
		names = open(data_train).read()
		
		
		namesList = names.split('|')
		for data in namesList:
			data.strip('\n')
		self.count_vect = CV(input=u'content')
		train_counts = self.count_vect.fit_transform(namesList)
		self.transformer = tf(use_idf = False).fit(train_counts)
		
	
		tfidf = self.transformer.fit_transform(train_counts)
	
	
		a = open(labels_train).read()
		lb = a.split(',')
		
		lb = lb[:len(lb)-1]
	
		self.clf = MLP().fit(tfidf,lb)
		
		
	def classify(self, newpoints):
		names = open(newpoints).read()
		namesList = names.split('|')
			
		finout = []
		
		of = open('out.txt', 'w')
		
		i = 0
		while i < len(namesList) -2:
			s = namesList[i] + '|' +  namesList[i+1] +'|'+ namesList[i+2]
			finout.append(s)
			i+=3
			
	
		almostthere = []
		for data in namesList:
			if not data[:4] == 'http':
				almostthere.append(data)
		del namesList[:]
		i = 0
		while i < len(almostthere) - 1:
			namesList.append(almostthere[i] + ' ' + almostthere[i+1])
			i+=2

		new = self.count_vect.transform(namesList)
		new_tfidf = self.transformer.transform(new)
		pred = self.clf.predict(new_tfidf)
		i = 0
		while i < len(finout)-1:	
			s = finout[i] + '|' + pred[i]
			of.write(s)
			of.write('\n')
			i +=1


c = dankMemeClassifier('training_labels.txt','training_points.txt')

print c.classify('articles.txt')
