from time import sleep

def load (text, duration):
    sleep(duration)
    print(text)

load(input("Enter a message: "), 5)