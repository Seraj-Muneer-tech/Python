import webbrowser

input1 = input("TYPE YOUR SEARCH: ")
if input1 == "exit_code(root)":
    print("--------------------INITIATING ROOT EXIT SEQUENCE!--------------------")
    exit()

else:
    print("INITIATING GOOGLE SEARCH SEQUENCE!")
    webbrowser.open("https://www.google.com/search?q=" + input1)

while True:
    input2 = input("DO YOU WISH TO SEARCH MORE?[Y/N] ").lower()
    if str(input2) == "y":
        input3 = input("TYPE YOUR SEARCH: ")
        if input3 == "exit_code(root)":
            print("--------------------INITIATING ROOT EXIT SEQUENCE!--------------------")
            break
            exit()
        else:
            print("INITIATING GOOGLE SEARCH SEQUENCE!")
            webbrowser.open("https://www.google.com/search?q=" + input3)

    elif str(input2) == "n":
        print("INITIATING EXIT SEQUENCE!")
        break
        exit()

    else:
        print("INVALID!")