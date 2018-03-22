from pynput import mouse
from queue import Queue
from PIL.ImageGrab import grab
from time import sleep, time

imgs = Queue()

def on_click(x, y, button, pressed):
    if pressed:
        imgs.put((grab(), time(), x, y, button))
    
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    while listener.running:
        while not imgs.empty():
            rec = imgs.get()
            rec[0].save("img"+"-".join(map(str, rec[1:]))+".png")
        sleep(1)
    #listener.join()
    
