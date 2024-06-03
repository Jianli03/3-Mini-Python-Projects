import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problems():
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)

  expr = str(left) + " " + operator+ " " + str(right)
  return expr, eval(expr)

wrong = 0
input("Press enter key to start: ")
print("--------------------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
  expr, answer = generate_problems()
  while True:
    guess = input("Problem #" + str(i+1) +  ": " + expr + " = ")
    if guess == str(answer):
      break
    wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("--------------------------------")
print(f"Nice work! Your finished in {round(total_time, 2)}  seconds!" )