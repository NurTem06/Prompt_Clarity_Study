import sys
import math

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    b, tx, ty = map(float, data)
    rho = math.hypot(tx, ty) / b
    theta = math.atan2(ty, tx)
    tau = 2.0 * math.pi

    q = theta + tau * math.floor((rho - theta) / tau)

    low = 0.0
    high = min(math.pi / 2.0, q)

    for _ in range(90):
        delta = (low + high) / 2.0
        phi = q - delta
        value = rho * (math.cos(delta) - math.sin(delta) / phi) - phi
        if value > 0.0:
            low = delta
        else:
            high = delta

    delta = (low + high) / 2.0
    radius = b * (q - delta)
    angle = theta - delta

    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    print(f"{x:.12f} {y:.12f}")

if __name__ == "__main__":
    main()