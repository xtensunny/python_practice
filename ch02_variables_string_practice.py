# Chapter 2 Practice: String Variables & String Methods

# 1. Declare string variables
student_name = "Sunny"
course_name = "Full stack python Developer"
terminal_env = "WSL Ubuntu Linux"

# 2. Combine variables into clean print statement
greeting = "Hello, " + student_name + " Welcome to " + course_name + "."
print(greeting)

# 3. Experiment with the string methods from notes
print("________________________________")
print(student_name)
print(student_name.upper())
print(student_name.lower())
print(len(student_name))
print(student_name.startswith("S"))
print(student_name.endswith("u"))
print(student_name.replace("Sunny", "xtensunny"))
print(student_name.isalpha())
print(student_name.isdigit())