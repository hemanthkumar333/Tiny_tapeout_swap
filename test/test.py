# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_nibble_swap(dut):
 """ Test the nibble swapping logic of tt_um_example """
     
    dut._log.info("Starting nibble swap test")

    # Set the clock period to 1 us (1 MHz)
    clock = Clock(dut.clk, 1, units="us")
    cocotb.start_soon(clock.start())

    # Apply Reset
    dut._log.info("Applying reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Wait a few cycles under reset 
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1 # Deassert reset

    # testing various input patterns
    test_vectors = [0x00, 0xFF, 0xA5, 0x12, 0xF0, 0x0F]

    for val in test_vectors:
        dut.ui_in.value = val
        await ClockCycles(dut.clk, 1) # wait 1 clk cycle to settle

        # Expected output is nibble swapped
        expected = ((val & 0x0F) << 4) | ((val & 0xF0) >> 4)
        observed = dut.uo_out.value.integer

        dut._log.info(f"Input={hex(val)}, Output={hex(observed)}, Expected={hex(expected)}")
        assert observed == expected, f"FAIL: Input={hex(val)} => Expected={hex(expected)}, Got={hex(observed)}"
        
    dut._log.info("Nibble swap test passed!")
