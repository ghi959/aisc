"""8-puzzle with a fixed, solvable start and the standard goal state.

0 denotes the blank tile. Edit START to try another arrangement.
"""

START = (1, 2, 3,
         5, 0, 6,
         4, 7, 8)
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def inversions(state):
    a = [v for v in state if v != 0]
    return sum(a[i] > a[j]
               for i in range(len(a)) for j in range(i + 1, len(a)))

def valid_puzzle():
    if sorted(START) != list(range(9)) or sorted(GOAL) != list(range(9)):
        raise ValueError('START and GOAL must contain 0 through 8 once each')
    # On odd-width (3x3) boards, inversions must have matching parity.
    return inversions(START) % 2 == inversions(GOAL) % 2

def neighbors(state):
    pos = state.index(0)
    r, c = divmod(pos, 3)
    for name, dr, dc in [('Left', 0, -1), ('Down', 1, 0),
                          ('Right', 0, 1), ('Up', -1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nxt = list(state)
            new_pos = nr * 3 + nc
            nxt[pos], nxt[new_pos] = nxt[new_pos], nxt[pos]
            yield name, tuple(nxt)

def show(path):
    if path is None:
        print('No solution')
    else:
        print('Moves:', len(path) - 1)
        for i, (action, s) in enumerate(path):
            print(f'\nStep {i}: {action}')
            for r in range(0, 9, 3):
                print(' '.join('_' if v == 0 else str(v) for v in s[r:r+3]))


from collections import deque

def bfs():
    if not valid_puzzle():
        return None
    queue = deque([[('Start', START)]])
    visited = {START}
    while queue:
        path = queue.popleft()
        state = path[-1][1]
        if state == GOAL:
            return path
        for action, nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [(action, nxt)])
    return None

if __name__ == '__main__':
    print('8-Puzzle - BFS (shortest moves)')
    show(bfs())
