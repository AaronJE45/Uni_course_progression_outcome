
from graphics import *

list_outcomes = []         

def progression_outcome(pass_credits, defer_credits, fail_credits):     
    """

    Compares pass credits, defer credits, fail credits and assigns
    a progression outcome. Takes outcome and appends it to list_outcomes[]
    
    """
    
    progress, trailer, retriever, exclude = 0, 0, 0, 0

    if pass_credits == 120:
        print("\nProgress\n")
        list_outcomes.append(["Progress -", pass_credits, defer_credits, fail_credits])
        progress += 1
    elif (defer_credits + fail_credits) == 20:
        print("\nProgress(module trailer)\n")
        list_outcomes.append(["Progress(module trailer) -", pass_credits, defer_credits, fail_credits])
        trailer += 1
    elif fail_credits >= 80:
        print("\nExclude\n")
        list_outcomes.append(["Exclude -", pass_credits, defer_credits, fail_credits])
        exclude += 1
    elif (defer_credits + fail_credits) >= 60 or pass_credits == 80:
        print("\nModule Retriever\n")
        list_outcomes.append(["Module Retriever -", pass_credits, defer_credits, fail_credits])
        retriever += 1

    return progress, trailer, retriever, exclude

def validating_credit(prompt):                                          
    """ 
    
    The function prompts that the user to enter specific credit and converts to integer
    and verifies whether the user input in within the credit options[0,20,40,80,100,120].
    
    
    """
    while True:                                           
        try:
            input_credits = int(input(prompt))
            credit_option = [0, 20, 40, 60, 80, 100, 120]
            if input_credits in credit_option:
                return input_credits
            else:
                print("==============================================")
                print("Out of range")
                print("==============================================")
        except ValueError:
            print("==============================================")
            print("Integer required!")
            print("==============================================")

def histogram(total_progress, total_trailer, total_retriever, total_exclude): 
    """ 
    
    Displays a histogram that has the total number of each type
    of progression outcomes in 4 different rectangles with texts,
    a line and displays the total number of total 
    outcome.
    
    """
    min_y = 150
    outcome = total_progress + total_exclude + total_retriever + total_trailer
    win = GraphWin("Histogram", 1000, 800)
    win.setBackground(color_rgb(222, 250, 222))

    '''    Text     '''

    title = Text(Point(200, 75), "Histogram Results")
    title.setSize(30)

    text_progress = Text(Point(175, 675), "Progress")

    text_trailer = Text(Point(375, 675), "Trailer")

    text_modular = Text(Point(575, 675), "Modular")

    text_exclude = Text(Point(775, 675), "Exclude")

    text_outcome = Text(Point(200, 775), "Total outcome = " + str(outcome))
    text_outcome.setSize(30)

    num_of_progress = Text(Point(175, max(min_y, 650 - total_progress * 50) - 8), str(total_progress))

    num_of_trailer = Text(Point(375, max(min_y, 650 - total_trailer * 50) - 8), str(total_trailer))

    num_of_modular = Text(Point(575, max(min_y, 650 - total_retriever * 50) - 8), str(total_retriever))

    num_of_exclude = Text(Point(775, max(min_y, 650 - total_exclude * 50) - 8), str(total_exclude))

    title.draw(win)
    
    text_progress.draw(win)
    text_trailer.draw(win)
    text_modular.draw(win)
    text_exclude.draw(win)
    text_outcome.draw(win)

    num_of_progress.draw(win)
    num_of_trailer.draw(win)
    num_of_modular.draw(win)
    num_of_exclude.draw(win)

    '''  Rectangles '''

    rect_of_progress = Rectangle(Point(100, max(min_y, 650 - total_progress*50)), Point(250, 650))
    rect_of_progress.setFill(color_rgb(142, 110, 142))

    rect_of_modular = Rectangle(Point(300, max(min_y, 650 - total_trailer*50)), Point(450, 650))
    rect_of_modular.setFill(color_rgb(110, 142, 142))

    rect_of_trailer = Rectangle(Point(500, max(min_y, 650 - total_retriever*50)), Point(650, 650))
    rect_of_trailer.setFill(color_rgb(142, 142, 110))

    rect_of_exclude = Rectangle(Point(700, max(min_y, 650 - total_exclude*50)), Point(850, 650))
    rect_of_exclude.setFill(color_rgb(110, 110, 142))

    rect_of_progress.draw(win)
    rect_of_modular.draw(win)
    rect_of_trailer.draw(win)
    rect_of_exclude.draw(win)

    '''  Line  '''

    line = Line(Point(100, 650), Point(900, 650))
    
    line.draw(win)


def staff_version():
    """

    This function allows the staff to enter numerous student records and get a histogram.

    """
    
    total_progress, total_trailer, total_retriever, total_exclude = 0, 0, 0, 0

    while True:                                                       
        pass_credits = validating_credit("\nEnter a pass credit: ")
        defer_credits = validating_credit("\nEnter a defer credit: ")
        fail_credits = validating_credit("\nEnter a fail credit: ")

        total = pass_credits + defer_credits + fail_credits

        if total != 120:
            print("==============================================")
            print("Total incorrect!")
            print("==============================================")
        else:
            progress, trailer, retriever, exclude = progression_outcome(pass_credits, defer_credits, fail_credits)

            total_progress += progress
            total_trailer += trailer
            total_retriever += retriever
            total_exclude += exclude

            outcome_option = input("Would you like to enter another set?\nEnter 'y' to continue or 'q' to quit and "
                                   "check results?: ").lower()

            if outcome_option == "q":
                histogram(total_progress, total_trailer, total_retriever, total_exclude)
                print("\nPart 2:")
                for outcome in list_outcomes:
                    print(outcome[0], outcome[1], ',', outcome[2], ',', outcome[3])
                                                                                        
                with open("Part3.txt", "w") as f:                               
                    f.write("Part 3:\n")
                    for outcome in list_outcomes:
                        f.write(f"{outcome[0]} {outcome[1]}, {outcome[2]}, {outcome[3]}\n")
                with open("Part3.txt", "r") as f:
                    progression_data = f.read()
                    print(progression_data)
                break

def student_version():
    '''

    This functions allows a student to enter their credits and get a progression outcome.

    '''

    pass_credits = validating_credit("\nEnter your pass credits: ")
    defer_credits = validating_credit("\nEnter your defer credits: ")
    fail_credits = validating_credit("\nEnter your fail credit: ")

    total = pass_credits + defer_credits + fail_credits

    if total != 120:
        print("==============================================")
        print("Total incorrect!")
        print("==============================================")
        student_version()
    else:
        progression_outcome(pass_credits, defer_credits, fail_credits)



print("Enter 1 - If you are a student")
print("Enter 2 - if you are a staff member")
user = int(input("==> "))
print("==============================================")


if user == 1:
    print("Welcome to student portal !")
    print("==============================================")
    student_version()
else:
    print("Welcome to staff portal !")
    print("==============================================")
    staff_version()

