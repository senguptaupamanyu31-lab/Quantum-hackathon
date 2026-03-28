# test_isa.py

from isa.instruction_set import parse_instruction, validate_instruction

program = [
    "ADD x1 x2 x3",
    "XOR x0 x1 x2",
    "AND x3 x1 x2",
    "MEASURE x1"
]

instructions = []

for line in program:
    inst = parse_instruction(line)
    validate_instruction(inst)
    instructions.append(inst)

for inst in instructions:
    print(inst)
    