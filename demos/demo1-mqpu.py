# Parallelize over the various kernels one would like to execute.

import cudaq

qubit_count = 2

# Set the simulation target.
cudaq.set_target("nvidia-mqpu")

# Kernel 1


@cudaq.kernel
def kernel_1(qubit_count: int):
    qvector = cudaq.qvector(qubit_count)

    # 2-qubit GHZ state.
    h(qvector[0])
    for i in range(1, qubit_count):
        x.ctrl(qvector[0], qvector[i])

    # If we dont specify measurements, all qubits are measured in
    # the Z-basis by default.
    mz(qvector)


# Kernel 2


@cudaq.kernel
def kernel_2(qubit_count: int):
    qvector = cudaq.qvector(qubit_count)

    # 2-qubit GHZ state.
    h(qvector[0])
    for i in range(1, qubit_count):
        x.ctrl(qvector[0], qvector[i])

    # If we dont specify measurements, all qubits are measured in
    # the Z-basis by default.
    mz(qvector)


# Asynchronous execution on multiple qpus via nvidia gpus.
result_1 = cudaq.sample_async(kernel_1, qubit_count, shots_count=1000, qpu_id=0)
result_2 = cudaq.sample_async(kernel_2, qubit_count, shots_count=1000, qpu_id=1)

print(result_1.get())
print(result_2.get())
