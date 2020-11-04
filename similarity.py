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
textstem   = stemmer.stem(df1)

b = open("doc2.txt", "r")
df2 = b.read()
textstem2   = stemmer.stem(df2)

c = open("doc3.txt", "r")
df3 = c.read()
textstem3   = stemmer.stem(df3)


doc = [textstem, textstem2, textstem3]

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

sum1 = 0
sum2 = 0
sum3 = 0

sumq = 0

for i in range (len(array_of_words)):
    dot_1 += matrix_of_query[0][i]*matrix_of_words[0][i]
    dot_2 += matrix_of_query[0][i]*matrix_of_words[1][i]
    dot_3 += matrix_of_query[0][i]*matrix_of_words[2][i]
    sum1 += matrix_of_words[0][i]*matrix_of_words[0][i]
    sum2 += matrix_of_words[1][i]*matrix_of_words[1][i]
    sum3 += matrix_of_words[2][i]*matrix_of_words[2][i]
    sumq += matrix_of_query[0][i]*matrix_of_query[0][i]

sim_1 = dot_1/math.sqrt(sumq*sum1) 
sim_2 = dot_2/math.sqrt(sumq*sum2)
sim_3 = dot_3/math.sqrt(sum1*sum2) 


sim = {'doc 1': sim_1, 'doc 2': sim_2, 'doc 3': sim_3}



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
                  index=['doc1', 'doc2', 'doc3'])
dfq = pd.DataFrame(matrix_of_query, columns=array_of_words, index=['query'])
print(dfq.append(df).T)