# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 准备训练集，测试集
import re
import jieba


def clean_str(string):
    # strings = re.sub(r"[A-Za-z0-9()（）、【】/\,，；。+：！?？:“”\"\-_!\[\]?$|.!;\'\`]", " ", string)
    strings = re.sub(r'[^\u4e00-\u9fa5]', " ", string)
    string = ''.join(strings.split())
    return string.strip()


def stop_word_list():
    stopwords = [line.strip() for line in open('../data/stopwords.txt', encoding='utf-8').readlines()]
    return stopwords


def seg_depart(sentence):
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stop_word_list()
    outstr = ''
    for word in sentence_depart:
        print(word)
        if word not in stopwords:
            outstr += word
            print(outstr)
            outstr += " "
    return outstr


# def movestopwords(sentence):
#     stopwords = stop_word_list('../data/stopwords.txt')  # 加载停用词的路径
#     words = [x for x in sentence if x not in stopwords]
#     return words


# fw_train = open('../data/train_input.txt', 'w', encoding='utf-8')
fw_test = open('../data/level2/all_data_level2_over_2000_clean.txt', 'w', encoding='utf-8')
with open('../data/level2/all_data_level2_over_2000.txt', 'r', encoding='utf-8') as train_data:
    lines = train_data.readlines()
    # jieba.load_userdict(dir+'dict.txt')
    for line in lines:
        line = line.strip().split('\t')
        if len(line) >= 2:
            clean_string = clean_str(line[0])
            # cut_string = jieba.lcut(clean_string)
            # cut_strings = movestopwords(clean_string)
            cut_string = seg_depart(clean_string)
            print(cut_string)
            if len(cut_string):
                # content = ' '.join(cut_string)
                content = cut_string
                # print(content+'\t__label__'+line[1])
                result = content + '\t__label__' + line[1]
                # fw_train.write(result+'\n')
                fw_test.write(result + '\n')

# fw_train.close()
fw_test.close()
