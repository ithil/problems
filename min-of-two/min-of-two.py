def way1():
    answers = list()
    print('data:')
    amount_of_values = int(input())
    for _ in range(amount_of_values):
        a, b = [int(i) for i in input().split()]
        if a < b:
            answers.append(a)
        else:
            answers.append(b)
    print('\nanswer:')
    print(*answers)

def way2():
    print('data:')
    amount_of_values = int(input())
    answers = [min(int(a), int(b)) for a, b in [input().split() for i in range(amount_of_values)]]
    print('\nanswer:')
    print(*answers)

way2()
