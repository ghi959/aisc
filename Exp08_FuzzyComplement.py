# Experiment 8(a): standard fuzzy sets (values from assignment PDF)
x = [0.64, 0.645, 0.65, 0.655, 0.66]
A = {0.64: 0, 0.645: 0.75, 0.65: 1, 0.655: 0.5, 0.66: 0}
B = {0.64: 0, 0.645: 0.25, 0.65: 0.75, 0.655: 1, 0.66: 0.5}

A_comp = {k: 1 - A[k] for k in x}
B_comp = {k: 1 - B[k] for k in x}
A_comp_union_B_comp = {k: max(A_comp[k], B_comp[k]) for k in x}
A_comp_inter_B_comp = {k: min(A_comp[k], B_comp[k]) for k in x}
print("complement A", A_comp)
print("complement B", B_comp)
print("complement A union complement B", A_comp_union_B_comp)
print("complement A intersection complement B", A_comp_inter_B_comp)
