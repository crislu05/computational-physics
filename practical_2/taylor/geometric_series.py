#solution 1: implemented by hand 
def taylor(g:float) -> float:
    
    tol = 1e-6  #termination tolerance 
    err = float('inf')
    f_old = 1

    while err >= tol:
        f_new = 1 - g * f_old
        err = abs(f_new - f_old) / abs(f_old)
        f_old = f_new
    return f_new


#solution 2: the formal implementation, provided by claude 
def geometric_series(g: float, tol: float = 1e-12, max_iter: int = 1000) -> float:
    #exceeding radius of convergence 
    if abs(g) >= 1.0:
        raise ValueError(f"series diverge") #makes failure visible 
    
    total = 0.0 #running total 
    term = 1.0 #value of the current term

    for i in range(max_iter):
        total += term 

        #condition for convergence 
        if abs(term) <= tol * abs(total):
            return total, abs(term) / abs(total), i
        
        term *= -g 
    
    raise RuntimeError("max iteration exceeded")