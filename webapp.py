from flask import Flask, render_template, request
from board import Board
from solver import Agent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    init_state = [int(request.form[f'init{i}']) for i in range(1, 10)]
    goal_state = [int(request.form[f'goal{i}']) for i in range(1, 10)]

    init_board = Board(init_state)
    goal_board = Board(goal_state)

    agent = Agent(init_board, goal_board)
    agent.solve()

    if agent.path:
        path = []
        for state in agent.path:
            path.append(state.what.values())

        return render_template('solution.html', path=path)
    else:
        return "No path available."

if __name__ == '__main__':
    app.run(debug=True)
