# Define a function f(number) that returns the sum of repeated digits in a number.
# Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    _sum = 0
    digit_count = {}
    for ch in str(number):
        count = digit_count.get(ch, 0)
        digit = int(ch)
        if count == 1:
            _sum += digit * 2 # we multiply by 2 to also add the previous number that wasnt yet summed because it appeared first time
        elif count > 1:
            _sum += digit
        digit_count[ch] = count + 1
    return _sum

print(f(1027))
print(f(230335))
print(f(513553007))
