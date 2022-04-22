from abc import ABC

class Tire(ABC):
    def needs_service(self):
        pass

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for num in self.tire_wear:
            if num >= 0.9:
                return True
        return False

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if sum(self.tire_wear) >= 3:
            return True
        return False