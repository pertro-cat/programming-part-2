def transition_table(nedle):
    """"
    This function builds the transition table for
    the finite automaton approach.
    """
    m = len(nedle)
    alphabet = set(nedle)
    transition_table = [{ch: 0 for ch in alphabet} for _ in range(m + 1)]

    for state in range(m + 1):
        for ch in alphabet:
            next_state = 0
            if state < m and ch == nedle[state]:
                next_state = state + 1
            else:
                if state > 0:
                    prefix = nedle[:state] + ch
                    for k in range(1, state + 1):
                        if prefix.endswith(nedle[:k]):
                            next_state = k
            transition_table[state][ch] = next_state
    return transition_table

def finite_automaton(haystack, nedle, transition_table):
    """
    This function uses a finite automaton to find and return
    all start indices of the substring 'needle' in 'haystack'.
    """
    if not nedle:
        return -1
    if not haystack:
        return -1
    if len(nedle) > len(haystack):
        return -1


    m = len(nedle)
    n = len(haystack)
    state = 0
    results = []

    for i in range(n):
        current_char = haystack[i]
        if current_char in transition_table[state]:
            state = transition_table[state][current_char]
        else:
            state = 0

        if state == m:
            start_index = i - m + 1
            results.append(start_index)
            state = transition_table[state - 1][haystack[i]]

    return results
