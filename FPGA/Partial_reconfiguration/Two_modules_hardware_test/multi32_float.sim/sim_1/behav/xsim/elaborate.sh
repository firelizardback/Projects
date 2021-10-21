#!/bin/bash -f
# ****************************************************************************
# Vivado (TM) v2019.1 (64-bit)
#
# Filename    : elaborate.sh
# Simulator   : Xilinx Vivado Simulator
# Description : Script for elaborating the compiled design
#
# Generated by Vivado on Sat Dec 14 13:21:24 CET 2019
# SW Build 2552052 on Fri May 24 14:47:09 MDT 2019
#
# Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
#
# usage: elaborate.sh
#
# ****************************************************************************
set -Eeuo pipefail
echo "xelab -wto 7790f7d269fe49f7b97fb8fed5ca5a03 --incr --debug typical --relax --mt 8 -L xil_defaultlib -L secureip --snapshot multiplier_tb_behav xil_defaultlib.multiplier_tb -log elaborate.log"
xelab -wto 7790f7d269fe49f7b97fb8fed5ca5a03 --incr --debug typical --relax --mt 8 -L xil_defaultlib -L secureip --snapshot multiplier_tb_behav xil_defaultlib.multiplier_tb -log elaborate.log
