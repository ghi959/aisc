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
    # Greedy estimate: how close either jug is to the requested amount.
    # This is NOT guaranteed to produce the shortest solution.
    return min(abs(s[0] - GOAL), abs(s[1] - GOAL))

def greedy():
    counter = count()
    heap = [(heuristic(START), next(counter), [('Start', START)])]
    seen = set()
    while heap:
        _, _, path = heappop(heap)
        state = path[-1][1]
        if state in seen:
            continue
        seen.add(state)
        if is_goal(state):
            return path
        for action, nxt in successors(state):
            if nxt not in seen:
                heappush(heap, (heuristic(nxt), next(counter),
                                path + [(action, nxt)]))
    return None

if __name__ == '__main__':
    print('Water Jug - Greedy Best First (heuristic search)')
    show(greedy())
