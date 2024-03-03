def oxford_comma(elements):
    if len(elements) == 0:
        return ''
    elif len(elements) == 1:
        return str(elements[0])
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        return ', '.join(elements[:-1]) + f", and {elements[-1]}"
