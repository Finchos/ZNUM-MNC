import numpy as np
def smallest_squares (vec_x, vec_f, poly_deg, vec_w=None, poly=None):
    #@TODO kontroly správnosti vstupů
    if vec_w is None:
        vec_w = np.ones(poly_deg)
    if poly is None:
        poly = create_poly(poly_deg)
    left_side_vectors, right_side_vectors = get_scalars(vec_x, vec_f, poly_deg, vec_w)
    coefs = get_coefs(left_side_vectors, right_side_vectors)

def get_coefs(left_side_vectors, right_side_vectors):
    pass #TODO

def get_scalars(vec_x, vec_f,poly_deg, poly):
    left_side_vectors = np.array() #this shit needs to upravit
    right_side_vectors = np.array()
    for i in range(poly_deg):  #@TODO vektory vah
        right_side_vectors = np.append(right_side_vectors, np.vectorize(poly[i])(vec_x) @ vec_f)
        for j in range(poly_deg):
            left_side_vectors =np.append(left_side_vectors, np.vectorize(poly[i])(vec_x) @ np.vectorize(poly[j])(vec_x))
    return left_side_vectors, right_side_vectors

def create_poly(poly_deg):
    poly = [] #@TODO check implementation
    for i in range(poly_deg):
        poly.append(lambda x:x**i)
    return poly