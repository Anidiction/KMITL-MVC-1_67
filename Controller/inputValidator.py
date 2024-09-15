def validateInput(cowId):
    isValid = True

    # The cow ID must be a numeric value, have a length of 8 characters, and the first character must not be "0".
    if not cowId.isdigit():
        isValid = False
    elif len(cowId) != 8:
        isValid = False
    elif cowId[0] == "0":
        isValid = False

    return isValid
