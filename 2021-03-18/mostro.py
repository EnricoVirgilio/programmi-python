import keyboard
class Entity:
    def __init__(self, hp, x, y, damage, field):
        self.hp = hp
        self.x = x
        self.y = y
        self.damage = damage
        self.field = field
        self.field.entities_list.append(self)
  
    def check_collision(self):
        for e in self.field.entities_list:
            if self == e:
                continue
            elif self.x == e.x and self.y == e.y:
                return True

    def move(self):
        if keyboard.is_pressed("w") and self.y > 0:
            while keyboard.is_pressed("w"):
                continue
            self.y -= 1
            if self.check_collision():
                self.y += 1
            else:  
                print()
                self.field.draw()
            
        elif keyboard.is_pressed("d") and self.x < self.field.w -1:
            while keyboard.is_pressed("d"):
                continue
            self.x += 1
            if self.check_collision():
                self.x -= 1
            else:  
                print()
                self.field.draw()
            
        elif keyboard.is_pressed("s") and self.y < self.field.h -1:
            while keyboard.is_pressed("s"):
                continue
            self.y += 1
            if self.check_collision():
                self.y -= 1
            else:  
                print()
                self.field.draw()
            
        elif keyboard.is_pressed("a") and self.x > 0:
            while keyboard.is_pressed("a"):
                continue
            self.x -= 1
            if self.check_collision():
                self.x += 1
            else:  
                print()
                self.field.draw()
    
class Monster(Entity):
    def __init__(self, hp, x, y, damage, field):
        super().__init__(hp, x, y, damage, field)

    def attack(self, monster2):
        monster2.hp -= self.damage
        
    def change_monster(self):
        if keyboard.is_pressed("space"):
            while keyboard.is_pressed("space"):
                continue
            return True
        

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
            
def close_program():
    if keyboard.is_pressed("e"):
        quit()
    
field = Field(10, 10)
monster1 = Monster(10, 5, 5, 20, field)
monster2 = Monster(10, 6, 5, 20, field)
monster3 = Monster(10, 8, 7, 22, field)
field.draw()
while True:
    for e in field.entities_list:
        while True:
            e.move()
            if e.change_monster():
                break
            close_program()
                