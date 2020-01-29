import requests

API = "RGAPI-a6bb54d6-ef81-45ab-922b-cebf6477606d"
region= "euw1"
def ID(Summoner):
    URL = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner+"?api_key=" +API
    r = requests.get(URL)
    #print URL
    id = r.json()["id"]
    #print id
    return id

def summonerInfo(Summoner):
    URL = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner+"?api_key=" +API
    r = requests.get(URL)
    return r.json()

def accountId(Summoner):
    URL = "https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner+"?api_key=" +API
    r = requests.get(URL)
    #print URL
    return r.json()["accountId"]
    
def Matchlist(accountId):
    #print accountId
    URL = "https://"+region+".api.riotgames.com/lol/match/v4/matchlists/by-account/"+accountId+"?api_key="+API
    r = requests.get(URL)
    return r.json()

def matchInfo(gameId):
    URL = "https://"+region+".api.riotgames.com/lol/match/v4/matches/"+gameId+"?api_key="+API
    r = requests.get(URL)
    return r.json()
    
def spectator(id):
    URL = "https://"+region+".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+id+"?api_key="+API
    r = requests.get(URL)
    #print(URL)
    return r.json()

def league(id):
    URL="https://"+region+".api.riotgames.com/lol/league/v4/entries/by-summoner/"+id+"?api_key="+API
    r = requests.get(URL)
    #print URL
    return r.json()

def rangos(Summoner):
    #Summoner=str(raw_input("Summoner"))
    #Summoner="WhiiteRaabbit"
    idd = ID(Summoner)
    #accountIdd=accountId(Summoner)
    #Matchlist = Matchlist(accountId)
    #print Matchlist["matches"][0]
    #gameId = Matchlist["matches"][0]["gameId"]
    #print gameId
    #matchInfo(gameId)
    spec = spectator(idd)
    #print spec
    try:
        specTeams = spec["participants"]
    except Exception as error:
        print("No hay partida activa")
    else:
        print("\n\nEquipo 1:\n")
        for i in range(0,5):
            summonerName = specTeams[i]["summonerName"]
            info = summonerInfo(summonerName)
            nivel = info["summonerLevel"]
            id = info["id"]
            try:
                liga = league(id)[0]
            except IndexError:
                print(i+1, summonerName,"Nivel "+ str(nivel))
            else:
                tier=liga["tier"]
                rank=liga["rank"]
                print(i+1, summonerName +":","Nivel "+ str(nivel),", Rango "+tier, rank)
        print("\n\nEquipo 2:\n")
        for i in range(5,10):
            summonerName = specTeams[i]["summonerName"]
            info = summonerInfo(summonerName)
            nivel = info["summonerLevel"]
            id = info["id"]
            try:
                liga = league(id)[0]
            except IndexError:
                print(i+1, summonerName,"Nivel "+ str(nivel))
            else:
                tier=liga["tier"]
                rank=liga["rank"]
                print(i+1, summonerName +":","Nivel "+ str(nivel),", Rango "+tier, rank)

    