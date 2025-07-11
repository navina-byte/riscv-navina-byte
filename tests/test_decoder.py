import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../model")))

from decoder_model import decode_instruction

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_instruction_decoder(dut):
    instruction = 0b000000000001_00000_000_00001_0010011  # addi x1, x0, 1
    dut.instruction.value = instruction

    await Timer(1, units="ns")

    expected_opcode, expected_funct3, expected_funct7 = decode_instruction(instruction)

    assert dut.opcode.value == expected_opcode, f"Opcode mismatch!"
    assert dut.funct3.value == expected_funct3, f"Funct3 mismatch!"
    assert dut.funct7.value == expected_funct7, f"Funct7 mismatch!"

