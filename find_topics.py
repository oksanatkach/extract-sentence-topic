from key_words import get_keywords
from config import load_gensim_model
import operator
from syntactic_analysis import preprocess, tokenize
import re
from regex import TOPICS


MODEL = load_gensim_model()


def get_topics(sentences):

    def find_topic(preproc):
        dict = {}
        for topic in TOPICS:
            n = len([re.match(var, preproc) for var in TOPICS[topic] if re.match(var, preproc) is not None])
            if n > 0:
                dict[topic] = n

        return dict

    return [find_topic(preprocess(sent)) for sent in sentences]


def rules(doc):

    sentences = tokenize(doc)
    results = get_topics(sentences)

    final = []

    def distance(sent0, sent1):
        return MODEL.wv.wmdistance(
            # list()?
            get_keywords(sent0),
            get_keywords(sent1)
        )

    def best_topic(topics):
        best = max(topics.iteritems(), key=operator.itemgetter(1))[0]
        if topics[best] == 1 and best in final:
            topics.pop(best)
            return check_length(topics, i)
        else:
            return best

    def check_length(topics, i):
        if len(topics) > 1:
            return best_topic(topics)

        elif len(topics) == 0:
            main_sent = sentences[i]
            sentences[i] = ''
            scores = [distance(main_sent, current_sent) for current_sent in sentences]
            check_length(results[scores.index(max(scores))], i)

        else:
            return topics.keys()[0]

    for i in xrange(len(results)):
        topics = results[i]
        final.append(check_length(topics, i))

    return final
