import sys
import math

def main():
    b, tx, ty = map(float, sys.stdin.buffer.read().split())
    radius = math.hypot(tx, ty) / b
    tau = 2.0 * math.pi
    alpha = math.atan2(ty, tx) % tau

    s = alpha + tau * math.floor((radius - alpha) / tau)
    lo = max(0.0, s - math.pi / 2.0)
    hi = s

    for _ in range(80):
        u = (lo + hi) / 2.0
        delta = s - u
        f = u * (radius * math.cos(delta) - u) - radius * math.sin(delta)
        if f > 0.0:
            hi = u
        else:
            lo = u

    u = (lo + hi) / 2.0
    angle = alpha - (s - u)
    r = b * u
    print(f"{r * math.cos(angle):.12f} {r * math.sin(angle):.12f}")

if __name__ == "__main__":
    main()