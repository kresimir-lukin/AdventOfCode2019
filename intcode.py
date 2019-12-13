class Instruction:
    code, argument_num = 0, 0
    def execute(self, intcode, arguments):
        pass
    def new_pc(self, intcode):
        return intcode.pc + self.argument_num + 1

class PlusInstruction(Instruction):
    code, argument_num = 1, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, arguments[0].value + arguments[1].value)
        return self.new_pc(intcode)

class MultiplyInstruction(Instruction):
    code, argument_num = 2, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, arguments[0].value * arguments[1].value)
        return self.new_pc(intcode)

class InputInstruction(Instruction):
    code, argument_num = 3, 1
    def execute(self, intcode, arguments):
        intcode.set(arguments[0].address, intcode.get_input())
        return self.new_pc(intcode)

class OutputInstruction(Instruction):
    code, argument_num = 4, 1
    def execute(self, intcode, arguments):
        intcode.output = arguments[0].value
        return self.new_pc(intcode)

class JumpIfTrueInstruction(Instruction):
    code, argument_num = 5, 2
    def execute(self, intcode, arguments):
        return arguments[1].value if arguments[0].value != 0 else self.new_pc(intcode)

class JumpIfFalseInstruction(Instruction):
    code, argument_num = 6, 2
    def execute(self, intcode, arguments):
        return arguments[1].value if arguments[0].value == 0 else self.new_pc(intcode)

class LessThanInstruction(Instruction):
    code, argument_num = 7, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, int(arguments[0].value < arguments[1].value))
        return self.new_pc(intcode)

class EqualsInstruction(Instruction):
    code, argument_num = 8, 3
    def execute(self, intcode, arguments):
        intcode.set(arguments[2].address, int(arguments[0].value == arguments[1].value))
        return self.new_pc(intcode)
        
class RelativeBaseOffsetInstruction(Instruction):
    code, argument_num = 9, 1
    def execute(self, intcode, arguments):
        intcode.relative_base += arguments[0].value
        return self.new_pc(intcode)

class HaltInstruction(Instruction):
    code, argument_num = 99, 0
    def execute(self, intcode, arguments):
        intcode.halted = True
        return None

class Argument:
    def __init__(self, value, address):
        self.value = value
        self.address = address
        
class IntCode:
    def __init__(self, program, inputs=[], input_func=None):
        self.program = program[:]
        self.inputs = inputs[::-1]
        self.input_func = input_func
        self.relative_base = 0
        self.memory = {}
        self.output = None
        self.halted = False
        self.pc = 0

    def _get_instruction(self, instruction_code):
        return next(cls for cls in Instruction.__subclasses__() if cls.code == instruction_code)

    def _parse_arguments(self, argument_num):
        modes = str(self.program[self.pc]).zfill(5)[:3][::-1]
        arguments = []
        for i in range(argument_num):
            value = self.program[self.pc+i+1] + (self.relative_base if modes[i] == '2' else 0)
            if modes[i] == '1':
                arguments.append(Argument(value, value))
            else:
                arguments.append(Argument(self.program[value] if value < len(self.program) else self.memory.get(value, 0), value))
        return arguments

    def run(self):
        self.output = None
        while not self.halted and self.output is None:
            instruction = self._get_instruction(self.program[self.pc] % 100)
            arguments = self._parse_arguments(instruction.argument_num)
            self.pc = instruction().execute(self, arguments)
        return self.output

    def execute(self):
        last_output = None
        while not self.halted:
            output = self.run()
            if not self.halted:
                last_output = output
        return last_output

    def get(self, address):
        return self.program[address] if address < len(self.program) else self.memory.get(value + self.relative_base, 0)

    def set(self, address, value):
        target = self.program if address < len(self.program) else self.memory
        target[address] = value

    def input(self, value):
        self.inputs = [value] + self.inputs

    def get_input(self):
        return self.inputs.pop() if self.inputs else self.input_func()