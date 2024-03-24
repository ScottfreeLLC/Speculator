import numpy as np

def powerball():
    limit = 69
    five_balls = np.random.choice(limit, 5, replace=False)
    limit = 26
    power_ball = np.random.choice(limit, 1)
    return five_balls, power_ball

def megamillions():
    limit = 70
    five_balls = np.random.choice(limit, 5, replace=False)
    limit = 25
    mega_ball = np.random.choice(limit, 1)
    return five_balls, mega_ball

five_balls, power_ball = powerball()
print("Power Ball Numbers %s %s" % (five_balls, power_ball))

five_balls, mega_ball = powerball()
print("Mega Millions Numbers %s %s" % (five_balls, mega_ball))