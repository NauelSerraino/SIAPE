URL = "https://siape.enea.it/api/v1/aggr-data"

CONTENT_TYPE = "application/x-www-form-urlencoded"
HEADERS = {
    "Content-Type": CONTENT_TYPE,
}

GROUP = ["cod_pro", "claen", "destuso", "motiv"]
DESTUSO = ["O", "1"]
ZONCLI = ["A", "B", "C", "D", "E", "F"]
MOTIV = ["0", "1", "2", "3", "4", "5"]
CODREG = [f"{i:02d}" for i in range(1, 23)]
CODPRO = [f"{i:03d}" for i in range(1, 111)]
COMBS_PRO_REG = [(i, j) for i in CODREG for j in CODPRO]

RESID_MAP_OUT = {
    "0": "Resid",
    "1": "Non Resid"
}

RESID_MAP_IN = {
    "res": "0",
    "non-res": "1"
}

YEARS_LIMITS = [
    ["-1000000000", "1944"],
    ["1944", "1972"],
    ["1972", "1991"],
    ["1991", "2005"],
    ["2005", "2015"],
    ["2015", "1000000000"]
]

SURFACE_LIMITS = [
    ["-1000000000", "50"],
    ["50", "100"],
    ["100", "200"],
    ["200", "500"],
    ["500", "1000"],
    ["1000", "5000"],
    ["5000", "1000000000"]
]

PAYLOAD_COMPLETE = {
    "group[]": GROUP,
    "where[destuso]": DESTUSO,
    "where[zoncli][]": ZONCLI,
    "where[motiv]": MOTIV,
    "where[cod_reg]": CODREG,
    "nofilter": "false"
}

PAYLOAD_REGION = {
    "group[]": "claen",
    "where[cod_reg]": CODREG,
    "where[cod_pro]": CODPRO,
    "where[zoncli]": ZONCLI,
    "nofilter": "false"
}

PAYLOAD_CLAEN_RAW = {
    "group[]": "claen",
    "nofilter": "false"
}

PAYLOAD_CLAEN = {
    "group[]": "claen",
    "nofilter": "false",
    "where[suris][range][]": SURFACE_LIMITS,
    "where[annoc][range][]": YEARS_LIMITS,
}

PAYLOAD_CLEAN_SINGLE_ZONCLI = {
    "group[]": "claen",
    "where[zoncli]": ZONCLI,
    "nofilter": "false"
}

REG_TO_CODREG = {
    'Piemonte': '01',
    "Valle d'Aosta": '02',
    'Lombardia': '03',
    'Veneto': '05',
    'Friuli Venezia Giulia': '06',
    'Liguria': '07',
    'Emilia Romagna': '08',
    'Toscana': '09',
    'Umbria': '10',
    'Marche': '11',
    'Lazio': '12',
    'Abruzzo': '13',
    'Molise': '14',
    'Campania': '15',
    'Puglia': '16',
    'Basilicata': '17',
    'Calabria': '18',
    'Sicilia': '19',
    'Sardegna': '20',
    'Bolzano': '21',
    'Trento': '22'
}

CODREG_TO_REG = {v : k for k, v in REG_TO_CODREG.items()}

ENERGETIC_CLASSES_ORDERED = ["A4", "A3", "A2", "A1", "B", "C", "D", "E", "F", "G"]
SURFACE_RANGES_ORDERED = [
    "['-1000000000', '50']",
    "['50', '100']",
    "['100', '200']",
    "['200', '500']",
    "['500', '1000']",
    "['1000', '5000']"
]
YEAR_RANGES_ORDERED = [
    "['-1000000000', '1944']",
    "['1944', '1972']",
    "['1972', '1991']",
    "['1991', '2005']",
    "['2005', '2015']",
    "['2015', '1000000000']"
]

COMBS_DP412_93_RESID = {
    "0":"0",
    "1":"1",
    "2":"0",
    "3":"1",
    "4":"1",
    "5":"1",
    "6":"1",
    "7":"1",
    "8":"1",
    "9":"1",
    "10":"1",
    "11":"1",
    "12":"1",
    "13":"1",
    "14":"1",
}

MAPPING_DP412_93_DESCR = {
    "0": "abitazioni adibite a residenza con carattere continuativo",
    "1": "collegi, luoghi di ricovero, case di pena, caserme, conventi",
    "2": "abitazioni adibite a residenza con occupazione saltuaria",
    "3": "edifici adibiti ad albergo, pensione ed attività simili",
    "4": "uffici e assimilabili",
    "5": "ospedali, cliniche, case di cura e assimilabili",
    "6": "cinema e teatri, sale di riunione per congressi e assimilabili",
    "7": "mostre, musei e biblioteche, luoghi di culto e assimilabili",
    "8": "bar, ristoranti, sale da ballo e assimilabili",
    "9": "attività commerciali e assimilabili",
    "10": "piscine, saune e assimilabili",
    "11": "palestre e assimilabili",
    "12": "servizi di supporto alle attività sportive",
    "13": "attività scolastiche",
    "14": "attività industriali, artigianali e assimilabili"
}

