# Find the first repeated word in a string
'''
Input : "Ravi had been saying that he had been there"
Output : had

Input : "Ravi had been saying that"
Output : No Repetition

Input : "he had had he"
Output : he
'''

def getResult(input):
    word_freq = {}
    for word in input.split(' '):
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    for word in word_freq:
        if word_freq[word] > 1:
            return word
    return 'No Repetition'

print(getResult('Ravi had been saying that he had been there'))
from collections import Counter
print(Counter('Ravi had been saying that he had been there'.split(' ')))