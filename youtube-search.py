import webbrowser

query = input("Type your Search: ")

webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

while True:
    query2 = input("Do you want to Search more:(Y/N) ")
    if "Y" in query2:
        query3 = input("Type your Search: ")
        print("Initiating Youtube Search Sequence!")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query3}")

    elif "y" in query2:
        query4 = input("Type your Search: ")
        print("Initiating Youtube Search Sequence!")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query4}")
   
    elif "N" in query2:
        print("Okay! No Problem!")
        break
    
    elif 'n' in query2:
        print("Okay! No Problem!")
        break

    else:
        print("Invalid")