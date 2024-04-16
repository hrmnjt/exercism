def translate(text):
    words = text.split()

    sentence = []

    for word in words:

        start_with_vowel = True if word[0] in ('a', 'e', 'i', 'o', 'u') else False
        start_with_consonant = not start_with_vowel

        vowel_sound = True if word[:2] in ('xr', 'yt') else False
        consonant_sound = True if word[:2] in ('ch', 'st', 'qu', 'th') else False
        three_consonant_sound = True if word[:3] in ('thr', 'sch') else False
        qu_following_consonant = True if start_with_consonant and word[1:3] == 'qu' else False
        y_after_consonant_cluster = True if start_with_consonant and 'y' in word and word[0] != 'y' else False

        if start_with_consonant:
            if vowel_sound:
                sentence.append(word+'ay')
            elif consonant_sound and not three_consonant_sound:
                sentence.append(word[2:]+word[:2]+'ay')
            elif three_consonant_sound:
                sentence.append(word[3:]+word[:3]+'ay')
            elif qu_following_consonant:
                sentence.append(word[3:]+word[:3]+'ay')
            elif y_after_consonant_cluster:
                sentence.append(word[word.index('y'):]+word[:word.index('y')]+'ay')
            else:
                sentence.append(word[1:]+word[0]+'ay')
        elif start_with_vowel:
            sentence.append(word+'ay')
        else:
            sentence.append(word)

    return ' '.join(sentence)
