# analyzer/algorithms.py

def rabin_karp(pattern, text, prime=101):
    result = []
    m, n = len(pattern), len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m-1):
        h = (h * 256) % prime

    for i in range(m):
        pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
        text_hash = (256 * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                result.append(i)
        if i < n - m:
            text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return result


def kmp(pattern, text):
    result = []
    lps = [0] * len(pattern)
    j = 0

    compute_lps(pattern, lps)

    i = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


def compute_lps(pattern, lps):
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
