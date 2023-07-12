import re

>>> re.findall("e[a-z]", "regex college")
['eg', 'ex', 'eg']
>>> re.findall("python", "regex college")
[]

>>> x = re.search("e[a-z]", "regex college")
>>> type(x)
<class '_sre.SRE_Match'>
>>> x.string
'regex college'
>>> x.span()
(1, 3)
>>> x.group()
'eg'

>>> re.split('a', 'salam')
['s', 'l', 'm']
>>> re.split('[0-9]+', 'you92398can820split729with26numbers')
['you', 'can', 'split', 'with', 'numbers']
>>> re.split('[a-z]+', '2093ab20a120dk')
['2093', '20', '120', '']

>>> re.sub('l', 'salam', 'hello')
'hesalamsalamo'
>>> re.sub('[0-9]', '_digit_', '12ab1')
'_digit__digit_ab_digit_'
>>> re.sub('[0-9]+', '_num_', '12ab1129h')
'_num_ab_num_h'
