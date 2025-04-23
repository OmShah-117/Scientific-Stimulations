from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
import numpy as np


# SIMPLE FLIP
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to put the qubit in superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# Print the results
print(counts)
plot_histogram(counts,color='red')
plt.show()


#2 QUBITS
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.h(1)
qc.measure([0, 1], [0, 1])  # Measure both qubits

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print(counts)
plot_histogram(counts,color='red')
plt.show()



#bIASED FLIP
qc = QuantumCircuit(1, 1)
qc.ry(np.pi / 4, 0)  # Rotate qubit by pi/4 (creates bias)
qc.measure(0, 0)

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print(counts)
plot_histogram(counts,color='red')
plt.show()

