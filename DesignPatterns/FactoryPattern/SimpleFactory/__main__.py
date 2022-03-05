from autoFactory import AutoFactory

factory = AutoFactory()

for carname in ['Nano', 'Nexon', 'Kia', 'Duster']:
    car = factory.create_instance(carname)
    car.start()
    car.stop()
