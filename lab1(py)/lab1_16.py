#Напишите скрипт, который на основе списка из 16 названий футбольных команд случайным образом формирует 4 группы по 4
#команды, а также выводит на консоль календарь всех игр (игры должны проходить по средам, раз в 2 недели, начиная с 15 сентября
#текущего года). Даты игр необходимо выводить в формате «15/09/2021, 22:45».


football_teams = ['Arsenal', 'Bedford', 'Bashley', 'Aston',
                      'Baldock Town', 'Blackpool', 'Alfreton Town', 'Basford United',
                      'Brocton', 'Atherton Laburnum Rovers', 'Aston Villa', 'Brimscombe & Thrupp',
                      'Annfield Plain', 'Aldershot Town', 'Bamber Bridge', 'Bootle'
                      ]
from itertools import combinations
football_teams = combinations(football_teams, 2)
from datetime import datetime, timedelta
dates = datetime(2021, 9, 15, 13, 30)
groups = [football_teams[i*4:i*4+4] for i in range(4)]
print("Groups")
[print(i) for i in football_teams]

print("\nGames")
for i in football_teams:
        print(i, dates.strftime("%d/%m/%Y %H:%M"))
        dates += timedelta(days=14, hours=4)

