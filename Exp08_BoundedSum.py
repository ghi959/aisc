# Experiment 8(b): algebraic/bounded fuzzy sets (values from assignment PDF)
x = [1, 2, 3, 4]
A = {1: 0.2, 2: 0.3, 3: 0.4, 4: 0.5}
B = {1: 0.1, 2: 0.2, 3: 0.2, 4: 1}

bounded_sum = {k: min(1, A[k] + B[k]) for k in x}
print("bounded sum", bounded_sum)
