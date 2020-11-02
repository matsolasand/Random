import numpy as np
import matplotlib.pyplot as plt
from astropy import units as uni
from astropy import constants as con

# -----------------------
# constants
# -----------------------
# c   = 2.99792458e8                  # m s^-1
# h   = 6.62607004e-34                # m^2 kg s^-1
# k_B = 1.38064852e-23                # m^2 ks s^-2 K^-1
# -----------------------

def B_nu(nu, T):
    factor1 = 2 * con.h * nu**3 / con.c**2
    factor2 = 1 / (np.exp(con.h * nu / (con.k_B * T)) - 1)

    return factor1 * factor2

def B_lam(lam, T):
    factor1 = 2 * con.h * con.c**2 / lam**5
    factor2 = 1 / (np.exp(con.h * con.c / (lam * con.k_B * T)) - 1)

    return factor1 * factor2

def plotting(Planck, unit):
    plt.semilogx(unit, Planck)
    if np.all(unit == nu):
        plt.plot(np.ones(50)*40e9, np.linspace(0, 2e-7, 50), label="bajs")
        plt.legend()
    plt.show()

if __name__ == "__main__":
    nu  = np.linspace(1e10, 1.5e12, 1e5)*uni.Hz
    lam = np.linspace(2e-4, 2e-2, 1e5)*uni.m

    plotting((B_nu(nu, 2.725*uni.K)*nu).decompose().to("W/m^2"), nu)
    plotting((B_lam(lam, 2.725*uni.K)*lam).decompose().to("W/m^2"), lam)