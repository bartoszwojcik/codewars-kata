def parse(data):
    if type(data) != str:
        return []

    value = 0
    output = []
    for character in data:
        if character == "i":
            value += 1
        elif character == "d":
            value -= 1
        elif character == "s":
            value *= value
        elif character == "o":
            output.append(value)

    return output


if __name__ == "__main__":
    print(parse("ooo"))
    print(parse("ioioio"))
    print(parse("idoiido"))
    print(parse("isoisoiso"))
    print(parse("codewars"))
    print(parse(""))
    print(parse("ccc"))
    print(parse(1))
