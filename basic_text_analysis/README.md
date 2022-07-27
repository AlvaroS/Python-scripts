# Basic text analysis in Python

This is a small code to analyse the amount of times words or characters of the alphabet appear in text and the number of words, lines and character present in a text file.

# Usage
char_freq.py will output the letters used in the text followed by the number of times they appear. Accented characters will be converted to non accented.

    $ python char_freq.py FILE_NAME.txt
    e: 69,421
    t: 46,644
    a: 41,683
    o: 40,041
    i: 37,774
    n: 37,687
    h: 34,068
    s: 33,110
    r: 32,298
    d: 22,300
    l: 21,592
    u: 14,986
    m: 14,764
    c: 13,461
    y: 12,704
    w: 12,306
    f: 12,001
    g: 10,029
    b: 9,085
    p: 8,225
    v: 5,725
    k: 3,208
    z: 936
    j: 871
    x: 839
    q: 628

word_freq.py will output all the words present in the text followed by the number of times each word appear. Use it with _head_ to show the first 10.

    $ python word_count.py FILE_NAME.txt | head
    the: 4332
    to: 4163
    of: 3612
    and: 3584
    her: 2225
    i: 2070
    a: 1949
    in: 1880
    was: 1846
    she: 1710

word_count.py will output the numbers of lines, words and characters in a file.

    $ python word_count.py FILE_NAME.txt
    Number of lines: 14,060
    Number of words: 121,532
    Number of characters: 754,876