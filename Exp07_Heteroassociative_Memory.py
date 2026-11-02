"""Experiment 7(b) PDF: heteroassociative memory with four pattern pairs."""
import numpy as np
import pandas as pd


def binary_activation(y):
    return np.where(y > 0, 1, 0)


S = np.array([[1, 0, 0, 0], [1, 1, 0, 0],
              [0, 0, 0, 1], [0, 0, 1, 1]])
T = np.array([[0, 1], [0, 1], [1, 0], [1, 0]])

W_hetero = np.zeros((4, 2))
for p in range(len(S)):
    W_hetero += np.outer(S[p], T[p])

print('Weight matrix W =\n', W_hetero)
rows = []
for p in range(len(S)):
    y_in = S[p] @ W_hetero
    y = binary_activation(y_in)
    correct = np.array_equal(y, T[p])
    rows.append({'Pattern': p + 1, 'Input s': str(S[p].tolist()),
                 'y_in': str(y_in.tolist()), 'Output y': str(y.tolist()),
                 'Target t': str(T[p].tolist()),
                 'Correct': 'Yes' if correct else 'No'})

pd.set_option('display.width', 200)
print('\nTesting with training inputs:')
print(pd.DataFrame(rows).to_string(index=False))
