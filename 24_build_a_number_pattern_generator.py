def number_pattern(n):
    # Requirement 6: Return specific string if not an integer
    if type(n) is not int:
        return "Argument must be an integer value."
    
    # Requirement 7: Return specific string if non-positive
    if n < 1:
        return "Argument must be an integer greater than 0."

    # Requirements 3, 4, 5: Return space-separated string
    result = ""
    for i in range(1, n + 1):
        if i == 1:
            result += str(i)
        else:
            result += " " + str(i)
            
    return result