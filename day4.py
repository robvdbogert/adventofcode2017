def validate_by_unique_words(passphrase: str):
    words = passphrase.split(' ')
    unique_words = set(words)
    return len(words) == len(unique_words)


def validate_no_anagrams(passphrase: str):
    words = passphrase.split(' ')
    sorted_words = [''.join(sorted(word)) for word in words]
    unique_sorted_words = set(sorted_words)
    return len(sorted_words) == len(unique_sorted_words)


if __name__ == '__main__':
    validation_methods = [validate_by_unique_words, validate_no_anagrams]

    for validation_method in validation_methods:
        total_valid = 0
        total = 0
        with open('./input/day4.txt') as f:
            for line in f:
                total += 1
                if validation_method(line.strip()):
                    total_valid += 1

        print('{} of {} pass phrases are valid using method {}'.format(total_valid, total, validation_method))
