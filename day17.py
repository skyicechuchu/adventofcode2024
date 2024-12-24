from enum import Enum
from typing import List, Optional

class RegistryType(Enum):
    A = 4
    B = 5
    C = 6

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()

class Opcode(Enum):
    ADV = 0  # division
    BXL = 1  # bitwise xor
    BST = 2  # modulo 8
    JNZ = 3  # jump
    BXC = 4  # bitwise xor
    OUT = 5  # modulo 8
    BDV = 6  # division
    CDV = 7  # division

class ThreeBitComputer:
    def __init__(self, register_a=0, register_b=0, register_c=0):
        self.registers = {
            RegistryType.A: register_a,
            RegistryType.B: register_b,
            RegistryType.C: register_c
        }
        self.instruction_pointer = 0
        self.output: List[str] = []

    def get_combo_operand_value(self, operand: int) -> int:
        if operand < 4:
            return operand
        return self.registers[RegistryType(operand)]

    def adv(self, operand: int, target_register: Optional[RegistryType] = None) -> None:
        # Division instruction (opcode 0, 6, 7)
        if target_register is None:
            target_register = RegistryType.A
            
        operand_value = self.get_combo_operand_value(operand)
        # Using bitwise right shift instead of division
        self.registers[target_register] = self.registers[RegistryType.A] >> operand_value
        self.instruction_pointer += 2

    def bxl(self, operand: int) -> None:
        # XOR B with literal (opcode 1)
        self.registers[RegistryType.B] ^= operand
        self.instruction_pointer += 2

    def bst(self, operand: int) -> None:
        # Set B to combo operand mod 8 (opcode 2)
        self.registers[RegistryType.B] = self.get_combo_operand_value(operand) % 8
        self.instruction_pointer += 2

    def jnz(self, operand: int) -> None:
        # Jump if A not zero (opcode 3)
        if self.registers[RegistryType.A] != 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self, operand: int) -> None:
        # XOR B with C (opcode 4)
        self.registers[RegistryType.B] ^= self.registers[RegistryType.C]
        self.instruction_pointer += 2

    def out(self, operand: int) -> None:
        # Output combo operand mod 8 (opcode 5)
        value = self.get_combo_operand_value(operand) % 8
        self.output.append(str(value))
        self.instruction_pointer += 2

    def execute_instruction(self, opcode: int, operand: int) -> None:
        opcode_enum = Opcode(opcode)
        match opcode_enum:
            case Opcode.ADV:
                self.adv(operand)
            case Opcode.BXL:
                self.bxl(operand)
            case Opcode.BST:
                self.bst(operand)
            case Opcode.JNZ:
                self.jnz(operand)
            case Opcode.BXC:
                self.bxc(operand)
            case Opcode.OUT:
                self.out(operand)
            case Opcode.BDV:
                self.adv(operand, RegistryType.B)
            case Opcode.CDV:
                self.adv(operand, RegistryType.C)

    def run_program(self, program: List[int]) -> str:
        while self.instruction_pointer < len(program):
            opcode = program[self.instruction_pointer]
            operand = program[self.instruction_pointer + 1]
            self.execute_instruction(opcode, operand)
        return ','.join(self.output)

def find_initial_a(program: List[int]) -> int:
    candidates = [0]
    
    for length in range(1, len(program) + 1):
        out = []
        for num in candidates:
            for offset in range(2**3):
                a = (2**3) * num + offset
                computer = ThreeBitComputer(register_a=a)
                output = list(map(int, computer.run_program(program).split(',')))
                
                if output == program[-length:]:
                    out.append(a)

        candidates = out

    return min(candidates)

def run_tests():
    computer = ThreeBitComputer(register_a=729)
    program = [0, 1, 5, 4, 3, 0]
    print(f"Test 1 Output: {computer.run_program(program)}")

    computer = ThreeBitComputer(register_a=64751475)
    program = [2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0]
    print(f"Test 2 Output: {computer.run_program(program)}")

    example_program = [0, 3, 5, 4, 3, 0]
    example_result = find_initial_a(example_program)
    print(f"Example test - Found value: {example_result} (expected: 117440)")
    assert example_result == 117440, "Example validation failed"

    program = [2, 4, 1, 2, 7, 5, 4, 5, 1, 3, 5, 5, 0, 3, 3, 0]
    result = find_initial_a(program)
    print(f"Puzzle solution - Found value: {result}")  #37221270076916

if __name__ == "__main__":
    run_tests()