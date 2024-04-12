import numpy as np
def crystal_rise(d_k, delta_t):
#parameters
    tau = 95*60
    alpha = 0.5
    rho_k = 1850
    x_xnas = 0.008
    w_l = 0.2*1450
    mu_l = 0.00833
    M_r = 0.018
    M_k = 0.050
    delta = 0.8E-04
    k_xs = 1
    j = 0
    #calculations
    for j in range (0,round(tau/delta_t)):
        
        k_xD = alpha * (w_l*d_k/mu_l)**0.6 * (mu_l/(M_r*delta))**0.3 * delta / d_k
        k_xm = 1/(1/k_xD+1/k_xs)
        G = 2 * k_xm * M_k * x_xnas / rho_k
        delta_dk = delta_t * G 
        d_k = d_k + delta_dk
        j +=1
    final_d = d_k * 1000
    print(final_d)
    return final_d

np.sizes = [0.356e-03,0.503e-03,0.711e-03,1.0005e-03,1.4095e-03,2.0065e-03]
for i in range (0,6):
    crystal_rise(np.sizes[i], 0.01)
