
CONTRACTIONS = {
                 "aren't": "are not / am not", "can't": "cannot", "could've": "could have",
                 "couldn't": "could not", "didn't": "did not", "doesn't": "does not",
                 "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",
                 "he'd": "he had / he would", "he'll": "he will", "he's": "he has / he is",
                 "how'd": "how did", "how's": "how is", "I'd": "I had / I would", "I'll": "I will",
                 "I'm": "I am", "I've": "I have", "isn't": "is not", "it'll": "it shall / it will",
                 "it's": "it has / it is", "let's": "let us", "ma'am": "madam", "might've": "might have",
                 "must've": "must have", "mustn't": "must not", "needn't": "need not", "oughtn't": "ought not",
                 "she'd": "she had / she would","she'll": "she will", "she's": "she has / she is", "should've":
                     "should have", "shouldn't": "should not", "that'd": "that would / that had",
                 "that's": "that has / that is", "there'd": "there had / there would",
                 "there's": "there has / there is", "they'd": "they had / they would",
                 "they'll": "they will", "they're": "they are", "they've": "they have",
                 "to've": "to have", "wasn't": "was not", "we'd": "we had / we would",
                 "we'll": "we will", "we're": "we are", "we've": "we have", "weren't": "were not",
                 "what'll": "what will", "what're": "what are", "what's": "what has / what is",
                 "what've": "what have", "when's": "when has / when is", "where'd": "where did",
                 "where's": "where has / where is", "where've": "where have", "who'll": "who will",
                 "who's": "who has / who is", "who've": "who have", "why's": "why has / why is",
                 "why've": "why have", "won't": "will not", "would've": "would have",
                 "wouldn't": "would not", "y'all": "you all", "you'd": "you had / you would",
                 "you'll": "you shall / you will", "you're": "you are", "you've": "you have",
                 "gonna": "going to", "daren't": "dare not", "everyone's": "everyone is"

                }


def _get_contractions():
    return CONTRACTIONS


def get_reverse_contractions():
    reverse_contraction_dict = dict()

    for key, value in CONTRACTIONS.items():

        if '/' in value:
            value = value.split(' / ')
        else:
            value = [value]

        for full_word in value:
            reverse_contraction_dict[full_word] = key

    return reverse_contraction_dict

