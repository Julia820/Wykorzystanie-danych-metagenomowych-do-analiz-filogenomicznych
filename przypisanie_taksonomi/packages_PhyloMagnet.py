# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile, join

d={'Aan' :'Aureococcus_anophagefferens', # ostateczny słownik z rozwinięciem skrutów
'Aca' :'Amphidinium_carterae', 
'Ala' :'Aureoumbra_lagunensis',
'Ath' :'Arabidopsis_thaliana',
'Bbo' :'Babesia_bovis',
'Cat' :'Chlorokybus_atmophyticus',
'Cca' :'Cyanidium_caldarium',
'Ccr' :'Chondrus_crispus',
'Chv' :'Chlorella_vulgaris',
'Cme' :'Cyanidioschyzon_merolae',
'Cpa' :'Cyanophora_paradoxa',
'Cpr' :'Cryptomonas_paramecium',
'Cre' :'Chlamydomonas_reinhardtii',
'Ctu' :'Calliarthron_tuberculosum',
'Cve' :'Chromera_velia', 
'Cvu' :'Chara_vulgaris',
'Dba' :'Durinskia_baltica',
'Ehu' :'Emiliania_huxleyi',
'Esi' :'Ectocarpus_siliculosus',
'Ete' :'Eimeria_tenella', 	
'Fcy' :'Fragilariopsis_cylindrus',
'Fpa' :'Florenciella_parvula',
'Fsp' :'Fistulifera_sp.',
'Fve' :'Fucus_vesiculosus',
'Gpo' :'Lingulodinium_polyedra', 
'Gsu' :'Galdieria_sulphuraria',
'Gte' :'Gracilaria_tenuistipitata',
'Gth' :'Guillardia_theta',
'Hak' :'Heterosigma_akashiwo',
'Htr' :'Heterocapsa_triquetra', 
'Kfo' :'Kryptoperidinium_foliaceum',
'Kve' :'Karlodinium_veneficum', 
'Mpo' :'Marchantia_polymorpha',
'Msp' :'Monomastix_sp.',
'Mvi' :'Mesostigma_viride',
'Nga' :'Nannochloropsis_gaditana',
'Noc' :'Nannochloropsis_oceanica',
'Nol' :'Nephroselmis_olivacea',
'Och' :'Ochromonas_sp.',
'Osi' :'Odontella_sinensis',
'Pan' :'Phaeocystis_antarctica',
'Pcr' :'Porphyridium_purpureum',
'Pel' :'Pseudopedinella_elastica',
'Pfa' :'Plasmodium_falciparum', 
'Plu' :'Pavlova_lutheri',
'Pmi' :'Pedinomonas_minor',
'Ppa' :'Pyramimonas_parkeae',
'Ppu' :'Porphyra_purpurea',
'Psp' :'Pelagomonas_sp.',
'Ptr' :'Phaeodactylum_tricornutum',
'Pye' :'Pyropia_yezoensis',
'Rsa' :'Rhodomonas_salina',
'Sja' :'Saccharina_japonica',
'Sru' :'Syntrichia_ruralis',
'Tgo' :'Toxoplasma_gondii', 
'Tmi' :'Trachydiscus_minutus',
'Tpa' :'Theileria_parva', 
'Tps' :'Thalassiosira_pseudonana',
'Vbr' :'Vitrella_brassicaformis', 
'Vli' :'Vaucheria_litorea'}


def taxPhyl(tax_report, location):
	# funkcja dopisująca do plików z ortogrupami ich id taksonomiczne
	# tax_report - plik z raportem taksonomicznym z bazy NCBI dla badanych organizmów
	# location - lokalizacja plików z ortogrupami 
	taxa = open(tax_report).read()
	taxa= taxa.split("\n")[1:]
	taxa2 = [ i.split("\t") for i in taxa]

	d2={}
	for i in range(len(taxa)):
		d2[taxa2[i][0]]=taxa2[i][1]
	D={}
	for i in d.keys():
		D[i]=d2[d[i]]

	pl=[]

	for i in onlyfiles:
		j = i.split(".")[0]
	
		f= open("PhyloMagnet/" + j + ".fasta","w+")
		f1=open(location + i).read()
		f1=f1.split("\n")[:-1]
		l=len(f1)
		k=0
		for j in range(0,l):
			p=f1[j]
			if f1[j][0] == ">":
				p=f1[j][0] + D[f1[j][1:4]] + "." + f1[j][1:]
			f.write(p + "\n")
		f.close()
