import time, threading

def show_ad():
    print("buy more stuff!!!")

def show_support_message():
    print("how can I help you?")

def show(call_back):
    call_back()
    time.sleep(3)
    for i in range(10):
        print(i, end=' ', flush=True)
        time.sleep(1)
    show(call_back)

def show():
    show_ad()
    threading.Timer(3, show).start()
    for i in range(100):
        print(i, end=' ', flush=True)
        time.sleep(1)

show()
# show(show_support_message)