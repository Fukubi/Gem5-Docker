import argparse

import m5
from m5.objects import *

m5.util.addToPath("../..")

parser = argparse.ArgumentParser(epilog=__doc__)

parser.add_argument(
    "commands_to_run",
    metavar="command(s)",
    nargs="*",
    help="Command(s) to run",
)

args = parser.parse_args()

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = "1GHz"
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = "timing"
system.mem_ranges = [AddrRange("512MB")]

system.cpu = ArmTimingSimpleCPU()

system.membus = SystemXBar()

system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

system.cpu.createInterruptController()
# system.cpu.interrupts[0].pio = system.membus.mem_side_ports
# system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
# system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

binary = args.commands_to_run[0]
print(f"Beginning to run {binary}")
system.workload = SEWorkload.init_compatible(binary)
system.workload.wait_for_remote_gdb = True

process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system=False, system=system)
m5.instantiate()

print("Beginning Simulation!")
exit_event = m5.simulate()

print(
    "Exiting @ tick {} because {}".format(m5.curTick(), exit_event.getCause())
)
