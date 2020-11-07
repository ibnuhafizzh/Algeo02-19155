#PROGRAM SIMILARITAS

import numpy as np
import math
from numpy.core.fromnumeric import sort
from numpy.core.multiarray import dot
from numpy.core.records import array
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

#Baca file & Stemming
a = open("doc1.txt", "r")
df1 = a.read()
textstem = stemmer.stem(df1)

b = open("doc2.txt", "r")
df2 = b.read()
textstem2 = stemmer.stem(df2)

c = open("doc3.txt", "r")
df3 = c.read()
textstem3 = stemmer.stem(df3)

d = open("doc4.txt", "r")
df4 = d.read()
textstem4 = stemmer.stem(df4)

e = open("doc5.txt", "r")
df5 = e.read()
textstem5 = stemmer.stem(df5)

f = open("doc6.txt", "r")
df6 = f.read()
textstem6 = stemmer.stem(df6)

g = open("doc7.txt", "r")
df7 = g.read()
textstem7 = stemmer.stem(df7)

h = open("doc8.txt", "r")
df8 = h.read()
textstem8 = stemmer.stem(df8)

i = open("doc9.txt", "r")
df9 = i.read()
textstem9 = stemmer.stem(df9)

j = open("doc10.txt", "r")
df10 = j.read()
textstem10 = stemmer.stem(df10)

k = open("doc11.txt", "r")
df11 = k.read()
textstem11 = stemmer.stem(df11)

l = open("doc12.txt", "r")
df12 = l.read()
textstem12 = stemmer.stem(df12)

m = open("doc13.txt", "r")
df13 = m.read()
textstem13 = stemmer.stem(df13)

n = open("doc14.txt", "r")
df14 = n.read()
textstem14 = stemmer.stem(df14)

o = open("doc15.txt", "r")
df15 = o.read()
textstem15 = stemmer.stem(df15)

doc = [textstem, textstem2, textstem3, textstem4, textstem5, textstem6, textstem7, textstem8, textstem9, textstem10, textstem11, textstem12, textstem13, textstem14, textstem15]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(doc) #vektor dokumen

print("\nKata-kata yang ada pada dokumen : ")
array_of_words = vectorizer.get_feature_names() #kata2 pada dokumen
print(array_of_words)
print("\n")

print ("Vektor Dokumen :")
matrix_of_words = X.toarray()
print(matrix_of_words) #vektor dokumen dlm array
print("\n")
# matrix_or_words [0][i] adalah elemen vektor doc 1, matrix_or_words [1][i] adalah elemen vektor doc 2, matrix_or_words [2][i] adalah elemen vektor doc 3, 

query = str(input("Search : "))
query_vec = vectorizer.transform([query]) #vektor query
matrix_of_query = query_vec.toarray() 

print("\n")
print("Query :", query)
print("Vektor Query : ")
print(query_vec.toarray())
print("\n")
# matrix_or_query [0][i] adalah elemen vektor query

dot_1 = 0
dot_2 = 0
dot_3 = 0
dot_4 = 0
dot_5 = 0
dot_6 = 0
dot_7 = 0
dot_8 = 0
dot_9 = 0
dot_10 = 0
dot_11 = 0
dot_12 = 0
dot_13 = 0
dot_14 = 0
dot_15 = 0

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0
sum11 = 0
sum12 = 0
sum13 = 0
sum14 = 0
sum15 = 0

sumq = 0

