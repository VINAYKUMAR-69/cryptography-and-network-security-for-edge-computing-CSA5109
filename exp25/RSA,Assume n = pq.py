def mod_inverse(e, phi_n):
    t, new_t = 0, 1
    r, new_r = phi_n, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t += phi_n
    return t

def generate_new_keys(e, n):
    p = 61
    q = 53
    
    n_new = p * q
    phi_n = (p - 1) * (q - 1)
    
    d = mod_inverse(e, phi_n)
    if d is None:
        print("No modular inverse found, key generation failed.")
        return None
    
    return (e, n_new), (d, n_new)

e = 31
n = 3599

public_key, private_key = generate_new_keys(e, n)
if public_key and private_key:
    print(f"New Public Key: e = {public_key[0]}, n = {public_key[1]}")
    print(f"New Private Key: d = {private_key[0]}, n = {private_key[1]}")
