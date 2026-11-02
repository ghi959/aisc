"""Full adder using McCulloch-Pitts threshold neurons (no external libraries)."""

def mcp(inputs, weights, threshold):
    total = sum(x * w for x, w in zip(inputs, weights))
    return 1 if total >= threshold else 0

def half_adder(a, b):
    # XOR = (A OR B) AND (A NAND B)
    or_gate = mcp([a, b], [1, 1], 1)
    nand_gate = mcp([a, b], [-1, -1], -1)
    total = mcp([or_gate, nand_gate], [1, 1], 2)
    carry = mcp([a, b], [1, 1], 2)
    return total, carry

def full_adder(a, b, carry_in):
    sum1, carry1 = half_adder(a, b)
    final_sum, carry2 = half_adder(sum1, carry_in)
    carry_out = mcp([carry1, carry2], [1, 1], 1)  # OR
    return final_sum, carry_out

print("A B Cin | Sum Cout")
for a in (0, 1):
    for b in (0, 1):
        for cin in (0, 1):
            s, c = full_adder(a, b, cin)
            print(a, b, cin, " | ", s, "  ", c)
            assert s + 2 * c == a + b + cin
