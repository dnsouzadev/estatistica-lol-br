from riotwatcher import LolWatcher

api_key = 'SUA API KEY'
# coloca sua key ai em cima dentro das aspas
watcher = LolWatcher(api_key)
my_region = 'br1'
# essa e a regiao br1 nosso brasil mas pode mudar caso queira pegar de outra regiao



def printStats(SummonerName):
    summoner = watcher.summoner.by_name(my_region, SummonerName)
    stats = watcher.league.by_summoner(my_region, summoner['id'])

    tier = stats[0]['tier']
    rank = stats[0]['rank']
    lp = stats[0]['leaguePoints']

    wins = int(stats[0]['wins'])
    losses = int(stats[0]['losses'])
    winrate = ((wins / (wins + losses)) * 100)
    winrate = round(winrate, 2)
    winrate = str(winrate) + "%"

    print("O elo de", SummonerName ,"e:" , tier, rank , "com" , lp , "pontos e" , winrate , "de winrate")
nick = input(str("Qual o nick: "))
printStats(nick)
