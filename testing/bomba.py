import sys
import time

i = int(sys.argv[1]) # fijamos el valor inicial

while i > 0:
    print(i)
    time.sleep(1) # 1 seg por cada iteración
    i -= 1

print("Boom!")
