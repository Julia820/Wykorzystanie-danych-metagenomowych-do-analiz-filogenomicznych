d={'Aan' :'Aureococcus_anophagefferens', # ostateczny słownik z rozwinięciem skrutów po adnotacji ręcznej
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

p1="pr2_version_4.12.0_18S_taxo_long.fasta"
p2="pr2_version_4.12.0_16S_taxo_long.fasta"
def creatTax(p1,p2,d,saveName):
	# funkcja zpisująca w formacie tsv w pierwszej kolumnie skrót trzy literowy, a w drugiej jego pełną taksonomię
	# p1, p2 to lokalizacje bazy danych, d to słownik w którym skrótom trzyliterowym przypisany jest organizm
	# saveName nazwa pliku w którym ma zostać zpisana tabela
	b=set()
	tax= {}
	for k in [p1,p2]:
		f1=open(p1).read()
		f1=f1.split("\n")
		for s in d.keys():
			p= d[s]
			u=False
			for i in f1[::2]:
				if p in i:
					i=i.split("|")
					j= i[2] 
					for n in i[4:]:
						j =j + "; " + n 
					tax[s]=j
					u=True
					break
			if not u:
				b.add(p)
	taxo= open(saveName, "w+")
	for i in tax.keys():
		taxo.write(i + "\t" + tax[i] + "\n")
	taxo.close()
	return b # lista organizmów wymagająca rcznej adnotacji
