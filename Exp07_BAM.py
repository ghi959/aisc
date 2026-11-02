"""Experiment 7(c) PDF: BAM patterns E and F, forward recall as in assignment."""
import numpy as np


def activation(y):
    return np.where(y > 0, 1, -1)


# Original PDF's 15-element bipolar input patterns
E = np.array([1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1])
F = np.array([1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1])
target_E = np.array([-1, 1])
target_F = np.array([1, 1])

W1 = np.outer(E, target_E)
W2 = np.outer(F, target_F)
W_bam = W1 + W2
print('Total weight matrix W (15 x 2):')
print(W_bam)


def bam_test(x_pattern, label):
    y_in = x_pattern @ W_bam
    y = activation(y_in)
    print(f'\nTest pattern {label}: y_in = {y_in.tolist()} -> '
          f'Final response = {y.tolist()}')
    return y


bam_test(E, 'E')
bam_test(F, 'F')
