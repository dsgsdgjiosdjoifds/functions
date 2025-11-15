# only first two and last four should be visible
def mask_cc_number(number):
    res = ""

    for i, ch in enumerate(number):
        if i <= 1 or i >= len(number) - 4:
            res += ch
        else:
            res += '*'
    
    return res