# Scientific-Stimulations
Imagination is more important than knowledge.

Quantum tunneling is a fascinating phenomenon in quantum mechanics where a particle can pass through a potential energy barrier, even if it doesn't have enough energy to classically overcome it. This is a direct violation of classical physics principles.

How does it work?
In the quantum world, particles exhibit wave-like properties. This wave-like nature allows them to exist in a superposition of states, meaning they can be in multiple states simultaneously. When a particle encounters a barrier, its wave function can extend into the barrier region. While the probability of finding the particle inside the barrier is low, there's a non-zero chance that it might tunnel through and appear on the other side.   

In this code it solves the time-dependent Schrödinger equation for a particle encountering a potential barrier.
1] Setting Up the System:
Defines constants like mass (m), reduced Planck constant (hbar), and spatial parameters.
Creates a grid of positions (x) and calculates the spacing between points (dx).
Defines the momentum (p) and potential barrier height (V0).
Defines the initial wave function (Psi0) as a Gaussian wave packet with a specific momentum.
2] Constructing the Hamiltonian:
Builds the Hamiltonian matrix (H) using finite difference approximations for the kinetic and potential energy terms.
3] Solving the Time-Dependent Schrödinger Equation:
Used np.linalg.eigh to solve the eigenvalue problem (Hpsi = Epsi) and obtain the energy eigenstates (psi) and eigenvalues (E).
Projects the initial wave function (Psi0) onto the energy eigenstates to get the expansion coefficients (c).
4] Time Evolution (Not Directly Tunneling):
Uses a loop to iterate over time steps (t).
Within the loop, calculates the wave function (Psi) at each time step by summing over the energy eigenstates with their corresponding coefficients and phase factors.
