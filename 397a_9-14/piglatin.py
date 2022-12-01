
def pigify(word):
    """Return a Pig Latin version of the word provided."""

    # find the first vowel in the word
    vowel_index = len(word)
    for i in range(len(word)):
        if word[i].lower() in 'aeiou':
            vowel_index = i
            break

    # if we found a vowel, move all the characters before it (if any) to the end and add an "ay"
    if vowel_index < len(word):
        prefix = word[:vowel_index]  # might be '' if index is 0!
        suffix = word[vowel_index:]
        word_pl = suffix + prefix + "ay"
        return word_pl

    # otherwise, just append "ay" and be on your way
    else:  
        return word + "ay"


print("397A amat te.")
print("My pig latin name is " + pigify('Luke Geel'))
