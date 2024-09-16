'''
Ransom note question from hackerrank
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''
def check_magazine(magazine, note):
    if len(note) > len(magazine):
        return (False)
    magazine_words_count = {}
    for word in magazine:
        if word in magazine_words_count:
            magazine_words_count[word] += 1
        else:
            magazine_words_count[word] = 1
    for word in note:
        if word in magazine_words_count and magazine_words_count[word] > 0:
            magazine_words_count[word] -= 1
        else:
            return (False)
    return (True)

magazine = 'give me one grand today night'
note = 'give one grand today'
returned_answer = check_magazine(magazine, note)
if returned_answer:
    print('Yes')
else:
    print('No')
    
