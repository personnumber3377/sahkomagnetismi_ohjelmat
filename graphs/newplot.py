
import matplotlib.pyplot as plt

import numpy as np

def main():
    
    # import numpy as np
    # import matplotlib.pyplot as plt

    # Constants
    epsilon_0 = 8.854e-12
    E0 = 1.0  # arbitrary scale
    c = 300_000_000
    # ky array
    ky = np.linspace(0, 2 * np.pi, 500)

    # Time values
    omega_t_values = [np.pi/4, np.pi/2, 3*np.pi/4]
    labels = [r"$\omega t = \pi/4$", r"$\omega t = \pi/2$", r"$\omega t = 3\pi/4$"]

    # Plot
    plt.figure()
    for omega_t, label in zip(omega_t_values, labels):
        # S_y = -2 * epsilon_0 * E0**2 * np.sin(2 * ky) * np.sin(2 * omega_t)
        S_y = 1/(2*c)*E0**2*(-np.cos(2*ky - 2*omega_t)+np.cos(2*ky+2*omega_t))
        # S_y = -2 * epsilon_0 * E0**2 * np.sin(2 * ky) * np.sin(2 * omega_t)
        plt.plot(ky, S_y, label=label)

    plt.title("Poyntingin vektorin $y$-komponentti seisovassa aallossa")
    plt.xlabel(r"$ky$")
    plt.ylabel(r"$S_y(ky, \omega t)$")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
   # plt.show()
    #plt.tight_layout()
    plt.savefig("plotting2.jpg", format="jpg")
    plt.show()

    return

if __name__=="__main__":
    main()
    exit(0)

