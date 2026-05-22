def alphabet_position(text):
    result = []

    for char in text.lower():

        if char == "a":
            result.append("1")

        elif char == "b":
            result.append("2")

        elif char == "c":
            result.append("3")

        elif char == "d":
            result.append("4")

        elif char == "e":
            result.append("5")

        elif char == "f":
            result.append("6")

        elif char == "g":
            result.append("7")

        elif char == "h":
            result.append("8")

        elif char == "i":
            result.append("9")

        elif char == "j":
            result.append("10")

        elif char == "k":
            result.append("11")

        elif char == "l":
            result.append("12")

        elif char == "m":
            result.append("13")

        elif char == "n":
            result.append("14")

        elif char == "o":
            result.append("15")

        elif char == "p":
            result.append("16")

        elif char == "q":
            result.append("17")

        elif char == "r":
            result.append("18")

        elif char == "s":
            result.append("19")

        elif char == "t":
            result.append("20")

        elif char == "u":
            result.append("21")

        elif char == "v":
            result.append("22")

        elif char == "w":
            result.append("23")

        elif char == "x":
            result.append("24")

        elif char == "y":
            result.append("25")

        elif char == "z":
            result.append("26")

        else:
            pass

    return " ".join(result)


print(alphabet_position("gelabarkalaia"))