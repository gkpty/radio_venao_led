from multiprocessing import Process, Lock
import board
import neopixel
import time
import sys
qty = 300
pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False)

def spiral():
    for i in range(qty):
       pixels[i] = (0, 200, 0)
       pixels.show()
    for j in range(51):
       pixels.fill((0, 200-j*4, 0))
       pixels.show()

def blink():
    for i in range(51):
       pixels.fill((0, i*4, 0))
       pixels.show()
    time.sleep(1)
    for j in range(51):
       pixels.fill((0, 200-j*4, 0))
       pixels.show()

def tunnel():
    for i in range(0, 300, 25):
       for y in range(51):
          for x in range(i, i+25):
             pixels[x] = (0, y*4, 0)
          pixels.show()
    for u in range(51):
       pixels.fill((0, 200-u*4, 0))
       pixels.show()

def f(c):
    if c == "tunnel":
        tunnel()
    elif c == "spiral":
        spiral()
    elif c == "blink":
        blink()
    elif c == "off":
        pixels.fill((0, 0, 0))
        pixels.show()
    else:
        pixels.fill((0, 0, 0))
        pixels.show()
        return 0
    return 1

while True:
    if __name__ == '__main__':
       choice = input("1. spiral\n2. tunnel\n3. blink\n4. off")
       Process(target=f, args=(choice)).start()