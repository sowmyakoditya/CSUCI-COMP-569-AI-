
sample_maze_map = [
    "111111111",
    "100010001",
    "1000100R1",
    "100000001",
    "100001001",
    "111001001",
    "111001111",
    "1100000D1",
    "111111111",
]


class Node:
    def __init__(self, loc, parent, cost):
        self.location = loc
        self.parent = parent
        self.cost = cost


class Robot:
    def __init__(self, map):
        self.map = map
        self.map_height = len(map)
        self.map_width = len(map[0])

    def up(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        moved_y = current_loc[1]

        for i in range(y - 1, -1, -1):
            next_location = self.map[i][x]
            if next_location == "1":
                break
            moved_y = i

        if y == moved_y:
            raise IndexError
        return (x, moved_y)

    def down(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        moved_y = current_loc[1]

        for i in range(y + 1, self.map_height):
            next_location = self.map[i][x]
            if next_location == "1":
                break
            moved_y = i

        if y == moved_y:
            raise IndexError
        return (x, moved_y)

    def left(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        moved_x = current_loc[0]

        for i in range(x - 1, -1, -1):
            next_location = self.map[y][i]
            if next_location == "1":
                break
            moved_x = i

        if x == moved_x:
            raise IndexError
        return (moved_x, y)

    def right(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        moved_x = current_loc[0]

        for i in range(x + 1, self.map_width):
            next_location = self.map[y][i]
            if next_location == "1":
                break
            moved_x = i

        if x == moved_x:
            raise IndexError
        return (moved_x, y)


def get_start_and_goal(map):
    start_letter = "R"
    goal_letter = "D"
    start_loc = None
    goal_loc = None

    for idx, row in enumerate(map):
        if start_loc is None and start_letter in row:
            x = row.find(start_letter)
            y = idx
            start_loc = (x, y)
        if goal_loc is None and goal_letter in row:
            x = row.find(goal_letter)
            y = idx
            goal_loc = (x, y)

        if start_loc is not None and goal_loc is not None:
            break

    return start_loc, goal_loc


def successor_fcn(current_node, robot):
    functions = [robot.down, robot.up, robot.left, robot.right]
    children = []

    # This method is a solution that follows the path previously taken.

    for f in functions:
        try:
            moved_location = f(current_node.location)
            if moved_location not in children:
                child = Node(loc=moved_location, parent=current_node, cost=current_node.cost + 1)
                children.append(child)
                print("1")
        except IndexError:
            continue
    #  if moved_location not in children:
    #   child = Node(loc=moved_location, parent=current_node, cost=current_node.cost + 1)
    #  children.append(child)

    return children


def goal_test(current_loc, goal_loc):
    return current_loc == goal_loc


def extract_plan(goal_node):
    current_node = goal_node
    cost = goal_node.cost
    temporary_path_stack = []

    while True:
        loc = current_node.location
        temporary_path_stack.append(loc)
        current_node = current_node.parent
        if current_node is None:
            break

    len_path = len(temporary_path_stack)
    result_path = [temporary_path_stack.pop() for i in range(len_path)]

    return result_path, cost


def DLS_tree_search(map):
    # initialize the search tree using the initial state of problem
    start_loc, goal_loc = get_start_and_goal(map)
    robot = Robot(map)
    fringe = [Node(start_loc, None, 0)]
    visited = []
    depth = 0
    current_node = fringe[0]
    while depth <= current_node.cost:

        # choose a leaf node for expansion according to strategy
        current_node = fringe.pop()
        # if the node contains a goal state then return the corresponding solution
        if goal_test(current_node.location, goal_loc):
            return extract_plan(current_node)
        # else expand the node and add the resulting nodes to the search tree
        elif current_node not in fringe:
            child_node = successor_fcn(current_node, robot)
            fringe += child_node
            visited += child_node
        else:
            depth += 1
        depth = current_node.cost + 1
        print("cost:", current_node.cost)
        print("Depth:", depth)


def tree_search(map):
    # initialize the search tree using the initial state of problem
    start_loc, goal_loc = get_start_and_goal(map)
    robot = Robot(map)
    fringe = [Node(start_loc, None, 0)]

    # loop do
    while True:
        # if there are no candidates for expansion then return failure
        if not fringe:
            raise Exception
        # choose a leaf node for expansion according to strategy
        current_node = fringe.pop()
        # if the node contains a goal state then return the corresponding solution
        if goal_test(current_node.location, goal_loc):
            return extract_plan(current_node)
        # else expand the node and add the resulting nodes to the search tree
        else:
            child_node = successor_fcn(current_node, robot)
            fringe += child_node


# DFS function
def DFS_tree_search(map):
    # initialize the search tree using the initial state of problem
    start_loc, goal_loc = get_start_and_goal(map)
    robot = Robot(map)
    fringe = [Node(start_loc, None, 0)]

    # loop do
    while True:
        # if there are no candidates for expansion then return failure
        if not fringe:
            raise Exception
        # choose a leaf node for expansion according to strategy
        current_node = fringe.pop()
        # if the node contains a goal state then return the corresponding solution
        if goal_test(current_node.location, goal_loc):
            return extract_plan(current_node)
        # else expand the node and add the resulting nodes to the search tree
        else:
            child_node = successor_fcn(current_node, robot)
            fringe += child_node


# BFS function
def BFS_tree_search(map):
    # initialize the search tree using the initial state of problem
    start_loc, goal_loc = get_start_and_goal(map)
    robot = Robot(map)
    fringe = [Node(start_loc, None, 0)]
    # depth = 0

    # loop do
    while True:
        # if there are no candidates for expansion then return failure
        if not fringe:
            raise Exception
        # choose a leaf node for expansion according to strategy
        current_node = fringe.pop(0)
        # if the node contains a goal state then return the corresponding solution
        if goal_test(current_node.location, goal_loc):
            return extract_plan(current_node)
        # else expand the node and add the resulting nodes to the search tree
        else:
            child_node = successor_fcn(current_node, robot)
            fringe += child_node


# Dispay result
def play_game():
    sample_maze_map = [
        "111111111",
        "100010001",
        "1000100R1",
        "100000001",
        "100001001",
        "111001001",
        "111001111",
        "1100000D1",
        "111111111",
    ]
    result = DLS_tree_search(sample_maze_map)  #### Please change search medthon HERE!!####
    final_res = []

    if isinstance(result, tuple):
        print("Cost ", result[1])
        print("Plan ", result[0])
        x = 0
        y = 0
        plan = result[0]
        for i in range(len(plan)):
            if plan[i][0] < x and plan[i][1] == y:
                # if current x is lesser than previous x and current y is equal to previous y then it is left
                final_res.append("Left")
            elif plan[i][0] > x and plan[i][1] == y:
                # if current x is greater than previous x then it is right
                final_res.append("Right")
            elif plan[i][1] < y and plan[i][0] == x:
                # if current y is lesser than previous y then it is up
                final_res.append("Up")
            elif plan[i][1] > y and plan[i][0] == x:
                # if current y is greater than previous y then it is down
                final_res.append("Down")

            x = plan[i][0]
            y = plan[i][1]

    return '->'.join(final_res)


play_game()

