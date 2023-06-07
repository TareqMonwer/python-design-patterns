from abs_factory import loader

factory_name = 'modern_furniture'

factory = loader.load_factory(factory_name)

modern_chair = factory.create_chair()
modern_chair.seat_on()
print("---------- Chair End ----------------")

coffee_table = factory.create_coffee_table()
coffee_table.get_color()
