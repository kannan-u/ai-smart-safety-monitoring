import random
import time

def ir_trigger():
    time.sleep(0.5)  # slow loop (important)
    return random.choice([True, False])