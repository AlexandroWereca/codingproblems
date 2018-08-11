def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
                print('num vowels ', num_vowels)
        if num_vowels % 2 == 0:
            score += 2
            print('score ', score)
        else:
            score+=1

    return score

if __name__=='__main__':
    n = int(input())
    words = input().split()
    print(score_words(words))