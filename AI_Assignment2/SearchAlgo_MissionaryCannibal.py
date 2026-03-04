from collections import deque

class MissionariesCannibals:
    def __init__(self):
        self.initial = (3, 3, 0)
        self.goal = (0, 0, 1)

    def is_valid(self, state):
        M, C, boat = state
        if M < 0 or C < 0 or M > 3 or C > 3:
            return False
        if (M > 0 and C > M):
            return False
        M_right = 3 - M
        C_right = 3 - C
        if (M_right > 0 and C_right > M_right):
            return False
        return True

    def get_successors(self, state):
        M, C, boat = state
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        successors = []

        for m, c in moves:
            if boat == 0:
                new_state = (M-m, C-c, 1)
            else:
                new_state = (M+m, C+c, 0)

            if self.is_valid(new_state):
                successors.append(new_state)

        return successors


def bfs(problem):
    queue = deque()
    queue.append((problem.initial, []))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == problem.goal:
            return path + [state]

        for successor in problem.get_successors(state):
            queue.append((successor, path + [state]))

    return None

def dfs(problem):
    stack = []
    stack.append((problem.initial, []))
    visited = set()

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state == problem.goal:
            return path + [state]

        for successor in problem.get_successors(state):
            stack.append((successor, path + [state]))

    return None

def dls(problem, limit):
    stack = [(problem.initial, [], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()

        if depth > limit:
            continue

        if state in visited:
            continue

        visited.add(state)

        if state == problem.goal:
            return path + [state]

        for successor in problem.get_successors(state):
            stack.append((successor, path + [state], depth+1))

    return None

def iddfs(problem, max_depth):
    for depth in range(max_depth):
        result = dls(problem, depth)
        if result is not None:
            return result
    return None

if __name__ == "__main__":
    problem = MissionariesCannibals()

    print("BFS Solution:")
    print(bfs(problem))

    print("\nDFS Solution:")
    print(dfs(problem))

    print("\nIDDFS Solution:")
    print(iddfs(problem, 20))