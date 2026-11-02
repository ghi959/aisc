# Experiment 8(c): fuzzy Cartesian product R = A x B
A = {"x1": 0.3, "x2": 0.7, "x3": 1}
B = {"y1": 0.4, "y2": 0.9}
R = {(xi, yi): min(A[xi], B[yi]) for xi in A for yi in B}
print("R", R)
