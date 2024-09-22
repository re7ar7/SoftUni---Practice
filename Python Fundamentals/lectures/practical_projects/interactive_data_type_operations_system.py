# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':
    # Declare a string variable, e.g., sentence = "Learning Python is fun!"
    # Extract and print a substring, such as the word "Python" from the sentence.
    # Convert the entire sentence to uppercase and print it.
    # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.


    message = 'Learning Python is fun!'
    print(message[9:15])
    uppercase_message = message.upper()
    print(uppercase_message)
    message = message.replace('fun', 'awesome')
    print(message)


elif choice == '2':

# Prompt the user to input two numbers, e.g., num1 and num2.
# Perform and print the results of addition, subtraction, multiplication, and division.
# Handle division by zero (e.g., print an error message if num2 is zero).
# Perform a power operation, raising num1 to the power of num2, and print the result.

    a = int(input('Choose the first number \'a\': '))
    b = int(input('Choose the second number \'b\': '))

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    raised_a_to_b = a ** b

    print(f'Addition: {addition:.1f}')
    print(f'Subtraction: {subtraction:.1f}')
    print(f'Multiplication: {multiplication:.1f}')
    if b == 0:
        print('Error! The second number is 0. You can\'t divide by 0.')
    else:
        print(f'Division: {division:.1f}')
    print(f'{a:.1f} raised to the power of {b:.1f} is: {raised_a_to_b:.1f}')

# If the user chooses Booleans (choice == '3'):
elif choice == '3':

# Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
# Perform and print the results of logical operations: AND, OR, NOT.
# Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
    is_python_fun = True
    is_sunny= False

    and_operation = is_sunny and is_python_fun
    or_operation = is_sunny or is_python_fun
    not_operation = not is_sunny

    print(f'AND operation result for: {is_python_fun} and {is_sunny} = {and_operation}')
    print(f'OR operation result for: {is_python_fun} or {is_sunny} = {or_operation}')
    print(f'AND operation result for: not {is_sunny} = {not_operation}')
    print('=============================================================')

    print(f'COMPARISON OPERATIONS WITH NUMBERS')
    a = int(input('Choose the first number \'a\': '))
    b = int(input('Choose the second number \'b\': '))



    print(f'a = {a}, b = {b}')
    print(f'a > b = {a>b}')
    print(f'a == b = {a == b}')
    print(f'a < b = {a < b}')
    print(f'a != b = {a != b}')

    print(f'a > a = {a > a}')
    print(f'a == a = {a == a}')
    print(f'a < b = {a < a}')
    print(f'a != b = {a != b}')

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
# ### List Operations ###
# Create a list with mixed data types (e.g., numbers, strings, booleans).
# Append a new element to the list and print the updated list.
# Access and print the 4th element in the list.
    print(f'LISTS')
    print('=============================================================')
    mixed_list = [1, 2, 'Mario', 'Daniel', True]
    print(f'Created list = {mixed_list}')
    mixed_list.append('Excellent!')
    print(f'Appended list = {mixed_list}')
    print(f'Fourth (4th) element of the list is: \'{mixed_list[4]}\'')


# ### Tuple Operations ###
# Create a tuple with some string elements (e.g., fruits).
# Print the length of the tuple.
# Try to modify one element in the tuple and handle the resulting TypeError.
    print('TUPLES')
    print('=============================================================')
    fruits = ('apple', 'banana', 'grape', 'cherry')
    print(f'The length of the tuple is: {len(fruits)}')

    print(f'Modifying the \'grape\' element into a \'peach\':')
    fruits_list = list(fruits)
    fruits_list[2] = 'peach'
    fruits = tuple(fruits_list)
    print(fruits)


# ### Dictionary Operations ###
# Create a dictionary with some key-value pairs (e.g., name, age, city).
# Access and print the value for one of the keys (e.g., "age").
# Add a new key-value pair to the dictionary and print the updated dictionary.

    print(f'DICTIONARIES')
    print('=============================================================')
    personal_data = {'name': 'Daniel', 'age': 23, 'city': 'Varna'}
    print(f'Created dictionary:')
    print(personal_data)
    print(f'Age of the person is: {personal_data["age"]}')
    personal_data['University'] = 'Softuni'
    print(f'Edited dictionary:')
    print(personal_data)

# If the user enters an invalid choice:
else:

    print(f'Error! You have chosen an invalid selection number!')
# Print an error message indicating an invalid selection.

