towers = []


def print_statistics(m_file, text):
    with open(m_file, "a") as _file_:
        _file_.write(text)

"""
data[0] - number of towers
data[1] -number of disks
"""


def get_data_from_file(file_path):
    m_file = open(file_path, "r+")

    data = m_file.readlines()

    return data

"""
initialize the towers
"""


def init(n, m):
    towers.append(list(reversed(range(1, m+1))))

    for i in range(1, n):
        towers.append([None] * m)

    return towers


"""
the first disk in the tower which is not none and position , otherwise, none
"""


def uppermost_disk(tower):
    uppermost = None
    position = 0

    for i in range(len(tower) - 1, -1, -1):
        if tower[i] is not None:
            uppermost = tower[i]
            position = i
            break

    return tuple([uppermost, position])

"""
shows the content of a tower
"""


def show_tower_content(tower):
    step = 0
    for i in range(len(tower) - 1, -1, -1):
        print
        print str(tower[i]),

        for j in range(0, step + 1):
            print "-",

        step += 1
    print


def get_tower_content(tower):
    step = 0
    content = ""
    for i in range(len(tower) - 1, -1, -1):
        content += "\n" + str(tower[i])

        for j in range(0, step + 1):
            content += "-"

        step += 1
    print

    return content

"""
shows the current state : towers and the disks' positioning
"""


def show_current_state(towers_):
    print "Current state : ",
    for t in towers_:
        show_tower_content(t)

    print

"""
checks if disk movement is valid
"""


def is_valid(t_source, t_destination):

    if t_source != t_destination:

        disk_to_be_moved = uppermost_disk(t_source)[0]
        destination_space = uppermost_disk(t_destination)[0]

        if destination_space is None and disk_to_be_moved is not None:
            return True

        if disk_to_be_moved < destination_space:
            return True

    return False


"""
move disk from source tower to source destination , return 1 -> as in one step to count the steps for
each transition
"""


def move_disk(t_source, t_destination):
    if is_valid(t_source, t_destination):

        moved_disk, position = uppermost_disk(t_source)
        t_source[position] = None

        for i in range(0, len(t_destination)):
            if t_destination[i] is None:
                t_destination[i] = moved_disk
                break
        return 1
    else:
        print "Transition not valid."
        return 0

"""
rewind the movement
"""


def rewind_move_disk(t_source, t_destination):
    move_disk(t_destination, t_source)

"""
checks if we are in the final state
"""


def is_final_state(towers_):
    if None in towers_[-1]:
        return False

    return True
