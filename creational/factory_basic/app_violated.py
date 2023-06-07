from factory import ChevyCar, DeepSaharaCar, HondaCar, NullCar


def get_car(car_name):
    if car_name == "Chevy":
        return ChevyCar()
    elif car_name == "DeepSahara":
        return DeepSaharaCar()
    elif car_name == "Honda":
        return HondaCar()
    else:
        return NullCar(car_name)


for carname in 'Chevy', 'DeepSahara', 'Honda', 'Toyota':
    car = get_car(carname)
    car.start()
    car.stop()
