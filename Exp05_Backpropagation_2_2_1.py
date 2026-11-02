"""Experiment 5 PDF: 2-2-1 BPNN, one pattern, 10 training iterations."""
import math
import pandas as pd

# Input pattern and target (from assignment)
x1, x2 = 0, 1
t = 1
alpha = 0.25

# Input -> hidden layer weights (including biases)
v11, v21, v01 = 0.6, -0.1, 0.3
v12, v22, v02 = -0.3, 0.4, 0.5

# Hidden -> output layer weights (including bias)
w1, w2, w0 = 0.4, 0.1, -0.2


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(fx):
    return fx * (1 - fx)


max_iterations = 10
rows = []

for iteration in range(1, max_iterations + 1):
    # Forward pass
    z_in1 = v01 + x1 * v11 + x2 * v21
    z1 = sigmoid(z_in1)
    z_in2 = v02 + x1 * v12 + x2 * v22
    z2 = sigmoid(z_in2)
    y_in = w0 + z1 * w1 + z2 * w2
    y = sigmoid(y_in)
    error = t - y

    # Backward pass - calculate all deltas using OLD weights
    delta1 = error * sigmoid_derivative(y)
    delta_w1 = alpha * delta1 * z1
    delta_w2 = alpha * delta1 * z2
    delta_w0 = alpha * delta1

    delta_in1 = delta1 * w1
    delta_in2 = delta1 * w2
    delta_j1 = delta_in1 * sigmoid_derivative(z1)
    delta_j2 = delta_in2 * sigmoid_derivative(z2)

    delta_v11 = alpha * delta_j1 * x1
    delta_v21 = alpha * delta_j1 * x2
    delta_v01 = alpha * delta_j1
    delta_v12 = alpha * delta_j2 * x1
    delta_v22 = alpha * delta_j2 * x2
    delta_v02 = alpha * delta_j2

    # Update all nine weights (biases included)
    v11 += delta_v11
    v21 += delta_v21
    v01 += delta_v01
    v12 += delta_v12
    v22 += delta_v22
    v02 += delta_v02
    w1 += delta_w1
    w2 += delta_w2
    w0 += delta_w0

    rows.append({
        'Iter': iteration,
        'z_in1': round(z_in1, 4), 'z1': round(z1, 4),
        'z_in2': round(z_in2, 4), 'z2': round(z2, 4),
        'y_in': round(y_in, 4), 'y': round(y, 4),
        'Error': round(error, 4),
        'd1(out)': round(delta1, 4),
        'dj1(Z1)': round(delta_j1, 4),
        'dj2(Z2)': round(delta_j2, 4),
        'v11': round(v11, 4), 'v21': round(v21, 4), 'v01': round(v01, 4),
        'v12': round(v12, 4), 'v22': round(v22, 4), 'v02': round(v02, 4),
        'w1': round(w1, 4), 'w2': round(w2, 4), 'w0': round(w0, 4),
    })

pd.set_option('display.width', 250)
pd.set_option('display.max_columns', None)
print(pd.DataFrame(rows).to_string(index=False))
print(f"\nFinal output y after {max_iterations} iterations = {rows[-1]['y']} (Target t = {t})")
