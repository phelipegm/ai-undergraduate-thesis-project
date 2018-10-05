import re

x = re.match('abc', 'abcdefg')
print(x)

word_regex = '\w+'
y = re.match(word_regex, 'Hello there!')
print(y)

digit_regex = '\d'
z = re.match(digit_regex, '9')
print(z)

"""
Obs.:     pattern      matches        example
            \w+         word          'Magic'
            \d          digit            9
            \s          space           ''
            .*         wildcard      'username74'
          + or *     greedy match     'aaaaaa'
            \S        not space      'no_spaces'
           [a-z]   lowercase group    'abcdefg'
"""

a = re.split('\s+', 'Split on spaces.')
print(a)

my_string = "Let's write RegEx!"
PATTERN = '\w+'
b = re.findall(PATTERN, my_string)
print(b)

# ---------------------------------------- 27/08/2018 -------------------------------------------

"""
Note: It's important to prefix your regex patterns with r to ensure that your patterns are interpreted in the way
 you want them to. Else, you may encounter problems to do with escape sequences in strings.
For example, "\n" in Python is used to indicate a new line, but if you use the r prefix, it will be interpreted
 as the raw string "\n" - that is, the character "\" followed by the character "n" - and not as a new line.
"""

my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?" \
            "  Or perhaps, all 19 words?"

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"

print(re.findall(capitalized_words, my_string))
