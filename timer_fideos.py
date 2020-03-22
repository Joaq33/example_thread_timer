import threading
import time
import winsound


def threadfunc(event, mins, secs, text):
    global adition
    barra = ""

    temp = secs + mins * 60
    # print("\r", "Time = {}:{}".format(mins, secs), end="")

    for i in range(0, temp + 2):
        if adition != "":
            barra = "____"
        print("\r", "Para los fideos faltan: {}:{} {} {}".format(mins, secs, barra, adition), end="")
        secs -= 1
        if secs == -1:
            if mins > 0:
                mins -= 1
                secs = 59
            else:
                event.set()
                # print(text)
                adition += " Todo bien, todo correcto"
                winsound.PlaySound("*", winsound.SND_ALIAS)
                winsound.PlaySound("*", winsound.SND_ALIAS)
                # print(text)
        time.sleep(1)


def timer_revolver():
    global adition
    adition = "Seteado"
    revolver.set()
    winsound.PlaySound("*", winsound.SND_ALIAS)
    winsound.PlaySound("*", winsound.SND_ALIAS)


if __name__ == '__main__':
    adition = ""
    minutes = 0
    seconds = 5
    revolver = threading.Event()
    th = threading.Timer(3 * 60, timer_revolver)
    th.start()
    # th = threading.Thread(target=threadfunc, args=(revolver, 3, 30, "revolver"))
    th2 = threading.Thread(target=threadfunc, args=(revolver, 8, 30, "listo"))
    th2.start()
