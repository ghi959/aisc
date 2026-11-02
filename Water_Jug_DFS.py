"""Water Jug problem: capacities 4 and 3; obtain exactly 2 litres in either jug."""

CAP_A, CAP_B, GOAL = 4, 3, 2
START = (0, 0)

def is_goal(s):
    return GOAL in s

def successors(s):
    a, b = s
    ab = min(a, CAP_B - b)
    ba = min(b, CAP_A - a)
    options = [
        ("Fill A", (CAP_A, b)),
        ("Fill B", (a, CAP_B)),
        ("Empty A", (0, b)),
        ("Empty B", (a, 0)),
        ("Pour A -> B", (a - ab, b + ab)),
        ("Pour B -> A", (a + ba, b - ba)),
    ]
    return [(name, nxt) for name, nxt in options if nxt != s]

def show(path):
    if path is None:
        print("No solution")
    else:
        print("Moves:", len(path) - 1)
        for i, (action, state) in enumerate(path):
            print(f"{i:2}. {action:<13} {state}")


def dfs():
    stack = [[('Start', START)]]
    visited = set()
    while stack:
        path = stack.pop()
        state = path[-1][1]
        if state in visited:
            continue
        visited.add(state)
        if is_goal(state):
            return path
        for action, nxt in reversed(successors(state)):
            if nxt not in visited:
                stack.append(path + [(action, nxt)])
    return None

if __name__ == '__main__':
    print('Water Jug - DFS (not necessarily shortest)')
    show(dfs())
