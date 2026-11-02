"""Experiment 9 PDF: Mamdani fuzzy controller for cruise-control throttle.

Original ranges, triangular MFs, 9 rules, 5 test cases, and 4 saved plots.
"""
import numpy as np
import matplotlib.pyplot as plt


def trimf(x, a, b, c):
    # Same numerical convention as the submitted assignment.
    return np.maximum(np.minimum((x - a) / (b - a + 1e-9),
                                 (c - x) / (c - b + 1e-9)), 0)


# Universes
x_err = np.linspace(-50, 50, 200)
x_acc = np.linspace(-10, 10, 200)
x_thr = np.linspace(0, 100, 200)

# Speed-error membership functions
err_neg = lambda v: trimf(v, -50, -50, 0)
err_zero = lambda v: trimf(v, -25, 0, 25)
err_pos = lambda v: trimf(v, 0, 50, 50)

# Acceleration membership functions
acc_decel = lambda v: trimf(v, -10, -10, 0)
acc_steady = lambda v: trimf(v, -5, 0, 5)
acc_accel = lambda v: trimf(v, 0, 10, 10)

# Throttle output membership functions
thr_low = trimf(x_thr, 0, 0, 50)
thr_med = trimf(x_thr, 25, 50, 75)
thr_high = trimf(x_thr, 50, 100, 100)

plt.figure()
plt.plot(x_err, err_neg(x_err), label='Negative')
plt.plot(x_err, err_zero(x_err), label='Zero')
plt.plot(x_err, err_pos(x_err), label='Positive')
plt.title('Speed Error Membership Functions')
plt.xlabel('Speed Error')
plt.ylabel('Membership')
plt.legend()
plt.savefig('speed_error_mf.png')

plt.figure()
plt.plot(x_acc, acc_decel(x_acc), label='Decel')
plt.plot(x_acc, acc_steady(x_acc), label='Steady')
plt.plot(x_acc, acc_accel(x_acc), label='Accel')
plt.title('Acceleration Membership Functions')
plt.xlabel('Acceleration')
plt.ylabel('Membership')
plt.legend()
plt.savefig('accel_mf.png')

plt.figure()
plt.plot(x_thr, thr_low, label='Low')
plt.plot(x_thr, thr_med, label='Medium')
plt.plot(x_thr, thr_high, label='High')
plt.title('Throttle Membership Functions')
plt.xlabel('Throttle')
plt.ylabel('Membership')
plt.legend()
plt.savefig('throttle_mf.png')


def fuzzy_controller(se, ac, return_agg=False):
    e_n, e_z, e_p = err_neg(se), err_zero(se), err_pos(se)
    a_d, a_s, a_a = acc_decel(ac), acc_steady(ac), acc_accel(ac)

    rules = [
        (min(e_n, a_d), 'Low'),
        (min(e_n, a_s), 'Low'),
        (min(e_n, a_a), 'Medium'),
        (min(e_z, a_d), 'Medium'),
        (min(e_z, a_s), 'Medium'),
        (min(e_z, a_a), 'Medium'),
        (min(e_p, a_d), 'High'),
        (min(e_p, a_s), 'High'),
        (min(e_p, a_a), 'High'),
    ]

    agg = np.zeros_like(x_thr)
    for strength, label in rules:
        if strength > 0:
            mf = {'Low': thr_low, 'Medium': thr_med, 'High': thr_high}[label]
            agg = np.maximum(agg, np.minimum(strength, mf))

    if agg.sum() == 0:
        crisp = 0.0
    else:
        crisp = np.sum(x_thr * agg) / np.sum(agg)  # centroid defuzzification

    if return_agg:
        return crisp, agg
    return crisp


test_cases = [(-30, -5), (0, 0), (20, 3), (40, 8), (-10, 2)]
print('speed_error accel throttle_output')
results = []
for se, ac in test_cases:
    out = fuzzy_controller(se, ac)
    results.append(out)
    print(f'{se:>10} {ac:>5} {out:.2f}')

# Defuzzification visualization for the assignment's demonstration case
se_demo, ac_demo = 20, 3
crisp_demo, agg_demo = fuzzy_controller(se_demo, ac_demo, return_agg=True)
plt.figure()
plt.plot(x_thr, thr_low, '--', linewidth=1, label='Low')
plt.plot(x_thr, thr_med, '--', linewidth=1, label='Medium')
plt.plot(x_thr, thr_high, '--', linewidth=1, label='High')
plt.fill_between(x_thr, agg_demo, color='gray', alpha=0.5,
                 label='Aggregated output')
plt.axvline(crisp_demo, color='red', linestyle='-', linewidth=2,
            label=f'Defuzzified = {crisp_demo:.2f}')
plt.title(f'Aggregated Fuzzy Output (speed_error={se_demo}, accel={ac_demo})')
plt.xlabel('Throttle')
plt.ylabel('Membership')
plt.legend()
plt.savefig('throttle_aggregated_output.png')

print('\nPlots saved: speed_error_mf.png, accel_mf.png, throttle_mf.png, '
      'throttle_aggregated_output.png')
