'''
Created on Nov 12, 2021

@author: pc786

'''

import re


message = 'Om uppdragetStartdatum: 2021-12-01Slutdatum: 2022-06-30Omfattning: 100%Ort: GöteborgAnsök senast: 2021-12-15Referensnummer: 179667'
print (re.findall(r'(\d+(?:\.\d+)?)','Startdatum'))