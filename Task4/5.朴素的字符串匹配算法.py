def matcher(t, p):
    '''
    :param t: the string to check
    :param p: pattern
    '''
    n = len(t)
    m = len(p)
    for s in range(0, n - m + 1):
        if p == t[s:s + m]:
            print('Pattern occurs with shift %d' % s)


matcher("cccaaabbbb", "aaa")