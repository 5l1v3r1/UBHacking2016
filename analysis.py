import json
import nltk
import meme

class Analysis:
	m = meme.Meme()
	
	def fits_blb(self, title):#returns 0 or 1 for which type of blb it fits
		tagged = nltk.pos_tag(nltk.word_tokenize(title))
		for i in range(len(tagged)-3):
			if (tagged[0][1].find('VB') != -1 or tagged[0][1].find('NNS') != -1)and (tagged[1][1].find('DT') != -1 or tagged[1][1].find('NN')!= -1 or tagged[1][1].find('TO') != -1 ) and tagged[2][1].find('NN') != -1:
				return 0
				#0 indicates it fits the verb first form			
#			if tagged[0][1].find 	#implement this if i care at some point
		return -1
							
				
	def blb_top_bottom(self, title):
		print("in top bot")
		if self.fits_blb(title) == 0: #if it fits blb verb first form
			top = title[0] + title[1] + title[2] + title[3]
			i = 4
			bottom = ""
			while i < len(title):
				bottom = bottom + title[i]
#		if self.fits_blb(title) == 1: #do this?
			return [top, bottom]
		
		return -1
		
				
	def gen_memes(self):
		blb = []
		#make a list of each type of meme. list contains urls 
		with open("out.txt", "r") as f:
			for line in f:
				print(line.split('|')[3].strip())
				if line.split('|')[3].strip().find('BLB') != -1: #.find workedkedked
					top_bottom = self.blb_top_bottom(line.split('|')[0])
					blb.append(m.gen_meme(m.meme_to_id("bad luck brian"), top_bottom[0], top_bottom[1]).json()['data']['url'])
		return blb
									
