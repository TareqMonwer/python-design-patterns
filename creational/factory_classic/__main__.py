from creational.factory_classic import loader

for factory_name in ['chevy_factory', 'deepsahara_factory', 'honda_factory', 'tesla_factory', 'ford_factory']:
    factory = loader.load_factory(factory_name)
    if factory:
        car = factory.create_auto()
        car.start()
        car.stop()
    else:
        print(f"No factory found for {factory_name}.")
