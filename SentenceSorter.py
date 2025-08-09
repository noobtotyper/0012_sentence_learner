from math import log,e

# Can be changed to other file for other language
# word_to_freq is a dict like {"ich":1,"ist":2,...}
with open("de_full.txt","r") as f:
    words=[line.split()[0] for line in f.readlines()]
word_to_freq={word:rank+1 for rank,word in enumerate(words)}

# Can be changed to other file for other language
# sentences is just a list of sentences.
with open("deu_sentences.tsv","r") as f:
    sentences=[line.split("\t")[2].rstrip() for line in f.readlines()]

def to_words(sentence:str):
    """Separates into words in lowercase. Removes numbers and symbols
    Input: 'Lass uns etwas versuchen!'
    Output: ['lass', 'uns', 'etwas', 'versuchen'] """
    lower=sentence.lower()
    words=[]
    word=[]
    for idx in range(len(lower)):
        # Checking where the word ends
        if lower[idx].isalpha():
            word.append(lower[idx])
        # Add to list when word finished
        else:
            if len(word)>0:
                words.append("".join(word))
                word=[]
    # If the sentence ends in an alphanumeric symbol
    if len(word)>0:
        words.append("".join(word))
        word=[]
    return words
    
def score(sentence):
    clean_sentence=to_words(sentence)
    if len(clean_sentence)==0:
        return 1
    # I take the geometric mean. Since numbers are large, I use logarithms.
    score=0
    for word in clean_sentence:
        score+=log(word_to_freq.get(word,99_999))
    return e**(score/len(clean_sentence))
    
sentences_with_score=[(sentence,score(sentence)) for sentence in sentences]
sentences_with_score.sort(key=lambda x : x[1])
for sentence,sco in sentences_with_score:
    #print(sco,sentence)
    print(sentence)