import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        self.positives = []
        with open('positive-words.txt') as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith(';'):
                    self.positives.append(line.rstrip('\n'))
                    
        self.negatives = []
        with open('negative-words.txt') as g:
            lines = g.readlines()
            for line in lines:
                if not line.startswith(';'):
                    self.negatives.append(line.rstrip('\n'))

    def analyze(self, text):
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0
        for word in tokens:
            word = word.lower()
            if word in self.positives:
                score+=1
            elif word in self.negatives:
                score-=1
            else:
                score = score
            
        return score
