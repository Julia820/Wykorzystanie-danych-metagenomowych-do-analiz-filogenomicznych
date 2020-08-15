#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ete3 import Tree

def saveTrees(name1, name2, name3):
    # name1 - plik z opisem taksonomicznym kontigów w formacie tsv
    # name2 - lokalizacja pliku z drzewem otrzymanym przez PhyloMagnet
    # name3 - lokalizacja, w której ma zostać zapisane nowe drzewo
    f2 = open(name1).read()
    f2 = f2.split("\n")[:-1]
    na_s=f2[0].split("-")[0]
    o={}
    for i in f2:
        name = i.split("-")[0]
        if name != na_s:
            t = Tree(name2 + na_s+".newick")
            for leaf in t.get_leaves():
                if leaf.name in o.keys():
                    leaf.name = leaf.name + "_"+o[leaf.name]
            t.write(format=1, outfile=name3+ na_s +".nw")
            na_s=name
            o={}
        l = i.split("\t")
        c = l[0].split("-")[1:]
        c='-'.join(c)
        c = "Q_C" + c[1:][:9]+ c[1:][10:]
        o[c] = l[1]
    t = Tree(name2 + name+".newick")
    for leaf in t.get_leaves():
        if leaf.name in o.keys():
            leaf.name = leaf.name + "_"+o[leaf.name]
    t.write(format=1, outfile=name3+ name +".nw")
    return "Done"
