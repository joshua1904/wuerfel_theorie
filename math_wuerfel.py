import time
from collections import defaultdict

from tqdm import tqdm
def get_all_possibilities() -> list:
    possibilities = list()
    for i in range(1, 7):
        for j in range(1, 7):
            for y in range(1, 7):
                for z in range(1, 7):
                    possibilities.append([i, j, y, z])
    return possibilities

def is_win(game_val: tuple):
    if game_val.count(game_val[0]) >= 3:
        return True
    if game_val.count(game_val[1]) >= 3:
        return True
    return False

def remove_values(arr_1, min_value):
    return arr_1[0] - min_value,arr_1[1] - min_value, arr_1[2] - min_value, arr_1[3] - min_value
def add_values(arr_1: tuple, arr_2):
    return arr_1[0] + arr_2[0], arr_1[1] + arr_2[1], arr_1[2] + arr_2[2],arr_1[3] + arr_2[3]

def run_game(current_game_state: dict, possibilities: list, already_won):
    """Erstellt ein neues state dictonary und printet die wins und games der runde"""
    game_dict = defaultdict(int)
    games = already_won
    wins = already_won
    for game_state, value in tqdm(current_game_state.items()):
        for i in possibilities:
            new_state = add_values(game_state, i)
            #zieht von allem dem minimalen wert ab um das dictonary kleiner zu halten
            min_value = min(new_state)
            new_state = remove_values(new_state, min_value)
            if not is_win(new_state):
                #sortiert die würfelsummen nach groeße um das dict kleiner zu halten
                new_state = tuple(sorted(new_state))
                game_dict[new_state] += value
            else:
                wins += value
            games += value
    print(wins, games, wins/games)
    return game_dict, wins

def just_count(current_game_state: dict, possibilities, already_won):
    """Zählt nur die wins und games aber fertigt kein dictonary mehr an
    FÜr Letzte runde benutzen"""
    wins = already_won
    games = already_won
    for key, value in tqdm(current_game_state.items()):
        game_state = [int(i) for i in key.split("-")]
        for i in possibilities:
            if is_win(add_values(i, game_state)):
                wins += value
            games += value
    print(wins, games, wins/games)


def run_games(games_to_simulate: int):
    possibilities = get_all_possibilities()
    current_game = {(0,0,0,0): 1}
    already_won = 0
    for i in range(games_to_simulate - 1):
        start_time = time.time()
        current_game, already_won = run_game(current_game, possibilities, already_won)
        end_time = time.time()
        print(end_time - start_time)
    just_count(current_game, possibilities, already_won)

start_time = time.time()
run_games(15)
end_time = time.time()

print(end_time- start_time)
