
class Vehicle:
    def __init__(self, main_color, max_occupancy, interior_color, vehicle_name= None):
        self.main_color = main_color
        self.maximum_occupancy = max_occupancy
        self.interior_color = interior_color
        self.vehicle_name = vehicle_name

# The blue Ram drives past. RRrrrrrummbbble!
    def drive(self, sound ="RRRRRRRUUUUUMMMMMM!!"):
        print(f" The {self.main_color} {self.vehicle_name} drives past. {sound}")

    def turn(self, direction):
        print(f"The vehicle turns {direction}")

    def stop (self):
        print(f"The {self.vehicle_name} has stoped.")

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0
        self.vehicle_name = "Tesla"

    def charge_battery(self):
        ...
class Honda(Vehicle):
    def __init__(self):
        self.gas_miles = 9
        self.vehicle_name = "Honda"

class Ford (Vehicle):
    def __init__(self):
        self.gas_miles = 10

class Alfa_Romeo(Vehicle):
    def __init__(self):
        self.gas_miles = 20
        self.vehicle_name = "Alfa Romeo"

class general_motors(Vehicle):
      def __init__(self, gas_miles):
          super().__init__("green", 6, "black", "General Motors")
          self.gas_miles = gas_miles



      def drive(self, sound ="VVRRRUMMM!!"):
        print(f" The {self.main_color} {self.vehicle_name} drives past. {sound}")

    #  "The white Cessna rolls to a stop after rolling a mile down the runway."
      def stop (self):
        print(f"The {self.vehicle_name} rolls to a stop after rolling a mile down the runway.")

      def turn(self, direction= "right"):
        print(f"The vehicle turns {direction}")





Matthew = Honda()
Matthew.main_color = "red"
Matthew.drive()

John = general_motors(24)
John.drive()
John.stop()
John.turn()
