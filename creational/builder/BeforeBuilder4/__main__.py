from custom_computer import CustomComputer
from budget_computer import BudgetComputer


# builder = CustomComputer()
builder = BudgetComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
