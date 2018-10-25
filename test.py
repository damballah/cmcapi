from cmcapi import *

Ncrypto=cmc()

fJSON=Ncrypto.FichierJSON
gDatas=Ncrypto.GlobalDatas
idCoin=Ncrypto.RecupIdCrypto(fJSON,"VET")

price=Ncrypto.GetCryptoInfo(gDatas,idCoin,"price")
rank=Ncrypto.GetCryptoInfo(gDatas,idCoin,"rank")
change24h=Ncrypto.GetCryptoInfo(gDatas,idCoin,"change_24h")

print("RANK : "+ rank)
print("PRICE : "+ price)
print("CHANGE 24H : "+ change24h)














		
	

		



