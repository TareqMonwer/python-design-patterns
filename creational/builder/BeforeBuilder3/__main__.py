from computer import Computer
from custom_computer import CustomComputer


builder = CustomComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
