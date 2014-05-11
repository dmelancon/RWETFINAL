import nltk
import random
class Rules(object):
	def __init__(self, ruleSet, seed):
		self.ruleSet =ruleSet
		self.seed = seed
	
	def checkRule(self):
		newSeed = str()
		for rule in self.ruleSet:
			if self.checkPOS() == rule:
				for i in range(len(self.ruleSet[rule])):
					newSeed +=self.ruleSet[rule][i]+' '
		return newSeed.strip()

	def checkPOS(self):
		return nltk.pos_tag(nltk.word_tokenize(self.seed))[0][1]


	def returnNewRule(self):
		newSeed = str()
		rulelist = self.seed
		for word in rulelist:
			for rule in self.ruleSet:
				if word == rule:
					for i in range(len(self.ruleSet[rule])):
						newSeed += " " + self.ruleSet[rule][i]	
		return newSeed.strip()

	def returnNewWord(self, corpus):
		sentence = str()
		for word in self.returnNewRule().split():
			for pos in corpus.keys():
				# return "word: "+ word + " pos:" + pos
				if word == pos:
					corpus[pos] = list(corpus[pos])
					sentence += random.choice(corpus[pos]) + " "
					break

		return sentence.strip()




			