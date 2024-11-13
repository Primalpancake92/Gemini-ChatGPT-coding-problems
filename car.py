class Car:
    def __init__(self, make: str, model: str, year: int, fuel_level: float):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        
    
    def drive(self, distance: int):
        if self.fuel_level <= 0:
            self.fuel_level = 0
            return f"Insufficient fuel. Please refuel."
        
        self.fuel_level -= 0.001 * distance 
        
        return self.fuel_level
    
    
    def refuel(self, amount: float):
        if self.fuel_level == 100: 
            return "The fuel tank is full."
        self.fuel_level += amount
        if self.fuel_level >= 100:
            self.fuel_level = 100
        return self.fuel_level
        
        
    def get_car_info(self):
        formatted = f"\nBrand: {self.make}\nModel: {self.model}\nYear released: {self.year}\nFuel level: {self.fuel_level}"
        return formatted
        

if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020, 50.0)
    print(car1.get_car_info())  # Should print car details with fuel level at 50%

    car1.drive(100)  # Drive 100 miles
    print(car1.get_car_info())  # Should print car details with reduced fuel level

    car1.refuel(30)  # Refuel the car by 30%
    print(car1.get_car_info())  # Should print car details with fuel level at 80%
    
    car1.refuel(100)
    print(car1.get_car_info())