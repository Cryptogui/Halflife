mass1 = 1.0 ##in kg
halflife = 8.5 ##in minutes
timestep = 0.1 ##in minutes
timeround = 1 ##decimal
timerun = 6 ##in minutes

timesum = 0
massleft = mass1
mass2 = 0

while timesum < timerun:
    print (str(round(timesum, timeround)) + ":" + "min" + " " + str(massleft) + ":" + "kg")
    timesum += timestep
    massleft = (mass1 / 2 ** (timesum / halflife))

