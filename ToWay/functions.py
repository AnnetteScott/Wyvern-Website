import random
def random_way(num_way):
    output = random.randrange(1, (num_way + 1))
    return output

def angle_spin(num_way, selected_way):
    offset = 90
    base = int(180 / (num_way - 1))
    angle = (base * selected_way) - offset
    return angle