MAPPING_DP412_93_CODE = {
    "0": "E1(1)",
    "1": "E1(1)bis",
    "2": "E1(2)",
    "3": "E1(3)",
    "4": "E2",
    "5": "E3",
    "6": "E4(1)",
    "7": "E4(2)",
    "8": "E4(3)",
    "9": "E5",
    "10": "E6(1)",
    "11": "E6(2)",
    "12": "E6(3)",
    "13": "E7",
    "14": "E8"
}

# CODREG_TO_PROV = { # TESTING DICT
#     '21': ['021'],
#     '22': ['022']
# }

CODREG_TO_PROV = {
    '01': ['001', '002', '003', '004', '005', '006', '096', '103'],
    '02': ['007'],
    '03': ['012', '013', '014', '015', '016', '017', '018', '019', '020', '097', '098', '108'],
    '05': ['023', '024', '025', '026', '027', '028', '029'],
    '06': ['030', '031', '032', '093'],
    '07': ['008', '009', '010', '011'],
    '08': ['033', '034', '035', '036', '037', '038', '039', '040', '099'],
    '09': ['045', '046', '047', '048', '049', '050', '051', '052', '053', '100'],
    '10': ['054', '055'],
    '11': ['041', '042', '043', '044', '109'],
    '12': ['056', '057', '058', '059', '060'],
    '13': ['066', '067', '068', '069'],
    '14': ['070', '094'],
    '15': ['061', '062', '063', '064', '065'],
    '16': ['071', '072', '073', '074', '075', '110'],
    '17': ['076', '077'],
    '18': ['078', '079', '080', '101', '102'],
    '19': ['081', '082', '083', '084', '085', '086', '087', '088', '089'],
    '20': ['090', '091', '092', '095', '111'],
    '21': ['021'],
    '22': ['022']
}

CODPROV_TO_CODREG= {v:k for k, values in CODREG_TO_PROV.items() for v in values}

CODPROV_TO_PROV = {
    '001': 'Torino',
    '002': 'Vercelli',
    '003': 'Novara',
    '004': 'Cuneo',
    '005': 'Asti',
    '006': 'Alessandria',
    '096': 'Biella',
    '103': 'Verbano-Cusio-Ossola',
    '007': 'Aosta',
    '012': 'Varese',
    '013': 'Como',
    '014': 'Sondrio',
    '015': 'Milano',
    '016': 'Bergamo',
    '017': 'Brescia',
    '018': 'Pavia',
    '019': 'Cremona',
    '020': 'Mantova',
    '097': 'Lecco',
    '098': 'Lodi',
    '108': 'Monza e della Brianza',
    '023': 'Verona',
    '024': 'Vicenza',
    '025': 'Belluno',
    '026': 'Treviso',
    '027': 'Venezia',
    '028': 'Padova',
    '029': 'Rovigo',
    '030': 'Udine',
    '031': 'Gorizia',
    '032': 'Trieste',
    '093': 'Pordenone',
    '008': 'Imperia',
    '009': 'Savona',
    '010': 'Genova',
    '011': 'La Spezia',
    '033': 'Piacenza',
    '034': 'Parma',
    '035': "Reggio nell'Emilia",
    '036': 'Modena',
    '037': 'Bologna',
    '038': 'Ferrara',
    '039': 'Ravenna',
    '040': 'Forl�-Cesena',
    '099': 'Rimini',
    '045': 'Massa-Carrara',
    '046': 'Lucca',
    '047': 'Pistoia',
    '048': 'Firenze',
    '049': 'Livorno',
    '050': 'Pisa',
    '051': 'Arezzo',
    '052': 'Siena',
    '053': 'Grosseto',
    '100': 'Prato',
    '054': 'Perugia',
    '055': 'Terni',
    '041': 'Pesaro e Urbino',
    '042': 'Ancona',
    '043': 'Macerata',
    '044': 'Ascoli Piceno',
    '109': 'Fermo',
    '056': 'Viterbo',
    '057': 'Rieti',
    '058': 'Roma',
    '059': 'Latina',
    '060': 'Frosinone',
    '066': "L'Aquila",
    '067': 'Teramo',
    '068': 'Pescara',
    '069': 'Chieti',
    '070': 'Campobasso',
    '094': 'Isernia',
    '061': 'Caserta',
    '062': 'Benevento',
    '063': 'Napoli',
    '064': 'Avellino',
    '065': 'Salerno',
    '071': 'Foggia',
    '072': 'Bari',
    '073': 'Taranto',
    '074': 'Brindisi',
    '075': 'Lecce',
    '110': 'Barletta-Andria-Trani',
    '076': 'Potenza',
    '077': 'Matera',
    '078': 'Cosenza',
    '079': 'Catanzaro',
    '080': 'Reggio Calabria',
    '101': 'Crotone',
    '102': 'Vibo Valentia',
    '081': 'Trapani',
    '082': 'Palermo',
    '083': 'Messina',
    '084': 'Agrigento',
    '085': 'Caltanissetta',
    '086': 'Enna',
    '087': 'Catania',
    '088': 'Ragusa',
    '089': 'Siracusa',
    '090': 'Sassari',
    '091': 'Nuoro',
    '092': 'Cagliari',
    '095': 'Oristano',
    '111': 'Sud Sardegna',
    '021': 'Bolzano',
    '022': 'Trento'
}

