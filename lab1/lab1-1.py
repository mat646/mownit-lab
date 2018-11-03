import numpy as np
import matplotlib.pyplot as plt

# ====================== TASK 1 ======================

# -----------------SUBTASK1-----------------------


def summing():
    return np.float32(0.0000001) + np.float32(100000)


def mul_sub():
    great = np.float32(100000)
    small = np.float32(0.001)
    for i in range(1000):
        great -= small
    return great


def mul_sum():
    suma = np.float32(0)
    small = np.float32(0.001)
    big = np.float32(100000)
    for i in range(1000):
        suma += small
    return big - suma


print("\nTASK 1\n")
print(summing(), "\n")
print(mul_sub(), "\n")
print(mul_sum(), "\n")


# -----------------SUBTASK2-----------------------

def task2(val, length):
    tab = np.empty(shape=[0, 1], dtype=np.float32)
    for e in range(int(length)):
        tab = np.append(tab, val)
    suma = np.float32(0)
    for e in np.nditer(tab):
        suma += e
    return suma


def count_abs_error(val, suma, length):
    return abs(val - (suma / length))


def count_rel_error(val, suma, length):
    return abs((val - (suma / length)) / val) * np.float32(100)


length = np.float32(300000)
float_val = np.float32(0.561025)

result = task2(float_val, length)
abs_error = count_abs_error(float_val, result, length)
rel_error = count_rel_error(float_val, result, length)

print("\nTASK 2\n")
print("ABS ERROR: ", abs_error)
print("REL ERROR: ", rel_error, "%\n")

# -----------SUBTASK3-------------------

# Data for plotting
y = []
for i in range(1000, 2000):
    y.append(count_rel_error(float_val, task2(float_val, np.float32(i)), np.float32(i)))

t = np.arange(1000, 2000, 1)

fig, ax = plt.subplots()
ax.plot(t, y)

ax.set(xlabel='quantity', ylabel='error')
ax.grid()
fig.savefig("test.png")
plt.show()


# --------------SUBTASK4-----------------------


def summing_rec(start, end, array):
    if end - start > 1:
        span = int((end - start) / 2)
        first = summing_rec(start, start + span, array)
        second = summing_rec(start + span, end, array)
        return first + second
    else:
        return array[start]


# Data for plotting
y = []
for i in range(1000, 2000):
    array_task4 = np.empty(i)
    array_task4.fill(float_val)
    print(summing_rec(0, i, array_task4))
    y.append(count_rel_error(float_val, summing_rec(0, i, array_task4), np.float32(i)))

fig, ax = plt.subplots()
ax.plot(t, y)

ax.set(xlabel='quantity', ylabel='error')
ax.grid()
fig.savefig("test_rec.png")
plt.show()