for i in range (len(array_of_words)):
    dot_1 += matrix_of_query[0][i]*matrix_of_words[0][i]
    dot_2 += matrix_of_query[0][i]*matrix_of_words[1][i]
    dot_3 += matrix_of_query[0][i]*matrix_of_words[2][i]
    dot_4 += matrix_of_query[0][i]*matrix_of_words[3][i]
    dot_5 += matrix_of_query[0][i]*matrix_of_words[4][i]
    dot_6 += matrix_of_query[0][i]*matrix_of_words[5][i]
    dot_7 += matrix_of_query[0][i]*matrix_of_words[6][i]
    dot_8 += matrix_of_query[0][i]*matrix_of_words[7][i]
    dot_9 += matrix_of_query[0][i]*matrix_of_words[8][i]
    dot_10 += matrix_of_query[0][i]*matrix_of_words[9][i]
    dot_11 += matrix_of_query[0][i]*matrix_of_words[10][i]
    dot_12 += matrix_of_query[0][i]*matrix_of_words[11][i]
    dot_13 += matrix_of_query[0][i]*matrix_of_words[12][i]
    dot_14 += matrix_of_query[0][i]*matrix_of_words[13][i]
    dot_15 += matrix_of_query[0][i]*matrix_of_words[14][i]
    sum1 += matrix_of_words[0][i]*matrix_of_words[0][i]
    sum2 += matrix_of_words[1][i]*matrix_of_words[1][i]
    sum3 += matrix_of_words[2][i]*matrix_of_words[2][i]
    sum4 += matrix_of_words[3][i]*matrix_of_words[3][i]
    sum5 += matrix_of_words[4][i]*matrix_of_words[4][i]
    sum6 += matrix_of_words[5][i]*matrix_of_words[5][i]
    sum7 += matrix_of_words[6][i]*matrix_of_words[6][i]
    sum8 += matrix_of_words[7][i]*matrix_of_words[7][i]
    sum9 += matrix_of_words[8][i]*matrix_of_words[8][i]
    sum10 += matrix_of_words[9][i]*matrix_of_words[9][i]
    sum11 += matrix_of_words[10][i]*matrix_of_words[10][i]
    sum12 += matrix_of_words[11][i]*matrix_of_words[11][i]
    sum13 += matrix_of_words[12][i]*matrix_of_words[12][i]
    sum14 += matrix_of_words[13][i]*matrix_of_words[13][i]
    sum15 += matrix_of_words[14][i]*matrix_of_words[14][i]
    sumq += matrix_of_query[0][i]*matrix_of_query[0][i]

sim_1 = dot_1/math.sqrt(sumq*sum1) 
sim_2 = dot_2/math.sqrt(sumq*sum2)
sim_3 = dot_3/math.sqrt(sumq*sum3)
sim_4 = dot_4/math.sqrt(sumq*sum4) 
sim_5 = dot_5/math.sqrt(sumq*sum5)
sim_6 = dot_6/math.sqrt(sumq*sum6)  
sim_7 = dot_7/math.sqrt(sumq*sum7) 
sim_8 = dot_8/math.sqrt(sumq*sum8)
sim_9 = dot_9/math.sqrt(sumq*sum9)
sim_10 = dot_10/math.sqrt(sumq*sum10)
sim_11 = dot_11/math.sqrt(sumq*sum11)
sim_12 = dot_12/math.sqrt(sumq*sum12)
sim_13 = dot_13/math.sqrt(sumq*sum13)
sim_14 = dot_14/math.sqrt(sumq*sum14)
sim_15 = dot_15/math.sqrt(sumq*sum15)

sim = {'doc 1': sim_1, 'doc 2': sim_2, 'doc 3': sim_3, 'doc 4': sim_4, 'doc 5': sim_5, 'doc 6': sim_6, 'doc 7': sim_7, 'doc 8' : sim_8, 'doc 9' : sim_9, 'doc 10' : sim_10, 'doc 11' : sim_11, 'doc 12' : sim_12, 'doc 13' : sim_13, 'doc 14' : sim_14, 'doc 15' : sim_15}


print("Similarity query dengan dokumen : ")
print(sim)
print("\n")

print("Similarity query dengan dokumen (sorted) : ")
print(sorted(sim.items(), key=lambda x: x[1], reverse=True))
print("\n")

#Tabel Term
print("Tabel Term :")
df = pd.DataFrame(matrix_of_words, 
                  columns=array_of_words, 
                  index=['doc1', 'doc2', 'doc3', 'doc4', 'doc5', 'doc6', 'doc7', 'doc8', 'doc9', 'doc10', 'doc11', 'doc12', 'doc13', 'doc14', 'doc15'])
dfq = pd.DataFrame(matrix_of_query, columns=array_of_words, index=['query'])
print(dfq.append(df).T)
