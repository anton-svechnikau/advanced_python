"""
HW -- 10.

Knapsack problem.
"""


def knapsack_problem(raw_data):
    """Solution of the knapsack problem."""
    sorted_items_list = sorted(
        [item.split(',') for item in raw_data.split('\n')],
        key=lambda i: float(i[2]) / float(i[1]),
        reverse=True
    )

    knapsack_weight = 0
    knapsack = []
    for i in sorted_items_list:
        if (knapsack_weight + float(i[1])) <= 400:
            knapsack.append(i)
            knapsack_weight += float(i[1])
    return knapsack


if __name__ == '__main__':
    raw_data = """map,9,150
    compass,13,35
    water,153,200
    sandwich,50,160
    glucose,15,60
    tin,68,45
    banana,27,60
    apple,39,40
    cheese,23,30
    beer,52,10
    suntan cream,11,70
    camera,32,30
    T-shirt,24,15
    trousers,48,10
    umbrella,73,40
    waterproof trousers,42,70
    waterproof overclothes,43,75
    note-case,22,80
    sunglasses,7,20
    towel,18,12
    socks,4,50
    book,30,10"""

    print(knapsack_problem(raw_data))
