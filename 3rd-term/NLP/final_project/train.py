from gensim.models import Word2Vec
import numpy as np
import os, re, argparse

DATA_PATH = '/news/'
FILE_NAMES = ['chosun_full', 'donga_full', 'hani_full', 'joongang_full', 'kh_full']

def train():
    # Load all preprocessed data.
    newspapers = []
    for f in FILE_NAMES:
        f_path = DATA_PATH + f + '.npy'
        if os.path.exists(f_path):
            tmp = np.load(f_path)
            newspapers.append(tmp)

    # Train model.
    for sg in [0, 1]:
        for size in [100, 300, 500]:
            for iter in [10, 20]:
                tr_type = 'sg' if sg else 'cbow'
                model_path = f'./wordvectors_{ tr_type }_{ size }_{ iter }'

                index = 0
                if os.path.exists(model_path):
                    model = Word2Vec.load(model_path)
                else:
                    model = Word2Vec(newspapers[index], size=size, window=5, min_count=5, workers=4, iter=iter, sg=sg)
                    index += 1

                while index < 5:
                    model.train(newspapers[index], total_examples=model.corpus_count, epochs=model.iter)
                    index += 1

                model.save(model_path)
                print(f"Complete training { tr_type }-{ size }-{ iter }-model")



if __name__=="__main__":
    train()
