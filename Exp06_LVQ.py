"""Experiment 6(b) PDF: LVQ, initial prototypes and three assigned samples."""
import pandas as pd

w1 = [0, 0, 1, 1]  # class 1 reference vector
w2 = [1, 0, 0, 0]  # class 2 reference vector
class_of = {1: 1, 2: 2}
alpha = 0.1
training_data = [
    ([0, 0, 0, 1], 2),
    ([1, 1, 0, 0], 1),
    ([0, 1, 1, 0], 1),
]


def distance(x, w):
    return sum((w[i] - x[i]) ** 2 for i in range(len(x)))


rows = []
for x, T in training_data:
    D1, D2 = distance(x, w1), distance(x, w2)
    J = 1 if D1 < D2 else 2  # ties select class 2 as in PDF
    winner = w1 if J == 1 else w2
    sign = 1 if T == J else -1

    updated = [round(winner[i] + sign * alpha * (x[i] - winner[i]), 4)
               for i in range(len(x))]
    if J == 1:
        w1 = updated
    else:
        w2 = updated

    rows.append({'Input': str(x), 'T': T, 'D1': round(D1, 4),
                 'D2': round(D2, 4), 'Winner(J)': J,
                 'Match(T=J)': T == J,
                 'w1(new)': str(w1), 'w2(new)': str(w2)})

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', None)
print(pd.DataFrame(rows).to_string(index=False))
print('\nFinal reference vectors:')
print(f'w1 (class 1) = {w1}')
print(f'w2 (class 2) = {w2}')
