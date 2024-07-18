import sys

matchs = {}
team_stats = {}
players_stats = {}

# Переменные для верной обработки результатов
name, minute, commands = '', 91, ''
number_match = 0
for info in sys.stdin:
    if info.strip().endswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        number_match += 1
        data = info.strip().split()
        index = data.index('-')
        command1 = ' '.join(word.strip(' "') for word in data[0:index])

        command2 = ' '.join(word.strip(' "') for word in data[index + 1: -1])


        score1, score2 = map(int, data[-1].strip().split(':'))
        matchs.setdefault((command1.strip(' "'), command2.strip(' "')), {}).setdefault('score', (score1, score2))
        team_stats.setdefault(command1, {}).setdefault('score_open', 0)
        team_stats.setdefault(command2, {}).setdefault('score_open', 0)
        # Добавляем первой команде количество забитых голов и матч +1
        team_stats.setdefault(command1, {}).setdefault('all_goals', 0)
        team_stats.setdefault(command1, {}).setdefault('matches', 0)
        team_stats[command1]['all_goals'] += score1
        team_stats[command1]['matches'] += 1
        # Добавляем второй команде количество забитых голов и матч +1

        team_stats.setdefault(command2, {}).setdefault('all_goals', 0)
        team_stats.setdefault(command2, {}).setdefault('matches', 0)
        team_stats[command2]['all_goals'] += score2
        team_stats[command2]['matches'] += 1

        # Вводим имена забивших первой команды
        for p in range(score1):
            player = input().strip().split()
            minutes = int(player[-1].strip(" '"))
            del player[-1]
            player = ' '.join(player)

            players_stats.setdefault(player, {}).setdefault('team', command1)
            players_stats.setdefault(player, {}).setdefault('score_open', 0)

            # добавляем игроку голы
            players_stats.setdefault(player, {}).setdefault('all_goals', []).append(minutes)
            if minutes < minute:
                name = player
                commands = command1
                minute = minutes

        # Имена забивших второй команды
        for j in range(score2):
            player = input().strip().split()
            minutes = int(player[-1].strip(" '"))
            del player[-1]
            player = ' '.join(player)

            players_stats.setdefault(player, {}).setdefault('team', command2)

            players_stats.setdefault(player, {}).setdefault('all_goals', []).append(minutes)
            players_stats.setdefault(player, {}).setdefault('score_open', 0)
            if minutes < minute:
                name = player
                commands = command2
                minute = minutes

        # Если у нас был забит хоть один гол в матче
        if score1 > 0 or score2 > 0:
            # Добавляем в статистику команды +1 в открытие счета
            team_stats[commands]['score_open'] += 1
            # Добавляем в статистику игрока +1 в открытие счета
            players_stats[name]['score_open'] += 1
            name, minute, commands = '', 91, ''

    #  Количество голов, забитое данной командой за все матчи
    elif info.startswith('Total goals for'):
        data = info.strip().split()
        name_team = ' '.join((word.strip('"') for word in data[3::]))
        team_stats.setdefault(name_team, {}).setdefault('all_goals', 0)
        print(team_stats[name_team]['all_goals'])

    #  Количество голов, забитое данным игроком за все матчи
    elif info.startswith('Total goals by'):
        data = info.strip().split()
        name_player = ' '.join((word.strip('"') for word in data[3::]))
        players_stats.setdefault(name_player, {}).setdefault('all_goals', [])
        print(len(players_stats[name_player]['all_goals']))

    # Cреднее количество голов, забиваемое данной командой за один матч
    elif info.startswith('Mean goals per game for'):
        data = info.strip().split()
        name_team = ' '.join((word.strip('"') for word in data[5::]))
        print(team_stats[name_team]['all_goals'] / team_stats[name_team]['matches'])

    # Cреднее количество голов, забиваемое данным игроком за один матч его команды
    elif info.startswith('Mean goals per game by'):
        data = info.strip().split()
        name_player = ' '.join((word.strip('"') for word in data[5::]))
        p = players_stats[name_player]['team']
        print(len(players_stats[name_player]['all_goals']) / team_stats[p]['matches'])

    # Количество голов, забитых данным игроком ровно на указанной минуте матча
    elif info.startswith('Goals on minute'):
        data = info.strip().split()
        name_player = ' '.join(data[5::])
        m = int(data[3].strip("'"))
        players_stats.setdefault(name_player, {}).setdefault('all_goals', [])
        print(sum(1 for minutes in players_stats[name_player]['all_goals'] if minutes == m))

    # количество голов, забитых данным игроком на минутах с первой по T-ю включительно
    elif info.startswith('Goals on first'):
        data = info.strip().split()
        name_player = ' '.join(data[6::])
        m = int(data[3].strip("'"))
        players_stats.setdefault(name_player, {}).setdefault('all_goals', [])
        print(sum(1 for minutes in players_stats[name_player]['all_goals'] if 1 <= minutes <= m))

    elif info.startswith('Goals on last'):
        data = info.strip().split()
        name_player = ' '.join(data[6::])
        m = int(data[3].strip("'"))
        players_stats.setdefault(name_player, {}).setdefault('all_goals', [])
        print(sum(1 for minutes in players_stats[name_player]['all_goals'] if (91 - m) <= minutes <= 90))

    elif info.startswith('Score opens by'):
        data = info.strip().split()
        name = ' '.join(word.strip() for word in data[3::])
        if '"' in name:
            name = name.strip(' "')
            team_stats.setdefault(name, {}).setdefault('score_open', 0)
            print(team_stats[name]['score_open'])
        else:
            players_stats.setdefault(name, {}).setdefault('score_open', 0)
            print(players_stats[name]['score_open'])



