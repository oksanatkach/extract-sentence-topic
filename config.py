import gensim
import os


DIR = os.path.abspath('GoogleNews-vectors-negative300.bin')


def load_gensim_model():
    model = gensim.models.KeyedVectors.load_word2vec_format(DIR, binary=True)
    model.init_sims(replace=True)
    return model
