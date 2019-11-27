
from multiprocessing import Process, Lock, Value
import board
import neopixel
import time
import sys
import random

#array that holds the number of pixels of each triangle
triangles = [0, 213, 184, 159, 141, 113, 84, 57, 32]
qty = sum(triangles)

#set the brightness of LEDs with the brightness param
#when auto_write=false must use pixels.show() to show pixels
pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False, brightness=0.1)
#colors
colors = {
    'red':(255, 0, 0),
    'coral':(255, 127, 80),
    'salmon':(250,128,114),
    'orange':(255,165,0),
    'gold': (255,215,0),
    'yellow': (255,255,0),
    'light-green': (124,252,0),
    'green': (0,128,0),
    'lime': (0,255,0),
    'spring': (0,250,154),
    'aqua': (0,255,255),
    'turquoise': (64,224,208),
    'sky-blue': (135,206,250),
    'dodger-blue': (30,144,255),
    'blue': (0,0,255),
    'navy': (0,0,128),
    'indigo': (75,0,130),
    'orchid': (153,50,204),
    'violet': (238,130,238),
    'purple': (128,0,128),
    'fuchsia': (255,0,255),
    'hot-pink': (255,105,180),
    'pink': (255,192,203),
    'skin': (255,248,220),
    'moccasin': (255,228,181),
    'smoke': (220,220,220),
    'white': (255,255,255)
}
colorarray = [
    (255, 0, 0),
    (128,128,0),
    (0,128,0),
    (0,255,0),
    (0,128, 128),
    (0,0,255),
    (0,0,128),
    (128,0,128)
]

def dim(color):
    for j in range(0, max(color)+5, 5):
        r = color[0]-j
        if r <= 0:
            r = 0
        g = color[1]-j
        if g <= 0:
            g = 0
        b =  color[2]-j
        if b <= 0:
            b = 0
        pixels.fill((r, g, b))
        pixels.show()

def brighten(color):
    for j in range(0, max(color)-5, 5):
        r = j
        if r >= color[0]:
            r = color[0]
        g = j
        if g >= color[1]:
            g = color[1]
        b =  j
        if b >= color[2]:
            b = color[2]
        pixels.fill((r, g, b))
        pixels.show()

def spiral(color):
    for i in range(0, qty-3, 3):
        if color == 'rainbow':
            pixels[i] = colorarray[random.randrange(len(colorarray))]
            pixels[i+1] = colorarray[random.randrange(len(colorarray))]
            pixels[i+2] = colorarray[random.randrange(len(colorarray))]
        else:
            pixels[i] = color
            pixels[i+1] = color
            pixels[i+2] = color
        pixels.show()
    if color == 'rainbow':
        dim((220, 220, 220))
    else:
        dim(color)    

def spiralback(color):
    for i in reversed(range(0, qty-3, 3)):
        if color == 'rainbow':
            pixels[i] = colorarray[random.randrange(len(colorarray))]
            pixels[i-1] = colorarray[random.randrange(len(colorarray))]
            pixels[i-2] = colorarray[random.randrange(len(colorarray))]
        else:
            pixels[i] = color
            pixels[i-1] = color
            pixels[i-2] = color
        pixels.show()
    dim(color)  

def tunnel(color):
    amt = 0
    for i in range(1, len(triangles)):
        for j in range(0, max(color), 5):
            r = j
            if r >= color[0]:
                r = color[0]
            g = j
            if g >= color[1]:
                g = color[1]
            b =  j
            if b >= color[2]:
                b = color[2]
        amt += triangles[i-1]
        for x in range(amt,amt+triangles[i],1):
            pixels[x] = (r, g, b)
        pixels.show()
        time.sleep(0.2)
    dim(color)

def tunnelback(color):
    amt = qty
    for i in reversed(range(1, len(triangles))):
        for j in range(0, max(color), 5):
            r = j
            if r >= color[0]:
                r = color[0]
            g = j
            if g >= color[1]:
                g = color[1]
            b =  j
            if b >= color[2]:
                b = color[2]
        for x in range(amt-triangles[i],amt,1):
            pixels[x] = (r, g, b)
        pixels.show()
        time.sleep(0.2)
        amt -= triangles[i]
    dim(color)

