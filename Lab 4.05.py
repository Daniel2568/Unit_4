'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])

    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program

One bug is that it says print_numbers(num_list) which you cant do because you cant print two lists the way the code appears.

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program

One major bug is that at the end it says "print(line_str)" when the variable being defined is swapping stars not line_str. 
line_str also needs to be tabbed over onec to be in line with the for loops.

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''
#first code

def print_numbers(list):
    for i in range(1, len(list)+1):
        print(list(i))

num_list = [1, 2, 3, 4, 5, 6]
print_numbers(num_list)

#second code

def swapping_stars():
    line_str  = ""
    for line in range(0, 6):
        for char in range(0,6):
            if line % 2 == char % 2:
                line_str += "*"
            else:
                line_str += "-"
    swapping_stars()
pass