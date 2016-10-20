"""

Author - marius
Date - 16.10.2016
Solving Hanoi using Hill Climbing
"""
import basics
import time
import sys
from random import randint

best = ([], [])

orig_stdout = sys.stdout
f = file('hill_climbing_output.txt', 'w')
sys.stdout = f


def probability():
    return randint(0, 2)


def no_none_values_count(tower):

    return len(tower) - tower.count(None)


def evaluate_movement(t_destination):

    if t_destination is None:
        return 0
    else:
        return no_none_values_count(t_destination)


def neighborhood_of_movement(t_source):
    global towers_
    neighbors = []
    for t in towers_:
        if basics.is_valid(t_source, t):
            neighbors.append(t)

    return neighbors


def improve(neighborhood, current_destination):
    global towers_

    if len(neighborhood) != 0:
        for i in range(0, len(neighborhood)):
            if i == current_destination and current_destination != 0:
                if probability() == 1:
                    return towers_[i-1]
                else:
                    return towers_[i+1]
            else:
                return towers_[i+1]

    return towers_[0]


def hill_climbing():

    global towers_
    global best
    global steps
    global total_exec_time
    global total_steps
    global solutions
    old_count = 0
    i = 0

    movement = ()
    exec_time = time.time()

    while i < 10000:

        local = False
        d_tower = 0
        we_have_a_movement = False

        while we_have_a_movement is False:
            s_tower = randint(0, len(towers_) - 1)
            d_tower = randint(0, len(towers_) - 1)

            if basics.is_valid(towers_[s_tower], towers_[d_tower]):
                we_have_a_movement = True
                basics.show_current_state(towers_)
                basics.move_disk(towers_[s_tower], towers_[d_tower])
                steps += 1
                basics.show_current_state(towers_)
                movement = tuple([towers_[s_tower], towers_[d_tower]])

        while local is False:
            vn_movement = tuple([movement[0], improve(neighborhood_of_movement(movement), d_tower)])
            if evaluate_movement(vn_movement[1]) > evaluate_movement(movement[1]):
                movement = vn_movement
            else:
                local = True

        if no_none_values_count(towers_[-1]) > old_count:
            old_count = no_none_values_count(towers_[-1])
            basics.move_disk(movement[0], movement[1])
            steps += 1
            basics.show_current_state(towers_)

            if basics.is_final_state(towers_):
                solutions += 1
                exec_time = time.time() - exec_time
                total_exec_time += exec_time
                total_steps += steps
                break

        i += 1

    return tuple([total_steps, total_exec_time])

steps = 0
solutions = 0
total_steps = 0
total_exec_time = 0
data = basics.get_data_from_file("data.txt")
towers_ = basics.init(int(data[0]), int(data[1]))
avg_steps = 0
avg_time = 0

for i in range(0, 30):
    m_steps, m_time = hill_climbing()
    avg_steps += m_steps
    avg_time += m_time

sys.stdout = orig_stdout
f.close()

basics.print_statistics("hill_climbing_output.txt", data[0] + "Towers and " + data[1] + "disks" + "\n" +
                        "Hill Climbing approach ~ 30 iter. \n Solutions :" + str(solutions) +
                        "Average transitions :" + str(float(avg_steps) / 30) +
                        ", Average execution time : " + str(float(avg_time) / 30) + "\n")
