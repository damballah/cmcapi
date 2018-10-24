from cmcapi import *
from datetime import datetime

Ncrypto=cmc()

a=Ncrypto.FichierJSON
b=Ncrypto.GlobalDatas
Ncrypto.IdCrypto=RecupIdCrypto(a,"VET")


print(a)
#print(b)
print(Ncrypto.IdCrypto)









		
	

		



