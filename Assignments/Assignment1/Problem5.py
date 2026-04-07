def check(words):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    for word in words:
        for ch in word:
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    print("Number of vowels are:", v_count)
    print("Number of consonants are:", c_count)


def main():
    words = ["agrihoe"]
    check(words)


if __name__ == "__main__":
    main()