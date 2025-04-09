import random
import turtle as tr
import math
import time
from livingthings import *
import gui
import tkinter as tk

#Domain
class Box:
    #Constructor
    def __init__(self, width, height):
        #Properties
        self.width = width
        self.height = height
        self.objects = []
        #Box representation
        self.draw_box()
    
    #Drawing box onto screen
    def draw_box(self):
        turtle_box = tr.Turtle()
        turtle_box.color("white")
        turtle_box.penup()
        turtle_box.goto(-self.width/2, -self.height/2)
        turtle_box.pendown()
        for _ in range(2):
            turtle_box.forward(self.width)
            turtle_box.left(90)
            turtle_box.forward(self.height)
            turtle_box.left(90)
        turtle_box.hideturtle()

    #Draw initial population into box
    def spawn_objects(self, counts, config):
        #Remove all old objects
        self.objects.clear()
        #Color
        colour = ["red", "green", "blue"]
        types = [ApexPredator, Predator, Sheep]
        for i, (cls) in enumerate(types):
            for _ in range(counts[i]):
                obj = cls(
                    #Spawning within 80% of box
                    x=random.uniform(-0.4*self.width, 0.4*self.width),
                    y=random.uniform(-0.4*self.height, 0.4*self.height),
                    #Random velocity
                    vx=random.uniform(-config['velocityb'][i], config['velocityt'][i]),
                    vy=random.uniform(-config['velocityb'][i], config['velocityt'][i]),
                    color=colour[i],
                    #Random lifespan b/w user defined ranges
                    lifespan=random.randint(int(config['stdtop'][i]*config['lifespans'][i]), int(config['stdbottom'][i]*config['lifespans'][i])),
                    #User defined time-things
                    age=0,
                    last_interaction_time=time.time(),
                    cooldown_time=config['rc'][i],
                    laste_interaction_time=time.time(),
                    ecooldown_time=config['ec'][i]
                )
                self.add_object(obj)

    #Add objects to box object - Method
    def add_object(self, obj):
        self.objects.append(obj)

    #Let the course of nature run - Method
    def dynamics(self, config):
        #To remove balls from old age
        to_remove = []
        
        #Go through all objects and check for old age
        for obj in self.objects:
            if obj.age > obj.lifespan:
                #Remove from screen
                obj.turtle_obj.hideturtle()
                #Add to list for removal
                to_remove.append(obj)
            #If still young
            else:
                #Move
                obj.move()
                #Bounce of wall if applicable
                self.wall_bounce(obj)
        
        #Check interaction between objects
        self.check_interactions(to_remove, config)
        
        #Update positions
        for obj in self.objects:
            obj.update_position()
        
        #Kill old balls :(
        for obj in to_remove:
            if obj in self.objects:
                self.objects.remove(obj)

    #Check interaction between each pair
    def check_interactions(self, to_remove, config):
        for i, obj1 in enumerate(self.objects):
                #To avoid repetition and self comparision
                for j in range(i+1, len(self.objects)):
                    obj2 = self.objects[j]
                    #Detect contact
                    if self.contact(obj1, obj2):
                        #Bouncing balls off each other
                        self.interaction(obj1, obj2, to_remove, config)
    
    #Bounce of wall
    def wall_bounce(self, obj):
        #Left wall bounce
        if obj.x < -self.width/2:
            obj.x = -self.width/2
            obj.vx = -obj.vx
        #Right wall bounce
        elif obj.x > self.width/2:
            obj.x = self.width/2
            obj.vx = -obj.vx
        #Bottom wall bounce
        if obj.y < -self.height/2:
            obj.y = -self.height/2
            obj.vy = -obj.vy
        #Top wall bounce
        elif obj.y > self.height/2:
            obj.y = self.height/2
            obj.vy = -obj.vy
    
    #Detect contact between two balls 
    def contact(self, obj1, obj2):
        distance = math.sqrt((obj1.x-obj2.x)**2 + (obj1.y-obj2.y)**2)
        return distance <= 10
    
    #Bounce balls off each other : Fully elastic bounce  
    def interaction(self, obj1, obj2, to_remove, config):
        #Object interactions
        #Storing current time for cool down calculation
        current_time = time.time()
        #Bouncing
        dx = obj1.x - obj2.x
        dy = obj1.y - obj2.y
        dvx = obj1.vx - obj2.vx
        dvy = obj1.vy - obj2.vy
        # Distance squared
        dist2 = dx**2 + dy**2
        # Avoid division by zero
        if dist2 == 0:
            return
        # Dot product of velocity difference and position difference
        dot_product = dvx * dx + dvy * dy
        # Masses (assumed equal for now)
        m1, m2 = 1, 1
        # Calculate the new velocities
        obj1.vx -= (2 * m2 / (m1 + m2)) * (dot_product / dist2) * dx
        obj1.vy -= (2 * m2 / (m1 + m2)) * (dot_product / dist2) * dy
        obj2.vx -= (2 * m1 / (m1 + m2)) * (dot_product / dist2) * -dx
        obj2.vy -= (2 * m1 / (m1 + m2)) * (dot_product / dist2) * -dy
        #Reproduction
        if current_time - obj1.last_interaction_time > obj1.cooldown_time and current_time - obj2.last_interaction_time > obj2.cooldown_time:
            self.reproduce(obj1, obj2, config)
        #Nutrition
        if current_time - obj1.laste_interaction_time > obj1.ecooldown_time and current_time - obj2.laste_interaction_time > obj2.ecooldown_time:
            self.eating(obj1, obj2, config, to_remove)            

    #Handle reproduction here
    def reproduce(self, obj1, obj2, config):
        current_time = time.time()
        #Apex predator reproduction
        if isinstance(obj1, ApexPredator) and isinstance(obj2, ApexPredator):
            baby_apexpredator = (ApexPredator(x = obj1.x, y = obj1.y, 
                vx=obj2.vx,
                vy=-obj1.vy,
                color="red",
                lifespan = random.randint(int(config['stdtop'][0]*config['lifespans'][0]), int(config['stdbottom'][0]*config['lifespans'][0])),
                age=0,
                last_interaction_time= current_time,
                cooldown_time=config['rc'][0],
                laste_interaction_time = current_time, 
                ecooldown_time = config['ec'][0]))
            obj1.last_interaction_time = current_time
            obj2.last_interaction_time = current_time
            self.add_object(baby_apexpredator)
        #Predator reproduction
        if isinstance(obj1, Predator) and isinstance(obj2, Predator):
            baby_predator = (Predator(x = obj1.x, y = obj1.y, 
                vx=-obj1.vx,
                vy=obj2.vy,
                color="green",
                lifespan = random.randint(int(config['stdtop'][1]*config['lifespans'][1]), int(config['stdbottom'][1]*config['lifespans'][1])),
                age=0,
                last_interaction_time= current_time,
                cooldown_time=config['rc'][1],
                laste_interaction_time = current_time, 
                ecooldown_time = config['ec'][1]))
            obj1.last_interaction_time = current_time
            obj2.last_interaction_time = current_time
            self.add_object(baby_predator)
        #Sheep reproduction
        if isinstance(obj1, Sheep) and isinstance(obj2, Sheep):
            baby_sheep1 = (Sheep(x = obj1.x, y = obj1.y, 
                vx=-obj2.vx,
                vy=-obj1.vy,
                color="blue",
                lifespan = random.randint(int(config['stdtop'][2]*config['lifespans'][2]), int(config['stdbottom'][2]*config['lifespans'][2])),
                age=0,
                last_interaction_time= current_time,
                cooldown_time=config['rc'][2],
                laste_interaction_time = current_time,
                ecooldown_time = 0))
            obj1.last_interaction_time = current_time
            obj2.last_interaction_time = current_time
            self.add_object(baby_sheep1)

    #Handle eating here
    def eating(self, obj1, obj2, config, to_remove):
        if isinstance(obj1, ApexPredator) and not isinstance(obj2, ApexPredator):
            obj2.turtle_obj.hideturtle()
            to_remove.append(obj2)
            #Eating gives longer life
            obj1.age -= config['lifegain'][0] if isinstance(obj2, Sheep) else config['lifegain'][1]
        elif isinstance(obj1, Predator) and isinstance(obj2, Sheep):
            obj2.turtle_obj.hideturtle()
            to_remove.append(obj2)
            obj1.age -= config['lifegain'][2] 
            obj1.laste_interaction_time = time.time()

#Method to run simulation
def simulate(wn, box, config):
    box.dynamics(config)
    wn.update()
    wn.ontimer(lambda: simulate(wn, box, config), config['frames'])

#Start of sim method
def start_simulation(config, counts):
    wn.clearscreen()
    wn.bgcolor("black")
    wn.title("Bouncing Ball Simulator")
    wn.setup(width = 800, height = 800)
    #CREATING THE BOX
    box = Box(width= 600, height= 600)
    #ADDING OBJECTS
    box.spawn_objects(counts, config)
    simulate(wn, box, config)

#Main
if __name__ ==  "__main__":
    #CREATING THE WINDOW
    wn = tr.Screen()
    wn.bgcolor("black")
    wn.title("Bouncing Ball Simulator")
    wn.setup(width = 800, height = 800)
    #Window for GUI
    root = tk.Tk()
    #Create gui and start simulation keeping input window open
    sgui = gui.ConfigGUI(root, start_simulation)
    #KEEP WINDOW OPEN
    root.mainloop()
    wn.mainloop()