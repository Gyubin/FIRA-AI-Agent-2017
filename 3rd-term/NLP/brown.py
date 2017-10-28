# 18. Read in some text from a corpus, tokenize it, and print the list of all wh-word types that occur. (wh-words in English are used in questions, relative clauses and exclamations: who, which, what, and so on.) Print them in order. Are any words duplicated in this list, because of the presence of case distinctions or punctuation?

import re
from nltk.corpus import brown

REGEX = re.compile('^wh', re.IGNORECASE)

wh_words = set([])
for genre in brown.categories():
    for word in brown.words(categories=genre):
        if REGEX.match(word):
            wh_words.add(word.lower())

print('==========')
print('Ex18 words : {}\n'.format(len(wh_words)))
print(wh_words)

# 25. Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay.  http://en.wikipedia.org/wiki/Pig_Latin

# + Write a function to convert a word to Pig Latin.
# + Write code that converts text, instead of individual words.
# + Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).

def pig_latinize_word(word):
    word = list(word)
    result = []
    back = []
    while len(word):
        c = word[0]
        if c in 'aeiou':
            result.extend(word)
            result.extend(back)
            break
        else:
            back.append(word.pop(0))
    return ''.join(result) + 'ay'

def pig_latinize_text(text):
    text = text.split(' ')
    text = map(pig_latinize_word, text)
    return ' '.join(text)

text = 'You can find an excellent introduction to regular experssoins at this site'
result = pig_latinize_text(text)
print('\n==========')
print("Ex28 test: {}".format(result))

