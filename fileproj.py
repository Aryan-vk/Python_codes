def mult(x):
    y = 6 * 0.2 * 9.8 * x
    return y

def mul():
    z = 0.025 * 500000
    return z

for i in range(1, 31):
    x = i * 0.001
    c = mult(x) / mul()
    print(f"x={x:.3f}, c={c}")

