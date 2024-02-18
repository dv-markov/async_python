import dis
import sys


def sum_2(a, b):
    return a + b


dis.dis(sum_2)
print(sys.getswitchinterval())
