# Base class for a Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Subclass for Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling ")

# Function to demonstrate polymorphism
def vehicle_move_demo(vehicles):
    for vehicle in vehicles:
        vehicle.move()  # Call the move method, behavior depends on the subclass

# Main execution
if __name__ == "__main__":
    # Create instances of different vehicle types
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()

    # Demonstrate polymorphic behavior
    vehicle_list = [car, plane, boat, bicycle]
    vehicle_move_demo(vehicle_list)
