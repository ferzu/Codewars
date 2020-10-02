# FILES *************************************************************************************************************************************
# Reading
f = open('my_path/myfile.txt','r') # Returns a file object
file_data = f.read() # Access the object. Takes the text contained in the file and puts it into a string (file_data)
f.close() # Always do, to free up resources.

# Writing
f = open('my_path/myfile.txt','w') # Opening a file in w mode deletes any content previously contained. If it does not exist, Python creates it.
f.write('Hello there!')
f.close()
# To add to an existing file use append(a) mode instead of write




# ITERATING FILE (flying_circus_cast.txt) and iterating trough it ***************************************************************************
    # - use with to open the file filename
    # - use the for loop syntax to process each line (extracting actor name spliting each line at the comma)
    # - and add the actor name to cast_list
def create_cast_list(filename):
    cast_list = []
    with open (filename) as cast: # with syntax closes the file automatically, to avoid too many opened files.
        for line in cast: # to create a list of lines
            cast_list.append(line.split(',')[0])
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

# His Solution:
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)




# IMPORTING MODULES ********************************************************************************************************************
import useful_functions as uf

scores = [88, 92, 79, 93, 85]
mean = uf.mean(scores)
curved = uf.add_five(scores)
mean_c = uf.mean(curved)
print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)
print(__name__) # global variable __name__ is set to the string value '__main__'
print(uf.__name__) # global variable __name__ takes the value from the imported module: "useful_funcions"
# IMPORTING (...)
    # useful_functions.py
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
# This statement (if __name__ == '__main__':) is useful when running this script standing alone.
# We could remove it and having all testing inside a function would not affect the demo_importing.py unless we called main() from there.
# Alternatively we could also substitute the def main(): statement for this if __name__ == '__main__':




# RAW USER INPUT ****************************************************************************************************************************
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
end = "c"
while  end != "q":
    names = input('Enter student name: ')
    assignments = input('Enter number assignments: ')
    grades = input("Enter grades separated by comma: ").split(",")
    print(message.format(names, assignments, grades[0], grades[1]))
    end = input("Enter q to quit, c to continue: ")





# DEBUGGING AND HANDLING EXCEPTIONS: use try to handle exceptions **********************************************************************
    # Syntax errors: Python can't interpret due to typo
    # Exceptions: unexpected things happen during execution. There are different types of
                # built-in expressions in Python. You see the type in error message.
user_list = []
list_sum = 0
for i in range(10): # seek user input for ten numbers
    user_input = int(input("Enter any 2-digit number: ")) # the errror was here, there was no int(), and a string was passed "not all arguments converted during string formating"
    try:
        number = user_input
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Exception ocurred:")
print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


# DEBUGGING (...) ***********************************************************************************************************************
    # TODO: Add a try-except block here to make sure no ZeroDivisionError occurs.
def party_planner(cookies, people):
    leftovers = None
    num_each = None
    while True:
        try:
            num_each = cookies // people
            leftovers = cookies % people
            break
        except ZeroDivisionError:
            print("0 is not a valid number")
        finally: #before leaving try it always runs finally, no matterwhat.
            return(num_each, leftovers)

lets_party = 'y'
while lets_party == 'y':
    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))
    cookies_each, leftovers = party_planner(cookies, people)
    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))
    lets_party = input("\nWould you like to party more? (y or n) ")

# His solution
def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")
    return(num_each, leftovers)
