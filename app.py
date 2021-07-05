from typing import DefaultDict
import myFunctions

books = []

myFunctions.print_options()
option = input()

while option != "x" and option != "X":
    if (option.isnumeric() and ( 1 <= int(option) <= 8) ):
        myFunctions.clear_screen()
        print("You have selected Option " + option)

        if(int(option) == 1):
            print("Creating Book...")
            books.append(myFunctions.create_book())
        elif(int(option) == 2):
            myFunctions.issue_book()
        elif(int(option) == 3):
            myFunctions.return_book()
        elif(int(option) == 4):
            myFunctions.update_book()
        elif(int(option) == 5):
            print("Showing Books...\n\n\n")
            myFunctions.print_books()    
        elif(int(option) == 6):            
            myFunctions.show_book()
        elif(int(option) == 7):
            myFunctions.find()
        #Add other options

    else :
        myFunctions.clear_screen()
        print("Wrong option, choose again \n\n")
        myFunctions.print_options()
    
    input("Press any key to continue...")
    myFunctions.clear_screen()
    myFunctions.print_options()
    option = input()