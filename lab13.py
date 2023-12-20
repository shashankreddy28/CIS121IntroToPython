class Vehicle:
    def __init__(self,make, model,year,VIN,price):
        self.make=make
        self.model=model
        self.year=year
        self.VIN=VIN
        self.price=price
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_VIN(self):
        return self.VIN
    def get_price(self):
        return self.price
    

    def set_make(self,newmake):
        self.make=newmake
    def set_model(self,newmodel):
        self.model=newmodel
    def set_year(self,newyear):
        self.year=newyear
    def set_VIN(self,newVIN):
        self.VIN=newVIN
    def set_price(self,newprice):
        self.price=newprice
    

    def display_details(self):
        return 'make: '+self.make+'\t model: '+self.model+'\t year: '+str(self.year)+'\t VIN: '+self.VIN+'\t price: '+str(self.price)
        
class Car(Vehicle):
    def __init__(self, make, model, year, VIN, price,doors,fuel):
        super().__init__(make, model, year, VIN, price)
        self.doors=doors
        self.fuel=fuel
        self.tax=10
    def get_doors(self):
        return self.doors
    def get_fuel(self):
        return self.fuel
    
    
    def total_cost_car(self):
        self.price=self.price+self.tax
    
    def set_doors(self,newdoors):
        self.doors=newdoors
    def set_fuel(self,newfuel):
        self.fuel=newfuel
    
    def display_details(self):
        
        return super().display_details()+'\t  doors: '+str(self.doors)+'\t fuel_type: '+self.fuel


class Truck(Vehicle):

    def __init__(self, make, model, year, VIN, price,cargo_capacity,towing_capacity):
        super().__init__(make, model, year, VIN, price)
        self.cargo_capacity=cargo_capacity
        self.towing_capacity=towing_capacity
    def get_cargo(self):
        return self.cargo_capacity
    def get_towing(self):
        return self.towing_capacity
    
    def set_cargo(self,newcargo_capacity):
        self.cargo_capacity=newcargo_capacity
    def set_towing(self,newtowing_capacity):
        self.towing_capacity=newtowing_capacity
    
    def display_details(self):
        return super().display_details()+'\t cargo_capacity: '+str(self.cargo_capacity)+'\t towing_capacity: '+str(self.towing_capacity)


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, VIN, price):
        super().__init__(make, model, year, VIN, price)


class VehicleInventory:

    def __init__(self):
        self.list1=[]
    def add_vehicle(self,vehicle_object):
        self.list1.append(vehicle_object)
    def remove_vehicle(self):
        self.list1.pop()
    def display_all(self):
        for x in self.list1:
            print(x.display_details())





car1=Car('make_of_car','model_of_car' , 2000, 'QWERTY123', 100,4,'pertol')
car2=Car('make_of_car2','model_of_car2' , 2002, 'QWERTY123(2)', 100,4,'diesel')
#print(car1.display_details())
VehicleInventory1=VehicleInventory()
VehicleInventory1.add_vehicle(car1)
VehicleInventory1.add_vehicle(car2)
VehicleInventory1.display_all()