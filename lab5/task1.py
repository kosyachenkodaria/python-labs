class Rocket(): 
    def __init__(self, mass, fuel, engine):  
        self.mass = mass
        self.fuel = fuel
        self.engine = engine

    def spend_fuel(self, count):  
        self.fuel -= count
        self.mass -= count
        if self.fuel <= 0:  
            self.fuel=0
            self.engine = False    
            return False
        elif self.fuel > 0:
            self.engine = True
            return True         

    def get_fuel_level(self):
        return f'Кол-во топлива: {self.fuel}'
    def get_total_weight(self):
        return f'Масса ракеты: {self.mass}'
    def get_is_engine_running(self):
        return f'Состояние двигателя: {self.engine}'
    
def Main():
    l = Rocket(150000, 60000, True)
    while l.fuel > 0:                    
        l.spend_fuel(2000)
        print(l.get_fuel_level(), end='; ')
        print(l.get_total_weight(), end='; ')
        print(l.get_is_engine_running())
Main()