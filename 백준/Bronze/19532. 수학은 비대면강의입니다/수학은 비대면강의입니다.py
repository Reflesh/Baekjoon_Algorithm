### brute force version
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            break


### z3 module version
from z3 import *

a, b, c, d, e, f = map(int, input().split())

x = Int('x')
y = Int('y')
solver = Solver()

solver.add(a * x + b * y == c)
solver.add(d * x + e * y == f)
solver.add(And(x >= -999, x <= 999))
solver.add(And(y >= -999, y <= 999))

if solver.check() == sat:
    solution = solver.model()
    print(solution[x], solution[y])
else:
    print("No solution")
