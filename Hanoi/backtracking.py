"""

Author - marius
Date - 18.10.2016

"""

import basics
import sys
import copy
import time
sys.setrecursionlimit(10000)

valid_states = []


def get_state(all_towers):
    content = ""
    for t in all_towers:
        content += basics.get_tower_content(t) + "\n"

    return content


def print_states_to_file(state):
    basics.print_statistics("backtracking_output.txt", state + "\n\n")


def bkt(m_towers):
    global valid_states, solutions, total_exec_time, transitions, total_transitions
    c_time = time.time()

    if basics.is_final_state(m_towers):
        for i in valid_states:
            print_states_to_file(i)
        valid_states.pop()
        total_exec_time += time.time() - c_time
        solutions += 1
        total_transitions += transitions
        transitions = 0
        return

    for i in range(0, len(m_towers)):
        for j in range(0, len(m_towers)):
            if basics.is_valid(m_towers[i], m_towers[j]):
                aux_towers = copy.deepcopy(m_towers)
                basics.move_disk(aux_towers[i], aux_towers[j])
                transitions += 1
                current_state = get_state(aux_towers)
                if current_state not in valid_states:
                    valid_states.append(current_state)
                    bkt(aux_towers)

    if len(valid_states) != 0:
        valid_states.pop()


solutions = 0
transitions = 0
total_transitions = 0
data = basics.get_data_from_file("data.txt")

towers_ = basics.init(int(data[0]), int(data[1]))
total_exec_time = 0
bkt(towers_)

basics.print_statistics("backtracking_output.txt", data[0] + "Towers and " + data[1] + "disks" + "\n" +
                        "Solutions :" + str(solutions) + "Average transitions :" +
                        str(total_transitions / solutions) + "\n Average execution time : " +
                        str(total_exec_time / solutions) + "\n")
