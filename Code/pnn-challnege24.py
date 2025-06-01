import pyNN.brainscales2 as sim  # Use BrainScaleS-2 as backend
import numpy as np
import matplotlib.pyplot as plt

# Setup simulator
sim.setup()

# Create a single LIF neuron
lif_neuron = sim.Population(1, sim.IF_cond_exp(), label="LIF Neuron")

# Create a spike source to stimulate the neuron
spike_source = sim.Population(1, sim.SpikeSourceArray(spike_times=[1.0, 2.0, 3.0]), label="Spike Source")

# Connect the spike source to the neuron
synapse = sim.StaticSynapse(weight=0.5)
connector = sim.OneToOneConnector()
projection = sim.Projection(spike_source, lif_neuron, connector, synapse, receptor_type='excitatory')

# Record spikes from neuron
lif_neuron.record(['spikes', 'v'])  # Record spike times and membrane potential

# Run simulation for 10 ms
sim.run(10.0)

# Retrieve and print data
data = lif_neuron.get_data()
spikes = data.segments[0].spiketrains[0]
vm = data.segments[0].filter(name="v")[0]

print("Spike times:", spikes)

# Plot voltage trace
plt.figure(figsize=(8, 4))
plt.plot(vm.times, vm, label="Membrane Potential (v)")
plt.title("LIF Neuron Response on BrainScaleS-2")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
plt.grid(True)
plt.legend()
plt.show()

# Clean up
sim.end()
