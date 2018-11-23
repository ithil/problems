sums = []

print('data:')
count_of_pairs = int(input())

for _ in range(count_of_pairs):
    a, b = input().split()
    sums.append(int(a) + int(b))

print('\nanswer:')
for sum in sums:
    print(sum, end=" ")

print()
