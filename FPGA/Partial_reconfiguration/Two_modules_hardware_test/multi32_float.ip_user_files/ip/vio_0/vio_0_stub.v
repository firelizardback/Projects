// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2019.1 (lin64) Build 2552052 Fri May 24 14:47:09 MDT 2019
// Date        : Sun Dec 15 18:32:37 2019
// Host        : hamed-PC running 64-bit Ubuntu 18.04.3 LTS
// Command     : write_verilog -force -mode synth_stub
//               /home/hamed/FPGA/Partial_reconfiguration/multi32_float/multi32_float.srcs/sources_1/ip/vio_0/vio_0_stub.v
// Design      : vio_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7z020clg400-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* X_CORE_INFO = "vio,Vivado 2019.1" *)
module vio_0(clk, probe_in0, probe_in1, probe_in2, probe_in3, 
  probe_out0, probe_out1, probe_out2)
/* synthesis syn_black_box black_box_pad_pin="clk,probe_in0[127:0],probe_in1[127:0],probe_in2[0:0],probe_in3[0:0],probe_out0[127:0],probe_out1[127:0],probe_out2[0:0]" */;
  input clk;
  input [127:0]probe_in0;
  input [127:0]probe_in1;
  input [0:0]probe_in2;
  input [0:0]probe_in3;
  output [127:0]probe_out0;
  output [127:0]probe_out1;
  output [0:0]probe_out2;
endmodule
