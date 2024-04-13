# To run as a script, use mpirun -np 4 python <fname> --target nvidia-mgpu
import cudaq

qubit_count = 33

cudaq.set_target("nvidia-mgpu") # activates the single-gpu backend

@cudaq.kernel
def kernel(qubit_count: int):
    # Allocate our qubits.
    qvector = cudaq.qvector(qubit_count)
    # Place the first qubit in the superposition state.
    h(qvector[0])
    # Loop through the allocated qubits and apply controlled-X,
    # or CNOT, operations between them.
    for qubit in range(qubit_count - 1):
        x.ctrl(qvector[qubit], qvector[qubit + 1])
    # Measure the qubits.
    mz(qvector)

#print("Preparing GHZ state for", qubit_count, "qubits.")
counts = cudaq.sample(kernel, qubit_count)
counts.dump()
