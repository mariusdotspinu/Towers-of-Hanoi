"""

Author - marius
Date - 17.10.2016
Solving hanoi , using a star algorithm
"""
import basics
import copy

close_list = []

# depth


g_x = {}

# number of disks in the towers before current and + 2* number of disks in the towers to the right
# which are smaller than disks from the left of..


h_x = {}

f_x = {}


def get_state(all_towers):
    content = ""
    for t in all_towers:
        content += basics.get_tower_content(t) + "\n"

    return content


def number_of_disks(tower):
    number = 0
    for i in tower:
        if i is not None:
            number += 1

    return number


def get_all_unique_disks_from_towers(towers):
    my_list = []
    for t in towers[:-1]:
        for j in range(0, len(t)):
            my_list.append(t[j])

    my_list = set(my_list)

    return my_list


def total_number_of_disks_from_left_towers(towers):
    return len(get_all_unique_disks_from_towers(towers))


def disks_from_smaller_than(t1, t2):
    my_list = []
    for i in t1:
        k = 0
        for j in t2:
            if i < j:
                k += 1
            elif i is None:
                k += 1
            else:
                k -= 1
        if k == len(t2):
            my_list.append(i)

    return len(my_list)


def get_all_possible_states(towers_):
    global g_x, h_x, f_x

    auxiliary_towers_ = copy.deepcopy(towers_)  # don't change the initial towers

    states = []
    depth = 0
    list_states = []
    final_list = []

    for i in range(0, len(auxiliary_towers_)):
        for j in range(0, len(auxiliary_towers_)):
            if basics.is_valid(auxiliary_towers_[i], auxiliary_towers_[j]):
                basics.move_disk(auxiliary_towers_[i], auxiliary_towers_[j])

                if auxiliary_towers_ not in states:
                    key = get_state(auxiliary_towers_)
                    g_x[key] = depth
                    h_x[key] = total_number_of_disks_from_left_towers(auxiliary_towers_) \
                        + 2 * disks_from_smaller_than(
                        auxiliary_towers_[-1],
                        get_all_unique_disks_from_towers(auxiliary_towers_))

                    f_x[key] = g_x[key] + h_x[key]
                    depth += 1
                    states.append(get_state(auxiliary_towers_))
                    list_states.append(auxiliary_towers_)

    final_list.append(states)
    final_list.append(list_states)

    return final_list


def algorithm_a_star(towers_):
    min_value = 320000
    saved_state = []
    steps = 0

    close_list.append(towers_)

    for i in close_list:
        open_list = []
        current_possible_states = get_all_possible_states(i)[0]
        current_possible_states_list = get_all_possible_states(i)[1]
        for j in current_possible_states_list:
            open_list.append(j)

        for k in range(0, len(open_list)):
            if current_possible_states[k] in f_x:
                a_function_value = f_x[current_possible_states[k]]
            if min_value > a_function_value:
                min_value = a_function_value
                saved_state = open_list[k]
                steps += 1
            if basics.is_final_state(saved_state):
                print steps
                break

        if saved_state not in close_list:
            close_list.append(saved_state)

        if saved_state in open_list:
            open_list.remove(saved_state)


data = basics.get_data_from_file("data.txt")

_towers_ = basics.init(int(data[0]), int(data[1]))

algorithm_a_star(_towers_)
