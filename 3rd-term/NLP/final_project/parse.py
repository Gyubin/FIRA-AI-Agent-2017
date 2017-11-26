from konlpy.tag import Mecab
import numpy as np

import os
import re


def save_sentences(file_name, mecab):
    print(f"Start processing { file_name }.txt", end="")
    with open(f'./data/news/{ file_name }.txt', 'r') as f:
        lines = f.read()

        # '최순실', '새누리당' 단어가 고유명사로 인식되지 않아서 vocab에 없는 단어로 대체
        # '새정치xxx'는 '새정치민주연합', '새정치연합' 등 다양하게 불러서 모두 한 단어로 대체
        lines = re.sub('최순실', '규빈', lines)
        lines = re.sub('새누리당', '완재', lines)
        lines = re.sub('(새정치.*?) ', '혜민스님 ', lines)
        lines = lines.split('.')
        lines = list(map(lambda x: mecab.morphs(x), lines))

        lines = np.array(lines)
        np.save(f'./data/news/{ file_name }.npy', lines)

        print(f" --- Complete!")


def main():
    mecab = Mecab()
    target_files = filter(lambda x: re.search(r'\.txt$', x), os.listdir('./data/news'))
    for news_name in target_files:
        news_name = news_name[:-4]
        if not os.path.exists(f'./data/news/{ news_name }.npy'):
            save_sentences(news_name, mecab)

if __name__ == "__main__":
    main()
