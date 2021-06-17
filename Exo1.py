dexiste = {'ltp':[15,14,17], 'proba-stat':[15,14,17], 'language C':[15,14,17], 'language Java':[15,14,17], 'SE':[15,14,17], 'Prograsys':[15,14,18], 'Python':[18,17,19], 'Web':[15,14,17], 'Analyse':[15,16,18], 'Algebre':[15,14,17], 'Anglais':[15,14,17], 'lsn':[15,14,17]}

val = [sum(dexiste['ltp'])/3, sum(dexiste['Prograsys'])/3, sum(dexiste['proba-stat'])/3, sum(dexiste['language C'])/3, sum(dexiste['language Java'])/3, sum(dexiste['Analyse'])/3, sum(dexiste['SE'])/3, sum(dexiste['Python'])/3, sum(dexiste['Web'])/3, sum(dexiste['Algebre'])/3, sum(dexiste['lsn'])/len('lsn')]
print(val)

moyenne = sum(val)/len(val)
print(moyenne)
