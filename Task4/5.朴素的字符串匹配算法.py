def matcher(t, p):
    '''
    :param t: the string to check
    :param p: pattern
    '''
    n = len(t)
    m = len(p)
    i, j = 0, 0
    while i < n and j < m:
        if t[i] == p[j]:
            i += 1
            j += 1

        else:
            i = i - j + 1
            j = 0

    if j == m:
        return i - j
    else:
        return -1
