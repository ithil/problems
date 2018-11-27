def way1():
    answers = list()
    print('data:')
    amount_of_values = int(input())
    for _ in range(amount_of_values):
        a, b, c = [int(i) for i in input().split()]
        min = a
        # Change conclusion as new data emerges
        if min > b:
            min = b
        if min > c:
            min = c
        answers.append(min)
    print('\nanswer:')
    print(*answers)

def way2():
    print('data:')
    amount_of_values = int(input())
    answers = [min(int(a), int(b), int(c)) for a, b, c in [input().split() for i in range(amount_of_values)]]
    print('\nanswer:')
    print(*answers)

way1()
