import numpy as np
def smallest_squares (vec_x, vec_f, poly_deg, vec_w=None, poly=None):
    #@TODO kontroly správnosti vstupů
    if vec_w is None:
        vec_w = np.ones(len(vec_x))
    if poly is None:
        poly = create_poly(poly_deg)
    left_side_vectors, right_side_vectors = get_scalars(vec_x, vec_f, poly, vec_w)
    coefs = get_coefs(left_side_vectors, right_side_vectors)
    return coefs

def get_coefs(left_side_vectors, right_side_vectors):
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

####TOTO ASI NIC UDELAL JSEM TO JINAK S CLAUDEM
# def get_scalars(vec_x, vec_f,poly_deg, poly):
#     left_side_vectors = np.array([]) #this shit needs to upravit
#     right_side_vectors = np.array([])
#         for i in range(poly_deg+1):  #@TODO vektory vah
#             right_side_vectors = np.append(right_side_vectors, np.vectorize(poly[i])(vec_x) @ vec_f)
#             for j in range(poly_deg+1):
#                 left_side_vectors =np.append(left_side_vectors, np.vectorize(poly[i])(vec_x) @ np.vectorize(poly[j])(vec_x))
#     return left_side_vectors, right_side_vectors

def create_poly(poly_deg):
    poly = [] #@TODO check implementation
    for i in range(poly_deg+1):
        poly.append(lambda x, i=i :x**i)
    return poly

def main():
    res = smallest_squares(np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]), np.array([2.9,2.8,2.7,2.3,2.1,2.1, 1.7]),2)
    print(res)

if __name__ == '__main__':
    main()