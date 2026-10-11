import numpy as np
import plt


def smallest_squares (vec_x, vec_f, poly_deg, vec_w=None, poly=None):
    #@TODO check correct input
    if vec_w is None:
        vec_w = np.ones(len(vec_x))
    if poly is None:
        poly = create_poly(poly_deg)
    left_side_vectors, right_side_vectors = get_scalars(vec_x, vec_f, poly, vec_w)
    return np.linalg.solve(left_side_vectors, right_side_vectors)

def get_scalars(vec_x, vec_f, poly, vec_w):
        n = len(poly)
        phi = [np.vectorize(p)(vec_x).astype(float) for p in poly]
        left = np.empty((n, n))
        right = np.empty(n)
        for i in range(n):
            right[i] = (phi[i] * vec_w) @ vec_f
            for j in range(n):
                left[i, j] = (phi[i] * vec_w) @ phi[j]
        return left, right

def create_poly(poly_deg):
    poly = []
    for i in range(poly_deg+1):
        poly.append(lambda x, i=i :x**i)
    return poly


def plot_results(vec_x, vec_f, coefs, poly=None):
    # Pokud nejsou dodány bázové funkce, vytvoříme je podle počtu koeficientů
    if poly is None:
        poly = create_poly(len(coefs) - 1)

    # Vykreslení původních naměřených dat
    plt.scatter(vec_x, vec_f, color='red', marker='x', label='Naměřená data')

    # Vytvoření jemnější osy x pro plynulou křivku
    x_smooth = np.linspace(min(vec_x), max(vec_x), 200)

    # Vyhodnocení polynomu pro všechny body x_smooth
    y_smooth = np.zeros_like(x_smooth)
    for i, c in enumerate(coefs):
        # Aplikujeme i-tou bázovou funkci na x_smooth a vynásobíme koeficientem
        y_smooth += c * np.vectorize(poly[i])(x_smooth).astype(float)

    # Vykreslení aproximované křivky
    plt.plot(x_smooth, y_smooth, color='blue', label=f'Aproximace (m={len(coefs) - 1})')

    # Nastavení popisků a zobrazení grafu
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Aproximation via smallest square method')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def main():
    x_data = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    f_data = np.array([2.9, 2.8, 2.7, 2.3, 2.1, 2.1, 1.7])

    res = smallest_squares(x_data, f_data, 2)
    print("Found coeffs:", res)

    plot_results(x_data, f_data, res)

if __name__ == '__main__':
    main()

