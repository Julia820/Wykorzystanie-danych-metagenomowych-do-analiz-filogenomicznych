# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import re

def clear(s):
    # funkcja usuwająca z napisu "-"
    o=""
    for i in s:
        if i !="-":
            o = o+i
    return o


def minRefLen(mypath):
    # funkcja zwaracająca słownik, którego kluczem jest nazwa grupy referncyjnej,
    # a kluczem długoć najktótrzej sekwencji wchodzącej w skład ortogrupy
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    D={}
    for i in onlyfiles:
        f = open(mypath + i).readlines()
        mx = len(f[1])
        n=i.split(".")[0]
        D[n] = mx
        for j in f[3::2]:
            if len(clear(j)) < D[n]:
                mi = len(clear(j))
                D[n]=mi
    return D
mypath = "PhyloMagnet/packages/"

D = minRefLen(mypath)


def howMany(mypath, pattern,path, save = False, mostCommon = False):
    # funkcja pozwaljąca na ocenę wyników PhyloMagnet
    # mypath - scieżka do wyników PhyloMagnet
    # pattern - nazwa pliku zawierającego złożone kontigi
    # save - nazwa pliku, w którym mają zostać zapisane sekwencje spełniające warunek 
    # mostCommon - opcja pozwaljąca na stworzenie posortowanego słownika, w którym
    # kluczem jest nazwa paczki, a wartoscią liczba kontigów złożonych na jej
    #podstawie prze i po filrowaniu
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    n=0 # ilosc znalezionych sekwencji
    m=0 # ilosc sekwencji spelniajacych warunek
    pacz=0 # ilosc wykorzystanych paczek
    l=[] # lista ilosci sekwencji, ktore spelnily warunek
    if save!= False:
        F = open(save, "w+")    
    D2={}
    for i in onlyfiles:
        if re.match(pattern,i):
            f=open(path +i).read()
            f = f.split(">")[1:]
            name = i.split("-")[1]
            name = name.split(".")[0]
            f= ["".join(i.split("\n")[1:]) for i in f] # tylko seq
            n+= len(f)
            pacz+=1
            p = len(f[0]) # porowanie z cala dlugoscia przyrownania
            p = D[name] # porownywanie z najkrotrza sekwencja
            z=0 # ilosc sekwencji spelniajacych warunek w paczce
            for j in f:
                o = clear(j)
                if len(o)> 0.5*p: # warunek do spełnienia
                    if save:
                        F.write(">"+name+"-contig-"+f'{z:07}' + "\n" + o + "\n")
                    m+=1
                    z+=1
            D2[i] = [len(f),z]
#            print(i,len(f),z,p, z/len(f))
            if z != 0:
                l.append(z)
    if mostCommon:
        sorted_d = sorted(D2.items(), key=lambda x: x[1])
        return sorted_d

    return n,m,pacz, len(l)

