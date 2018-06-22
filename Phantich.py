*Snake:
-Attributes:
x: int
y: int
length:int
speed: int
-Method:
Draw(): None
Update(): None
Move(pos):None
Eat_food()bool
Hit_celling()bool
Hit_floor()bool
Hit_wall()bool
Die(: None

*Food:
- Attributes:
x: int
y: int
radius: int
-Methods:
Draw():None
Update():None

*Scoreboard:
-Attribute:
Score: int
-Methods:
Draw():None

*Game:
-Attributes:
Snake(dict_tail_segment):None
Food(pos):int, random pos-x and pos-y
Scoreboard(score): int
-Methods:
Draw-arena():None
Update():None