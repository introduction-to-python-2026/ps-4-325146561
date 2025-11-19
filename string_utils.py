def split_before_each_uppercases(formula):
    if not formula:
        return []
    parts = []
    start = formula[0]
    
    for end in range(1,len(formula)):
        if end.isupper():
            parts.append(current)
            start = end
        else:
            start += end

    parts.append(start)
    return parts


def split_at_first_digit(formula):
    digit_location = 1
    
    for char in formula[1:]:
        if char.isdigit():
            break
            digit_location += 1

    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number = int(formula[digit_location:])
    return prefix, number


