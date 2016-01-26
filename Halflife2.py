import plotly
from plotly.graph_objs import Scatter, Layout
##how fun
mass1 = 1.0 ##in kg
halflife = 8.5 ##in minutes
timestep = 0.1 ##in minutes
timeround = 1 ##decimal
timerun = 6 ##in minutes

timesum = 0
massleft = mass1
mass2 = 0
times = []
masses = []
while timesum < timerun:
    times.append(timesum)
    masses.append(massleft)
    print (str(round(timesum, timeround)) + ":" + "min" + " " + str(massleft) + ":" + "kg")
    timesum += timestep
    massleft = (mass1 / 2 ** (timesum / halflife))

plotly.offline.plot({

"data": [
    Scatter(x = times, y = masses)
],

"layout": Layout(
    title="Sönderfall"
)
})
