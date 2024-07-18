def play_game(x, y, p):
    n = y
    all_variants_alternative = []
    round = 0
    round_main = 0
    y -= x
    if y <= 0:
        return 1

    if x <= y and x <= p:
        return -1
    # Так как казарма с первого хода не упала, она спавнит солдат
    soldiers = p
    round_main += 1  # Счетчик роундов для основной ветки

    for _ in range(1, n + 1):
        # После хода у меня может возникуть ситуация, когда здоровье барака меньше кол-ва моих солдат
        # Пробуем решение, когда сносим сначала барак
        if y <= x:
            fix_round = round_main
            barack = y
            mine_s = x
            enemy = soldiers
            while barack > 0 or enemy > 0:
                reserve = mine_s - barack
                barack = 0
                enemy -= reserve
                mine_s -= enemy
                round += 1
                if mine_s <= 0:
                    round = 0
                    break
            else:
                round += fix_round
                all_variants_alternative.append(round)
                round = 0
        # В остальных случаях выбираем стратегию отталкиваясь от кол-ва наших солдат и кол-ва солдат противника
        # Если моих солдат больше, то убиваем сначала солдат , потом атакуем барак
        if x > soldiers:
            reserve = x - soldiers
            soldiers = 0
            y -= reserve
            round_main += 1
            if y > 0:
                soldiers += p
        else:
            reserve = x - y
            y = 0
            soldiers -= reserve
            x -= soldiers
            round_main += 1
        if y <= 0 and soldiers <= 0:
            break
        if x <= 0:
            round_main = -1
            break

    if round_main == -1 and all_variants_alternative == []:
        return -1
    if round_main == -1:
        return min(all_variants_alternative)
    return min(round_main, min(all_variants_alternative))


x, y, p = int(input()), int(input()), int(input())
print(play_game(x, y, p))


