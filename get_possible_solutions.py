


def get_all_possible_solutions_of_this_round(start_array):
    solution_array = list()
    for i in range(1, 7):
        for j in range(1, 7):
            for y in range(1, 7):
                for z in range(1, 7):
                    value = start_array[0] + i
                    value_2 = start_array[1] + j
                    value_3 = start_array[2] + y
                    value_4 = start_array[3] + z
                    solution_array.append([value, value_2, value_3, value_4])
    return solution_array

def is_win(arr: list()):
    for i in range(2):
        x = arr.count(arr[i])
        if arr.count(arr[i]) >= 3:
            return True
    return False

def get_wins(solution_array):
    win_array = []
    for i in solution_array:
        x = is_win(i)
        if x:
            win_array.append(i)
    return win_array

def remove_wins(solutions_array: list, win_array: list):
    for i in win_array:
        solutions_array.remove(i)
    return solutions_array

"""
second_round_solutions = list()
x = get_all_possible_solutions_of_this_round([0, 0, 0, 0])
y = get_wins(x)
for i in remove_wins(x, y):
    second_round_solutions.append(i)

print(second_round_solutions)
wins = 0
possibilities = 0
"""

def get_possibilities_for_all_rounds(arr: list()):
    possibilitie_list = list()
    for i in arr:
        possibilitie_list = possibilitie_list + get_all_possible_solutions_of_this_round(i)
    return possibilitie_list

def get_winrate_of_rounds(rounds: int):
    game_arr = [[0, 0, 0, 0]]
    for i in range(0, rounds):
        game_arr = get_possibilities_for_all_rounds(game_arr)
        win_arr = get_wins(game_arr)
        possibilities = len(game_arr)
        game_arr = remove_wins(game_arr, win_arr)
        wins = len(win_arr)
        print(wins/possibilities)

    return game_arr

print(len(get_winrate_of_rounds(3)))



