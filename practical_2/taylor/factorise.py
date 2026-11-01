#task 3: workaroud for g > 1 
#solution 1: implemented by hand 
#1/ab = 1/a x 1/b, where a is a multiple of 2, in other words a = 2 ^ m, where we have used the property where a multiple of 2 can always be exactly computed

def factorise(x:float) -> float:
    m = 0
    n = x 

    while n >= 2:
        n = n * 0.5
        m += 1
    
    return m,n


#hence we may redefine geometric_series by using the helper function factorise:


def geometric_series(g: float, tol: float = 1e-12, max_iter: int = 1000) -> float:

    c, g = factorise(g)
    g = g - 1
    multiple = 0.5 ** c
    
    total = 0.0 #running total 
    term = 1.0 #value of the current term

    for i in range(max_iter):
        total += term 

        #condition for convergence 
        if abs(term) <= tol * abs(total):
            return multiple*total, abs(term) / abs(total), i
        
        term *= -g 
    
    raise RuntimeError("max iteration exceeded")


print(geometric_series(3))