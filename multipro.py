from multiprocessing import Process, Lock, Value
import board
import neopixel
import time
import sys
import random
qty = 300
#set brightness with the brightness param i.e. brightness=0.01
pixels = neopixel.NeoPixel(board.D18, qty, auto_write=False)

#array that holds the number of pixels of each triangle
triangles = []

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
    (255, 127, 80),
    (250,128,114),
    (255,165,0),
    (255,215,0),
    (255,255,0),
    (124,252,0),
    (0,128,0),
    (0,255,0),
    (0,250,154),
    (0,255,255),
    (64,224,208),
    (135,206,250),
    (30,144,255),
    (0,0,255),
    (0,0,128),
    (75,0,130),
    (153,50,204),
    (238,130,238),
    (128,0,128),
    (255,0,255),
    (255,105,180),
    (255,192,203),
    (255,248,220),
    (255,228,181),
    (220,220,220),
    (255,255,255)
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
    for i in range(qty):
        if color == 'rainbow':
            pixels[i] = colorarray[random.randrange(len(colorarray))]
        else:
            pixels[i] = color
        pixels.show()
    dim(color)    

def spiral(color):
    for i in range(qty):
        if color == 'rainbow':
            pixels[i] = colorarray[random.randrange(len(colorarray))]
        else:
            pixels[i] = color
        pixels.show()
    dim(color)    

def spiralback(color):
    for i in reversed(range(qty)):
        if color == 'rainbow':
            pixels[i] = colorarray[random.randrange(len(colorarray))]
        else:
            pixels[i] = color
        pixels.show()
    dim(color)  

def blink(color):
    brighten(color)
    time.sleep(1)
    dim(color)

def tunnel(color):
    for i in range(0, qty-50, 50):
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
            for x in range(50):
                pixels[i+x] = (r, g, b)
            pixels.show()
    dim(color)

#executes the function depending on input
def f(l, c, o):
    l.acquire()
    if c == "1":
        o.value = 1
        while cho.value == o.value:
           tunnel(colorarray[random.randrange(len(colorarray))])
    elif c == "2":
        o.value = 2
        while cho.value == o.value:
           spiral(colorarray[random.randrange(len(colorarray))])
    elif c == "3":
        o.value = 3
        while cho.value == o.value:
           spiral('rainbow')
    elif c == "4":
        o.value = 4
        while cho.value == o.value:
           spiralback(colorarray[random.randrange(len(colorarray))])
    elif c == "5":
        o.value = 5
        while cho.value == o.value:
           blink(colorarray[random.randrange(len(colorarray))])
    else:
        pixels.fill((0, 0, 0))
        pixels.show()
        return 0
    l.release()

#main
if __name__ == '__main__':
    option = Value('i', 0)
    cho = Value('i', 4)
    lock = Lock()
    while True:
       choice = input("1. tunnel\n2. spiral\n3. rainbow spiral\n4. spiral reverse\n5. blink\n6. off")
       if len(choice) > 0:
         cho.value = int(choice)
       Process(target=f, args=(lock, str(cho.value), option)).start()