import random

def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)
while True:
    print(Unicode())
