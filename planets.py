
import matplotlib.pyplot as plt
from physics import velocity

class solar_sys:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(1, 1, 
            subplot_kw = {"projection" : "3d"}, 
            figsize = (self.size / 50, self.size /50))

        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)

class cosmic_body:
    pass


class planet:
    """
    This is the main class for the planets
    """
    def __init__(self, solar_sys, size, color, orbit, speed):
        self.solar_sys = solar_sys
        self.size = size
        self.color = color
        self.orbit = orbit
        self.speed = velocity(*speed)

        self.solar_sys.add_body(self)

    def move(self):
        self.orbit = (self.orbit[0])


class asteroids:
    def __init__(size, speed, period):
        pass

        def speed():
            print(speed)
            pass

        def period():
            print(period)
            pass

"""""
mercury = planet(10, grey, "Mercury")
venus = planet(12, gold, "Venus")
earth = planet(14, grey, "Earth", 1)
mars = planet(11, grey, "Mars")
jupiter = planet(30, grey, "Jupiter")
saturn = planet(25, grey, "Saturn")
uranus = planet(10, grey, "Uranus")
neptune = planet(10, grey, "Neptune")

"""""