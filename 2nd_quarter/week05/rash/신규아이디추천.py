import string


def solution(new_id):
    first = False
    last = False
    answer = ''

    punctuation = string.punctuation
    # 1단계
    new_id = new_id.lower()

    # 2단계
    symbols = punctuation.replace("-", "").replace("_", "").replace(".", "")
    for symbol in symbols:
        new_id = new_id.replace(symbol, "")

    # 3단계
    while ".." in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if len(new_id) > 0:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    # 5단계
    if new_id == "":
        new_id = "a"

    # 6단계
    if len(new_id) > 15:
        new_id = new_id[0:15]

    # 7단계
    while (len(new_id) < 3):
        new_id += new_id[-1]

    if len(new_id) > 0:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    answer = new_id
    return answer