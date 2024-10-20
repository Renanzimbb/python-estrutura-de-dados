numbers = [5, 1, 8, 7, 3, 4, 10, 9]
for i in range(1, len(numbers)):
  j = i
  print(i)
  while j > 0 and numbers[j] < numbers[j-1]:
    numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
    j -= 1
    print(numbers)

