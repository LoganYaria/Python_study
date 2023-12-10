n = int(input("Enter number plz: "))
for i in range(n):
    if n % (i + 1) == 0:
        print(f'{i+1} is factor of n!')

