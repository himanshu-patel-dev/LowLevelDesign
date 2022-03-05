class Computer:

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))

# in main.py
# from computer_expose_attribute import Computer

class MyComputer:

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = 'Coolermaster N300'
        computer.mainboard = 'MSI 970'
        computer.cpu = 'Intel Core i7-4770'
        computer.memory = 'Corsair Vengeance 16GB'
        computer.hard_drive = 'Seagate 2TB'
        computer.video_card = 'GeForce GTX 1070'

builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
