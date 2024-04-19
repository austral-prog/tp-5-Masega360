def roots(a, b, c):
    disc = int((b**2) - (4*a*c))
    root_disc = disc**(1/2)
    if disc > 0:
        root_1 = ((-b) + root_disc)/(2*a)
        root_2 = ((-b) - root_disc)/2*a
        root = f"({root_1}, {root_2})"
    elif disc == 0:
        root_0 = (-b + root_disc)/2*a
        root = f"({root_0})"
    else:
        root = "( )"
    return root


def value_y(a, b, c, x):
    x_square = x**2
    y = (a*x_square) + b*x + c
    return y


def to_string(a, b, c):
    if a == 0 or b==0:
        if a == 0 and b != 0:
            funct = f"f(x) = {b} * X + {c}"
        elif a != 0 and b == 0:
            funct = f"f(x) = {a} * X^2 + {c}"
        elif a == 0 and b == 0:
            funct = f"f(x) = {c}"
    else:
        funct = f"f(x) = {a} * X^2 + {b} * X + {c}"

    return funct


def derivation(a, b, c):
    if a == 0 or b == 0:
        if a == 0:
            deri = f"f'(x) = {b}"
        elif a != 0:
            deri = f"f'(x) = {2*a} * X"
    else:
        deri = f"f'(x) = {2*a} * X + {b}"
    return deri
