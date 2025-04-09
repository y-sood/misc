## Overview
This simulation models the interactions between three types of entities (Apex Predators, Predators, and Sheep) within a box. The entities move, interact, reproduce, and consume each other in various ways, with each interaction impacting their lifespan and other properties. The system is visualized using the turtle graphics library and controlled via a graphical user interface (GUI) built using tkinter.

You can customize the behavior of the simulation by adjusting various parameters through the GUI, such as the number of entities, their velocities, lifespans, and more. The simulation showcases interactions such as bouncing off walls, reproduction, and eating, with each of these interactions affecting the entities' lifecycle.

## Controls
The graphical user interface allows you to modify the following parameters before starting the simulation:
# Number of Entities: 
You can specify the number of each type of entity (Apex Predators, Predators, Sheep) in the simulation. These are the primary entities that interact with each other within the box.
<b>Parameters:</b>[Apex Predators, Predators, Sheep]

# Entity Velocities:
Each entity type has configurable velocity ranges for both the X and Y directions. This determines how fast the entities move within the simulation.
<b>Parameters:</b>[Velocity Range for Apex Predators (min and max), Velocity Range for Predators (min and max), Velocity Range for Sheep (min and max)]

# Lifespans:
The lifespan of each entity type is controlled by setting a lifespan factor. The actual lifespan of an entity is randomly determined within a range based on this factor.
<b>Parameters:</b>[Lifespan Range for Apex Predators, Lifespan Range for Predators, Lifespan Range for Sheep]

# Reproduction Cooldown:
After interacting, entities must wait for a cooldown period before they can reproduce. You can set this cooldown for each entity type.
<b>Parameters:</b>[Reproduction Cooldown for Apex Predators, Reproduction Cooldown for Predators, Reproduction Cooldown for Sheep]

# Eating Cooldown:
Entities also have a cooldown period after eating, during which they cannot consume another entity. This cooldown can be set for each entity type.
<b>Parameters:</b>[Eating Cooldown for Apex Predators, Eating Cooldown for Predators, Eating Cooldown for Sheep]

# Lifespan Gain from Eating:
Eating other entities contributes to the eater's lifespan. You can adjust how much lifespan is gained when one entity consumes another.
<b>Parameters:</b>
[Lifespan Gain for Apex Predators when eating Sheep, Lifespan Gain for Apex Predators when eating Predators, Lifespan Gain for Predators when eating Sheep]

# Simulation Frames Per Update:
Controls how often the simulation updates. A smaller value means more frequent updates, making the simulation run faster but potentially less smooth.
<b>Parameter:</b>Frames per update