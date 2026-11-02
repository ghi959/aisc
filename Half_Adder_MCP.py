"""MCP Half Adder - program covered in chat (no Experiment 1-4 PDF supplied)."""


def mcp(inputs, weights, threshold):
    total = sum(x * w for x, w in zip(inputs, weights))
    return 1 if total >= threshold else 0


def half_adder(a, b):
    inputs = [a, b]
    or_out = mcp(inputs, [1, 1], 1)
    nand_out = mcp(inputs, [-1, -1], -1)
    sum_out = mcp([or_out, nand_out], [1, 1], 2)
    carry_out = mcp(inputs, [1, 1], 2)
    return sum_out, carry_out


print('A B | Sum Carry')
for a in [0, 1]:
    for b in [0, 1]:
        s, c = half_adder(a, b)
        print(a, b, '| ', s, '  ', c)
