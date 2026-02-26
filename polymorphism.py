class vehicle:
  def __init__(self,vehicle_id,brand):
    self.vehicle_id=vehicle_id
    self.brand=brand
  
  def calculate_rent():
    pass

class Car(vehicle):
  def __init__(self,vehicle_id,brand,price_per_day):
    super().__init__(vehicle_id,brand)
    self.price_per_day=price_per_day
  
  def calculate_rent(self,days):
    return self.price_per_day*days
  

class Bike(vehicle):
  def __init__(self,vehicle_id,brand,price_per_hour):
    super().__init__(vehicle_id,brand)
    self.price_per_hour=price_per_hour
  
  def calculate_rent(self,hour):
    return self.price_per_hour*hour
  

class Truck(vehicle):
  def __init__(self,vehicle_id,brand,price_per_km):
    super().__init__(vehicle_id,brand)
    self.price_per_km=price_per_km
  
  def calculate_rent(self,km):
    return self.price_per_km*km

truck=Truck(101,"Tata",45)
print(f"{truck.calculate_rent(42)} km")

car=Car(102,"BMW",5)
print(f"{car.calculate_rent(40)} days")

    
    