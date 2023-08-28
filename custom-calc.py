# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

#calculate the volume of a box
print("Please enter the following in feet.")
height = input("Enter height: ")
width = input("Enter width: ")
length = input("Enter length: ")

volume = (int(height) * int(width) * int(length))
print(f"""The dimension of the box are {height} feet in height, {width} feet in width, and {length} feet in length.
      As a result, the box has a volume of {volume} ft³!""")