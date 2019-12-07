class Instruction:
    code, argument_num = 0, 0
    def execute(self, intcode, arguments):
        pass

class PlusInstruction(Instruction):
    code, argument_num = 1, 3
    def execute(self, intcode, arguments):
        intcode.update(arguments[2].address, arguments[0].value + arguments[1].value)
        return intcode.pc + 4

class MultiplyInstruction(Instruction):
    code, argument_num = 2, 3
    def execute(self, intcode, arguments):
        intcode.update(arguments[2].address, arguments[0].value * arguments[1].value)
        return intcode.pc + 4

class InputInstruction(Instruction):
    code, argument_num = 3, 1
    def execute(self, intcode, arguments):
        intcode.update(arguments[0].address, intcode.pop_input())
        return intcode.pc + 2

class OutputInstruction(Instruction):
    code, argument_num = 4, 1
    def execute(self, intcode, arguments):
        intcode.output = intcode.get(arguments[0].address)
        return intcode.pc + 2

class JumpIfTrueInstruction(Instruction):
    code, argument_num = 5, 2
    def execute(self, intcode, arguments):
        return arguments[1].value if arguments[0].value != 0 else intcode.pc + 3

class JumpIfFalseInstruction(Instruction):
    code, argument_num = 6, 2
    def execute(self, intcode, arguments):
        return arguments[1].value if arguments[0].value == 0 else intcode.pc + 3

class LessThanInstruction(Instruction):
    code, argument_num = 7, 3
    def execute(self, intcode, arguments):
        intcode.update(arguments[2].address, int(arguments[0].value < arguments[1].value))
        return intcode.pc + 4

class EqualsInstruction(Instruction):
    code, argument_num = 8, 3
    def execute(self, intcode, arguments):
        intcode.update(arguments[2].address, int(arguments[0].value == arguments[1].value))
        return intcode.pc + 4

class HaltInstruction(Instruction):
    code, argument_num = 99, 0
    def execute(self, intcode, arguments):
        return None

class Argument:
    def __init__(self, address, value):
        self.address = address
        self.value = value

class IntCode:
    def __init__(self, program, inputs):
        self.program = program[:]
        self.inputs = inputs[::-1]
        self.output = None
        self.pc = 0

    def _get_instruction(self, instruction_code):
        return next(cls for cls in Instruction.__subclasses__() if cls.code == instruction_code)

    def _parse_arguments(self, argument_num):
        modes = str(self.program[self.pc]).zfill(5)[:3][::-1]
        arguments = []
        for i in range(argument_num):
            address = self.program[self.pc+i+1]
            arguments.append(Argument(address, self.program[address] if modes[i] == '0' else address))
        return arguments

    def run(self):
        self.output = None
        while self.pc is not None and self.output is None:
            instruction = self._get_instruction(self.program[self.pc] % 100)
            arguments = self._parse_arguments(instruction.argument_num)
            self.pc = instruction().execute(self, arguments)
        return self.pc is None

    def get(self, address):
        return self.program[address]

    def update(self, address, value):
        self.program[address] = value

    def pop_input(self):
        return self.inputs.pop()

    def add_input(self, value):
        self.inputs = [value] + self.inputs