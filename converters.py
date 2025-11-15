def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(cm):
    return cm / 2.54

def ft_in_to_cm(ft, inches):
    return ft * 30.48 + inches * 2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'152cm = {cm_to_in(152):.02f}in')
    print(f'7\'2" = {ft_in_to_cm(7, 2):.02f}cm')
