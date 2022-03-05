# computer.py
class Computer:

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))


# abstract_builder.py

# from computer import Computer
from abc import ABC, abstractmethod

class AbsBuilder(ABC):

    def new_computer(self):
        self._computer = Computer()

    def get_computer(self):
        return self._computer

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass

    @abstractmethod
    def install_video_card(self):
        pass

# desktop_builder.py

# from abstract_builder import AbsBuilder

class DesktopBuilder(AbsBuilder):

    def get_case(self, case='Coolermaster N300'):
        self._computer.case = case
     
    def install_mainboard(self, 
                        mainboard='MSI 970',
                        cpu='Intel Core i7-4770',
                        memory='Corsair Vengeance 16GB'
                    ):
        self._computer.mainboard = mainboard
        self._computer.cpu = cpu
        self._computer.memory = memory

    def install_hard_drive(self, hard_drive='Seagate 2TB'):
        self._computer.hard_drive = hard_drive

    def install_video_card(self, video_card='GeForce GTX 1070'):
        self._computer.video_card = video_card


# directory.py

class Director:

    def __init__(self, builder):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def get_computer(self):
        return self._builder.get_computer()

# main.py

# from director import Director
# from desktop_builder import DesktopBuilder

computer_director = Director(DesktopBuilder())
computer_director.build_computer()
computer = computer_director.get_computer()
# computer here is actual object which we want to build
computer.display()


# laptop_builder.py

# from abstract_builder import AbsBuilder

class LaptopBuilder(AbsBuilder):

    def get_case(self, case='IN WIN BP655'):
        self._computer.case = case
     
    def install_mainboard(self, 
                        mainboard='ASRock AM1H-ITX',
                        cpu='AMD Athlon 5150',
                        memory='Kingston ValueRAM 4GB'
                    ):
        self._computer.mainboard = mainboard
        self._computer.cpu = cpu
        self._computer.memory = memory

    def install_hard_drive(self, hard_drive='WD Blue 1TB'):
        self._computer.hard_drive = hard_drive

    def install_video_card(self, video_card='On board'):
        self._computer.video_card = video_card


# main.py

# from director import Director
# from laptop_builder import LaptopBuilder

laptop_director = Director(LaptopBuilder())
laptop_director.build_computer()
laptop = laptop_director.get_computer()
laptop.display()

# in case we need same builder to build same product with 
# different specs we can control the building of product on our own
# instead of handeling it to director

AppleDesktop = DesktopBuilder()
AppleDesktop.new_computer()
AppleDesktop.get_case(case="Apple Case")
AppleDesktop.install_mainboard(mainboard="Apple Mainboard", memory="Apple RAM")
AppleDesktop.install_hard_drive(hard_drive="Apple SDD")
AppleDesktop.install_video_card(video_card="Apple Video Card")
apple_desk = AppleDesktop.get_computer()
apple_desk.display()
