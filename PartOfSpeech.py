import nltk
class PartOfSpeech(object):
		def __init__(self, sentence):
			self.sentence = sentence
		def returnPOS(self):   
			token = nltk.word_tokenize(self.sentence)
			PartOfSpeech = str()
			#return token
			for i in nltk.pos_tag(token):
				PartOfSpeech += i[1]+' '
			return PartOfSpeech

		def returnToken(self):
			token = nltk.word_tokenize(self.sentence)
			TokenWords =list()
			for i in nltk.pos_tag(token):
				TokenWords.append(i[0])
			return TokenWords

		def returnPOSDict(self):
			token = nltk.word_tokenize(self.sentence)
			POSDict = dict()
			for i in nltk.pos_tag(token):
				if i[1] not in POSDict:
					POSDict[i[1]] = set()
				POSDict[i[1]].add(i[0])
			return POSDict

		def checkPOS(self, word):
			return nltk.pos_tag(nltk.word_tokenize(word))[0][1]
