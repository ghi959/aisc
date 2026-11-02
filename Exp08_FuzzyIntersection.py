# Experiment 8(a): standard fuzzy sets (values from assignment PDF)
x = [0.64, 0.645, 0.65, 0.655, 0.66]
A = {0.64: 0, 0.645: 0.75, 0.65: 1, 0.655: 0.5, 0.66: 0}
B = {0.64: 0, 0.645: 0.25, 0.65: 0.75, 0.655: 1, 0.66: 0.5}

A_inter_B = {k: min(A[k], B[k]) for k in x}
print("A intersection B", A_inter_B)
