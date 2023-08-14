### SCS 2201 - DSA - String Matching Assignment

    Index Number: 21001707

#### File Structure

> main.py - Main File

> kmp.py - contain the implementation of the KMP algorithm

> filtterPattern.py - Get the first substring of the pattern that dosen't include any regex symbols at the begining of the pattern.

> naive.py - If filtterPattern.py can't find a substring naive method will be used to match

> regex.py - Handle regex syntax

> #### input.txt - Contain the string

> #### patterns.txt - Contain a list of patterns that need to match with the string

> #### output.txt - Output will be written in this file, It will be created automatically when the program run

<hr>

> edit input.txt file to change the string
> add patterns to patterns.txt file

To run

```bash
  simply run the main.py file or in bash type "python main.py"
```

<hr>

### Explanation

First main.py file will read the input.txt file content. It will split the lines (using readlines()) and pass each pattern to getFirstValidPattern function.

Now this getFirstValidPattern() will return a substring of the pattern that doesn't includes any regex syntax such as (\*, ?, +, etc) at the begining of the pattern.

ex 01:
assume ptn = "abb+p"
return data = "abb"

ex02:
assume ptn = "abc.abc"
return data = "abc"

ex03:
assume ptn = a\*bc
return data = ""

ex04:
assume ptn = a?bc
return data = ""

ex05:
assume ptn = abbabb
return data = "abbabb"

Point of this getFirstValidPattern() function is, if it find a substring, then we can pass it into the KMP, construct PI array and do the first part of the matching efficiently.(as an exmple take ex01, so we will construct pi array for "abb" and do the matching. when we found a match, we can linearly check the rest "+p" is also matching or not. Advantage of this method is we can match the first part efficiently, if it has large substring that doesn't contain any regex Symbols)

But if getFirstValidPattern() return a empty string(in ex03, ex04), we have to go with naive method anyway.

The KMP will build a LCSArr/ Pi array according to the filtered substring of the pattern. Since it doesn't have any regex symbols searching have implemented as normal. When a match is found in KMP, we have to check rest of the pattern (because we only match the first sub-string that dosen't contain any regex) is matching or not. So the rest part can contain with regex expressions. To do that It will call regex() function

In this implementation, regex function will only handle below syntax

"\*" -> zero or more
"+" -> one or more
"?" -> zero or one
"." -> any character other than new line
