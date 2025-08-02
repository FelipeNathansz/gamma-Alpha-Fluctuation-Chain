import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros físicos da cadeia de Kitaev
N = 20
mu = 0.5
t = 1.0
delta = 0.8

# Construção da Hamiltoniana
H = np.zeros((2 * N, 2 * N), dtype=float)
for i in range(N - 1):
    H[2*i, 2*(i+1)] = -t
    H[2*i+1, 2*(i+1)+1] = -t
    H[2*i, 2*(i+1)+1] = delta
    H[2*i+1, 2*(i+1)+1] = delta
for i in range(N):
    H[2*i, 2*i+1] = mu
    H[2*i+1, 2*i] = mu


eigenvalues = np.linalg.eigvalsh(H)
abs_E = np.abs(eigenvalues)


gamma = 1.2
alpha = 0.7
beta = 0.8
Omega_vals = np.linspace(0.1, 2.0, 60)

X, Y = np.meshgrid(eigenvalues, Omega_vals)
Z = np.exp(-Y * ((gamma + alpha) / beta) * np.abs(X))


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')


ax.set_title("ψ(Ω·(γ+α)/β · |ψ_E|) — Cadeia de flutuação Gamma, Alpha em exponencial Beta  (Onda em 3D)")
ax.set_xlabel("Autovalores |ψ_E|")
ax.set_ylabel("Ω")
ax.set_zlabel("ψ modulado")
ax.set_zlim(0, 1.05)
ax.view_init(elev=30, azim=225)

plt.tight_layout()
plt.show()
