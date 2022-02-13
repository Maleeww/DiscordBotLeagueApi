import requests

# Need to change API key every 24h 
# https://developer.riotgames.com/
API = "RGAPI-f3cc52f6-5fc0-43e2-b6dc-671a96175002"
region = "euw1"
# https://developer.riotgames.com/docs/lol


def regionn(palabra):
    # Change region for the code to use, by default "euw1"
    # Options: br1 eun1 euw1 jp1 kr la1 la2 na1 oc1 ru
    global region 
    region = palabra


def ID(Summoner):
    # Get ID from summoner name
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner + "?api_key=" + API
    r = requests.get(URL)
    idd = r.json()["id"]
    return idd


def summonerInfo(Summoner):
    # Get all JSON info from summoner name
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner + "?api_key=" + API
    r = requests.get(URL)
    return r.json()


def accountId(Summoner):
    # Get account ID from summoner name
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + Summoner + "?api_key=" + API
    r = requests.get(URL)
    return r.json()["accountId"]

    
def Matchlist(accountId):
    # Get match list (history) from accId
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + API
    r = requests.get(URL)
    return r.json()


def matchInfo(gameId):
    # Get match info from gameId
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + gameId + "?api_key=" + API
    r = requests.get(URL)
    return r.json()

    
def spectator(idd):
    # Get active game (spectate) from user id
    URL = "https://" + region + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + idd + "?api_key=" + API
    r = requests.get(URL)
    return r.json()

def league(idd):
    # Get active season's league from user id
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + idd + "?api_key=" + API
    r = requests.get(URL)
    return r.json()


def rangos(Summoner):
    # Get team's and enemy team's active season's ranks from one of their summoner names
    idd = ID(Summoner)
    salida = ("")
    spec = spectator(idd)
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
            idd = info["id"]
            try:
                liga = league(idd)[0]
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
        salida += ("\n\nEquipo 2:\n")
        for i in range(5, 10):
            summonerName = specTeams[i]["summonerName"]
            info = summonerInfo(summonerName)
            nivel = info["summonerLevel"]
            idd = info["id"]
            try:
                liga = league(idd)[0]
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
