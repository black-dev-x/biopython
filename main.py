import random_generator
import statictics_calculator

list = random_generator.generateIntegerList(10)
mean = statictics_calculator.mean(list)
median = statictics_calculator.median(list)
mode = statictics_calculator.mode(list)


print(f"list - {list}")
print(f"mean - {mean}")
print(f"median - {median}")
print(f"mode - {mode}")
