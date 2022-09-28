a = input()
a = int(a,16) # 16진수로 저장

for i in range(1,16):
  print("%X*%X=%X"%(a,i,a*i))