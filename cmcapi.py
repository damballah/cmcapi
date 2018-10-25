import urllib.request
import json
from datetime import datetime

	# Générateur du nom de fichier JSON reprenant la date et l'heure système #
def GenNomDeFichierJson():
	T=str(datetime.now())
	T=T.replace('-','')
	T=T.replace(':','')
	T=T.replace('.','')
	T=T.replace(' ','')
	NomFichierJson="CoinMarketCap_"+T+".json"
	return NomFichierJson

	# Récupération du fichier JSON en utilisant l'API de CoinMarketCap
def GetCMCJson(NomDeFichier):
	LesDatas=""
	with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/") as url:
		LesDatas = json.loads(url.read().decode())
		with open(NomDeFichier, 'w') as f:
			f.write(json.dumps(LesDatas, indent=4))
	return LesDatas
	
	''' Récupération de l'id d'une crypto dans le fichier JSON en passant
		en paramètre le nom du fichier JSON et le symbole de la crypto '''
		
class cmc():
	""" Classe permettant de jouer avec l'API de coinmarketcap """
	
	def __init__(self):
		
		self.FichierJSON=GenNomDeFichierJson()
		self.GlobalDatas=GetCMCJson(self.FichierJSON)
	

	def RecupIdCrypto(self,leFichier,SymbCrypto):
		nLigne=0
		tLigne=0
		laBonneLigne=0
		SiExiste=False
	
		f=open(leFichier, "r")
		for line in f.readlines():
			nLigne=nLigne+1
			if SymbCrypto in line:
				laBonneLigne=nLigne-2
				SiExiste=True				
		f.close
		
		if SiExiste==True:
			f=open(leFichier,"r")
			for line in f.readlines():
				tLigne=tLigne+1
				if tLigne==laBonneLigne:
					#print(line)
					id=line
					id=id.replace(',','')
					id=id.replace('"id": ','')
					id=id.replace(' ','')	
			f.close()
		else:
			id="id non trouvé !"
			nLigne=0
			tLigne=0
			laBonneLigne=0
			SiExiste=False
		
		return(id)
	
	def GetCryptoInfo(self,GlbDatas,IdCrypto,Valeur):
		if IdCrypto!="id non trouvé !":
			LaValeur=""
			if Valeur=="name":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['name'])
			elif Valeur=="symbol":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['symbol'])
			elif Valeur=="website_slug":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['website_slug'])
			elif Valeur=="rank":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['rank'])
			elif Valeur=="circulating_supply":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['circulating_supply'])
			elif Valeur=="total_supply":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['total_supply'])
			elif Valeur=="max_supply":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['max_supply'])
			elif Valeur=="price":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['quotes']['USD']['price']) + "$"
			elif Valeur=="volume_24h":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['quotes']['USD']['volume_24h']) + "$"
			elif Valeur=="market_cap":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['quotes']['USD']['market_cap']) + "$"
			elif Valeur=="change_1h":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['quotes']['USD']['percent_change_1h']) + "%"
			elif Valeur=="change_24h":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['quotes']['USD']['percent_change_24h']) + "%"
			elif Valeur=="change_7d":
				LaValeur=str(GlbDatas['data'][IdCrypto.rstrip()]['quotes']['USD']['percent_change_7d']) + "%"
			else:
				LaValeur="Err : Valeur vide où non existante"
		return LaValeur
		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		