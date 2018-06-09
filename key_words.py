from nltk import RegexpParser, tag, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# Su Nam Kim Paper
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = RegexpParser(grammar)


def parse(text):
    return chunker.parse(
        tag.pos_tag(
            word_tokenize(text)
        ))


def leaves(tree):
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        yield subtree.leaves()


def normalise(word):
    # Normalises words to lowercase and lemmatizes it.
    return lemmatizer.lemmatize(word.lower())


def acceptable_word(word):
    # Checks conditions for acceptable word: length, stopword.
    return bool(2 <= len(word) <= 40
                and word.lower() not in stopwords)


def get_terms(tree):
    for leaf in leaves(tree):
        for term in [normalise(w) for w, t in leaf if acceptable_word(w)]:
            yield term


def get_keywords(sent):
    return get_terms(parse(sent))
