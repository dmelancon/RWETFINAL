class NGramPOSCounter(object):

	  # parameter n is the 'order' (length) of the desired n-gram
	def __init__(self, n):
	    self.n = n
	    self.ngrams = dict()

	  # feed method calls tokenize to break the given string up into units
	def tokenize(self, text):
		text = text.strip()
		return text.split(" ")

	def feed(self, text):

	    tokens = self.tokenize(text)
	    for i in range(len(tokens) - self.n + 1):
	      gram = tuple(tokens[i:i+self.n])
	      if gram in self.ngrams:
	        self.ngrams[gram] += 1
	      else:
	        self.ngrams[gram] = 1

	def get_ngrams(self):
	    return self.ngrams
