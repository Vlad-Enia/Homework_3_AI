from random import sample
from itertools import permutations
import copy


def choose_k_from_m_times_n(n, m, k):
    ball_sample = [e // m for e in range(n * m)]
    return sample(ball_sample, k)


def init(n, m, k):
    # n = number of colours
    # m = number of balls of each colour
    # k = number of chosen balls
    # A_list = the sequence of balls chosen by A
    # B_list = a list of sequences; will be updated each time player B chooses a sequence of balls
    # return [n, m, k, A_list, B_list]
    return [n, m, k, choose_k_from_m_times_n(n, m, k), []]


def is_final(state):
    no_moves_B = len(state[4])
    if no_moves_B > 0:  # if B has made at least one move
        A_list = state[3]
        n = state[0]
        B_list = list(state[4][-1])
        if no_moves_B < 2 * n:  # if B hasn't reached the maximum number of moves (2*n)
            if A_list == B_list:  # check if B guessed list of colours chosen by A
                return 1  # if so, B wins
            else:
                return 0  # if not, our state is not final
        elif no_moves_B == 2 * n:  # else if B has made the last move
            if A_list == B_list:  # check if the guess is right
                return 1  # if so, B wins
            else:
                return -1  # if not, A wins
    else:
        return 0  # if B hasn't made any moves then state is not final


def get_number_of_matches(l1, l2):
    counter = 0
    length = len(l1)
    for i in range(0, length):
        if l1[i] == l2[i]:
            counter += 1
    return counter


# initial_state = init(3, 2, 3)
# print("Initial state:", initial_state)
# print("Is initial state final (should be 0):", is_final(initial_state))
# print()
#
# state = copy.deepcopy(initial_state)
# state[4].append([1, 1, 1])
# print("State:", state)
# print("Is State final (should be 0):", is_final(state))  # not a final state
# state[4].append(state[3])
# print("Is State final (should be 1):", is_final(state))  # correct guess and the move  is not last => B wins
# print()
#
# state2 = copy.deepcopy(state)
# state2[4].append([])
# state2[4].append([])
# state2[4].append([])
# state2[4].append([])
# print("State2:", state2)
# print("Is State2 final (should be -1):",
#       is_final(state2))  # B has reached max number of moves and hasn't guessed yet => A wins
# print()
#
# state3 = copy.deepcopy(state2)
# state3[4][-1] = state3[3]
# print("State3:", state3)
# print("Is State2 final (should be 1):", is_final(state3))  # B guessed on the last move => B wins
# print()
#
# print("Matching:", get_number_of_matchings(initial_state[3], [1, 1, 1]))
# print("Matching:", get_number_of_matchings(initial_state[3], initial_state[3]))

########### Interface implementation ######


def process_input(B_input, n, m, k):
    if B_input[-1].isdigit() is False:
        B_input = B_input.rstrip(B_input[-1])
    B_input_list = B_input.replace(' ', '').split(',')
    B_input_list = list(map(int, B_input_list))

    if len(B_input_list) != k:
        print("Invalid input! You may choose a sequence of", k, 'balls!')
        return False
    else:
        d = {}
        for colour in range(0, n):
            d[colour] = 0
        for ball in B_input_list:
            if ball >= n:
                print("Invalid input! Not a correct color! You may choose from the following color set: ",
                      list(range(0, n)), '.', sep='')
                return False
            else:
                d[ball] += 1
                if d[ball] > m:
                    print("Invalid input! You can't choose more than", m, "balls of the same color.")
                    return False
    return B_input_list


def player_interface():
    initial_state = init(3, 2, 3)
    n = initial_state[0]
    m = initial_state[1]
    k = initial_state[2]
    A_list = initial_state[3]
    B_moves = initial_state[4]
    moves = 2 * n
    print("There are ", n, " colors available: ", list(range(0, n)), ".", sep='')
    print("There are", m, "balls of each color.")
    ball_sample = [e // m for e in range(n * m)]
    print("All of the available balls to choose from: ", ball_sample, ".", sep='')
    print("A has chosen", k, "balls.")
    print("You may choose a sequence of", k, "balls. Note that you can't choose more than", m,
          "balls of the same color.")
    print("Attention! Sequence elements need to be separated by comma! There may also be whitespaces between elements.")
    B_won = False
    while moves:
        print("\nYou have", moves - 1, "moves left.")
        moves -= 1
        B_input = input("Your sequence of balls: ")
        B_list = process_input(B_input, n, m, k)
        if B_list:
            B_moves.append(B_list)
            final = is_final(initial_state)
            if final == 1:
                print("\nYou won!")
                B_won = True
                break
            elif final == 0:
                no_matches = get_number_of_matches(A_list, B_list)
                print("Number of matches with A's sequence of colours: ", no_matches, '.', sep='')
    if not B_won:
        print("\nGame over! A won!")


def generate_all_possible_codes(state):
    n = state[0]
    m = state[1]
    k = state[2]
    ball_sample = [e // m for e in range(n * m)]
    print(ball_sample)
    return set(permutations(ball_sample, k))



print(generate_all_possible_codes(init(3, 2, 3)))

