import os

def merging(directory, ver):
	# funkcja pozwalająca na łączenie informacji z wyników GraftM dla wielu paczek w jeden plik
	# ver == 1 łączenie combined_count_table.txt w jeden plik przy czym w 
    # pierszej kolumnie jest nazwa grupy, z której pochodzi wynik
    # ver == 2 tworzona jest tabela, która ma w kolumnach nazwę grupy referncyjnej, id kontigu 
    # oraz przypisaną mu taksonomie 
	directories = filter(lambda x: os.path.isdir(x), os.listdir(directory))
	if ver ==1:
		F= open("combined_table.txt","w+")
	
		F.write("OrtoGrup" + "\t" + "IDfromFile" + "\t" + "final.contigs" + "\t" + "ConsensusLineage" + "\n")
		for i in directories:
			if "combined_count_table.txt" in os.listdir(i):
				f= open(i + "/combined_count_table.txt").read()
				f = f.split("\n")[1:-1]
				f = [ p.split("\t") for p in f]
			for j in f:
				F.write(i[:-5] + "\t" + p[0] + "\t" + p[1] + "\t" + p[2] + "\n")
		F.close()
	elif ver == 2:
		F= open("combined_table2.txt","w+")
		F2.write("OrtoGrup" + "\t" + "ID" + "\t" "ConsensusLineage" + "\n")
		for i in directories:
			if "combined_count_table.txt" in os.listdir(i):
				f2 = open(i + "/final.contigs/final.contigs_read_tax.tsv").read()
				f2 = f2.split("\n")[1:-1]
				f2 = [ p.split("\t") for p in f2]
				for j in f2:
					m=j[0].split("_")[1:]
					F.write(i[:-5] + "\t" + m + "\t" + j[1] + "\n")
		F.close()
    return "Done"