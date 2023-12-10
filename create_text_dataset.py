




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
from csv import writer
import csv



delimiter = "------------------------------\n"
array = []
section = ""
index = 0
numpyArray = np.array([['1','label']])
#header = ['1','label']



f = open("./mvd.txt/mvd.txt")
lines = f.readlines()
for line in lines:
    if line != delimiter:
        prev = line 
        section += line
    else:   
        if index == 0:
            array.append(['Index','1','label'])
        array.append([index,section,int(prev)])
        section = ""
        if index % 10000 == 0:
            if len(array) > 0:
                with open('text_dataset.csv', 'a', newline='') as file:
                    print("🚀 ~ file: 1.py:56 ~ index:", index)
                    print(len(array))
                    writer = csv.writer(file)
                    writer.writerows(array)
            array = []
        index+=1
        

# header = [str(i+1) for i in  range(50)]
# header.append('label')


#pd.DataFrame(numpyArray[1:]).to_csv('text_dataset.csv', index_label = "Index", header  = header)  

