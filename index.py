import random
import time


class Health:
    __health = 100
    __max_health = 100

    def get_health(self):
        return self.__health

    def set_health(self, health):
        if health > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health = health

    def __init__(self, max_health=100):
        self.__max_health = max_health
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0


class Name:
    __name = "default"
    __id = -1

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def __init__(self, id=0, name="plane"):
        if name == "plane":
            if id <= 40:
                name = f"Destroyer [{id}]"
            elif 40 < id <= 80:
                name = f"Bomber [{id}]"
            elif id > 80:
                name = f"Scouter [{id}]"
            else:
                name = f"Unknown plane [{id}]"
        else:
            name = f"Base [{id}]"
        self.__name = name
        self.__id = id


class Position:
    __position = [0, 0]
    __move_speed = 1

    def get_position(self):
        return self.__position

    def move(self, x, y):
        if x > 1:
            x = 1
        elif x < -1:
            x = -1
        if y > 1:
            y = 1
        elif y < -1:
            y = -1

        self.__position[0] += x * self.__move_speed
        self.__position[1] += y * self.__move_speed

    def __init__(self, x=0, y=0, move_speed=1):
        self.__position = [x, y]
        self.__move_speed = move_speed


class Attack:
    __damage = 10

    def get_damage(self):
        return self.__damage

    def attack(self, target: Health):
        target.damage(self.__damage)

    def __init__(self, damage=10):
        self.__damage = damage


class Spot:
    __spotted = False

    def get_spot_status(self):
        return self.__spotted
    
    def set_spot_status(self, spot=True):
        self.__spotted = spot
    
    def __init__(self, spot=False):
        self.__spotted = spot

def generate_plane():
    random_value = random.randint(0, 100)

    if random_value <= 40:

        class Plane(Health, Name, Position, Attack):
            def move(self, x, y):
                if self.get_health() > 0:
                    return super().move(x, y)

            def __init__(self, max_health=100, x=0, y=0, move_speed=1, damage=10):
                Health.__init__(self, max_health)
                Name.__init__(self, id=random_value)
                Position.__init__(self, x, y, move_speed)
                Attack.__init__(self, damage)

        return Plane
    elif 40 < random_value <= 80:

        class Plane(Health, Name, Position, Attack):
            def move(self, x, y):
                if self.get_health() > 0:
                    return super().move(x, y)

            def __init__(self, max_health=100, x=0, y=0, move_speed=1, damage=10):
                Health.__init__(self, max_health)
                Name.__init__(self, id=random_value)
                Position.__init__(self, x, y, move_speed)
                Attack.__init__(self, damage)

        return Plane
    elif random_value > 80:

        class Plane(Health, Name, Position):
            def move(self, x, y):
                if self.get_health() > 0:
                    return super().move(x, y)

            def __init__(self, max_health=100, x=0, y=0, move_speed=2):
                Health.__init__(self, max_health)
                Name.__init__(self, id=random_value)
                Position.__init__(self, x, y, move_speed)

        return Plane


def generate_base():
    random_value = random.randint(101, 111)

    class Base(Health, Name, Position, Spot):
        def __init__(
            self,
            max_health=250,
            x=random.randint(-10, 10),
            y=random.randint(-10, 10),
            move_speed=0,
            spot=False
        ):
            Health.__init__(self, max_health)
            Name.__init__(self, id=random_value, name="base")
            Position.__init__(self, x, y, move_speed)
            Spot.__init__(self, spot)

    return Base


planes = []
bases = []
players_num = 10
bases_num = 3
for i in range(players_num):
    def create_plane():
        plane = generate_plane()()
        plane_id = plane.get_id()
        for temp_plane in planes:
            if(temp_plane.get_id() == plane_id):
                create_plane()
        plane.set_health(100)
        planes.append(plane)
        time.sleep(0.1)

    create_plane()

for i in range(bases_num):
    def create_base():
        base = generate_base()()
        base_id = base.get_id()
        for temp_base in bases:
            if(temp_base.get_id() == base_id):
                create_base()
        base.set_health(250)
        bases.append(base)
        time.sleep(0.1)

    create_base()

while True:
    for plane in planes:
        plane.move(random.randint(-1, 1), random.randint(-1, 1))

    crashed_planes = []
    for plane in planes:
        if plane.get_health() == 0:
            crashed_planes.append(plane)

    destroyed_bases = []
    for base in bases:
        if base.get_health() == 0:
            destroyed_bases.append(base)

    if len(destroyed_bases) == bases_num:
        print('Every Base was destroyed. The game is Completed!')
        break
            

    if len(crashed_planes) >= (players_num - 1):
        for plane in planes:
            if plane.get_health() > 0:
                print(
                    f"{plane.get_name()} : {plane.get_health()} ♥️ : {plane.get_position()} - Last Plane Standing!"
                )
                break
        break

    for plane in planes:
            
        plane_id = plane.get_id()

        if plane.get_health() == 0:
            pass
        else:


            if plane_id <= 40:
                def create_attack_target():
                    attack_target = random.choice(planes)
                    if attack_target.get_health() == 0:
                        create_attack_target()
                    return attack_target

                target = create_attack_target()

                if target.get_id() == plane_id:
                    pass
                else:
                    plane.attack(target)
                
            elif 40 < plane_id <= 80:
                def create_attack_target():
                    attack_target = random.choice(bases)
                    if(len(destroyed_bases) >= bases_num):
                        pass
                    else:
                        if attack_target.get_health() == 0:
                            create_attack_target()
                        return attack_target

                target = create_attack_target()

                if target.get_spot_status() == False:
                    pass
                else:
                    plane.attack(target)
            else:
                def spot_the_base():
                    spotted_base = random.choice(bases)
                    status = spotted_base.get_spot_status()
                    if status == True:
                        spot_the_base()
                    spotted_base.set_spot_status()

                bases_revealed = False

                for base in bases:
                    status = base.get_spot_status()
                    if status == False:
                        bases_revealed = False
                    else:
                        bases_revealed = True

                if bases_revealed == False:

                    random_num = random.randint(0, 100)

                    if random_num < 20:
                        spot_the_base()
                

    for plane in planes:
        if plane.get_health() == 0:
            print(f"{plane.get_name()} : dead inside 💀 : {plane.get_position()}")
        else:
            print(
                f"{plane.get_name()} : {plane.get_health()} ♥️ : {plane.get_position()}"
            )


    base_position = 'Unknown'
    for base in bases:
        if base.get_health() == 0:
            print(f"{base.get_name()} : ass destroyed 💀 : {base.get_position()}")
        else:
            status = base.get_spot_status()
            if status == True:
                base_position = base.get_position()
            else:
                base_position = 'Unknown'
            print(
                f"{base.get_name()} : {base.get_health()} ♥️ : {base_position}"
            )
    print("--------------------------------")

    if input() == "q":
        break
