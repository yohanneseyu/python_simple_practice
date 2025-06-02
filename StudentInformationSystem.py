def option():
    print('THESE ARE THE OPTIONS, \nNOW CHOOSE A VALID OPTION (1 OR 2 ...)')
    print('1.ADD')
    print('2.VIEW')
    print('3.SEARCH')
    print('4.EDIT')
    print('5.DELETE')
    print('6.EXIT')


def add():
    print("ADD code comming soon ......")


def view():
    print("VIEW code comming soon .......")


def search():
    print("SERACH code comming soon ......")


def edit():
    print("EDIT code comming soon .....")


def delete():
    print("DELETE code comming soon ......")


def menu():
    while True:
        option()
        choice = input("Enter your choice :- ")
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            search()
        elif choice == "4":
            edit()
        elif choice == "5":
            delete()
        elif choice == "6":
            print("GOOD BYE !!!")
            break
        else:
            print("********** ENTER A VALID OPTION **********")


def main():
    print("========================= WELLCOME TO STUDENT INFORMATION CONSOLE SYSTEM =========================\n")
    while True:
        first_name = input("Enter your first name :- ").strip()
        last_name = input("Enter your last name :- ").strip()
        if first_name.isalpha() and last_name.isalpha():
            print(f"hello {first_name.capitalize()}, {last_name.capitalize()} Wellcome back to our student "
                  f"information system")
            menu()
        else:
            print("Both first and last names must contain only letters. Please try again.")


if __name__ == '__main__':
    main()
