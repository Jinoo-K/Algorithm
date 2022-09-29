num = int(input())
total = 0
n = 0

while True :
  total += n
  n += 1
  if total >= num :
    break
print(total)