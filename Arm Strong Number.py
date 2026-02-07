n = 153
temp = n
total = 0

while temp > 0:
    d = temp % 10
    total += d ** 3
    temp //= 10

print("Armstrong" if total == n else "Not Armstrong")