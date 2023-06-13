def find_smallest_multiple(p, d):
    if p % 2 != 0:
        return None

    for i in range(1, p+1):
        multiple = d * i
        remainder = multiple % p
        if remainder <= p/2:
            return multiple
    return None
