import requests

API = "RGAPI-a1682f06-5d33-4969-9ea8-e99cdabe10ba"
region = "euw1"


def regionn(palabra):
    region = palabra


def ID(Summoner):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner + "?api_key=" + API
    r = requests.get(URL)
    # print URL
    idd = r.json()["id"]
    # print id
    return idd


def summonerInfo(Summoner):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner + "?api_key=" + API
    r = requests.get(URL)
    return r.json()


def accountId(Summoner):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner + "?api_key=" + API
    r = requests.get(URL)
    # print URL
    return r.json()["accountId"]

    
def Matchlist(accountId):
    # print accountId
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + API
    r = requests.get(URL)
    return r.json()


def matchInfo(gameId):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + gameId + "?api_key=" + API
    r = requests.get(URL)
    return r.json()

    
def spectator(id):
    URL = "https://" + region + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + id + "?api_key=" + API
    r = requests.get(URL)
    # print(URL)
    return r.json()

def league(id):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + API
    r = requests.get(URL)
    # print URL
    return r.json()


def rangos(Summoner):
    # Summoner=str(raw_input("Summoner"))
    # Summoner="WhiiteRaabbit"
    idd = ID(Summoner)
    salida = ("")
    # accountIdd=accountId(Summoner)
    # Matchlist = Matchlist(accountId)
    # print Matchlist["matches"][0]
    # gameId = Matchlist["matches"][0]["gameId"]
    # print gameId
    # matchInfo(gameId)
    spec = spectator(idd)
    # print spec
    try:
        specTeams = spec["participants"]
    except Exception as error:
        salida += "No hay partida activa"
    else:
        salida+="Tiempo: " + str(int(spec["gameLength"]/60))+":"+str(spec["gameLength"]%60) +'\n'
        salida += ("\n\nEquipo 1:\n")
        for i in range(0, 5):
            summonerName = specTeams[i]["summonerName"]
            info = summonerInfo(summonerName)
            nivel = info["summonerLevel"]
            id = info["id"]
            try:
                liga = league(id)[0]
            except IndexError:
                # salida+=str((i+1, summonerName,"Nivel "+ str(nivel),'\n'))
                salida += str(i + 1)
                salida += (". ")
                salida += str(summonerName)
                salida += (": Nivel ")
                salida += str(str(nivel) + '\n')
            else:
                tier = liga["tier"]
                rank = liga["rank"]
                # salida+=str((i+1, summonerName +":","Nivel "+ str(nivel),", Rango "+tier, rank,'\n'))
                salida += str(i + 1)
                salida += (". ")
                salida += str(summonerName) 
                salida += (": Nivel ")
                salida += str(nivel)
                salida += (", Rango ")
                salida += str(tier + " " + rank + '\n')
        salida += ("\n\nEquipo 2:\n")
        for i in range(5, 10):
            summonerName = specTeams[i]["summonerName"]
            info = summonerInfo(summonerName)
            nivel = info["summonerLevel"]
            id = info["id"]
            try:
                liga = league(id)[0]
            except IndexError:
                salida += str(i + 1)
                salida += (". ")
                salida += str(summonerName)
                salida += (": Nivel ")
                salida += str(str(nivel) + '\n')
            else:
                tier = liga["tier"]
                rank = liga["rank"]
                salida += str(i + 1)
                salida += (". ")
                salida += str(summonerName) 
                salida += (": Nivel ")
                salida += str(nivel)
                salida += (", Rango ")
                salida += str(tier + " " + rank + '\n')

    return salida
