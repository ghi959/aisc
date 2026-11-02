"""Single-Layer Perceptron for AND - program covered in chat; no source PDF supplied."""

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
T = [0, 0, 0, 1]  # Change to [0, 1, 1, 1] for OR.

weights = [0.0, 0.0]
bias = 0.0
lr = 0.1


def activation(z):
    return 1 if z >= 0 else 0


for epoch in range(20):
    errors = 0
    for x, target in zip(X, T):
        z = sum(x[i] * weights[i] for i in range(2)) + bias
        y = activation(z)
        error = target - y

        for i in range(2):
            weights[i] += lr * error * x[i]
        bias += lr * error
        errors += abs(error)

    if errors == 0:
        break

print('Final weights:', weights)
print('Final bias:', round(bias, 2))
print('A B | Output')
for x in X:
    z = sum(x[i] * weights[i] for i in range(2)) + bias
    print(x[0], x[1], '|', activation(z))
