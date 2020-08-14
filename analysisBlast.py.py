# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:01:32 2020

@author: Jula
"""
import itertools
from ete3 import NCBITaxa
ncbi = NCBITaxa()

def LCA(l1,l2):
    # funkcja zwracająca tasonomię ostatniego wspólnego przodka dla dwóch organizmów
    l = min(len(l1),len(l2))
    p =[]
    for i in range(l):
        if l1[i] == l2[i]:
            p.append(l1[i])
        else: break
    return p

def short(name, number):
# funkcja zwaracająca tylko dla number pierwszych wyników z BLAST słownik,
# którego kluczme jest nazwa sekwencji, a wartocią lista identyfikatorów najlepszych przyrównań
# name nazwa pliku z wynikami Blast
    f= open(name).read()
    f = f.split("\n")[:-1]
    N = ""
    l=0
    L=0 #ilosc zaklasyfikowanych kontigow
    D={}
    for i in f:
        p = i.split("\t")
        n = p[0] # nazwa kontigu
        tax = p[1].split("|")[3]
        if n==N and l<number:
            l+=1
            D[n].append(tax)
        elif n!=N:
            D[n]=[tax]
            L+=1
            N = n
            l=1
    return D, L

def saveValSet(name, D ,L):
    # funkcja zapisująca do pliku identyfikatory najlepszych wyników z przyrównania 
    # w kolejnoci alfabetycznej
    val = D.values()
    merged = list(itertools.chain.from_iterable(val))
    val_set = set(merged)
    val_set = list(set(merged))
    val_set.sort()
    F_p = open(name,"w+")
    for i in val_set:
        F_p.write(i+"\n")
    F_p.close()
    return len(merged), len(val_set),L

def id_dict(name):
    # funkcja tworząca słownik, w którym kluczem jest identyfikator wyniku Blast,
    # a wartocią jego id taksonomiczne 
    d2 ={}
    db = open(name).read()
    db = db.split("\n")[:-1]
    for i in db:
        i = i.split("\t")
        d2[i[0]]=i[1]
    return d2


def savTax(D, d2,save_cont_tax = False , save_tax= False  ):
    # funkcja dziłająca na słowniku będącym wynikiem short oraz na slowniku z id_dict
    # pozwala ona na zapisanie do pliku kontigów z przypisana im taksonomią (save_cont_tax)
    # oraz policznenie ile razy w ynikach występuja eukariota, bakterie oraz sinice (save_tax)
    if save_cont_tax: 
        F = open(save_cont_tax, "w+")  
    if save_tax: F2= open(save_tax, "w+") 
    lis = D.keys()
    nazwa_s = lis[0].split("-") # nazwa pierwszego kontigu
    e =0
    b =0
    c=0
    n = 0
    no = 0
    for i in lis:
        nazwa_n = i.split("-")[0] # nazwa genu przy zapisie dla Phylo
        nazwa_n = nazwa_n.split("_")[0]
        if nazwa_n!=nazwa_s: 
            print(nazwa_s,e,c,b,no)
            if save_tax: F2.write(nazwa_s + "\t" + str(e) + "\t"+ str(c) +"\t"+ str(b) +"\t"+ str(no)+"\n")
            nazwa_s = nazwa_n
            b =0 # cyjano + bakteria
            e = 0
            c = 0 # na 5 pozycji 1117
            no = 0 #tylko cellular organisms lub mniej
        p =  ncbi.get_lineage(d2[D[i][0]])
        for j in D[i]:
            p = LCA(p,ncbi.get_lineage(d2[j]))
        lineage = p
        print(p)
        if len(p) < 3:
            no+=1
        elif len(p)> 5 and p[5]==1117:
            c+=1
            n+=1
        elif p[2] == 2: 
            b+=1   
            n+=1
        elif p[2] == 2759:
            e+=1

        names = ncbi.get_taxid_translator(lineage)
        l = [names[taxid] for taxid in lineage]
        s1=', '.join(l)
        if save_cont_tax:
            F.write(i + "\t" + s1 +"\n")
    if save_cont_tax: F.close()
    print(nazwa_s,e,c,b,no)
    if save_tax:
        
        F2.write(nazwa_s + "\t" + str(e) + "\t"+ str(c) +"\t"+ str(b) +"\t"+ str(no)+ "\n")
        F2.close()
    return n

def searchDB(db_name,val_set_name, save_name):     
    # funkcja pozwalająca na przeszukanie bazy db_name, id wyników Blast
    # save_name plik w którym są zapisywane id wyników oraz ich odpowiadajace im id taksonomiczne 
    db = open(db_name)
    F = open(save_name, "+w")
    val_set = open(val_set_name).read()
    val_set = val_set.split("\n")[:-1]
    db.readline()
    n=0
    for i in val_set:
        if i[0] != "#":
            pom = True
            while pom:   
                j = db.readline()
                tax_id = j.split("\t")[2]
                tax = j.split("\t")[1]
                if tax == i:
                    n+=1
                    print(tax,n)
                    F.write(i + "\t" + tax_id +"\n")
                    pom = False
                elif i[0] < tax[0]:
                    pom = False
                    print("uwaga",i, tax_id, tax) 
    F.close()

