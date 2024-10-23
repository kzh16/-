class Animals:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age  
        self.weight = weight
        self.habitat = habitat  
        self.diet = diet  
    
    def eat(self):
        return f"{self.name} ест {self.diet}."

    def sleep(self):
        return f"{self.name} спит."

    def make_sound(self):
        return f"{self.name} издает звук."

    def move(self):
        return f"{self.name} передвигается."


class Reptiles(Animals):
    def __init__(self, name, age, weight, habitat, diet, scale_type):
        super().__init__(name, age, weight, habitat, diet)
        self.scale_type = scale_type  

    def crawl(self):
        return f"{self.name} ползет."

    def shed_skin(self):
        return f"{self.name} сбрасывает кожу."

    def bask_in_sun(self):
        return f"{self.name} греется на солнце."

    def lay_eggs(self):
        return f"{self.name} откладывает яйца."


class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet, special_feature):
        super().__init__(name, age, weight, habitat, diet)
        self.special_feature = special_feature  

    def run(self):
        return f"{self.name} бежит."

    def hunt(self):
        return f"{self.name} охотится."

    def nurture_young(self):
        return f"{self.name} заботится о потомстве."

    def communicate(self):
        return f"{self.name} общается с другими."


class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name  
        self.ticket_price = ticket_price  
        self.animal_performer = animal_performer  
        self.tickets_sold = 0  

    def perform_show(self):
        if isinstance(self.animal_performer, Reptiles):
            return f"На шоу {self.show_name} {self.animal_performer.name} демонстрирует ползание и сбрасывание кожи."
        elif isinstance(self.animal_performer, Mammals):
            return f"На шоу {self.show_name} {self.animal_performer.name} показывает бег и охоту."

    def display_info(self):
        return (f"Шоу: {self.show_name}\n"
                f"Животное-участник: {self.animal_performer.name}\n"
                f"Среда обитания: {self.animal_performer.habitat}\n"
                f"Тип питания: {self.animal_performer.diet}")

    def sell_ticket(self, quantity=1):
        self.tickets_sold += quantity
        return f"Продано {quantity} билетов на шоу {self.show_name}."

    def calculate_revenue(self):
        return f"Выручка от шоу: {self.tickets_sold * self.ticket_price}."



snake = Reptiles("Змея", 5, 10, "Джунгли", "Мясо", "Гладкая")
lizard = Reptiles("Ящерица", 2, 0.5, "Пустыня", "Насекомые", "Шероховатая")
turtle = Reptiles("Черепаха", 100, 200, "Океан", "Растения", "Твердая")


lion = Mammals("Лев", 8, 190, "Саванна", "Мясо", "Большая грива")
elephant = Mammals("Слон", 25, 5000, "Саванна", "Растения", "Длинные бивни")
kangaroo = Mammals("Кенгуру", 4, 85, "Австралия", "Растения", "Большой хвост")


lion_show = ZooShow("Король Саванны", 50, lion)


print(lion_show.perform_show())  
print(lion_show.display_info()) 
print(lion_show.sell_ticket(100))  
print(lion_show.calculate_revenue())  
