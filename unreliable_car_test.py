from unreliable_car import UnreliableCar

# test constructor
good_car = UnreliableCar("Lamborghini", 100, 95)
ok_car = UnreliableCar("Old Toyota", 100, 50)
old_car = UnreliableCar("Old Huynhdai", 100, 10)

# test drive()
for i in range(10):
    print(f"{good_car} did drive {good_car.drive(10)}km")
    print(f"{ok_car} did drive {ok_car.drive(50)}km")
    print(f"{old_car} did drive {old_car.drive(10)}km")
# test str
print(good_car)
print(ok_car)
print(old_car)
