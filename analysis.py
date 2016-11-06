import json
import nltk
import meme

class Analysis:
	m = meme.Meme()
	
	def tag_titles(self):
		titles = []
		with open("out.txt", "r") as f:
			for line in f:
				titles.append(line.split('|')[0])
		for i in range(len(titles)):
			title = nltk.pos_tag(nltk.word_tokenize(titles[i]))
			titles[i]=title
		return titles

	def is_possible_blb(self, titles):
		fit_the_template_start_verb = []
		fit_the_template_start_noun = []
		for i in range(len(titles)):
		#	for word in titles[i]:
			for j in range(len(titles[i])-3):
				#first one handles if an action is first. they are sometimes internpreted as NNS
				#measurements of time like all or A are expressed as DDT
	#pattern 1: first:( vb || nns ) second:( dt || nn || toi
				if (titles[i][j][1].find('VB') != -1 or titles[i][j][1].find('NNS') != -1)and (titles[i][j+1][1].find('DT') != -1 or titles[i][j+1][1].find('NN')!= -1 or titles[i][j+1][1].find('TO') != -1 ) and titles[i][j+2][1].find('NN'):
					print("fuuuck")
					fit_the_template_start_verb.append(titles[i][j][0])
				if titles[i][j][1].find(' '): #write the criteria for the one that starts with noun here	
					fit_the_template_start_noun.append(titles[i][j][0])
	if evans output is badluckbrian and line is stored as templine 
	def fits_blb(self, title):
		tagged = nltk.pos_tag(nltk.word_tokenize(title))
		for i in range(len(tagged)-3):
			
			
							
	def out_txt_fits_blb(self): # outputs 
		memes = []
		
		tagged = self.tag_titles()
				
		

	
