
import matplotlib.pyplot as plt

import numpy as np

def main():
    
    # import numpy as np
    # import matplotlib.pyplot as plt

    # Constants
    epsilon_0 = 8.854187817e-12  # Vacuum permittivity
    E0 = 1.0  # Arbitrary amplitude (scales everything)

    # ky from 0 to 2π
    ky = np.linspace(0, 2 * np.pi, 500)

    # Different ωt values
    omega_t_values = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    labels = [r"$\omega t = 0$", r"$\omega t = \pi/4$", r"$\omega t = \pi/2$", r"$\omega t = 3\pi/4$", r"$\omega t = \pi$"]

    # Compute energy density for each ωt
    fig, ax = plt.subplots()
    for omega_t, label in zip(omega_t_values, labels):
        # u = 2 * epsilon_0 * E0**2 * (np.sin(ky)**2 * np.cos(omega_t)**2 + np.cos(ky)**2 * np.sin(omega_t)**2)
        u = 1/2*E0**2*epsilon_0*(-np.cos(2*ky-2*omega_t)-np.cos(2*ky+2*omega_t)+2)
        ax.plot(ky, u, label=label)

    # Plot styling
    ax.set_title("Energiatiheys seisovassa sähkömagneettisessa aallossa")
    ax.set_xlabel(r"$ky$")
    ax.set_ylabel(r"$u(ky, \omega t)$")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.savefig("plotting.jpg", format="jpg")
    plt.show()


    return

if __name__=="__main__":
    main()
    exit(0)

