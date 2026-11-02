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


from heapq import heappop, heappush
from itertools import count

def heuristic(s):
    # Admissible lower bound: if not already solved, at least 1 move.
    # Safe but deliberately weak; A* still finds a shortest solution.
    return 0 if is_goal(s) else 1

def astar():
    counter = count()
    heap = [(heuristic(START), 0, next(counter), START,
             [('Start', START)])]
    best_g = {START: 0}
    while heap:
        _, g, _, state, path = heappop(heap)
        if g != best_g[state]:
            continue
        if is_goal(state):
            return path
        for action, nxt in successors(state):
            new_g = g + 1
            if new_g < best_g.get(nxt, float('inf')):
                best_g[nxt] = new_g
                heappush(heap, (new_g + heuristic(nxt), new_g,
                                next(counter), nxt, path + [(action, nxt)]))
    return None

if __name__ == '__main__':
    print('Water Jug - A* (f = g + h)')
    show(astar())
