from director import Director
from workspace_computer_builder import WorkspaceComputerBuilder
from jadupc_builder import JaduPCBuilder


# workspace_computer
computer_builder = Director(WorkspaceComputerBuilder())
computer_builder.build_computer()
work_computer = computer_builder.get_computer()
work_computer.display()

# jadupc
computer_builder = Director(JaduPCBuilder())
computer_builder.build_computer()
jadupc = computer_builder.get_computer()
jadupc.display()
