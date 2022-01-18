import numpy as np

def N_0_3(t: float):
    if t < 0 or t > 4:
        return 0
    if t < 1:
        return (t**3)/6.0
    if t < 2:
        return (-3*(t-1)**3+3*(t-1)**2+3*(t-1)+1)/6.0
    if t < 3:
        return (3*(t-2)**3-6*(t-2)**2+4)/6.0
    if t < 4:
        return (-(t-3)**3+3*(t-3)**2-3*(t-3) + 1)/6.0
    return 0


def N_3_i(i, t):
    return N_0_3(t-i)


def b_spline_3(t, puntos: np.array):
    m = np.zeros(2) 
    for i in range(5):
        m = m + puntos[i]*N_3_i(i, t)
    return m

def calcular_spline (t,puntos):
    curva_s = np.array(list(map (lambda t_i:b_spline_3(t_i, puntos) , t)))
    return curva_s.T

