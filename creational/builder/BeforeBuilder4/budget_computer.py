from computer import Computer


class BudgetComputer(object):
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
        self._computer.case = "Antec Tower"
    
    def build_mainboard(self):
        self._computer.mainboard = "ASUS H110M-K"
        self._computer.cpu = "Intel i5 9th Gen"
        self._computer.memory = "Corsair Vengeance 8GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = "Western Digital 2TB"

    def install_video_card(self):
        self._computer.video_card = ""
        