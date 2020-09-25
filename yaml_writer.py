import yaml
import pandas as pd

intents = pd.read_csv('../mira-proj/intents.csv')

dict_file = []

prevIntent = ''
utterances = []
for index, row in intents.iterrows():
    thisIntent = row['Intent']
    if (thisIntent == prevIntent or prevIntent == ''):
        utterances.append(row['Utterances'])
    else: 
        new_intent = { thisIntent : utterances }
        dict_file.append(new_intent)
        #print(new_intent)
        utterances = []
    
    prevIntent = thisIntent

thisIntent = intents.iloc[0]['Intent']
utterances =  ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']
new_intent = { thisIntent : utterances }
#dict_file.append(new_intent)
#print(dict_file)
#dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']}]

#new_intent = {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}

#dict_file.append(new_intent)

#with open(r'.\store_file.yaml', 'w') as file:
#    documents = yaml.dump(dict_file, file)

stream = open(".\store_file.yaml'", 'r')
for key, value in dictionary.items():
    print (key + " : " + str(value))

