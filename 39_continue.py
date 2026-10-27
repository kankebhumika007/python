# this program prints numbers from 1 to 10, skipping the numbers that are divisible by 3 
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)