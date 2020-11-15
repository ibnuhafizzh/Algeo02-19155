from django.http import HttpResponse
from django.shortcuts import render

from operator import index
import math
from re import split
import numpy as np
from numpy.core.fromnumeric import sort
from numpy.core.multiarray import dot
from numpy.core.records import array
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import Counter
from scipy.sparse import csr_matrix
import pandas as pd

#method view
def index(request):

    context = {}
    if(request.method == 'POST'):
        print('post')
        context['cari'] = request.POST['cari']
        # #PROGRAM SIMILARITAS
        def judul(document):
            isi = []
            fh = open(document)
            list = fh.readlines()
            url= document
            judul= list[0]
            kalimat = list[1] + list[2] + list[3]
            isi.append(url)
            isi.append(judul)
            isi.append(kalimat)
            return isi

        def tabel(var,query):
            cell = []
            for i in range(len(query)):
                cell_i = [query[i]]
                for item in var:
                    cell_i.append(item[i])
                cell.append(cell_i)
            return cell

        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        #Baca file & Stemming
        a = open("static/doc/doc1.txt", "r")
        df1 = a.read()
        textstem = stemmer.stem(df1)
        texterm = textstem.split(' ')
        content_a = judul("static/doc/doc1.txt")

        b = open("static/doc/doc2.txt", "r")
        df2 = b.read()
        textstem2 = stemmer.stem(df2)
        texterm2 = textstem2.split(' ')
        content_b = judul('static/doc/doc2.txt')

        c = open("static/doc/doc3.txt", "r")
        df3 = c.read()
        textstem3 = stemmer.stem(df3)
        texterm3 = textstem3.split(' ')
        content_c = judul('static/doc/doc3.txt')

        d = open("static/doc/doc4.txt", "r")
        df4 = d.read()
        textstem4 = stemmer.stem(df4)
        texterm4 = textstem4.split(' ')
        content_d = judul('static/doc/doc4.txt')

        e = open("static/doc/doc5.txt", "r")
        df5 = e.read()
        textstem5 = stemmer.stem(df5)
        texterm5 = textstem5.split(' ')
        content_e = judul('static/doc/doc5.txt')

        f = open("static/doc/doc6.txt", "r")
        df6 = f.read()
        textstem6 = stemmer.stem(df6)
        texterm6 = textstem6.split(' ')
        content_f = judul('static/doc/doc6.txt')

        g = open("static/doc/doc7.txt", "r")
        df7 = g.read()
        textstem7 = stemmer.stem(df7)
        texterm7 = textstem7.split(' ')
        content_g = judul('static/doc/doc7.txt')

        h = open("static/doc/doc8.txt", "r")
        df8 = h.read()
        textstem8 = stemmer.stem(df8)
        texterm8 = textstem8.split(' ')
        content_h = judul('static/doc/doc8.txt')

        i = open("static/doc/doc9.txt", "r")
        df9 = i.read()
        textstem9 = stemmer.stem(df9)
        texterm9 = textstem9.split(' ')
        content_i = judul('static/doc/doc9.txt')

        j = open("static/doc/doc10.txt", "r")
        df10 = j.read()
        textstem10 = stemmer.stem(df10)
        texterm10 = textstem10.split(' ')
        content_j = judul('static/doc/doc10.txt')

        k = open("static/doc/doc11.txt", "r")
        df11 = k.read()
        textstem11 = stemmer.stem(df11)
        texterm11 = textstem11.split(' ')
        content_k = judul('static/doc/doc11.txt')

        l = open("static/doc/doc12.txt", "r")
        df12 = l.read()
        textstem12 = stemmer.stem(df12)
        texterm12 = textstem12.split(' ')
        content_l = judul('static/doc/doc12.txt')

        m = open("static/doc/doc13.txt", "r")
        df13 = m.read()
        textstem13 = stemmer.stem(df13)
        texterm13 = textstem13.split(' ')
        content_m = judul('static/doc/doc13.txt')

        n = open("static/doc/doc14.txt", "r")
        df14 = n.read()
        textstem14 = stemmer.stem(df14)
        texterm14 = textstem14.split(' ')
        content_n = judul('static/doc/doc14.txt')

        o = open("static/doc/doc15.txt", "r")
        df15 = o.read()
        textstem15 = stemmer.stem(df15)
        texterm15 = textstem15.split(' ')
        content_o = judul('static/doc/doc15.txt')

        query = context['cari']
        querystem = stemmer.stem(query)
        termq = querystem.split(' ')

        doc = [query, textstem, textstem2, textstem3, textstem4, textstem5,
               textstem6, textstem7, textstem8, textstem9, textstem10,
               textstem11, textstem12, textstem13, textstem14, textstem15]
        def custum_fit(x):
          kataunik = set()
          for docindex in x:
            for kata in docindex.split(' '):
              kataunik.add(kata)
          vocab = {}
          for indeks, kata in enumerate(sorted(list(kataunik))):
            vocab[kata] = indeks
          return vocab

        vocab = custum_fit(doc)
        row, col, val = [],[],[]
        for idx, sentence in enumerate(doc):
          count_word = dict(Counter(sentence.split(' ')))
          for word, count in count_word.items():
            col_idx = vocab.get(word)
            if col_idx >= 0:
              row.append(idx)
              col.append(col_idx)
              val.append(count)

        arrvec = csr_matrix((val, (row, col)), shape=(len(doc), len(vocab))).toarray()

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

        for i in range (len(vocab)):
            dot_1 += arrvec[0][i]*arrvec[1][i]
            dot_2 += arrvec[0][i]*arrvec[2][i]
            dot_3 += arrvec[0][i]*arrvec[3][i]
            dot_4 += arrvec[0][i]*arrvec[4][i]
            dot_5 += arrvec[0][i]*arrvec[5][i]
            dot_6 += arrvec[0][i]*arrvec[6][i]
            dot_7 += arrvec[0][i]*arrvec[7][i]
            dot_8 += arrvec[0][i]*arrvec[8][i]
            dot_9 += arrvec[0][i]*arrvec[9][i]
            dot_10 += arrvec[0][i]*arrvec[10][i]
            dot_11 += arrvec[0][i]*arrvec[11][i]
            dot_12 += arrvec[0][i]*arrvec[12][i]
            dot_13 += arrvec[0][i]*arrvec[13][i]
            dot_14 += arrvec[0][i]*arrvec[14][i]
            dot_15 += arrvec[0][i]*arrvec[15][i]
            sum1 += arrvec[1][i]*arrvec[1][i]
            sum2 += arrvec[2][i]*arrvec[2][i]
            sum3 += arrvec[3][i]*arrvec[3][i]
            sum4 += arrvec[4][i]*arrvec[4][i]
            sum5 += arrvec[5][i]*arrvec[5][i]
            sum6 += arrvec[6][i]*arrvec[6][i]
            sum7 += arrvec[7][i]*arrvec[7][i]
            sum8 += arrvec[8][i]*arrvec[8][i]
            sum9 += arrvec[9][i]*arrvec[9][i]
            sum10 += arrvec[10][i]*arrvec[10][i]
            sum11 += arrvec[11][i]*arrvec[11][i]
            sum12 += arrvec[12][i]*arrvec[12][i]
            sum13 += arrvec[13][i]*arrvec[13][i]
            sum14 += arrvec[14][i]*arrvec[14][i]
            sum15 += arrvec[15][i]*arrvec[15][i]
            sumq += arrvec[0][i]*arrvec[0][i]

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

        content_a.append(sim_1)
        content_b.append(sim_2)
        content_c.append(sim_3)
        content_d.append(sim_4)
        content_e.append(sim_5)
        content_f.append(sim_6)
        content_g.append(sim_7)
        content_h.append(sim_8)
        content_i.append(sim_9)
        content_j.append(sim_10)
        content_k.append(sim_11)
        content_l.append(sim_12)
        content_m.append(sim_13)
        content_n.append(sim_14)
        content_o.append(sim_15)

        item_doc = []
        item_doc.append(content_a)
        item_doc.append(content_b)
        item_doc.append(content_c)
        item_doc.append(content_d)
        item_doc.append(content_e)
        item_doc.append(content_f)
        item_doc.append(content_g)
        item_doc.append(content_h)
        item_doc.append(content_i)
        item_doc.append(content_j)
        item_doc.append(content_k)
        item_doc.append(content_l)
        item_doc.append(content_m)
        item_doc.append(content_n)
        item_doc.append(content_o)

        context['doc'] = item_doc
        sim = { 'doc 1': sim_1, 'doc 2': sim_2, 'doc 3': sim_3,
                'doc 4': sim_4, 'doc 5': sim_5, 'doc 6': sim_6,
                'doc 7': sim_7, 'doc 8' : sim_8, 'doc 9' : sim_9,
                'doc 10' : sim_10, 'doc 11' : sim_11, 'doc 12' : sim_12,
                'doc 13' : sim_13, 'doc 14' : sim_14, 'doc 15' : sim_15}


        print("\nQuery:", query)
        context['doc'] = sorted(context['doc'], key=lambda x: x[3], reverse=True)


        term1 = {}
        term2 = {}
        term3 = {}
        term4 = {}
        term5 = {}
        term6 = {}
        term7 = {}
        term8 = {}
        term9 = {}
        term10 = {}
        term11 = {}
        term12 = {}
        term13 = {}
        term14 = {}
        term15 = {}
        termquery = {}


        for w in termq:
            if w not in termquery:
                termquery[w] = termq.count(w)

            if w not in term1:
                term1[w] = texterm.count(w)

            if w not in term2:
                term2[w] = texterm2.count(w)

            if w not in term3:
                term3[w] = texterm3.count(w)

            if w not in term4:
                term4[w] = texterm4.count(w)

            if w not in term5:
                term5[w] = texterm5.count(w)

            if w not in term6:
                term6[w] = texterm6.count(w)

            if w not in term7:
                term7[w] = texterm7.count(w)

            if w not in term8:
                term8[w] = texterm8.count(w)

            if w not in term9:
                term9[w] = texterm9.count(w)

            if w not in term10:
                term10[w] = texterm10.count(w)

            if w not in term11:
                term11[w] = texterm11.count(w)

            if w not in term12:
                term12[w] = texterm12.count(w)

            if w not in term13:
                term13[w] = texterm13.count(w)

            if w not in term14:
                term14[w] = texterm14.count(w)

            if w not in term15:
                term15[w] = texterm15.count(w)

        termvalue1 = list(term1.values())
        termvalue2 = list(term2.values())
        termvalue3 = list(term3.values())
        termvalue4 = list(term4.values())
        termvalue5 = list(term5.values())
        termvalue6 = list(term6.values())
        termvalue7 = list(term7.values())
        termvalue8 = list(term8.values())
        termvalue9 = list(term9.values())
        termvalue10 = list(term10.values())
        termvalue11 = list(term11.values())
        termvalue12 = list(term12.values())
        termvalue13 = list(term13.values())
        termvalue14 = list(term14.values())
        termvalue15 = list(term15.values())
        termqvalues = list(termquery.values())

        matrix_of_term = [termqvalues, termvalue1, termvalue2, termvalue3, termvalue4, termvalue5,
                          termvalue6, termvalue7, termvalue8, termvalue9, termvalue10,
                          termvalue11, termvalue12, termvalue13, termvalue14, termvalue15]

        term_coloumns = []
        for w in termq:
            if w not in term_coloumns:
                term_coloumns.append(w)
        context['tabel'] = tabel(matrix_of_term,term_coloumns)
        datframe = pd.DataFrame(np.array(matrix_of_term),
                                columns=term_coloumns, index=['query', 'doc1', 'doc2', 'doc3', 'doc4', 'doc5', 'doc6', 'doc7', 'doc8', 'doc9', 'doc10', 'doc11', 'doc12', 'doc13', 'doc14', 'doc15'])
        print("matriks term :")
        print(datframe.T)
        context['header'] = ['','query','doc1','doc2','doc3','doc4','doc5','doc6','doc7','doc8','doc9','doc10','doc11','doc12','doc13','doc14','doc15']
    else:
        print('get ini')
    return render(request,'index.html',context)

def index2(request):
    return HttpResponse("<h1>Hallo dunia</h1>")
def about(request):
    return HttpResponse("<h1>ini about</h1>")
