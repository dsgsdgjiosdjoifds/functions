def count_letter(text, letter):
    count = 0
    for ch in text:
        if ch == letter:
            count += 1
    return count