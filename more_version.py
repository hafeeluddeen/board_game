def names():
    while True:
        first_name = input("Enter your name:")
        second_name = input("Enter the other person's name : ")
        counter1 = 0
        counter2 = 0

        first_name = first_name.upper()
        second_name = second_name.upper()

        first_name_list = first_name.split()  # used to remove white spaces
        second_name_list = second_name.split()
        first_name_final_list = []
        second_name_final_list = []
        for word in first_name_list:
            for letter in word:
                counter1 += 1
                if letter.isalpha():  # only letters are added
                    first_name_final_list.append(letter)

        for word in second_name_list:  # if the counter gets incremented and the letter doesn't it means that it is
            # not alphabetical
            for letter in word:
                counter2 += 1
                if letter.isalpha():
                    if letter.isalpha():
                        second_name_final_list.append(letter)

        if len(first_name_final_list) == counter1 and len(second_name_final_list) == counter2:
            break
        else:
            print("Only letters and white spaces are allowed")

    common_alphabets(first_name_final_list, second_name_final_list)


def common_alphabets(first_name, second_name):
    common = []
    for letter in first_name:
        if letter in second_name:
            common.append(letter)

    unique_elements_list(common, first_name, second_name)


def unique_elements_list(common, first_name, second_name):
    for letter in common:
        if letter in first_name and letter in second_name:
            first_name.remove(letter)
            second_name.remove(letter)
    final_list = first_name + second_name

    flames_finder(len(final_list))


def flames_finder(length_1):
    flm = ["f", "l", "a", "m", "e", "s"]
    counter = 1  # to compare with the
    index_of_flm = 0
    while len(flm) != 1:

        if counter == length_1:
            flm.remove(flm[index_of_flm])
            counter = 1
            if index_of_flm == len(flm):
                index_of_flm = 0

        else:
            counter += 1
            index_of_flm += 1

        if index_of_flm == len(flm):
            index_of_flm = 0
    print(flm)


names()
