class Computer(object):

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))

# from computer_ordering import Computer

class MyComputerBuilder(object):

    def get_computer(self):
        return self._computer

    def build_computer(self):
        self._computer = Computer()
        self.get_case()
        self.build_mainboard()
        self.install_mainboard()
        self.install_hard_drive()
        self.install_video_card()

    def get_case(self):
        self._computer.case = 'Coolermaster N300'
     
    def build_mainboard(self):
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7-4770'
        self._computer.memory = 'Corsair Vengeance 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate 2TB'

    def install_video_card(self):
        self._computer.video_card = 'GeForce GTX 1070'


builder = MyComputerBuilder()
builder.build_computer()
computer = builder.get_computer()
computer.display()
