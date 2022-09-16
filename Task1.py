import math

import sys
from decimal import *

print(sys.float_info.epsilon)
sys_eps = sys.float_info.epsilon


eps = 1
while 1 + eps / 2 > 1:
    eps /= 2


def pf(msg, val):
    print(msg, val, float.hex(val))


pf('eps =', eps)

while eps / 2 > 0:
    eps /= 2
print('min =', float.hex(eps), eps)

while eps * 2 < math.inf:
    eps *= 2
print('max =', float.hex(eps), eps)


test_number_1 = float(1 + sys_eps/2)
test_number_2 = float(1 + sys_eps)
test_number_3 = float(1 + sys_eps + sys_eps/2)

test_number_4 = float(1 +  sys_eps/2 + sys_eps)
print("1 + eps/2: ", Decimal(test_number_1), " ", float.hex(test_number_1))

print("1 + eps: ", test_number_2, " ", float.hex(test_number_2))

print("1 + eps/2 + eps: ", test_number_3, " ", float.hex(test_number_3))

print("1 + eps + eps/2: ", test_number_4, " ", float.hex(test_number_4))
if __name__ == "__main__":
    pass
