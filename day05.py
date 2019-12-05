import sys

class Instruction:
    code, argument_num = 0, 0
    def execute(self, program, pc, arguments):
        pass

class PlusInstruction(Instruction):
    code, argument_num = 1, 3
    def execute(self, program, pc, arguments):
        program[arguments[3][0]] = arguments[1][1] + arguments[2][1]
        return (pc+4, None)

class MultiplyInstruction(Instruction):
    code, argument_num = 2, 3
    def execute(self, program, pc, arguments):
        program[arguments[3][0]] = arguments[1][1] * arguments[2][1]
        return (pc+4, None)

class InputInstruction(Instruction):
    code, argument_num = 3, 1
    def execute(self, program, pc, arguments):
        program[arguments[1][0]] = arguments[0]
        return (pc+2, None)

class OutputInstruction(Instruction):
    code, argument_num = 4, 1
    def execute(self, program, pc, arguments):
        return (pc+2, program[arguments[1][0]])

class JumpIfTrueInstruction(Instruction):
    code, argument_num = 5, 2
    def execute(self, program, pc, arguments):
        return (arguments[2][1] if arguments[1][1] != 0 else pc+3, None)

class JumpIfFalseInstruction(Instruction):
    code, argument_num = 6, 2
    def execute(self, program, pc, arguments):
        return (arguments[2][1] if arguments[1][1] == 0 else pc+3, None)

class LessThanInstruction(Instruction):
    code, argument_num = 7, 3
    def execute(self, program, pc, arguments):
        program[arguments[3][0]] = int(arguments[1][1] < arguments[2][1])
        return (pc+4, None)

class EqualsInstruction(Instruction):
    code, argument_num = 8, 3
    def execute(self, program, pc, arguments):
        program[arguments[3][0]] = int(arguments[1][1] == arguments[2][1])
        return (pc+4, None)

class HaltInstruction(Instruction):
    code, argument_num = 99, 0
    def execute(self, program, pc, arguments):
        return (-1, None)

def get_instruction(instruction_code):
    return next(cls for cls in Instruction.__subclasses__() if cls.code == instruction_code)

def parse_arguments(program, pc, argument_num):
    modes = str(program[pc]).zfill(5)[:3][::-1]
    return [(program[pc+i+1], program[program[pc+i+1]] if modes[i] == '0' else program[pc+i+1]) for i in range(argument_num)]

def execute(program, input_value):
    program = program[:]
    pc = output = 0
    while pc != -1:
        instruction = get_instruction(program[pc] % 100)
        arguments = [input_value] + parse_arguments(program, pc, instruction.argument_num)
        pc, toutput = instruction().execute(program, pc, arguments)
        if toutput:
            output = toutput
    return output

assert len(sys.argv) == 2
program = list(map(int, open(sys.argv[1]).read().split(',')))

part1 = execute(program, 1)
part2 = execute(program, 5)

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))