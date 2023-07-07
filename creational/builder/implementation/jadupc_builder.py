from abs_builder import AbsComputer


class JaduPCBuilder(AbsComputer):
    def get_case(self):
        self._computer.case = "Antec Basic Tower"

    def build_mainboard(self):
        self._computer.mainboard = "ASUS H110M-K"
        self._computer.cpu = "Intel i5 9th Gen"
        self._computer.memory = "Adata DDR4 4GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = "Toshiba 500GB"

    def install_video_card(self):
        self._computer.video_card = "On board"