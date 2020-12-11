# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6
def reverseInParentheses(inputString):
    chars = list(inputString)
    open_bracket = []
    for i,c in enumerate(chars):
        if c == '(':
            open_bracket.append(i)
        elif c == ')':
            j = open_bracket.pop()
            chars[j:i] = chars[i:j:-1]
    return ''.join(c for c in chars if c not in '()')

print(reverseInParentheses("(bar)"))
print(reverseInParentheses("foo(bar)baz"))
print(reverseInParentheses("foo(bar)baz(blim)"))
print(reverseInParentheses("foo(bar(baz))blim"))
print(reverseInParentheses(""))
print(reverseInParentheses("()"))