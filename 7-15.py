# A device in a door registers people entering and leaving a room.
# The + sign means a person entering a room and the -- sign a person leaving a room.
# Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise.
# Sample result:
# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

def f(detector):
    count = 0
    for ch in detector:
        if ch == '+':
            count += 1
        elif ch == '-':
            count -= 1
        
        if count >= 3:
            return True
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))