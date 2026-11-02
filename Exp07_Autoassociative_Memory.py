"""Experiment 7(a) PDF: autoassociative memory and corrupted pattern tests."""
import numpy as np
import pandas as pd


def activation(y):
    return np.where(y > 0, 1, -1)


x = np.array([-1, 1, 1, 1])
W_auto = np.outer(x, x)
print('Input vector x =', x.tolist())
print('Weight matrix W =\n', W_auto)

test_vectors = {
    'Same as input': np.array([-1, 1, 1, 1]),
    'One missing (0 1 1 1)': np.array([0, 1, 1, 1]),
    'One mistake (-1 -1 1 1)': np.array([-1, -1, 1, 1]),
    'Two missing (0 0 1 1)': np.array([0, 0, 1, 1]),
    'Two mistake (-1 -1 -1 1)': np.array([-1, -1, -1, 1]),
}

rows = []
for label, x_test in test_vectors.items():
    y_in = x_test @ W_auto
    y = activation(y_in)
    correct = np.array_equal(y, x)
    rows.append({'Test case': label, 'Test input': str(x_test.tolist()),
                 'y_in': str(y_in.tolist()), 'Output y': str(y.tolist()),
                 'Recognized': 'Yes' if correct else 'No'})

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', None)
print('\nResults:')
print(pd.DataFrame(rows).to_string(index=False))
