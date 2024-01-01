import sys
class Agent:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.moves = ['up', 'down', 'left', 'right']
        self.path = []  
        self.visited = set()
        self.parent = {}
        self.queue = []
        self.soln = False
        
    def solve(self):
        self.queue = [(self.start, 0)]
        self.visited.add(self.start)
        x=0
        while self.queue:
            x+=1
            sys.stdout.write('\r'+str(x))
            current, depth = self.queue.pop(0)

            if current == self.goal:
                self.soln = True
                while current != self.start:
                    self.path.insert(0, current) 
                    current = self.parent[current]
                self.path.insert(0, self.start)  
                break

            for move in self.moves:
                new = current.transition(move)

                if new.name != "invalid" and new not in self.visited:
                    self.visited.add(new)
                    self.parent[new] = current
                    self.queue.append((new, depth + 1))
                    self.queue.sort(key=lambda x: x[0].manhattan_distance(self.goal) + x[1])

        if self.soln:
            print("Solved!")
            # self.show_path()
        else:
            print("No solution found.")
            
    def show_path(self):
        if self.path:
            print("Path:")
            for node in (self.path):
                print(node)  # Print the formatted matrix of each node in the path
            print("\n")
        else:
            print("No path available.")

