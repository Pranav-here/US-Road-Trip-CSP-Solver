"""
CSP constraints:
    selects states in increasing zone order.
    ensures the route covers a minimum number of parks.
    a valid path is not found, it returns an appropriate failure message.
"""

import numpy as np
import sys
from copy import deepcopy

# Only valid input
if len(sys.argv) != 3:
    print('Pranav, Kuchibhotla, A20511026 solution:')
    print('ERROR: Not enough or too many input arguments.')
    sys.exit(0)

# Set initial state and minimum parks from arguments
initial_State = sys.argv[1].upper()
NumOfParks = int(sys.argv[2])

# Load data
parks_path = "parks.csv"
parks = np.loadtxt(parks_path, str, delimiter=',')

driving_path = "driving2.csv"
driving_data = np.loadtxt(driving_path, str, delimiter=',')

zones_path = "zones.csv"
zones = np.loadtxt(zones_path, str, delimiter=',')

# make ket-valye pairs connects zones and states
state_zones = {zones[0][i]: int(zones[1][i]) for i in range(1, len(zones[0]))}
state_num = len(driving_data[0])
state_parks = {parks[0][i]: int(parks[1][i]) for i in range(1, state_num)}
state_road = {}

# road connections between states
for i in range(1, state_num):
    state = driving_data[0][i]
    connections = []
    for j in range(1, len(driving_data[0])):
        if driving_data[i][j] != "-1" and driving_data[i][j] != "0":
            if state_zones[driving_data[0][j]] == state_zones[state] + 1:
                connections.append((driving_data[0][j], int(driving_data[i][j])))
    connections.sort(key=lambda x: x[0])
    state_road[state] = connections

# for backtracking
state_road_backup = deepcopy(state_road)

# Initialize
initial = initial_State
NO_OF_PARKS = NumOfParks
assignment = [initial]


def main():
    print('Pranav, Kuchibhotla, A20511026 solution:')
    print('Initial state:', initial_State)
    print('Minimum number of parks:', NumOfParks)

    ROAD = backtrack_search(assignment)
    if ROAD != "no correct road":
        path_cost, PARKS_VISITED, ROAD1 = calculate_path_cost_and_parks(ROAD)
        print(f'Solution path: {ROAD1}')
        print(f'Number of states on a path: {len(ROAD)}')
        print(f'Path cost: {path_cost}')
        print(f'Number of national parks visited: {PARKS_VISITED}')
    else:
        print('Solution path: FAILURE: NO PATH FOUND')
        print('Number of states on a path: 0')
        print('Path cost: 0')
        print('Number of national parks visited: 0')


# calculate path cost and number of parks visited
def calculate_path_cost_and_parks(road):
    path_cost = sum(j[1] for i in range(len(road) - 1) for j in state_road[road[i]] if j[0] == road[i + 1])
    PARKS_VISITED = sum(state_parks[state] for state in road)
    return path_cost, PARKS_VISITED, " ".join(road)


# backtracking function
def backtrack_search(assignment):
    unused_states = []
    return backtrack(assignment, unused_states)


# Order domain values
def ORDER_DOMAIN_VALUES(variable, unused_states):
    while len(unused_states) >= 2:
        key = unused_states.pop(0)
        state_road[key] = state_road_backup[key]
    return state_road[variable]


# to check if assignment is complete
def is_complete(assignment):
    if assignment[-1] not in ["WA", "OR", "NV", "CA"]:  # Zone 12 states
        return False
    parks_visited = sum(state_parks[state] for state in assignment)
    return parks_visited >= NO_OF_PARKS


# backtracking function from question
def backtrack(assignment, unused_states):
    if is_complete(assignment):
        return assignment
    if not state_road[assignment[-1]]:
        if len(assignment) > 1:
            unused_states.append(assignment.pop(-1))
            if state_road[assignment[-1]]:
                state_road[assignment[-1]].pop(0)
            return backtrack(assignment, unused_states)
        else:
            return "no correct road"
    else:
        for value in ORDER_DOMAIN_VALUES(assignment[-1], unused_states):
            assignment.append(value[0])
            result = backtrack(assignment, unused_states)
            if result != "failure":
                return result
            if state_road[assignment[-1]]:
                state_road[assignment[-1]].pop(0)
            assignment.pop(-1)
        return "failure"


# Execute the main function
if __name__ == "__main__":
    main()
