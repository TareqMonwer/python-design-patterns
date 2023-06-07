from auto_factory import AutoFactory

factory = AutoFactory()


for car_name in 'Chevy', 'DeepSahara', 'Honda', 'Toyota', 'Ford':
    car = factory.create_instance(car_name)
    car.start()
    car.stop()
