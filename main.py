for _ in range(int(input())):
    n, p, i = map(float, input().split())
    if p < 1e-7:
        print("0.0000")
    else:
        print(f"{p * pow(1 - p, i - 1)/(1 - pow(1 - p, n)):.4f}")