REG_TO_CODREG = {
    'Piemonte': '01',
    "Valle d'Aosta": '02',
    'Lombardia': '03',
    'Veneto': '05',
    'Friuli Venezia Giulia': '06',
    'Liguria': '07',
    'Emilia Romagna': '08',
    'Toscana': '09',
    'Umbria': '10',
    'Marche': '11',
    'Lazio': '12',
    'Abruzzo': '13',
    'Molise': '14',
    'Campania': '15',
    'Puglia': '16',
    'Basilicata': '17',
    'Calabria': '18',
    'Sicilia': '19',
    'Sardegna': '20',
    'Bolzano': '21',
    'Trento': '22'
}

DICT_PROV = {
    'Rovigo': 'RO',
    'Savona': 'SV',
    'Livorno': 'LI',
    'Catania': 'CT',
    'Terni': 'TR',
    'Imperia': 'IM',
    'Sud Sardegna': 'SU',
    'Lodi': 'LO',
    'Salerno': 'SA',
    'Frosinone': 'FR',
    'Como': 'CO',
    'Firenze': 'FI',
    'Trieste': 'TS',
    'Sondrio': 'SO',
    'Potenza': 'PZ',
    'Treviso': 'TV',
    'Reggio di Calabria': 'RC',
    'La Spezia': 'SP',
    'Piacenza': 'PC',
    'Grosseto': 'GR',
    'Agrigento': 'AG',
    'Barletta-Andria-Trani': 'BT',
    'Crotone': 'KR',
    'Ancona': 'AN',
    'Bolzano': 'BZ',
    'Vicenza': 'VI',
    'Gorizia': 'GO',
    'Cuneo': 'CN',
    'Brescia': 'BS',
    'Matera': 'MT',
    'Prato': 'PO',
    'Pisa': 'PI',
    'Latina': 'LT',
    'Bergamo': 'BG',
    'Ravenna': 'RA',
    'Oristano': 'OR',
    "L'Aquila": 'AQ',
    'Varese': 'VA',
    'Trento': 'TN',
    'Siena': 'SI',
    'Macerata': 'MC',
    'Verona': 'VR',
    'Monza e della Brianza': 'MB',
    'Cosenza': 'CS',
    'Pistoia': 'PT',
    'Messina': 'ME',
    'Roma': 'RM',
    'Sassari': 'SS',
    'Alessandria': 'AL',
    'Bari': 'BA',
    'Viterbo': 'VT',
    'Benevento': 'BN',
    'Rieti': 'RI',
    'Modena': 'MO',
    'Bologna': 'BO',
    'Enna': 'EN',
    'Pavia': 'PV',
    'Caltanissetta': 'CL',
    'Campobasso': 'CB',
    'Trapani': 'TP',
    'Palermo': 'PA',
    'Perugia': 'PG',
    'Napoli': 'NA',
    'Pesaro e Urbino': 'PU',
    'Asti': 'AT',
    'Rimini': 'RN',
    'Padova': 'PD',
    'Ragusa': 'RG',
    'Udine': 'UD',
    'Nuoro': 'NU',
    "Forli'-Cesena": 'FC',
    'Foggia': 'FG',
    'Isernia': 'IS',
    'Genova': 'GE',
    'Pordenone': 'PN',
    'Torino': 'TO',
    'Brindisi': 'BR',
    'Novara': 'NO',
    'Arezzo': 'AR',
    'Siracusa': 'SR',
    'Belluno': 'BL',
    'Lucca': 'LU',
    'Vercelli': 'VC',
    'Fermo': 'FM',
    'Venezia': 'VE',
    'Taranto': 'TA',
    'Verbano-Cusio-Ossola': 'VB',
    'Chieti': 'CH',
    'Caserta': 'CE',
    'Pescara': 'PE',
    'Catanzaro': 'CZ',
    'Teramo': 'TE',
    "Reggio nell'Emilia": 'RE',
    'Cagliari': 'CA',
    'Aosta': 'AO',
    'Parma': 'PR',
    'Lecco': 'LC',
    'Massa Carrara': 'MS',
    'Cremona': 'CR',
    'Ascoli Piceno': 'AP',
    'Lecce': 'LE',
    'Ferrara': 'FE',
    'Biella': 'BI',
    'Vibo Valentia': 'VV',
    'Mantova': 'MN',
    'Avellino': 'AV',
    'Milano': 'MI'
}

DICT_PROV_REV = {v: k for k, v in DICT_PROV.items()}

MAPPING_CAT_TOP15 = {
    'resid_nzeb': 'Resid',
    'non_resid_nzeb': 'Altri Non Resid (hotel, cinema, teatri, palestre, musei e altri)',
    'uffici_nzeb': 'Uffici',
    'bar_risto_nzeb': 'Bar e Ristoranti',
    'industriale_artigianale_nzeb': 'Industriale e Artigianale'
}