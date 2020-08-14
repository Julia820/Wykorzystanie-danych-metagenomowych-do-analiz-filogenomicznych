# -*- coding: utf-8 -*-


l=["ERR868402", "ERR1726574","ERR1726673"]

def clasification(l,s = False, k = "plastid\n"):
    # funkcja zwarcająca listę sekwencji z wyników Tiara zaklasyfikowanych jako k
    # Jesli s= True to wyniki w formie takiej jak w plikach ze złożeniami
    # Jesli s = False to wyniki jako numer zlożeni oraz kontigu
    o=[]
    f=open( l + "_026/"+l +"_deep.txt").readlines()
    for i in f:
        p = i.split("\t")
        if p[2] == k: # znalzienie linijki z plastid
            if not s: # ktory plik i nr sekwencji
                n = p[0].split(" ")[0]
                z= l + "_" +n.split("_")[1]
                o.append(z)
            else: # dokladny id sekwencji
                o.append(p[0])
    return o


def extrac_sequences(location, name):
    # funkcja pozwlająca na wyciągnięcie do pliku kontigów zaklasyfikowanych jako plastydowe 
    F = open(name, "w+")
    do = clasification(location, True)
    sek = open(location + "_026/"+ location +"_megahit/final.contigs.fa")
    lines = sek.readlines()
    pocz=0 
    for j in do:
        print(j, )
        for r in range(pocz,len(lines)):
            if j in lines[r]:
                print(j, )
                sekwencja = lines[r+1]
                pocz = r+ 1
                break
        l = '>' + j + '\n' + sekwencja 
        print(l)
        F.write(l)
    F.close()
