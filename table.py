# -*- coding: utf-8 -*-


def LCA(s1,s2):
    # funkcja zwracająca tasonomię ostatniego wspólnego przodka dla dwóch organizmów
    l = min(len(s1),len(s2))
    p =""
    for i in range(l):
        if s1[i] == s2[i]:
            p+=s1[i]
        else: break
    return p

def ids_tiara(l = "out.txt"):
    # funkcja zwaracająca dla pliku l, będącego wynikiem Tiara, słowniki
    # D - słownik, w którym znajdują sie sekwencje plastydowe z ich opisem z Tiara
    # D2 - słownik, w którym znajdują się pozostałe sekwencje z ich opisem
    k = "plastid"
    D={}
    D2={}
    f = open(l).read()
    f = f.split("\n")[:-1]
    for i in f:
        p = i.split("\t")
        if p[2] == k: # znalzienie linijki z plastid
            n = p[0].split(" ")[0]
            z= n.split("_")[0] + "_" +n.split("_")[1]
            D[z]= [p[1], p[2]]
        else:
            n = p[0].split(" ")[0]
            z= n.split("_")[0] + "_" +n.split("_")[1]
            D2[z]= [p[1], p[2]]
    return D, D2

def ids_GraftM(location): 
    # funkcja, która na podstawi pliku combined_table2.txt, wyniku działania mereg.py, zwraca słowniki
    # D - słownik, w którym kluczem są nazwy kontigów, a wartociią jego taksonomia 
    # na podstwie wyników elgorytm LCA oraz liczba znalezionych w nim genów
    # D2 - słownik, w którym kluczem są nazwy kontigów zaierający >= 3 geny oraz mających przypisaną taksonomię
    # na podstawie LCA dłuższą niż Root; nucleus; Eukaryota; A, a wartocią jego taksonomia 
    # na podstwie wyników algorytmu LCA oraz liczba znalezionych w nim genów
    D={}
    f = open(location + "/combined_table2.txt").read()
    f = f.split("\n")[1:-1]
    for i in f:
        i = i.split("\t")
        p = i[1].split("_")
        p[1] = int(p[1])
        if p[1] not in D.keys():
            D[p[1]] = [i[2],1]
        else:
            D[p[1]] = [LCA(D[p[1]][0], i[2]), D[p[1]][1]+1]
    do={}
    for i in D.keys():
        if D[i][1] >=3:
            do[i]=D[i]
    D2={}
    for j in sorted(do.keys(), reverse = False):
        if len(do[j][0]) > len("Root; nucleus; Eukaryota; A"):
            D2[location + '_' + str(j)] =  do[j]
    return D2,D

def tabelka(location):
    # funkcja tworząca tabelę dla kontigów plastydowych wg Tiara oraz takich, które 
    # zawierają >= 3 geny oraz mają taksonomię dłuzszą niż Root; nucleus; Eukaryota; A wg GraftM
    # tabela zawiera w kolumnach nazwę kontigu, klasyfikacj z pierwszego i drugie etapu Tiara,
    # taksonomię oraz liczbę znalezionych w nim genów wg GraftM
    tiara = ids_tiara()[0]
    tiara_caly = ids_tiara()[1]
    graftM = ids_GraftM(location)[0]
    graftM_caly = ids_GraftM(location)[1]
    D = {}
    for i in tiara.keys():
        p=tiara[i]
        p.append('n/a')
        p.append('n/a')
        D[i]=p
    for j in graftM.keys():
        if j in D.keys():
            D[j][2]=graftM[j][0]
            D[j][3]=graftM[j][1]
        else:
            D[j]=["n/a","n/a",graftM[j][0],graftM[j][1]]
    for j in D.keys():
        if D[j][2] == "n/a":
            p=int(j.split("_")[1])
            if p in graftM_caly.keys():
                D[j][2]=graftM_caly[p][0]
                D[j][3]=graftM_caly[p][1]
        elif D[j][0] == "n/a" and j in tiara_caly.keys():
            D[j][0] = tiara_caly[j][0]
            D[j][1] = tiara_caly[j][1]
        elif D[j][0] == "n/a" and j not in tiara_caly.keys():
            D[j][0] = "too short"
            D[j][1] = "too short"
    return D
