import random
import time

for i in range(5):
    random_text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=10))
    print(random_text)
    time.sleep(1)
