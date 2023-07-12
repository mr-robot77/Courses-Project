# phone number evaluation with regex

mobile_number = input()
if len(mobile_number) == 11 and mobile_number.startswith('09') and mobile_number.isdigit(): 
    print('✅Valid mobile number')
else:
    print('❌Invalid mobile number')

"abcd"
"$^%#"
"1234"

"abc."
"123."
"defg"

"asd7"
"6sd1"
"dsdg"

"bQ"
"6s"
"d5"

"aB"
"6_"
"<?"

"bQ@"
"6_!"
"d56"

"sx"
"sxxx"
"s"

"sx"
"sxxx"
"s"

"df"
"ef"
"f"
"def"
"deef"

"@!#$"
"IAmAli"
"12345678"
"Hi"

"beg"
"cdi"
"abc"

"o"
"i"
"p"
"x"

"abcd"
"abcf"
"abck"

"abcabcabc"
"abc"
"abdccccc"

"Mahtab"
"Mahan"
"TabMah"

"َAlipour"
"Rashidpour"
"pourMansour"