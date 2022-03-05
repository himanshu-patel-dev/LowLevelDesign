from factories import loader

for factory_name in [
        "kia_factory",
        "nano_factory",
        "nexon_factory",
        "null_factory"
]:

    factory = loader.load_factory(factory_name)
    car = factory.create_auto()

    car.start()
    car.stop()
