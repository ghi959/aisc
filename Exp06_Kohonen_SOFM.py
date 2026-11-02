"""Experiment 6(a) PDF: Kohonen SOM, five winner-take-all cluster neurons.

Unlike a neighbourhood-based SOM demo, THIS ASSIGNMENT UPDATES ONLY THE WINNER.
"""
import pandas as pd

# Weight matrix: 2 inputs (rows) x 5 cluster neurons (columns)
W = [[0.3, 0.2, 0.1, 0.8, 0.4],
     [0.5, 0.6, 0.7, 0.9, 0.2]]
num_clusters = 5


def distance(x, j):
    return (W[0][j] - x[0]) ** 2 + (W[1][j] - x[1]) ** 2


def find_winner(x):
    distances = [distance(x, j) for j in range(num_clusters)]
    return distances.index(min(distances)), distances


def update_weights(x, winner, alpha):
    for i in range(2):
        W[i][winner] += alpha * (x[i] - W[i][winner])


rows = []

# Assignment part (a) and part (b) use the SAME original weights separately.
for part, x, alpha in [('a', (0.2, 0.4), 0.2),
                       ('b', (0.6, 0.6), 0.1)]:
    W = [[0.3, 0.2, 0.1, 0.8, 0.4],
         [0.5, 0.6, 0.7, 0.9, 0.2]]

    winner, distances = find_winner(x)
    row = {'Part': part, 'Input': str(x), 'Alpha': alpha}
    row.update({f'D{j+1}': round(d, 4) for j, d in enumerate(distances)})
    row['Winner'] = f'Y{winner + 1}'
    update_weights(x, winner, alpha)
    row['W1(new)'] = round(W[0][winner], 4)
    row['W2(new)'] = round(W[1][winner], 4)
    rows.append(row)

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', None)
print(pd.DataFrame(rows).to_string(index=False))
print('\nFinal updated weight matrix (part b):')
print(f'W1 row: {[round(v, 4) for v in W[0]]}')
print(f'W2 row: {[round(v, 4) for v in W[1]]}')
