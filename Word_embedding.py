
# f = open("./mvd.txt/mvd.txt")
# lines = f.readlines()
# for line in lines:
#     print(line)

# exit()




import numpy as np
import gensim
from gensim.models import word2vec
from gensim.models.word2vec import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import string
import gensim.downloader as api

wv = api.load('glove-twitter-50')
def sent_vec(sent):
    vector_size = wv.vector_size
    wv_res = np.zeros(vector_size)
    ctr = 1
    for w in sent:
        if w in wv:
            ctr += 1
            wv_res += wv[w]
    wv_res = wv_res/ctr
    return wv_res




delimiter = "------------------------------\n"
array = []
section = ""
index = 0


f = open("./mvd.txt/mvd.txt")
lines = f.readlines()
for line in lines:
    if line != delimiter:
        prev = line 
        section += line 
    else:   
        temp = (sent_vec(section))
        temp = np.append(temp,int(prev))
        array.append(temp)
        section = ""
        index+=1
        print("🚀 ~ file: 1.py:56 ~ index:", index)
        


numpyArray = np.array(array)
header = [str(i+1) for i in  range(50)]
header.append('label')


pd.DataFrame(numpyArray).to_csv('sample.csv', index_label = "Index", header  = header)  

