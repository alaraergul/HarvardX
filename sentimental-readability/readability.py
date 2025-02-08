
def get_text():
    while True:
        text = input("Text: ")
        if text:
            return text


def calculate_grade_level(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)


def main():
    text = get_text()
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    grade_level = calculate_grade_level(letters, words, sentences)

    if grade_level < 1:
        print("Before Grade 1")
    elif grade_level >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade_level}")


if __name__ == "__main__":
    main()
