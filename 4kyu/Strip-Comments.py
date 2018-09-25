def solution(string, markers):
    split_string = string.split("\n")

    for character in markers:
        split_string = [
            part.split(character)[0].rstrip() for part in split_string
        ]

    uncommented_string = "\n".join(split_string)
    return uncommented_string

# Old idea, working too
# def solution(string, markers):
#     uncommented_string = ""
#     comment = False
#
#     for index, character in enumerate(string):
#         if comment is True:
#             if character == "\n":
#                 comment = False
#                 uncommented_string += character
#         elif character in markers:
#             comment = True
#         elif index < len(string) - 1 and string[index + 1] in markers:
#             if character == "\n":
#                 uncommented_string += character
#             comment = True
#         else:
#             uncommented_string += character
#
#     return uncommented_string


if __name__ == "__main__":
    text_1 = "apples, pears # and bananas\ngrapes\nbananas !apples"
    print(solution(text_1, ["#", "!"]))
    text_2 = ""
    print(solution(text_2, ["#", "!"]))
    text_3 = "\n"
    print(solution(text_3, ["#", "!"]))
    text_4 = "#"
    print(solution(text_4, ["#", "!"]))
    text_5 = "a #b\nc\nd $e f g"
    print(solution(text_5, ["#", "$"]))
