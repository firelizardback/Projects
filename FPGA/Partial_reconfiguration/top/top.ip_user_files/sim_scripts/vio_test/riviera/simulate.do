onbreak {quit -force}
onerror {quit -force}

asim -t 1ps +access +r +m+vio_test -L xil_defaultlib -L secureip -O5 xil_defaultlib.vio_test

do {wave.do}

view wave
view structure

do {vio_test.udo}

run -all

endsim

quit -force
