hz, bit, byte, sec = map(int, input().split())
print(round(hz*bit*byte*sec/8/1024/1024, 1),"MB")