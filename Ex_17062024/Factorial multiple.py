# Loop from 1 to 10
for i in range(1, 11):
  # Initialize factorial as 1
  fact = 1
  # Loop from 1 to i (inclusive) and multiply
  for j in range(1, i + 1):
    fact *= j
  # Print the factorial
  print(f"The factorial of {i} is {fact}")
