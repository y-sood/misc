import turtle as tr
import time as time

#Base class for moving objects
class Organism:
    #Constructor
    def __init__(self, x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time):
        #X coord
        self.x = x
        #Y coord
        self.y = y
        #X-velocity
        self.vx = vx
        #Y-velocity
        self.vy = vy
        #Colour
        self.color = color
        #Turtle
        self.turtle_obj = tr.Turtle()
        self.turtle_obj.shape("circle")
        self.turtle_obj.color(self.color)
        self.turtle_obj.penup()
        self.turtle_obj.goto(self.x, self.y)
        self.turtle_obj.shapesize(0.5, 0.5, 0.5)
        #Lifespan
        self.lifespan = lifespan
        #Age
        self.age = 0
        #Reproduction cooldown
        self.last_interaction_time = time.time()
        self.cooldown_time = cooldown_time
        #Eating cooldown
        self.laste_interaction_time = 0
        self.ecooldown_time = ecooldown_time
    #Move object
    def move(self):
        #New position changed by velocity
        self.x += self.vx
        self.y += self.vy
        #Increase age at end of each time step
        self.age += 1
    #Reflect movement
    def update_position(self):
        self.turtle_obj.goto(self.x, self.y)

class ApexPredator(Organism):
    def __init__(self, x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time):
        super().__init__(x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time)

class Predator(Organism):
    def __init__(self, x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time):
        super().__init__(x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time)

class Sheep(Organism):
    def __init__(self, x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time):
        super().__init__(x, y, vx, vy, color, lifespan, age, last_interaction_time, cooldown_time, laste_interaction_time, ecooldown_time)
