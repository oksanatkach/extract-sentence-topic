from nltk import pos_tag, sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer


lm = WordNetLemmatizer()


def tokenize(doc):
    return sent_tokenize(doc)


def preprocess(sent):
    sent = word_tokenize(sent)
    sent = pos_tag(sent)
    sent = ('/'.join([lm.lemmatize(tpl[0].lower()), tpl[1]]) for tpl in sent)
    sent = ' '.join(sent)
    return sent
