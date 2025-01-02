def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        letter_count = {}
        sorted_letters =  []
        def sort_on(dict):
            return dict["num"]
        for letter in file_contents:
            if letter not in letter_count:
                letter_count.update({letter: 1})
            else: letter_count[letter] +=1
        word_array = file_contents.split()
        word_count = 0
        for word in word_array:
            word_count += 1
        for letter in letter_count:
            if letter.isalpha():
                sorted_letters.append({"letter": letter, "num": letter_count[letter]})

        sorted_letters.sort(reverse=True, key=sort_on)
        for letter in sorted_letters:
            print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
main()