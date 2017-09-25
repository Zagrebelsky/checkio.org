#!/usr/bin/python
def checkio(text):
    #replace this for solution
    string = text.lower()
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        elif char.isalpha():
            count[char] = 1

    maxv = max(count.values())
    new_list = [k for k, v in count.items() if v == maxv]
    letter =  min(new_list)
    return letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hellow world!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("oooAAa!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
