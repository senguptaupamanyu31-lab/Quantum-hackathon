# qrisc2/isa/instruction_set.py

class Instruction:
    def __init__(self, opcode, rd=None, rs1=None, rs2=None):
        self.opcode = opcode.upper()
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2

    def __repr__(self):
        args = [self.rd, self.rs1, self.rs2]
        args = [str(arg) for arg in args if arg is not None]
        return f"{self.opcode} {' '.join(args)}"

SUPPORTED_INSTRUCTIONS = {
    "ADD": {"type": "R", "qubits": "multi"},
    "XOR": {"type": "R", "qubits": "2"},
    "AND": {"type": "R", "qubits": "3"},
    "MEASURE": {"type": "I", "qubits": "1"}
}

def validate_instruction(inst):
    if inst.opcode not in SUPPORTED_INSTRUCTIONS:
        raise ValueError(f"Unsupported instruction: {inst.opcode}")

    if inst.opcode == "MEASURE":
        if inst.rd is None:
            raise ValueError("MEASURE requires a target register")
    else:
        if None in (inst.rd, inst.rs1, inst.rs2):
            raise ValueError(f"{inst.opcode} requires 3 operands")

REGISTERS = ["x0", "x1", "x2", "x3"]
QUBITS_PER_REGISTER = 2
ANCILLA_QUBITS = 2

def parse_instruction(line):
    parts = line.strip().split()

    opcode = parts[0]

    if opcode == "MEASURE":
        return Instruction(opcode, rd=parts[1])

    return Instruction(opcode, parts[1], parts[2], parts[3])