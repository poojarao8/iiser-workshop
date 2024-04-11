Books
  1. Preskill's book: https://www.lorentz.leidenuniv.nl/quantumcomputers/literature/preskill_1_to_6.pdf
  2. Preskill lecture notes: http://theory.caltech.edu/~preskill/ph229/
  3. Nielsen and Chung's book.

Suggested Topics

1. Quantum algorithms - including QFT, Grover's , Shor's
   https://nvidia.github.io/cuda-quantum/latest/examples/python/tutorials/noisy_simulations.html#
   Preskill's book, page - 231

2. Density Matrices
   Preskill's book: https://www.lorentz.leidenuniv.nl/quantumcomputers/literature/preskill_1_to_6.pdf
   Preskill's book, page - 49

3. Noise Modeling
   Preskill's book, sec 3.4 on the three quantum channels (page 104) 
   Additional reference: https://aws.amazon.com/blogs/quantum-computing/noise-in-quantum-computing/
   
   CUDA-Q examples for noisy simulation
   https://nvidia.github.io/cuda-quantum/latest/examples/python/tutorials/noisy_simulations.html#

Suggested exercises

1. Implement Grover's algorithm in CUDA-Q and check against the existing example.
2. Add a single qubit depolarizing channel in your code.
3. Write a kernel that takes in the other kernel as an argument.
4. Compare the cpu vs gpu performance for the GHZ example by running on the CDAC cluster.
5. Switch out the optimizer from COBYLA to another one. Play around with number of iterations and initial point.
6. Switch out the optimizer with the scipy optimizer.
7. Try out the tensortnet backend for any example of your choice. Think about the pros and cons of this approach for your example.