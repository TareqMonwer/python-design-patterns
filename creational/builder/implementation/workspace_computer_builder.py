from abs_builder import AbsComputer


class WorkspaceComputerBuilder(AbsComputer):
    def get_case(self):
        self._computer.case = "Antec Minimal Tower"

    def build_mainboard(self):
        self._computer.mainboard = "MSI 970"
        self._computer.cpu = "Intel i9 13th Gen"
        self._computer.memory = "Corsair Vengeance 16GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = "Western Digital SSD 2TB"

    def install_video_card(self):
        self._computer.video_card = "GeForce GTX"