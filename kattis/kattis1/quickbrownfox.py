import string


def get_input():
    n = int(input())

    strings = []
    for _ in range(n):
        strings.append(input().strip().lower())

    return strings


def return_pangram_res(stri):
    chars = list(string.ascii_lowercase)
    missing_chars = []

    for char in chars:
        char_exist_in_text = char in stri
        if not char_exist_in_text:
            missing_chars.append(char)

    return missing_chars


def main():
    strings = get_input()
    for stri in strings:
        res = return_pangram_res(stri)
        if not res:
            print("pangram")
        else:
            print("missing " + "".join(res))


if __name__ == "__main__":
    main()
