import fflogsApi
import json
import csv

# {73: 9, 74: 10, 75: 11, 76: p1, 77: p2}


def get():
    # {73: 9, 74: 10, 75: 11, 76: p1, 77: p2}
    partitions = [13] # only echo
    fights = [73, 74, 75, 76, 77]
    servers = ['Balmung', 'Brynhildr', 'Coeurl', 'Diabolos', 'Goblin', 'Malboro', 'Mateus', 'Zalera']
    number = 1
    check = {'Balmung': [], 'Brynhildr': [], 'Coeurl': [], 'Diabolos': [], 'Goblin': [], 'Malboro': [], 'Mateus': [], 'Zalera': []}
    for partition in partitions:
        for fight in fights:
            for server in servers:
                result = fflogsApi.eligible(server, fight, partition, number)
                while result['data']['worldData']['encounter']['characterRankings']['count'] != 0:
                    number += 1
                    for player in result['data']['worldData']['encounter']['characterRankings']['rankings']:
                        if fight == 73 or fight == 74:
                            if player['name'] not in check[server]:
                                check[server].append(player['name'])
                        else:
                            if player['name'] in check[server]:
                                check[server].remove(player['name'])
                    result = fflogsApi.eligible(server, fight, partition, number)
                number = 1
    with open('eligible.txt', 'w') as outfile:
        json.dump(check, outfile)


def remover():
    with open('eligible.txt') as json_file:
        data_full = json.load(json_file)
    partitions = [1, 7]
    fights = [75, 76, 77]
    servers = ['Balmung', 'Brynhildr', 'Coeurl', 'Diabolos', 'Goblin', 'Malboro', 'Mateus', 'Zalera']
    number = 1
    for partition in partitions:
        for fight in fights:
            for server in servers:
                result = fflogsApi.eligible(server, fight, partition, number)
                while result['data']['worldData']['encounter']['characterRankings']['count'] != 0:
                    number += 1
                    for player in result['data']['worldData']['encounter']['characterRankings']['rankings']:
                        if player['name'] in data_full[server]:
                            data_full[server].remove(player['name'])
                    result = fflogsApi.eligible(server, fight, partition, number)
                number = 1
    with open('eligible.txt', 'w') as outfile:
        json.dump(data_full, outfile)


def csv2():
    # [name, job, world, fflogs]
    out = []
    with open('eligible.txt') as json_file:
        data = json.load(json_file)
    for server in data:
        for player in data[server]:
            try:
                url = player.replace(' ', '%20')
                roles = fflogsApi.role(player, server, 73)
                job = roles['data']['characterData']['character']['encounterRankings']['ranks'][0]['bestSpec']
                adder = [player, job, server, f'https://www.fflogs.com/character/na/{server}/{url}#partition=13']
                out.append(adder)
            except TypeError:
                try:
                    url = player.replace(' ', '%20')
                    roles = fflogsApi.role(player, server, 74)
                    job = roles['data']['characterData']['character']['encounterRankings']['ranks'][0]['bestSpec']
                    adder = [player, job, server, f'https://www.fflogs.com/character/na/{server}/{url}#partition=13']
                    out.append(adder)
                except TypeError:
                    url = player.replace(' ', '%20')
                    adder = [player, 'unknown1', server, f'https://www.fflogs.com/character/na/{server}/{url}#partition=13']
                    out.append(adder)
            except IndexError:
                try:
                    url = player.replace(' ', '%20')
                    roles = fflogsApi.role(player, server, 74)
                    job = roles['data']['characterData']['character']['encounterRankings']['ranks'][0]['bestSpec']
                    adder = [player, job, server, f'https://www.fflogs.com/character/na/{server}/{url}#partition=13']
                    out.append(adder)
                except IndexError:
                    url = player.replace(' ', '%20')
                    adder = [player, 'unknown2', server, f'https://www.fflogs.com/character/na/{server}/{url}#partition=13']
                    out.append(adder)

    outss = open('output.csv', 'w', newline='')
    # outDictWriter = csv.DictWriter(outss, ['Team', 'Name', 'Role', 'Class', 'World', 'FFlogs', 'Note'])
    outDictWriter = csv.DictWriter(outss, ['Team', 'Name', 'Role', 'Class', 'World', 'FFlogs', 'Note'])
    outDictWriter.writeheader()
    for listing in out:
        job = get_role(listing[1])
        outDictWriter.writerow({'Name': listing[0], 'Role': job, 'Class': listing[1], 'World': listing[2], 'FFlogs': listing[3]})
    outss.close()

    with open('eligible2.txt', 'w') as outfile:
        json.dump(out, outfile)


def get_role(job):
    jobbs = {'melee':['Monk', 'Samurai', 'Dragoon', 'Ninja'], 'ranged': ['Bard', 'Machinist', 'Dancer'], 'caster': ['BlackMage', 'RedMage', 'Summoner'], 'tank':['Paladin', 'Warrior', 'Gunbreaker', 'DarkKnight'], 'healer':['WhiteMage', 'Scholar', 'Astrologian']}
    for key, value in jobbs.items():
        if job in value:
            return key


csv2()

