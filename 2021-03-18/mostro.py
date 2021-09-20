import keyboard
from random import choice

DIRECTIONS = ("up", "down", "left", "right")

class Entity:
    def __init__(self, x, y, field, graphic):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities_list.append(self)
        self.graphic = graphic

    def move(self, direction):
        futureX = self.x
        futureY = self.y
        
        if direction == "up" and self.y > 0:
          futureY -= 1
        elif direction == "down" and self.y < self.field.h - 1:
            futureY += 1
        elif direction == "left" and self.x > 0:
            futureX -= 1
        elif direction == "right" and self.x < self.field.w - 1:
            futureX += 1
        e = self.field.get_entity_at_coords(futureX, futureY)

        if e == None:
            self.x = futureX
            self.y = futureY
        else:
            self.collide(e)        
            
    def update(self):
        pass
            
class Gold(Entity):
    def __init__(self, x, y, field):
        super().__init__(x, y, field, "$")
        self.value = 100

class Wall(Entity):
    def __init__(self, x, y, field):
        super().__init__(x, y, field, "#")
            
class Living_Entity(Entity):
    def __init__(self, x, y, name, hp, damage, field, graphic):
        super().__init__(x, y, field, graphic)
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
    
    def attack(self, monster):
        print(self.name, "attacks", monster.name)
        monster.hp -= self.damage
        print(monster.name, "has", monster.hp, "hp")
        if monster.hp <= 0:
            self.field.entities_list.remove(monster)
                    
class Monster(Living_Entity):
    def __init__(self, x, y, name, field):
        super().__init__(x, y, name, 10, 5, field, "m")

    def move(self):
        super().move(choice(DIRECTIONS))
            
    def collide(self, entity):
        if isinstance(entity, Player):
          self.attack(entity)
        
    def update(self):
        self.move()
        
class Player(Living_Entity):
    def __init__(self, x, y, name, field):
        super().__init__(x, y, name, 20, 5, field, "p")
  
    def collide(self, entity):
        if isinstance(entity, Monster):
            self.attack(entity)
        elif isinstance(entity, Gold):
            self.field.score += entity.value
            self.field.entities_list.remove(entity)
      
class Field():
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.entities_list = []
        self.score = 0
        
    def get_entity_at_coords(self, x, y):
        for e in self.entities_list:
            if e.x == x and e.y == y:
                return e

        return None

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities_list:
                    if x == e.x and y == e.y:
                        print("[" + e.graphic + "]", end = "")
                        break   
                else:
                    print("[ ]", end = "")
            print()
    
    def update(self):
        for e in self.entities_list:
            e.update()
    
field = Field(10, 10)
m1 = Monster(2, 2, "Pino", field)
m2 = Monster(1, 1, "Gino", field)
g = Gold(3, 3, field)
w = Wall(4, 4, field)
w = Wall(3, 4, field)
w = Wall(2, 4, field)
w = Wall(2, 3, field)
p = Player(0, 0, "Player", field)
field.draw()
while True:

    if keyboard.is_pressed("w"):
        p.move("up")
        print()
        while keyboard.is_pressed("w"):
            continue
        field.draw()
        field.update()
        
        
    elif keyboard.is_pressed("d"):
        p.move("right")
        print()
        while keyboard.is_pressed("d"):
            continue

        field.draw()
        field.update()  
  
    elif keyboard.is_pressed("s"):
        p.move("down")
        print()
        while keyboard.is_pressed("s"):
            continue
        field.draw()
        field.update()
        
    elif keyboard.is_pressed("a"):
        p.move("left")
        print()
        while keyboard.is_pressed("a"):
            continue
        field.draw()
        field.update()
                
    if p not in field.entities_list or len(field.entities_list) == 1:
        break
