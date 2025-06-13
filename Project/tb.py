import cocotb
from cocotb.triggers import RisingEdge, Timer
import random
import csv

@cocotb.test()
async def scan_chain_test(dut):
    CHAIN_LEN = int(dut.CHAIN_LEN)
    FAULT_POS = 3
    FAULT_TYPE = 0

    # Initialize signals
    dut.reset.value = 1
    dut.test_mode.value = 0
    dut.scan_in.value = 0
    await Timer(20, units="ns")
    dut.reset.value = 0
    dut.test_mode.value = 1

    # Open CSV file
    with open("scan_results.csv", mode="w", newline='') as csvfile:
        fieldnames = ["scan_len", "pattern_bit", "fault_pos", "fault_type", "scan_out"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Send scan patterns
        for i in range(16):
            bit = i & 0x1
            dut.scan_in.value = bit
            await RisingEdge(dut.clk)
            await Timer(1, units="ns")  # Wait for value to settle
            writer.writerow({
                "scan_len": CHAIN_LEN,
                "pattern_bit": bit,
                "fault_pos": FAULT_POS,
                "fault_type": FAULT_TYPE,
                "scan_out": int(dut.scan_out.value)
            })

    cocotb.log.info("Scan chain test completed and output written to scan_results.csv")
