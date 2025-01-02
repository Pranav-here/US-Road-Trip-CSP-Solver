# US Road Trip CSP Solver

This project is a Python implementation of a Constraint Satisfaction Problem (CSP) solver. It plans an optimal road trip across the contiguous United States by solving constraints related to state zones, driving distances, and national parks.

## Features
- Plans a road trip that adheres to constraints:
  - Starts from a user-defined state and ends in one of the states in the westernmost zone.
  - Visits exactly one state per zone along the path.
  - Meets or exceeds a user-defined minimum number of national parks.
- Processes structured CSV input files:
  - `driving2.csv`: Driving distances between state capitals.
  - `parks.csv`: Number of national parks per state.
  - `zones.csv`: Zone assignments for each state.
- Implements the Backtracking algorithm to find valid paths efficiently.

## Input
- Command-line arguments:
  1. **Initial State**: The starting state for the trip.
  2. **Minimum Parks**: The minimum number of national parks to visit.

Example:
```bash
python cs480_P02_A11111111.py MD 5
```

## Output
The program outputs the following road trip details:
- Initial state and the minimum number of parks specified.
- Path of states visited.
- Total number of states in the path.
- Total driving distance.
- Number of national parks visited.

If no valid path is found, the program reports failure with appropriate details:
- Path: `FAILURE: NO PATH FOUND`
- Number of states: `0`
- Path cost: `0`
- National parks visited: `0`

## File Structure
- **`cs480_P02_A20511026.py`**: Main script containing the CSP solver implementation.
- **`driving2.csv`**: Matrix of driving distances between state capitals.
- **`parks.csv`**: Number of national parks in each state.
- **`zones.csv`**: Zone assignment for states.

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/pranav-here/US-Road-Trip-CSP-Solver.git
    ```
2. Navigate to the project directory:
    ```bash
    cd US-Road-Trip-CSP-Solver
    ```
3. Run the script with the following arguments:
    ```bash
    python cs480_P02_20511026.py <Initial State> <Minimum Parks>
    ```
   
## Skills Demonstrated

- **Artificial Intelligence (AI)**: Developed a CSP solver using backtracking to navigate complex constraints.
- **Backtracking Algorithm**: Designed an efficient pathfinding approach through state variables with constraints.
- **Graph Theory and Pathfinding**: Applied graph traversal techniques to ensure valid road trip paths based on distance and connectivity constraints.
- **Data Processing and Analysis**: Processed structured CSV files containing state information, driving distances, and park data.
- **Python Programming**: Leveraged Python for implementing the algorithm, managing data, and generating outputs.
