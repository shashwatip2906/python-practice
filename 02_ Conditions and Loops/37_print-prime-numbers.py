lower = 2
upper = 100

print(f"Prime numbers between {lower} and {upper}:")

for num in range(lower, upper + 1):
    if num > 1:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            print(num)
