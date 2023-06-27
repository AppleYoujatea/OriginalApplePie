def solution(keymap, targets):
    answer = []
    key_dict = {}
    for key in keymap:
        for idx, val in enumerate(key):
            if (val in key_dict):
                if (key_dict[val] > idx + 1):
                    key_dict[val] = idx + 1
            else:
                key_dict[val] = idx + 1
    for target in targets:
        tmp = 0

        for t in target:
            if (t in key_dict):
                tmp += key_dict[t]
            else:
                tmp = -1
                break
        answer.append(tmp)
    return answer