def beg():
    print("Welcome to the Bookstore Ordering Chatbot")
    name = input("What is your name?: ")
    age = input("Hi "+ name + ", how old are you? ")
    wmessage = print("Welcome "+ name +"!!! Way to be "+ age + "! How may I help you today?")


poptions = {
    "1" : "Order a young adult romance novel",
    "2" : "Order a young adult sci fi novel",
    "3" : "Order a young adult murder mystery novel",
    "4" : "Exit the conversation"
}
def displayoption():
    print("Please choose from the following options: ")
    for key, value in poptions.items():
        print(f"{key}. {value}")
      

       



def option_choices(poption):
    if poption == "1":
        return yaromance()
    elif poption == "2":
        return yascifi()
    elif poption == "3":
        return yamm()
    elif poption == "4":
        return "Okay!!!!!"
    else:
        return "Nonexistant option. Please try again!!"
    

def yaromance(poption):
    roptions = {
        "1" : "Five Feet Apart",
        "2" : "All The Bright Places",
        "3" : "Last Night At The Telegraph Club",
        "4" : "The Spanish Love Deception"
    }
    print("Choose one of the following options: ")
    for key, value in roptions.items():
        print(f"{key}. {value}")
    yachoice = input("Enter your choice: ")
    



def yascifi(poption):
    sfoptions = {
        "1" : "The Loneliest Girl in the Universe",
        "2" : "This Mortal Coil",
        "3" : "Feed",
        "4" : "The Last Days"
    }
    print("Choose one of the following Sci Fi options: ")
    for key, value in sfoptions.items():
        print(f"{key}. {value}")
    sf_choice = input("Enter your choice: ")

def yamm():
    mmoptions = {
        "1" : "They wish They Were Us",
        "2" : "Nothing More To Tell",
        "3" : "How To Survive Your Murder",
        "4" : "They'll Never Catch Us"
    }
    print("Choose one of the following Murder Mystery options: ")
    for key, value in mmoptions.items():
        print(f"{key}. {value}")
    mmchoice = input("enter your choice: ")




def main():
    while True:
        beg()
        displayoption()
        poption = input("choose an option: ")
        response = option_choices(poption)
        print(response)
        if poption == "4":
            print("Thank you for stopping by!! Have a good day!!")
            break
        
if __name__ == "__main__":
    main()