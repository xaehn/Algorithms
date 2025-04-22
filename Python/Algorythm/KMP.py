def kmp_table(pattern):
    length = len(pattern)
    table = length * [0]

    prefix = 0
    for suffix in range(1, length):
        while 0 < prefix and pattern[prefix] != pattern[suffix]:
            prefix = table[prefix - 1]

        if pattern[prefix] == pattern[suffix] :
            prefix += 1
            table[suffix] = prefix

    return table

def kmp(string, pattern, length = None, plength = None):
    table = kmp_table(pattern)
    if length == None:
        length = len(string)

    if plength == None:
        plength = len(pattern)

    plength = len(pattern)
    results = []
    pidx = 0
    for idx in range(length):
        while 0 < pidx and string[idx] != pattern[pidx]:
            pidx = table[pidx - 1]

        if string[idx] == pattern[pidx]:
            if pidx == plength - 1:
                results.append(idx - plength + 1)
                pidx = table[pidx]
            else:
                pidx += 1

    return results