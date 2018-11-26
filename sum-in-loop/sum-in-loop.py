def way1():
    sum_of_values = 0

    print('data:')
    amount_of_values = int(input())

    values = input().split()

    for i in range(amount_of_values):
        sum_of_values += int(values[i])

    print('\nanswer:')
    print(sum_of_values)

def way2():
    print('data:')
    amount_of_values = int(input())
    values = [int(i) for i in input().split()[:amount_of_values]]
    print('\nanswer:')
    print(sum(values))

way2()
