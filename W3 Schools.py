import webbrowser

print('''List of W3 Schools' pages you can open: 
1. Home
2. Javasript
3. HTML
4. CSS
5. Bootstrap
6. Python
''')

while True:

    page = str(input("Which Page Do You Wish to Open: ")).lower()
    if page == "home" or page == "1":
        print("Initiating Home Search Sequence!")
        webbrowser.open("https://www.w3schools.com")

    elif page == "javascript" or page == "2" or page == "js":
        print("Initiating Javasript Search Sequence!")
        webbrowser.open("https://www.w3schools.com/js/default.asp")

    elif page == "html" or page == "3":
        print("Initiating HTML Search Sequence!")
        webbrowser.open("https://www.w3schools.com/html/default.asp")

    elif page == "css" or page == "4":
        print("Initiating CSS Search Sequence!")
        webbrowser.open("https://www.w3schools.com/css/default.asp")

    elif page == "bootstrap" or page == "5" or page == 'bs4' or page == 'bs':
        print("Initiating Bootstrap Search Sequence!")
        webbrowser.open("https://www.w3schools.com/bootstrap4/default.asp")

    elif page == "python" or page == "6":
        print("Initiating Python Search Sequence!")
        webbrowser.open("https://www.w3schools.com/python/default.asp")
    
    elif page == 'exit':
        print("Initiating Exit Sequence!")
        break
        exit()

    else:
        print("Invalid")