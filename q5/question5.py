def reverse_words(string):
    str_list = string.replace('\n', ' ').split(' ')
    str_list.reverse()
    string = ""
    for i in range(0, len(str_list)):
        string += str_list[i]
        if (i != len(str_list) - 1):
            string += " "
    return string

if (__name__ == "__main__"):
    string1 = """Two roads diverged in a yellow wood, And sorry I could not travel both And 
be one traveler, long I stood And looked down one as far as I could To where 
it bent in the undergrowth;"""
    print("input string1 : \n{0:s}".format(string1))
    print("output string1 : \n{0:s}".format(reverse_words(string1)))
    string2 = """Then took the other, as just as fair, And having perhaps the better claim, 
Because it was grassy and wanted wear; Though as for that the passing there 
Had worn them really about the same,"""
    print()
    print("input string2 : \n{0:s}".format(string2))
    print("output string2 : \n{0:s}".format(reverse_words(string2)))
