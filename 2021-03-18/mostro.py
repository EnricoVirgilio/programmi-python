import keyboard
class Entity:
    def __init__(self, hp, x, y, damage, field):
        self.hp = hp
        self.x = x
        self.y = y
        self.damage = damage
        self.field = field
        self.field.entities_list.append(self)

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "right" and self.x < self.field.w - 1:
            self.x += 1
        elif direction == "down" and self.y < self.field.h - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1

class Monster(Entity):
    def __init__(self, hp, x, y, damage, field):
        super().__init__(hp, x, y, damage, field)

    def attack(self, monster2):
        monster2.hp -= self.damage
        
class Field():
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.entities_list = []
        
    def draw(self):
        for a in range(self.h):
            for b in range(self.w):
                for e in self.entities_list:
                    if a == e.y and b == e.x:
                        print("[x]", end = "")
                        break
                else:
                    print("[ ]", end = "")
            print()
    
field = Field(10, 10)
monster1 = Monster(10, 5, 5, 20, field)
monster2 = Monster(10, 6, 5, 20, field)
monster3 = Monster(10, 8, 7, 22, field)
field.draw()
while True:
    for e in field.entities_list:
        while True:
            if keyboard.is_pressed("w"):
                e.move("up")
                print()
                field.draw()
                while keyboard.is_pressed("w"):
                    continue
                
            elif keyboard.is_pressed("d"):
                e.move("right")
                print()
                field.draw()
                while keyboard.is_pressed("d"):
                    continue
            
            elif keyboard.is_pressed("s"):
                e.move("down")
                print()
                field.draw()
                while keyboard.is_pressed("s"):
                    continue
                
            elif keyboard.is_pressed("a"):
                e.move("left")
                print()
                field.draw()
                while keyboard.is_pressed("a"):
                    continue
                
            elif keyboard.is_pressed("space"):
                if e == field.entities_list[-1]:
                    break
                else:
                    while keyboard.is_pressed("space"):
                        continue
                    break
            
            elif keyboard.is_pressed("e"):
                break
        if keyboard.is_pressed("space"):
            while keyboard.is_pressed("space"):
                continue
            break
            
        if keyboard.is_pressed("e"):
            break
        
    if keyboard.is_pressed("e"):
        break