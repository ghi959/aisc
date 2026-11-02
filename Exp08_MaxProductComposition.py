# Experiment 8(c): fuzzy relation composition (matrices from assignment PDF)
R2 = {
    ("x1", "y1"): 0.6, ("x1", "y2"): 0.3,
    ("x2", "y1"): 0.2, ("x2", "y2"): 0.9,
}
S = {
    ("y1", "z1"): 1, ("y1", "z2"): 0.5, ("y1", "z3"): 0.3,
    ("y2", "z1"): 0.8, ("y2", "z2"): 0.4, ("y2", "z3"): 0.7,
}
xs = ["x1", "x2"]
ys = ["y1", "y2"]
zs = ["z1", "z2", "z3"]

T_maxproduct = {
    (xi, zi): max(R2[(xi, yi)] * S[(yi, zi)] for yi in ys)
    for xi in xs for zi in zs
}
print("T max-product composition", T_maxproduct)
