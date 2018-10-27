import urllib.request
import json

# Récupération du fichier JSON en utilisant l'API de CoinMarketCap
def ifSymboleExist(symbolCrypto,LesDatas):
	i=0
	flag=False
	for values in LesDatas['data']:
		symb=LesDatas['data'][i]['symbol']
		if symb==symbolCrypto:
			flag=True
		i=i+1
	return flag
	
def getIdFromSymbol(symbolCrypto,LesDatas):
	i=0
	flag=False
	for values in LesDatas['data']:
		symb=LesDatas['data'][i]['symbol']
		if symb==symbolCrypto:
			id=LesDatas['data'][i]['id']
		i=i+1
	return id
	
def GetDatasFromApi(AdresseURL):
	with urllib.request.urlopen(AdresseURL) as url:
		LesDatas = url.read().decode()
	return LesDatas
	
def MakeJsonFromDatas(Datas):
	JsonDatas=json.loads(Datas)
	return JsonDatas

	
def ConfigGetApiFromIdWithDevise(devise):
	if devise!="USD":
		urlFromIdWithDevise="https://api.coinmarketcap.com/v2/ticker/" + str(id) + "/?convert=" + devise
	else:
		urlFromIdWithDevise="https://api.coinmarketcap.com/v2/ticker/" + str(id) + "/"
		devise="USD"
	return urlFromIdWithDevise

	

class cmc():
	def __init__(self,Symbole,devise):
		
		urlApiListingGlobal="https://api.coinmarketcap.com/v2/listings/"
		
		Symbole=Symbole.upper()
		devise=devise.upper()
		self.symbol=Symbole
		self.devise=devise
		
		
		listingPrincipal=GetDatasFromApi(urlApiListingGlobal)
		listingJsonPrin=MakeJsonFromDatas(listingPrincipal)
			
		if ifSymboleExist(Symbole,listingJsonPrin)==True:
			
			id=getIdFromSymbol(Symbole,listingJsonPrin)
			
			if self.devise!="":
				urlFromIdWithDevise="https://api.coinmarketcap.com/v2/ticker/" + str(id) + "/?convert=" + self.devise
				
			else:
				urlFromIdWithDevise="https://api.coinmarketcap.com/v2/ticker/" + str(id) + "/"
				self.devise="USD"


			print(urlFromIdWithDevise)

			urlApiGetPropertyFromId=urlFromIdWithDevise
			listingParCrypto=GetDatasFromApi(urlApiGetPropertyFromId)
			listingJsonCrypto=MakeJsonFromDatas(listingParCrypto)
			
			self.id=str(listingJsonCrypto['data']['id'])
			self.name=str(listingJsonCrypto['data']['name'])
			self.symbol=str(listingJsonCrypto['data']['symbol'])
			self.websiteslug=str(listingJsonCrypto['data']['website_slug'])
			self.rank=str(listingJsonCrypto['data']['rank'])
			self.circulating=str(listingJsonCrypto['data']['circulating_supply']) + " " + self.symbol
			self.total=str(listingJsonCrypto['data']['total_supply']) + " " + self.symbol
			self.max=str(listingJsonCrypto['data']['max_supply']) + " " + self.symbol
			self.price=str(listingJsonCrypto['data']['quotes'][self.devise]['price']) + " "+ self.devise
			self.marketcap=str(listingJsonCrypto['data']['quotes'][self.devise]['market_cap']) + " "+ self.devise
			self.vol24h=str(listingJsonCrypto['data']['quotes'][self.devise]['volume_24h']) + " "+ self.devise
			self.change1h=str(listingJsonCrypto['data']['quotes'][self.devise]['percent_change_1h']) + "%"
			self.change24h=str(listingJsonCrypto['data']['quotes'][self.devise]['percent_change_24h']) + "%"
			self.change7d=str(listingJsonCrypto['data']['quotes'][self.devise]['percent_change_7d']) + "%"

		else:
			print("\nErr : la variable 'symbol' est mal affectée. \nSoit la valeur est vide, soit le symbol de la crypto demandée n'existe pas.")
			print('Exemple correct avec le bitcoin : newInfoCrypto=cmc("btc")')
			print("")
			
		
		
		
		 
		
		
		
	










		