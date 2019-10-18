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


while True:
    if len(sys.argv) > 1:
       if sys.argv[1] == "spiral":
          spiral()
       elif sys.argv[1] == "blink":
          blink()
       elif sys.argv[1] == "tunnel":
          tunnel()
    else:
       pixels.fill((0, 0, 0))
       pixels.show()