month = int(input())

if month // 3 == 1:
  print("spring")
elif month // 3 == 2:
  print("summer")
elif month // 3 == 3:
  print("fall")
elif month // 3 == 4 or month // 3 == 0:
  print("winter")