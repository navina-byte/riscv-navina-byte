def decode_instruction(instruction):
    opcode = instruction & 0x7F
    funct3 = (instruction >> 12) & 0x7
    funct7 = (instruction >> 25) & 0x7F
    return opcode, funct3, funct7
