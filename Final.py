import sys
import random
from NGramPOSCounter import NGramPOSCounter
from PartOfSpeech import PartOfSpeech
from Rules import Rules
nGramValue = int(sys.argv[1])
####this file creates parts of speech NGRAM rules
mFile = sys.argv[2]
#####this file creates the corpus 
mFile2 = sys.argv[3]
# seed = sys.argv[4]
text = open(mFile)

#create NGram object and feed in the parts of speech in order from the text
mNGram = NGramPOSCounter(nGramValue)
for line in text:
	mPos = PartOfSpeech(line)
	mNGram.feed(mPos.returnPOS())

#create a dictionary of the POS NGRAMS that have over 4 options
ngrams = mNGram.get_ngrams()
mGrams = dict()
for ngram in ngrams.keys():
	count = ngrams[ngram]
	if count > 4:
		mGrams[ngram] = count

# #create a selection of rules	
allRule = dict()
for mGram in mGrams:
	if mGram[0] not in allRule:
		allRule[mGram[0]] = []
	allRule[mGram[0]].append(tuple(mGram[:]))
#create a dictionary of unique words paired with their parts of speech
text = open(mFile2)
corpus = dict()
seed = str()
for line in text:
	mPos = PartOfSpeech(line)
	for i in mPos.returnPOSDict():
		if i not in corpus:
			corpus[i] = set()
		corpus[i] |= mPos.returnPOSDict()[i]
