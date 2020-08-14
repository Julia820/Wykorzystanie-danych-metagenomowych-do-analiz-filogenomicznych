# -*- coding: utf-8 -*-

l=["ERR868402", "ERR1726574","ERR1726673"]

def LCA(s1,s2):
    # funkcja zwracająca tasonomię ostatniego wspólnego przodka dla dwóch organizmów
    l = min(len(s1),len(s2))
    p =""
    for i in range(l):
        if s1[i] == s2[i]:
            p+=s1[i]
        else: break
    return p

def analysis(location, sav= False, lenght = 0, tax):
    # funkcja pozwalająca na zapisanie do pliku kontigów spełniających warunek 
    # długoci większej niż lenght oraz takosomi dłuższej niż tax
    # laction lokalizacja pliku combined_table2.txt oraz całego złożenia metagenomu
    D={}
    f = open(location + "/combined_table2.txt").read()
    f = f.split("\n")[1:-1]
    if sav != False:
        F = open(sav, "w+")
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
        if D[i][1] >=3: #w ilu ma byc znalezione
            do[i]=D[i]
#            
    n = 0
    p=0
    seq = open(location + "_026/"+ location +"_megahit/final.contigs.fa")
    lines = seq.readlines()
    beg=0 
    for j in sorted(do.keys(), reverse = False):
        if len(D[j][0]) > len("tax"):
            n+=1
            print(j, )
            for r in range(pocz,len(lines)):
                if str(j) in lines[r]:
                    sequence = lines[r+1]
                    beg = r
                    break
            if len(sequence) > lenght:
                l = '>' + location + '_' + str(j) +'_' + D[j][0] + '\n' + sequence
                F.write(l)
                p+=1
    return(p,n)
    


