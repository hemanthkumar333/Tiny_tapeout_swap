/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_swap_nibble (
    input wire [7:0] ui_in, // Dedicated inputs (8 bits)
    output wire [7:0] uo_out, // Dedicated outputs (8 bits)
    // Additional lines required by the TinyTapeout interface.
    input wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    // Provided power/clock/reset signals, but not used in this logic.
    input wire ena,
    input wire clk,
    input wire rst_n
 );
    // The design simply swaps the high nibble [7:4] with the low nibble [3:0].
    assign uo_out = {ui_in[3:0], ui_in[7:4]};
    // Unused I/O signals are tied to 0 or set as inputs only.
    assign uio_out = 8’b0000_0000;
    assign uio_oe = 8’b0000_0000;
    // Tie off unused signals to prevent warnings.
    wire _unused = &{ena, clk, rst_n, uio_in, 1’b0};
 endmodule

`default_nettype none
