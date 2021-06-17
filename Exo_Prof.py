#Exo 1
dexiste = {'ltp':[15,14,17], 'proba-stat':[15,14,17], 'language C':[15,14,17], 'language Java':[15,14,17], 'SE':[15,14,17], 'Prograsys':[15,14,18], 'Python':[18,17,19], 'Web':[15,14,17], 'Analyse':[15,16,18], 'Algebre':[15,14,17], 'Anglais':[15,14,17], 'lsn':[15,14,17]}

val = [sum(dexiste['ltp'])/3, sum(dexiste['Prograsys'])/3, sum(dexiste['proba-stat'])/3, sum(dexiste['language C'])/3, sum(dexiste['language Java'])/3, sum(dexiste['Analyse'])/3, sum(dexiste['SE'])/3, sum(dexiste['Python'])/3, sum(dexiste['Web'])/3, sum(dexiste['Algebre'])/3, sum(dexiste['lsn'])/len('lsn')]
print(val)

moyenne = sum(val)/len(val)
print(moyenne)

#Exo 2

#Question 1
L = [0,1,2,3,4,5,6,7,8,9]

#Question 2
L[0] = L[0] + 11
L[1] = L[1] + 11
L[2] = L[2] + 11
L[3] = L[3] + 11
L[4] = L[4] + 11
L[5] = L[5] + 11
L[6] = L[6] + 11
L[7] = L[7] + 11
L[8] = L[8] + 11
L[9] = L[9] + 11

#Question 3
L.append(22)

#Question 4
L.extend((23,24))

#Question 5
L1 =L[::2]
L2 =L[1::2]
#Question 6
L.pop(3)



#Exo 3

d = {'nom':'Dupuis', 'prenom':'Jacque', 'age':30}

#Question a
d['prenom']= 'Jacques'

#Question b
d.keys()

#Question c
d.values()

#Question d
d.keys()

#Question e
print(d['prenom'] + ' ' + d['nom'] + 'a' + ' ' + str(d['age']) + ' ' + 'ans.')
