xy = [[0 for j in range(20)] for i in range(20)]

n = int(input())
for i in range(n):
  x, y = input().split()
  xy[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(xy[i][j], end=" ")
  print()