import numpy as np
import plt


def smallest_squares (vec_x, vec_f, poly_deg, vec_w=None, poly=None):
    if vec_w is None:
        vec_w = np.ones(len(vec_x))
    if poly is None:
        poly = create_poly(poly_deg)
    left_side_vectors, right_side_vectors = get_scalars(vec_x, vec_f, poly, vec_w)
    print_lin_eq(left_side_vectors, right_side_vectors)
    return np.linalg.solve(left_side_vectors, right_side_vectors)

def get_scalars(vec_x, vec_f, poly, vec_w):
        n = len(poly)
        phi = [np.vectorize(p)(vec_x).astype(float) for p in poly]
        print(phi)
        left = np.empty((n, n))
        right = np.empty(n)
        for i in range(n):
            right[i] = (phi[i] * vec_w) @ vec_f
            for j in range(i, n):
                left[i, j] = (phi[i] * vec_w) @ phi[j]
                if i!=j:
                    left[j, i] = left[i, j]
        return left, right

def create_poly(poly_deg):
    return [lambda x, i=i: x**i for i in range(poly_deg + 1)]

def print_lin_eq(A, x, decimals=4):
    cells = [[f"{A[i][j]:.{decimals}f}" for j in range(len(A[0]))] for i in range(len(A))]
    rhs = [f"{x[i]:.{decimals}f}" for i in range(len(x))]
    width = max(len(s) for s in [c for row in cells for c in row] + rhs)
    for i in range(len(A)):
        row = "  ".join(c.rjust(width) for c in cells[i])
        print(f"{row}  |  {rhs[i].rjust(width)}")

def plot_results(vec_x, vec_f, coefs, poly=None):

    if poly is None:
        poly = create_poly(len(coefs) - 1)

    # Vykreslení dat
    plt.scatter(vec_x, vec_f, color='red', marker='x', label='Naměřená data')

    # Vytvoření jemnější osy x pro plynulou křivku
    x_smooth = np.linspace(min(vec_x), max(vec_x), 200)

    # Vyhodnocení polynomu
    y_smooth = np.zeros_like(x_smooth)
    for i, c in enumerate(coefs):
        y_smooth += c * np.vectorize(poly[i])(x_smooth).astype(float)

    # Vykreslení
    plt.plot(x_smooth, y_smooth, color='blue', label=f'Aproximace (m={len(coefs) - 1})')

    # Nastavení
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Approximation via smallest square method')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def calculate_and_visualize(x_data, y_data, poly_deg, weights=None, poly=None):
    res = smallest_squares(x_data, y_data, poly_deg, vec_w=weights, poly=poly)
    print("Found coeffs:", res)
    plot_results(x_data, y_data, res)

def main():
    # 1.a
    x_data = np.array([-2, -1, 0, 1, 2, 3])
    f_data = np.array([-15, -8, -7, -6, 1, 20])
    # 1.b
    weights = np.array([0.125, 0.5, 1, 1, 0.5, 0.125])

    # 2
    #x_data = np.array([-3,-2,-1,0,1,2,3])
    #f_data = np.array([4,2,3,0,-1,-2,-5])

    # 3
    #x_data = np.array([-1, -0.5, 0, 0.5, 1])
    #f_data = np.array([3, 1, 2, 7, 8])
    #poly = [lambda x:1, lambda x:x, lambda x: (2*pow(x, 2))-1]


    calculate_and_visualize(x_data, f_data, 2)


#TODO printnovat hodnoty, optimalizovat, vizualizovat vsechny priklady

if __name__ == '__main__':
    main()

