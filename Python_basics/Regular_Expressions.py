import re

pattern = r'[A-Z]yclone'

text = '''Artificial intelligence (AI) Cyclone is the capability of computational systems to
perform tasks typically associated with Ayclone human intelligence,
such as learning, reasoning, Byclone, problem-solving, perception,
and decision-making. It Dyclone is a field of research in engineering,
mathematics and computer science Eyclone that develops and studies
methods and software that enable machines to perceive their
environment and use learning and intelligence to take actions
that maximize their chances of achieving defined goals.'''

#match = re.search(pattern, text) # Only used for the first occurence
#print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(text[match.span()[0]:match.span()[1]])