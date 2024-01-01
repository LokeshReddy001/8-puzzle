from board import Board
from solver import Agent

def main():
    print('''
    8-Puzzle Solver
    ------------------------
    This program solves the 8-puzzle problem using A* search algorithm.

    Provide the initial and goal states of the board as space-separated permutations of numbers 0-8,
    

    Example: 
                                    1 2 3
        1 2 3 4 5 6 7 8 0   ---->   4 5 6
                                    7 8 0

    This represents the 8-puzzle initial/goal state, where 0 denotes the empty space.
    ''')

    init_state = list(map(int, input("Enter numbers separated by spaces for the init state: ").split()))
    goal_state = list(map(int, input("Enter numbers separated by spaces for the goal state: ").split()))

    init_board = Board(init_state)
    goal_board = Board(goal_state)
    agent = Agent(init_board, goal_board)
    agent.solve()

    agent.show_path()

if __name__ == '__main__':
    main()

