"""
test for math
"""
from decimal import Decimal, getcontext

if __name__ == "__main__":
    getcontext().prec = 6
    print(1 / 7)
    print(Decimal("1") / Decimal("7"))

    data = list(map(Decimal, "1.34 1.87 3.45 2.35 1.00 0.03 9.25".split()))
    data_f = list(map(float, "1.34 1.87 3.45 2.35 1.00 0.03 9.25".split()))
    print(data, data_f)
    print(max(data), max(data_f))
    print(sum(data), sum(data_f))
