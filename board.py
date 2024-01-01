class Board:
    def __init__(self, positions, name="valid"):
        self.name = name
        self.where = {pos: idx for idx, pos in enumerate(positions)}
        self.what = {idx: pos for idx, pos in enumerate(positions)}
        self.dirs = {'up': -3, 'down': +3, 'left': -1, 'right': +1}
        self.edges = {'up': [0, 1, 2], 'down': [6, 7, 8], 'left': [0, 3, 6], 'right': [2, 5, 8]}
        
    def transition(self, dir):
        new = self.copy()
        blank_pos = new.where[0]

        if blank_pos in new.edges[dir]:
            new.name = "invalid"
            return new

        new_blank_pos = blank_pos + new.dirs[dir]
        
        new.where[0],  new.where[new.what[new_blank_pos]] = new_blank_pos, blank_pos
        new.what[blank_pos], new.what[new_blank_pos] = new.what[new_blank_pos], 0
        
        return new
    
    def copy(self):
        return Board(self.what.values(), self.name)    
    
    def __eq__(self, __value):
        return tuple(self.what.values()) == tuple(__value.what.values()) and self.name == __value.name
    
    
    def __hash__(self):
        return hash((tuple(self.what.values()), self.name))
    
    
    
    def __str__(self):
        rows = [str(self.what[i]) for i in range(9)]  # Fetch positions from 0 to 8 and convert to string
        rows[self.where[0]] = " "
        matrix = [rows[i:i + 3] for i in range(0, len(rows), 3)]  # Split into rows
        
        # Create the formatted string representation of the matrix
        formatted_matrix = "\n-------------\n"  # Top border

        for row in matrix:
            formatted_matrix += "| " + " | ".join(row) + " |\n"  # Format each row

        formatted_matrix += "-------------"  # Bottom border
        return formatted_matrix
    
    def manhattan_distance(self, goal):
        distance = 0
        for pos in self.what.values():
            if pos != 0:  # Exclude the blank space
                cur_row, cur_col = divmod(self.where[pos], 3)
                goal_row, goal_col = divmod(goal.where[pos], 3)
                distance += abs(cur_row - goal_row) + abs(cur_col - goal_col)
        return distance 