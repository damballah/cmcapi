from cmcapi import cmc

xrp=cmc("xrp","eur")

print("")
print("INFOS SUR LE XRP : ")
print("------------------ ")
print("")

numId="Numéro ID dans l'API CoinMarketCap : "+ xrp.id
classement="Classé n°" + xrp.rank
nom="Nom : " + xrp.name
symbol="Symbole : " + xrp.symbol
webslug="WebsiteSlug : " + xrp.websiteslug
marketcap="MarketCap actuel : " + xrp.marketcap + " " + xrp.devise
circulation="Monnaie en circulation : " + xrp.circulating + " " + xrp.symbol
coinstotal="Total monnaie : " + xrp.total + " " + xrp.symbol
maxcreacoin="Maximum prévu : " + xrp.max + " " + xrp.symbol
prixactuel="Prix actuel : " + xrp.price + " " + xrp.devise
vol24="Volume échangé en 24h : " + xrp.vol24h + " " + xrp.devise
tauxChange1h="Taux de change depuis 1h : " + xrp.change1h + "%"
tauxChange24h="Taux de change depuis 24h : " + xrp.change24h + "%"
tauxChange7j="Taux de change depuis 7 jours : " + xrp.change7d + "%"

print(numId)
print(classement)
print(nom)
print(symbol)
print(webslug)
print("")
print(marketcap)
print(circulation)
print(coinstotal)
print(maxcreacoin)
print(prixactuel)
print("")
print(vol24)
print(tauxChange1h)
print(tauxChange24h)
print(tauxChange7j)
print("")
print("-------------------- ")
print("FIN DES INFORMATIONS")
print("")





















		
	

		



