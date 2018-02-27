//available UI languages
var avlang=["English","Fran&ccedil;ais","Castellano","Portugu&ecirc;s","Italiano","Deutsch"],Translations=[],days=[];
var Countries={'ABW':'AW','AFG':'AF','AGO':'AO','AIA':'AI','ALB':'AL','AND':'AD','ANT':'AN','ARE':'AE','ARG':'AR','ARM':'AM','ASM':'AS','ATA':'AQ','ATF':'TF','ATG':'AG','AUS':'AU','AUT':'AT','AZE':'AZ','BDI':'BI','BEL':'BE','BEN':'BJ','BFA':'BF','BGD':'BD','BGR':'BG','BHR':'BH','BHS':'BS','BIH':'BA','BLR':'BY','BLZ':'BZ','BMU':'BM','BOL':'BO','BRA':'BR','BRB':'BB','BRN':'BN','BTN':'BT','BUL':'BU','BVT':'BV','BWA':'BW','CAF':'CF','CAN':'CA','CCK':'CC','CHE':'CH','CHL':'CL','CHN':'CN','CIV':'CI','CMR':'CM','COD':'CD','COG':'CG','COK':'CK','COL':'CO','COM':'KM','CPV':'CV','CRI':'CR','CRO':'HR','CUB':'CU','CXR':'CX','CYM':'KY','CYP':'CY','CZE':'CZ','DEN':'DK','DEU':'DE','DJI':'DJ','DMA':'DM','DNK':'DK','DOM':'DO','DZA':'DZ','ECU':'EC','EGY':'EG','ERI':'ER','ESH':'EH','ESP':'ES','EST':'EE','ETH':'ET','FIN':'FI','FJI':'FJ','FLK':'FK','FRA':'FR','FRO':'FO','FSM':'FM','FXX':'FX','GAB':'GA','GBR':'GB','GEO':'GE','GER':'DE','GHA':'GH','GIB':'GI','GIN':'GN','GLP':'GP','GMB':'GM','GNB':'GW','GNQ':'GQ','GRC':'GR','GRD':'GD','GRE':'GR','GRL':'GL','GTM':'GT','GUF':'GF','GUM':'GU','GUY':'GY','HKG':'HK','HMD':'HM','HND':'HN','HRV':'HR','HTI':'HT','HUN':'HU','IDN':'ID','IND':'IN','IOT':'IO','IRL':'IE','IRN':'IR','IRQ':'IQ','ISL':'IS','ISR':'IL','ITA':'IT','JAM':'JM','JOR':'JO','JPN':'JP','KAZ':'KZ','KEN':'KE','KGZ':'KG','KHM':'KH','KIR':'KI','KNA':'KN','KOR':'KR','KWT':'KW','LAO':'LA','LAT':'LV','LBN':'LB','LBR':'LR','LBY':'LY','LCA':'LC','LIE':'LI','LKA':'LK','LSO':'LS','LTU':'LT','LUX':'LU','LVA':'LV','MAC':'MO','MAR':'MA','MCO':'MC','MDA':'MD','MDG':'MG','MDV':'MV','MEX':'MX','MHL':'MH','MKD':'MK','MLI':'ML','MLT':'MT','MMR':'MM','MNE':'ME','MNG':'MN','MNP':'MP','MON':'MO','MOZ':'MZ','MRT':'MR','MSR':'MS','MTQ':'MQ','MUS':'MU','MWI':'MW','MYS':'MY','MYT':'YT','NAM':'NA','NCL':'NC','NED':'NL','NER':'NE','NFK':'NF','NGA':'NG','NIC':'NI','NIU':'NU','NLD':'NL','NOR':'NO','NPL':'NP','NRU':'NR','NZL':'NZ','OMN':'OM','PAK':'PK','PAN':'PA','PCN':'PN','PER':'PE','PHL':'PH','PLW':'PW','PNG':'PG','POL':'PL','POR':'PT','PRI':'PR','PRK':'KP','PRT':'PT','PRY':'PY','PYF':'PF','QAT':'QA','REU':'RE','ROM':'RO','ROU':'RO','RSA':'ZA','RUS':'RU','RWA':'RW','SAF':'ZA','SAU':'SA','SDN':'SD','SEN':'SN','SGP':'SG','SGS':'GS','SHN':'SH','SJM':'SJ','SLB':'SB','SLE':'SL','SLO':'SI','SLV':'SV','SMR':'SM','SOM':'SO','SPM':'PM','SRB':'RS','SSD':'SS','STP':'ST','SUI':'CH','SUR':'SR','SVK':'SK','SVN':'SI','SWE':'SE','SWZ':'SZ','SYC':'SC','SYR':'SY','TCA':'TC','TCD':'TD','TGO':'TG','THA':'TH','TJK':'TJ','TKL':'TK','TKM':'TM','TMP':'TP','TON':'TO','TTO':'TT','TUN':'TN','TUR':'TR','TUV':'TV','TWN':'TW','TZA':'TZ','UGA':'UG','UKR':'UA','UMI':'UM','URY':'UY','USA':'US','UZB':'UZ','VAT':'VA','VCT':'VC','VEN':'VE','VGB':'VG','VIR':'VI','VNM':'VN','VUT':'VU','WLF':'WF','WSM':'WS','YEM':'YE','ZAF':'ZA','ZMB':'ZM','ZWE':'ZW'};
//ENGLISH
Translations[0]={0:'Results',1:'Search an individual',2:'Language',3:'Bib',4:'Average speed',5:'Place',6:'Time',7:'Race',8:'Withdrawal',9:'Category',10:'Race time',
11:'Bib or name',12:'km',13:'mi.',14:'km',15:'mi.',16:'Start',17:'Finish',18:'At start',19:'Awaited',20:'Virtual rank',
21:'Finish line',22:'Category rank',23:'km/h',24:'mph',25:'Split time',26:'Pl.',27:'Women rank',28:'Bib',29:'Name',30:'Stage',
31:'Sx',32:'Cat',33:'RUNNER',34:'Prologue',35:'Press format',36:'Women ranking',37:'Diploma',38:'Sex',39:'General',40:'By cat.',
41:'Club',42:'Team',43:'Club-town',44:'Women',45:'lap',46:'laps',47:'Man',48:'Woman',49:'Runners',50:'Ranked',
51:'Real time',52:'Real start',53:'Select',54:'Avg',55:'Remove grouping',56:'By category',57:'Men',58:'By',59:'Stages',60:'Download',
61:'Laps',62:'Last split',63:'Disqualified',64:'Ranking',65:'Best lap(s)',66:'Last modif.',67:'Gap',68:'Best lap',69:'Sports',70:'Splits',71:'Round',
72:'min/km',73:'min/mi',74:'Map',75:'Non starter',76:'Mixed',77:'Distance',78:'Final general ranking',79:'Points',80:'Teams',81:'Share'};
days[0]=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
//FRENCH
Translations[1]={0:'Résultats',1:'Rechercher un coureur',2:'Langue',3:'Dossard',4:'Moyenne',5:'Place',6:'Temps',7:'Course',8:'Abandon',9:'Catégorie',10:'Temps course',
11:'Dossard ou nom',12:'km',13:'mi.',14:'km',15:'mi.',16:'Départ',17:'Arrivée',18:'Coureurs au départ',19:'Coureurs attendus',20:'Pl. provisoire',
21:'Ligne d\'arrivée',22:'Place par catégorie',23:'km/h',24:'mph',25:'Heure passage',26:'Pl.',27:'Scratch f&eacute;minin',28:'Dos',29:'Nom',30:'Etape',
31:'Sx',32:'Cat',33:'COUREUR',34:'Prologue',35:'Format presse',36:'F&eacute;minines',37:'Dipl&ocirc;me',38:'Sexe',39:'Général',40:'Par cat.',
41:'Club',42:'Equipe',43:'Club-ville',44:'F&eacute;minines',45:'tour',46:'tours',47:'Homme',48:'Femme',49:'Engag&eacute;s',50:'Classés',
51:'Temps réel',52:'Départ réel',53:'Sélectionner',54:'Moy',55:'Supprimer le groupement',56:'Par catégories',57:'Hommes',58:'Par',59:'Etapes',60:'Télécharger',
61:'Tours',62:'Dernier passage',63:'Disqualifi&eacute;',64:'Classement',65:'Meilleur(s) tour(s)',66:'Dernière modif',67:'Ecart',68:'Meilleur tour',69:'Disciplines',70:'Pointages',71:'Manche',
72:'min/km',73:'min/mi',74:'Carte',75:'Non partant',76:'Mixte',77:'Distance',78:'Classement général final',79:'Points',80:'Equipes',81:'Partager'};
days[1]=['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'];
//CASTELLANO
Translations[2]={0:'Resultados',1:'Busqueda de un participante',2:'Idioma',3:'Dorsal',4:'Ritmo',5:'Place',6:'Tiempo',7:'Recorrido',8:'Retidado',9:'Categor&iacute;a',10:'Tiempo de carrera',
11:'Dorsal o nombre',12:'km',13:'mi.',14:'km',15:'mi.',16:'Salida',17:'Meta',18:'At start',19:'Pendientes',20:'Clasificaci&oacute;n provisional',
21:'L&iacute;nea de meta',22:'Clasificaci&oacute;n por categor&iacute;as',23:'km/h',24:'mph',25:'Tiempo parcial',26:'Pl.',27:'Clasificaci&oacute;n Femenina',28:'Dorsal',29:'Nombre',30:'Etapa',
31:'Sx',32:'Cat',33:'PARTICIPANTE',34:'Pr&oacute;logo',35:'Formato Prensa',36:'Clasificaci&oacute;n Femenina',37:'Diploma',38:'Sexo',39:'General',40:'Por Cat.',
41:'Club',42:'Equipo',43:'Club-Ciudad',44:'Femenina',45:'vuelta',46:'vueltas',47:'Hombre',48:'Mujer',49:'Participantes',50:'Clasificados',
51:'Tiempo real',52:'Salida real',53:'Selecciona',54:'Ritmo',55:'Remove grouping',56:'Por categor&iacute;a',57:'Hombre',58:'Por',59:'Etapas',60:'Descarga',
61:'Vueltas',62:'&Uacute;ltima vuelta',63:'Descalificado',64:'Ranking',65:'Mejor vuelta(s)',66:'Last modif.',67:'Gap',68:'Mejor vuelta',69:'Sports',70:'Splits',71:'Round',
72:'min/km',73:'min/mi',74:'Carta',75:'Non starter',76:'Mixto',77:'Distancia',78:'Clasificación general final',79:'Puntos',80:'Equipos',81:'Compartir'};
days[2]=['Domingo','Lunes','Martes','Mi&eacute;rcoles','Jueves','Viernes','S&aacute;bado'];
//PORTUGUES
Translations[3]={0:'Resultados',1:'Procurar um atleta',2:'Idioma',3:'Num',4:'km/h',5:'Col',6:'Tempo',7:'Modalidade',8:'Descassificados',9:'Categoria',10:'Tempo de Corrida',
11:'Nome ou Número de Peito',12:'km',13:'mi.',14:'km',15:'mi.',16:'Largada',17:'Chegada',18:'At start',19:'Aguardando',20:'Colocação virtual',
21:'Linha de chegada',22:'Col Categoria',23:'km/h',24:'mph',25:'Tempo Percurso',26:'Col',27:'Somente Mulheres',28:'Num',29:'Nome',30:'Etapa',
31:'Sx',32:'Cat',33:'BUSCA',34:'Prologo',35:'Formato Imprensa',36:'Classificação Feminina',37:'Diploma',38:'Sexo',39:'Geral',40:'Por Categoria',
41:'Clube',42:'Equipe',43:'Clube-Cidade',44:'Mulheres',45:'volta',46:'voltas',47:'Masculino',48:'Feminino',49:'Atletas',50:'Completaram',
51:'Tempo Líquido',52:'Hora Largada',53:'Selecionar',54:'Vel.Média',55:'Remover filtro',56:'Por Categoria',57:'Masculino',58:'Por',59:'Etapas',60:'Download',
61:'Voltas',62:'&Uacute;ltima Volta',63:'Desclassificado',64:'Ranking',65:'Melhor volta',66:'&Uacute;ltima Alteração',67:'Gap',68:'Melhor volta',69:'Esportes',70:'Voltas',71:'Round',
72:'min/km',73:'min/mi',74:'Carta',75:'Non starter',76:'Mista',77:'Distância',78:'Classificação geral final',79:'Pontos',80:'Equipes',81:'Compartilhar'};
days[3]=['Domingo','Segunda-Feira','Ter&ccedil;a-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','S&aacute;bado'];
//ITALIANO
Translations[4]={0:'Risultati',1:'Ricerca atleta',2:'Lingua',3:'Pettorale',4:'Media',5:'Classifica',6:'Tempo',7:'Corsa',8:'Ritirato',9:'Categoria',10:'Tempo di corsa',
11:'Nome o Numero',12:'km',13:'mi.',14:'km',15:'mi.',16:'Partenza',17:'Arrivo',18:'Atleti partenti',19:'Atleti attesi',20:'Class. provvisoria',
21:'Arrivo',22:'Class. per categoria',23:'km/h',24:'mph',25:'Ora passaggio',26:'Class.',27:'Scratch femminile',28:'No',29:'Nome',30:'Tappa',
31:'Sx',32:'Cat',33:'ATLETA',34:'Prologo',35:'Formato stampa',36:'Femminile',37:'Diploma',38:'Sesso',39:'Generale',40:'Per cat.',
41:'Club',42:'Team',43:'Club-citt&aacute',44:'Femminile',45:'giro',46:'giri',47:'Uomo',48:'Donna',49:'Partecipanti',50:'Classificati',
51:'Tempo reale',52:'Partenza reale',53:'Seleziona',54:'Media',55:'Elimina filtri',56:'Per categorie',57:'Uomini',58:'Per',59:'Tappe',60:'Download',
61:'Giri',62:'Ultimo passaggio',63:'Squalificato(a);',64:'Classifica',65:'Miglior(i) giro(i)',66:'Ultima modifica',67:'Scarto',68:'Miglior giro',69:'Discipline',70:'Controlli',71:'Manche',
72:'min/km',73:'min/mi',74:'Mappa',75:'Non starter',76:'Misto',77:'Distanza',78:'Finale classifica generale',79:'Punti',80:'Squadre',81:'Condividi'};
days[4]=['Domenica','Lunedi','Martedi','Mercoledi','Giovedi','Venerdi','Sabato'];
//DEUTSCH
Translations[5]={0:'Ergebnis',1:'Laüfer suchen',2:'Sprach',3:'Laüfer nummer',4:'Durchschnitt',5:'Rang',6:'Zeit',7:'Lauf',8:'Aufgabe',9:'Kategorie',10:'Lauf zeit',11:'Laüfer nummer oder name',12:'km',13:'mi.',14:'km',15:'mi.',16:'Start',17:'Ziel',18:'Läufer bei der start',19:'Erwartete Laüfer ',20:'Rg. provisorisch',21:'Ziellinie',22:'Rang von kategorie',23:'km/h',24:'mph',25:'Stunden vorbeikommen',26:'Rg.',27:'Scratch Frau',28:'Dos',29:'Name',30:'Etappe',31:'Sx',32:'Kat',33:'LAUFER',34:'Prolog',35:'Presse format',36:'Frauen',37:'Diplom',38:'Sexe',39:'Allgemein',40:'Nach kat.',41:'Klub',42:'Mannschaft',43:'Klub-Stadt',44:'Frauen',45:'Rund',46:'Runden',47:'Män',48:'Frau',49:'Teilnehmer',50:'Geordnet',51:'Realzeit',52:'Real start',53:'Aufstellen',54:'Moy',55:'Die gruppierung entziehen',56:'Von katégories',57:'Mäner',58:'Von',59:'Etappen',60:'Download',61:'Runden',62:'Letztes vorbeikommen',63:'Disqualifiziert',64:'Rang',65:'Beste(n) Rund(en)',66:'Letzte änderumg',67:'Unterschied',68:'Beste Rund',69:'Disziplinen',70:'Zeitkontroll',71:'Drittel',72:'min/km',73:'min/mi',74:'Karte',75:'Non starter',76:'Gemischte',77:'Distanz',78:'Abschließende Gesamtwertung',79:'Punkte',80:'Mannschaften',81:'Teilen'};
days[5]=['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag'];
