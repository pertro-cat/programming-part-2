NO_OF_CHARS = 256

def nextState(haystack, m, state, x):
    if state < m and x == ord(needle[state]):
        return state + 1
    i = 0
    for ns in range(state, 0, -1):
        if needle[ns - 1] == x:
            while i < ns - 1:
                if needle[i] != needle[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0

def automaton_matcher(needle, n):
    global NO_OF_CHARS
    m = len(needle)
    n = len(haystack)
    TF = [[0 for i in range(NO_OF_CHARS)] for j in range(m + 1)]
    for state in range(m + 1):
        for x in range (NO_OF_CHARS):
            z = nextState(needle, m, state, x)
            TF[state][x] = z
    return TF

def search_inText(needle, haystack, m, n):
    global NO_OF_CHARS
    TF = automaton_matcher(needle, haystack)
    state = 0
    found_indexes = []
    for i in range(n):
        state = TF[state][ord(haystack[i])]
        if state == m:
            found_indexes.append(i - m + 1)
    return found_indexes if found_indexes else None


