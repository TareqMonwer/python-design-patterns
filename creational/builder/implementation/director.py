from abs_builder import AbsComputer


class Director(object):
    def __init__(self, builder: AbsComputer) -> None:
        self._builder: AbsComputer = builder

    def get_computer(self):
        return self._builder.get_computer()
    
    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()