# corpus = {'PRP$': set(['their', 'his', 'her', 'our', 'my', 'your']), 'VBD': set(['shut', 'bent', 'ran', 'made', 'picked', 'put', 'saw', 'said', 'did', 'had', 'tame', 'looked', 'fell', 'were', 'got', 'went', 'was', 'sank', 'came', 'gave']), 'VBN': set(['gone', 'shut', 'bed', 'wet', 'fun', 'come', 'asked', 'red']), 'VBP': set(['do', 'play', 'run', 'want', 'do.\xe2\x80\x9d', 'are', 'have', 'fall', 'hear', 'sat', 'pink', 'like', 'wish', 'stand', 'call', 'take', 'hop', 'mother', 'let', 'tell', 'bet', 'know']), 'WDT': set(['what', 'that', 'That']), 'JJ': set(['\xe2\x80\x9cPut', 'kite', '\xe2\x80\x9cHow', 'sad', 'high', 'dish', '\xe2\x80\x9cNow', 'cold', 'rid', 'that.\xe2\x80\x9d', 'funny', 'little', 'toy', 'top', '\xe2\x80\x9cHave', 'fast', 'wet', 'new', 'white', 'fish', '\xe2\x80\x9cWhy', 'good', '\xe2\x80\x9cWith', 'big', '\xe2\x80\x9cOh', '\xe2\x80\x9cThese', '\xe2\x80\x9cThat', '\xe2\x80\x9cLook', 'net', '\xe2\x80\x9cYour', 'last', '\xe2\x80\x9cThey', '\xe2\x80\x9cDid', 'fun.\xe2\x80\x9d', 'cat', 'bad', 'tall']), 'WP': set(['what', 'Who', 'What']), 'VBZ': set(['is', 'has', 'tricks', 'kites']), 'DT': set(['all', 'that', 'some', 'ALL', 'no', 'another', 'The', 'any', 'those', 'a', 'All', 'That', 'these', 'No', 'this', 'Another', 'the', 'Those']), 'RP': set(['down', 'out', 'up', 'UP']), 'NN': set(['gown', 'wall', 'tip', 'pot', 'go', 'fear', 'milk', 'toy', 'cup', 'tail', 'wood', 'call', 'way', 'wet', 'hat', 'head', 'good', 'string', 'get', 'rake', 'game', 'fan', 'bit', 'day', 'me', 'kind', 'look', 'cat', 'trick', 'cake', 'went', 'pack', 'bump', 'house', 'fish', 'shame', 'something', 'dear', 'home', 'ship', 'said', 'sun', 'fox', 'book', 'red', 'ball', 'mat', 'mess', 'hand', 'fun', 'lot', 'Things.\xe2\x80\x9d', 'nothing', 'kit', 'man', 'box', '\xe2\x80\x9d', 'mother', 'shook', 'came']), ',': set([',']), '.': set(['!', '?', '.']), 'TO': set(['to', 'To']), 'PRP': set(['we', 'I', 'it', 'them', 'She', 'they', 'YOU', 'him', 'he', 'me', 'We', 'her', 'It', 'us', 'she', 'They', 'you', 'You', 'He']), 'RB': set(['then', 'back', 'here', 'NOT', 'as', 'So', 'not', 'now', 'yet', 'fly', 'Then', 'little', 'NOW', 'always', 'away', 'there', 'fast', 'so', 'too', 'Not', 'Now', 'Sally']), ':': set(['...', '\xe2\x80\x9d']), 'NNS': set(['dots', 'kinds', 'Things', 'jumps', 'bumps', 'books', 'hands', 'kicks', 'playthings', 'thumps', 'lots', 'things', 'tricks', 'hops', 'games', 'kites', 'strings']), 'NNP': set(['BOX', 'no.', 'THEN', 'hat.', 'What', 'down.', 'Hat', 'up.', 'We', 'Would', '\xe2\x80\x9cTake', '\xe2\x80\x9cYou', 'Hat.', 'Not', 'Now', 'it.', 'On', 'Oh', 'look.', 'Cat', 'hook.', 'She', 'Mother', 'about.', 'Came', '\xe2\x80\x9cNo', 'all.', 'tame.', 'Saw', 'Two.', 'A', 'new.', 'her.', 'rake.', 'me.', 'house.', 'Fast', 'Should', 'away.', 'FUN', 'pat.', 'come.', 'That', '\xe2\x80\x9cMy', 'day.', 'Put', 'how.', 'Sally', 'He', '\xe2\x80\x9cDo', '\xe2\x80\x9cWhy', 'Look', 'This', '\xe2\x80\x9cThis', 'Thing', '\xe2\x80\x9cThat', 'say.', 'Sank', 'things.', 'Bump', 'UP', 'stop.', 'here.', 'NOT', 'play.', 'out.', 'dear.', 'Yes.', 'Said', 'Her', '\xe2\x80\x9cI', 'too.', 'Things', 'Make', 'There', 'Two', '\xe2\x80\x9cA', 'Too', 'Thump', 'two.', 'now.', 'Sit', 'Think', 'sunny.', 'ball.', 'you.', 'box.', 'BUMP', 'Well', 'So', 'Then', 'red.', 'hands.', 'cake.', 'And', 'bit.', 'PLOP', 'How', 'cat.', 'SHOULD', 'Down', 'pot.', 'Those', 'Our', 'Your', 'DO', 'hall.', 'net.', '\xe2\x80\x9d', 'tricks.', 'To', 'fall.', '\xe2\x80\x9cNow', 'You', 'Tell', 'Do', '\xe2\x80\x9cIn', 'do.', '\xe2\x80\x9cHave', 'bet.', 'Did', 'They', 'With', 'These', '\xe2\x80\x9cWith', 'shine.', 'I', 'Will', 'fast.', 'IN', 'The', 'fish.', '\xe2\x80\x9cSo', '\xe2\x80\x9cThey', 'fish.\xe2\x80\x9dHe', 'It', 'bow.', 'fear.', 'lit.', 'Have', 'In', 'not.', 'If']), 'VB': set(['want', 'show', 'bump', 'mind', 'deep', 'jump', 'see', 'have', 'shake', 'go', 'find', 'sit', 'bite', 'give', 'hop', 'do', 'play', 'hit', 'get', 'step', 'hear', 'know', 'fall', 'be', 'hold', 'like', 'fan', 'look', 'wish', 'say', 'pick', 'let']), 'WRB': set(['When', 'when', 'Why']), 'CC': set(['And', 'and', '\xe2\x80\x9cBut', 'But']), 'PDT': set(['ALL']), 'CD': set(['one', 'TWO', 'two', 'One']), '-NONE-': set(['Mother\xe2\x80\x99s', 'day.\xe2\x80\x9d', '\xe2\x80\x9cSo']), 'EX': set(['there']), 'IN': set(['On', 'For', 'that', 'into', 'after', 'down', 'as', 'As', 'at', 'in', 'with', 'out', 'on', 'about', 'from', 'like', 'of', 'up', 'near', 'At', 'In', 'if', 'With', 'If']), 'MD': set(['will', 'can', 'would', 'could', 'should', 'SHOULD'])}
# realRules ={'MD': ('MD', 'VB', 'RP'), 'VB': ('VB', 'RP', 'DT'), 'RB': ('RB', 'VB', 'PRP'), 'NN': ('NN', ',', 'CC'), 'VBD': ('VBD', ',', 'JJ'), 'CC': ('CC', 'NNP', 'NNP'), ',': (',', 'PRP', 'VBP'), '.': ('.', 'NNP', '.'), 'TO': ('TO', 'NNP', 'NNP'), 'VBP': ('VBP', 'RB', 'VB'), 'PRP': ('PRP', 'VBP', 'RB'), 'JJ': ('JJ', 'IN', 'DT'), 'IN': ('IN', 'PRP$', 'NN'), 'VBZ': ('VBZ', 'RB', 'DT'), 'DT': ('DT', 'NN', 'IN'), ':': (':', 'NNP', 'DT'), 'NNP': ('NNP', '.', 'NNP')}
#narrow it down to one rule per part of speech and match each rule set to a word set
realRules = dict()
for rule in allRule:
	realRules[rule] = random.choice(allRule[rule])
matchRules =dict()
for rules in realRules:
	t = list()
	for rule in realRules[rules]:
		corpus[rule] = list(corpus[rule])
		t.append(random.choice(corpus[rule]))
	l = list()
 	l = [realRules[rules], t]	
 	matchRules[rules] = l 



firstWord = next(iter(corpus[random.choice(corpus.keys())]))
mRule = Rules(realRules, firstWord)
mPos = PartOfSpeech(mRule)
newRule =[mPos.checkPOS(firstWord)]
print firstWord
print newRule
newDict = list()
t = firstWord, newRule
newDict.append(t)
newSentence= list()
for rule in newRule:
	for rules in matchRules:
		if rules == rule:
			for word in matchRules[rules][1]:
				newSentence.append(word)
newSentence[0] = firstWord
final = str()
for x in newSentence:
	final+=x+' '
print final.strip()	

for x in range(5):
	mRule = Rules(realRules, newRule)
	newRule = mRule.returnNewRule()
	tempRule = list()
	for rule in newRule.split():
		tempRule.append(rule)
	newRule = tempRule
	print newRule
	newSentence= list()
	for rule in newRule:
		for rules in matchRules:
			if rules == rule:
				for word in matchRules[rules][1]:
					newSentence.append(word)
	newSentence[0] = firstWord
	final = str()
	for x in newSentence:
		final+=x+' '
	print final.strip()	

