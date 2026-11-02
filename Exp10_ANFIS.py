"""Experiment 10 PDF: ANFIS-style model on scikit-learn diabetes progression data.

IMPORTANT: The 0/1 label in this class demonstration is obtained by splitting
continuous disease-progression targets at the median. It is NOT an actual
clinical diabetes diagnosis or validated medical risk predictor.
"""
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# Inputs: age, bmi, bp, blood sugar 's6' (same as assignment)
features = ['age', 'bmi', 'bp', 's6']
labels = ['age', 'bmi', 'bp', 'glucose']

data = load_diabetes()
cols = [data.feature_names.index(f) for f in features]
X = data.data[:, cols]
y = (data.target > np.median(data.target)).astype(int)
X = (X - X.mean(axis=0)) / X.std(axis=0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
print('X train:', X_train.shape, ' y train:', y_train.shape)
print('X test:', X_test.shape, ' y test:', y_test.shape)


def gaussian(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))


means = [-1.0, 1.0]
sigma = 1.0
n_in = X.shape[1]
rules = list(product([0, 1], repeat=n_in))
n_rules = len(rules)
print('Number of rules:', n_rules)


def rule_strength(x):
    mu = np.array([[gaussian(x[i], m, sigma) for m in means]
                   for i in range(n_in)])
    return np.array([min(mu[i, r[i]] for i in range(n_in))
                     for r in rules])


W = np.zeros((n_rules, n_in + 1))


def infer(x):
    strength = rule_strength(x)
    xb = np.append(x, 1)
    rule_out = W @ xb
    output = np.sum(strength * rule_out) / (np.sum(strength) + 1e-9)
    return output, strength, xb


eta = 0.05
epochs = 100
rng = np.random.default_rng(0)
loss_history = []

for epoch in range(epochs):
    total = 0
    for i in rng.permutation(len(X_train)):
        output, strength, xb = infer(X_train[i])
        error = y_train[i] - output
        norm_strength = strength / (np.sum(strength) + 1e-9)
        W += eta * error * np.outer(norm_strength, xb)
        total += error ** 2
    loss_history.append(total / len(X_train))
    if (epoch + 1) % 20 == 0:
        print(f'Epoch {epoch + 1} MSE = {loss_history[-1]:.4f}')


def predict(Xs):
    return np.array([int(infer(x)[0] >= 0.5) for x in Xs])


train_pred = predict(X_train)
test_pred = predict(X_test)
train_acc = np.mean(train_pred == y_train) * 100
test_acc = np.mean(test_pred == y_test) * 100
print(f'\nTrain accuracy = {train_acc:.2f} %')
print(f'Test accuracy = {test_acc:.2f} %')

tn = np.sum((test_pred == 0) & (y_test == 0))
fp = np.sum((test_pred == 1) & (y_test == 0))
fn = np.sum((test_pred == 0) & (y_test == 1))
tp = np.sum((test_pred == 1) & (y_test == 1))
print('\nConfusion matrix (test)')
print('              Pred 0 Pred 1')
print(f'Actual 0      {tn:>6} {fp:>6}')
print(f'Actual 1      {fn:>6} {tp:>6}')

print('\nSample predictions on unseen data')
print('Patient ANFIS output Predicted Actual')
for i in range(8):
    out = infer(X_test[i])[0]
    print(f'{i + 1:>7} {out:>11.3f} {test_pred[i]:>9}    {y_test[i]:>6}')

# Membership-function plots and training error plot
xs = np.linspace(-3, 3, 200)
fig, axs = plt.subplots(2, 2, figsize=(9, 6))
for i, ax in enumerate(axs.ravel()):
    ax.plot(xs, gaussian(xs, means[0], sigma), label='Low')
    ax.plot(xs, gaussian(xs, means[1], sigma), label='High')
    ax.set_title(labels[i] + ' membership functions')
    ax.set_xlabel(labels[i] + ' (standardized)')
    ax.set_ylabel('Membership')
    ax.legend()
plt.tight_layout()
plt.savefig('anfis_membership_functions.png')

plt.figure()
plt.plot(range(1, epochs + 1), loss_history)
plt.title('ANFIS training error')
plt.xlabel('Epoch')
plt.ylabel('Mean squared error')
plt.savefig('anfis_training_error.png')
plt.show()