def blink(color):
    brighten(color)
    time.sleep(1)
    dim(color)

def rings(color):
    amt = 0
    for i in range(1, len(triangles)):
        for j in range(0, max(color), 5):
            r = j
            if r >= color[0]:
                r = color[0]
            g = j
            if g >= color[1]:
                g = color[1]
            b =  j
            if b >= color[2]:
                b = color[2]
        amt += triangles[i-1]
        for x in range(amt,amt+triangles[i],1):
            pixels[x] = (r, g, b)
        pixels.show()
        time.sleep(0.2)
        pixels.fill((0, 0, 0))
        pixels.show()

def sparkle(color):
    inc = 80
    for x in range(inc, qty, inc):
        pixels[random.randrange(x-inc, x)] = color
        inc-=1
    pixels.show()
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    pixels.show()

def sparkleless(color):
    inc = 150
    for x in range(inc, qty, inc):
        pixels[random.randrange(x-inc, x)] = color
        inc-=5
    pixels.show()
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    pixels.show()

#alternate through animations
def alternate(num):
    if num == 1:
        spiral(colorarray[random.randrange(len(colorarray))])
    elif num == 2:
        spiral('rainbow')
    elif num == 3:
        spiralback(colorarray[random.randrange(len(colorarray))])
    elif num == 4:
        tunnel(colorarray[random.randrange(len(colorarray))])
    elif num == 5:
        tunnelback(colorarray[random.randrange(len(colorarray))])
    elif num == 6:
        blink(colorarray[random.randrange(len(colorarray))])
    elif num == 7:
        rings(colorarray[random.randrange(len(colorarray))])
    elif num == 8:
        sparkle(colorarray[random.randrange(len(colorarray))])
    elif num == 9:
        sparkless(colorarray[random.randrange(len(colorarray))])
    
#executes the function depending on input
def f(l, c, o):
    l.acquire()
    pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False, brightness=0.1)
    if c == "1":
        o.value = 1
        while cho.value == o.value:
            spiral(colorarray[random.randrange(len(colorarray))])
    elif c == "2":
        o.value = 2
        while cho.value == o.value:
            spiral('rainbow')
    elif c == "3":
        o.value = 3
        while cho.value == o.value:
            spiralback(colorarray[random.randrange(len(colorarray))])
    elif c == "4":
        o.value = 4
        while cho.value == o.value:
           tunnel(colorarray[random.randrange(len(colorarray))])
    elif c == "5":
        o.value = 5
        while cho.value == o.value:
           tunnelback(colorarray[random.randrange(len(colorarray))])
    elif c == "6":
        o.value = 6
        while cho.value == o.value:
           blink(colorarray[random.randrange(len(colorarray))])
    elif c == "7":
        o.value = 7
        while cho.value == o.value:
           rings(colorarray[random.randrange(len(colorarray))])
    elif c == "8":
        o.value = 8
        pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False, brightness=1)
        while cho.value == o.value:
           sparkle(colorarray[random.randrange(len(colorarray))])
    elif c == "9":
        o.value = 9
        pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False, brightness=1)
        while cho.value == o.value:
           sparkless(random.randrange(1, 9))
    elif c == "10":
        o.value = 10
        while cho.value == o.value:
           alternate(random.randrange(1, 10))
    else:
        pixels.fill((0, 0, 0))
        pixels.show()
    l.release()

#main
if __name__ == '__main__':
    option = Value('i', 0)
    cho = Value('i', 4)
    lock = Lock()
    while True:
        choice = input("1. spiral\n2. rainbow spiral\n3. reverse spiral\n4. tunnel\n5. reverse tunnel\n6. blink\n7. rings\n8. sparkle\n9. sparkle less\n10. random sequence\nother. off")
        if len(choice) > 0:
            cho.value = int(choice)
        Process(target=f, args=(lock, str(cho.value), option)).start()


