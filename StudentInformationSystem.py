students_info = {}


def option():
    print('\n THESE ARE THE OPTIONS, \nNOW CHOOSE A VALID OPTION (1 OR 2 ...)')
    print('1.ADD')
    print('2.VIEW')
    print('3.SEARCH')
    print('4.EDIT')
    print('5.DELETE')
    print('6.EXIT')


def viewoption():
    print(f"\n ***********Hello  What do you want to do ***********")
    print("1.For Individual Student")
    print("2.For All Student Information")
    return


def deloption():
    print(f"\n ***********Hello  What do you want to do ***********")
    print(f"\n 1.Delete an Individual Student ")
    print(f"\n 2.Delete All Student Information")
    return


def serachoption():
    print(f"\n ************** Choose search by name,by age or by grade **************")
    print(f"1.Name ")
    print(f"2.Age ")
    print(f"3.Grade ")


def add():
    try:
        print(" ==============Here Enter All Student information ==============\n")
        student_id = input("Enter your ID Number ")
        student_name = input("Enter your First name :- ")
        if student_id in students_info:
            print(f"{student_id}: student already exists on the system!!! \n")

        student_age = input("Enter your Age :- ")
        student_grade = input("Enter your Grade :- ")

        if not student_age.isdigit():
            print(f"{student_age}: you have entered the wrong format !")

        students_info[student_id] = {
            "name": student_name,
            "age": student_age,
            "grade": student_grade
        }

        print(f"\nStudent ID: - {student_id} Successfully Added ")

    except ValueError as ve:
        print(f"Value Error: {ve} please check your inputs")
    except KeyboardInterrupt:
        print(f"\nInterrupted by the user ")
        exit()

    except Exception as e:
        print(f"Something went wrong please try again !!!")


def view():
    viewoption()
    view_choice = input("\nEnter Your Choice :- ")
    if view_choice == "1":
        try:
            studentid = input("\nEnter The Student ID :- ")
            if studentid not in students_info:
                print(f"\nThe ID you entered does not exist")
                return
            print(f"\n ********* The student with the correspond Id number {studentid} have this Info *********")
            for key, value in students_info[studentid].items():
                print(f"{key.capitalize()}: {value}")
        except ValueError as e:
            print(f"Value Error: {e} please check your inputs")

    elif view_choice == "2":
        if not students_info:
            print(f"\n No Student Information Available")
        else:
            for sid, info in students_info.items():
                print(f"\nStudent ID: {sid}")
                for key, value in info.items():
                    print(f"{key.capitalize()}: {value}")
    else:
        print(f"Invalid Choice. Please use 1 or 2")


def search():
    serachoption()
    searchchoice = input("\n Enter your choice :- ").strip()
    if searchchoice == "1":
        serachname = input("\n Enter the student name :- ").strip().lower()
        searchfound = False
        for studentsserachid, infosearch in students_info.items():
            if serachname in infosearch["name"].lower():
                print(f"\n Found Student ID : {studentsserachid}")
                for key, value in infosearch.items():
                    print(f"{key}: {value}")
                    searchfound = True
        if not searchfound:
            print(f"student name doesnt exists in the database !")
    elif searchchoice == "2":
        searchage = input("\n Enter Student's age (should be number!) :- ").strip()
        searchfound = False
        for studentsearchage, infoage in students_info.items():
            if searchage in infoage["age"]:
                print(f"\n Student has been Found ID number :- {studentsearchage}")
                for key, value in infoage.items():
                    print(f"{key}: {value}")
                    searchfound = True
        if not searchfound:
            print(f"student age number doesnt exists in the database !")
    elif searchchoice == "3":
        searchgrade = input("\n Enter Students Grade :- ")
        searchfound = False
        for studentgrade, infograde in students_info.items():
            if searchgrade in infograde["grade"].upper():
                print(f"\n Student has been Found ID number :- {studentgrade}")
                for key, value in infograde.items():
                    print(f"{key}: {value}")
                    searchfound = True
        if not searchfound:
            print(f"student Grade doesnt exists in the database !")
    else:
        print(f"\n please enter a valid option 1,2 or 3")


def edit():
    print("EDIT code comming soon .....")


def delete():
    deloption()
    delchoice = input("\nEnter Your Choice :- ")
    try:
        if delchoice == "1":
            delchoice1 = input("\nEnter Student ID :- ")
            if delchoice1 in students_info:
                del students_info[delchoice1]
                print(f"\nStudent ID {delchoice1} has been Deleted successfully ")
            else:
                print(f"\nStudent ID {delchoice1} Does not exist. please Enter correct student ID")
        elif delchoice == "2":
            confirmdel = input("\nAre you sure you want to delete the entire the student information, Answer with "
                               "yes/no :- ").lower()
            if confirmdel == "yes":
                students_info.clear()
                print(f"\n The Entire student information has been deleted ")
            else:
                print(f"\n Deletion has been Aborted")
        else:
            print(f"\n Enter a Valid Option. please use 1 or 2. ")
    except Exception as e:
        print(f"an error occurred: {e}")


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
