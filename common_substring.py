'''
Common substring.
This is a question from hackerrank - https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''

def twoStrings(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    if (set_s1 & set_s2):
        return ('YES')
    return ('NO')

s1 = 'and'
s2 = 'art'
print(twoStrings(s1, s2))
