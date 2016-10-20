"""

Author - marius
Date - 15.10.2016

Solving the towers of hanoi , using the random optimised approach.
"""
import basics
import time
from random import randint

data = []
already_passed_states = []
solutions = 0


def get_state(all_towers):
    content = ""
    for t in all_towers:
        content += basics.get_tower_content(t) + "\n"

    return content


def search(towers):
    global solutions
    transitions = 0
    execution_time = time.time()

    while basics.is_final_state(towers) is False:
        s_tower = randint(0, len(towers) - 1)
        d_tower = randint(0, len(towers) - 1)

        if basics.is_valid(towers[s_tower], towers[d_tower]):
            transitions += basics.move_disk(towers[s_tower], towers[d_tower])
            basics.show_current_state(towers)

    if basics.is_final_state(towers) is True:   # save to file, only last state -> file_size issue
        state = ""
        for t in towers:
            state += basics.get_tower_content(t)
            solutions += 1
            basics.print_statistics("random_opt_output.txt", state + "\n\n\n")
            basics.print_statistics("random_opt_output.txt", "------------------")
            state = ""
    execution_time = time.time() - execution_time

    return tuple([transitions, execution_time])


def random_optimised_search():
    global data
    data = basics.get_data_from_file("data.txt")
    m_towers = basics.init(int(data[0]), int(data[1]))
    return search(m_towers)

total_steps = 0
total_execution_time = 0

"""
average transitions , execution time for 30 iterations , solution will be found eventually
"""
for i in range(0, 30):

    current_steps, time_spent = random_optimised_search()
    total_steps += current_steps

    total_execution_time += time_spent

basics.print_statistics("random_opt_output.txt", data[0] + "Towers and " + data[1] + "disks" + "\n" +
                        "Random optimized approach ~ 30 iter. \n Average transitions :" +
                        str(total_steps / 30) + "Solutions :" + str(solutions) + "\n\n, Average execution time : " + str(total_execution_time / 30)
                        + "\n")
