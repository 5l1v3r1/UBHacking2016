import requests
import json
import nltk

class Meme:

	base = "https://api.imgflip.com/"

	def meme_to_id(self, meme_name):
		response = requests.get(self.base + "get_memes").json()
#		if response['success']  check if success is true
		for meme in response['data']['memes']:
			if (meme['name'].lower()).find(meme_name.lower()) != -1:
				return meme['id']
		return "you fucked up"	


	def gen_meme(self, meme_id, top, bottom):
		parameters = {
				'template_id': meme_id,
				'username': 'ubhacking2016',
				'password': 'ubhacking2016',
				'text0': top, #top text for meme
				'text1': bottom, #bottom text for meme
#				self.meme_to_id(meme	
				}
		response = requests.post(self.base + "caption_image", params=parameters)
		return response

#	def words_to_types(self, input):
			

#	def title_to_meme(self, title):
		#split title into action and reaction. Action top, reaction bottom
		
#	def gen_tree():
#		tokens = nltk.word_tokenize
#		kk
	
	def sentence_to_tree(self, sentence):
		tokenized = nltk.word_tokenize(sentence)
		tagged = nltk.pos_tag(tokenized)
		
		grammar = r"""
			NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
			PP: {<IN><NP>}               # Chunk prepositions followed by NP
			VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
			CLAUSE: {<NP><VP>}           # Chunk NP, VP
			"""
		template_shit = nltk.RegexpParser(grammar)
		response = template_shit.parse(tagged)
		print(response)
		return response
		
		
		
