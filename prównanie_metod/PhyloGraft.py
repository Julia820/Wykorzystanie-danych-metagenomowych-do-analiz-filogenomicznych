# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:43:55 2020

@author: Jula
"""
from os import listdir
from os.path import isfile, join

def oczyszczanie(s):
    o=""
    for i in s:
        if i !="-":
            o = o+i
    return o

def minRefLen(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    D={}
    for i in onlyfiles:
        f = open(mypath + i).readlines()
        mx = len(f[1])
        n=i.split(".")[0]
        D[n] = mx
        for j in f[3::2]:
            if len(oczyszczanie(j)) < D[n]:
                mi = len(oczyszczanie(j))
                D[n]=mi
    return D


def make_db(name):
    F = open("mybd_"+name+".fa","w+")
    f1 = open("PhyloMagnet/ERR1726673/"+name+"_seq.fasta").read()
    f1 = f1.split("\n")[:-1]
    n_old = f1[0].split("-")[0][1:]
    f = open("/home/rymuza/"+name+"_026/"+name+"_megahit/"+n_old+".gpkg/final.contigs/final.contigs_orf.fa").read()
    f = f.split("\n")[:-1]
    h=0
    pac = n_old
    pom = 1
    for i in range(0,len(f1),2):
        n_new = f1[i].split("-")[0][1:]
        if n_old != n_new:
            f = open("/home/rymuza/"+name+"_026/"+name+"_megahit/"+n_new+".gpkg/final.contigs/final.contigs_orf.fa").read()
            pom+=1
            f = f.split("\n")[:-1]
            pac = n_new
            n_old = n_new
            h=0
        for j in range(0,len(f),2):
            n=">"+pac+"_"+f'{h:05d}'
            h+=1
            F.write(n+"\n"+f[j+1]+"\n")
    F.close()
    
def howMany(name):
    f = open(name).read()
    f = f.split("\n")[:-1]
    odp = 0
    for i in f:
        i = i.split("\t")
        phylo = i[0].split("-")[0]
        graft = i[1][:-6]
        ide = float(i[2])
        if phylo == graft and ide>=95:
            odp+=1
    return odp
#print(howMany("PhyloMagnet/queries/ERR868402_graftM.tsv"))

def repeat(name):
    mypath = "PhyloMagnet/packages/"
    Le = minRefLen(mypath)
    f = open(name).read()
    f = f.split("\n")[:-1]
    D={}
    for i in f:
        i = i.split("\t")
        phylo = i[0].split("-")[0]
        graft = i[1]
        s = int(i[8])
        e = int(i[9])
        ide = float(i[2])
        if graft in D.keys() and phylo == graft[:-6] and ide >= 95:
            D[graft].append([s,e])
        elif phylo == graft[:-6] and ide >= 95:
            D[graft]=[Le[graft],[s,e]]
    return D
#r = repeat("PhyloMagnet/queries/ERR868402_graftM.tsv")
#g=0
#g2=0
#for i in r.keys():
#    if len(r[i])>1:
#        g+=1
##        g2+= len(r[i])
#        print(i, r[i][0], r[i][1:])
#print(g)
    
def tabPhyloGraft(name,blast,sav):
    f1 = open(name).read()
    f1 = f1.split("\n")[:-1]
    f2 = open(blast).read()
    f2 = f2.split("\n")[:-1]
    F=open(sav, "w+")
    for i in f1:
        n = i.split("\t")[0]
        tax = i.split("\t")[1]
        pom = False
        for j in f2:
            j = j.split("\t")
            phylo = j[0].split("-")[0]
            graft = j[1][:-6]
            ide = float(j[2])    
            if n in j and ide>=95 and phylo==graft:
                pom = True
                z = j[1]+"\t"+ n +"\t"+ tax +"\n"
        if not pom:
            print(n)
            z = "n/a\t"+ n +"\t"+ tax +"\n"
        F.write(z)

    
name = "PhyloMagnet/queries/ERR868402_kont_id.tsv"
blast = "PhyloMagnet/queries/ERR868402_graftM.tsv"
sav = "PhyloMagnet/queries/ERR868402_graftPhylo.tsv"
tabPhyloGraft(name,blast,sav)