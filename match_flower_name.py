# Write your code here
flower_file = "flowers.txt"
flower_names = []
# HINT: create a dictionary from flowers.txt
with open(flower_file, "r") as f:
    for line in f:
        flower_name = line.title()
        flower_names.append(flower_name)

# HINT: create a function to ask for user's first and last name
# def find_letter(first_name, last_name):
#     first_letter = first_name[0].title()
#     return first_letter

# vorname = str(input("Enter your first name: "))
# nachname = str(input("Enter your last name: "))

# x = find_letter(vorname, nachname)

# def flower_print(letter, names):
#     for name in names:
#         if name[0] == letter:
#             return print(name)
            
# flower_print(x, flower_names)
# print the desired output



#Alternatively
def find_flower(name, flow_names):
    full_name = name.split(" ")
    first_name = full_name[0].title()
    last_name = full_name[1].title()
    first_letter = first_name[0].title()
    for flow_name in flow_names:
        if flow_name[0] == first_letter:
            return print("Unique flower name with the first letter: ", flow_name)
        
name = str(input("Enter your First [space] Last name only: "))
find_flower(name, flower_names)


# ## function that creates a flower_dictionary from filename
# def create_flowerdict(filename):
#     flower_dict = {}
#     with open(filename) as f:
#         for line in f:
#             letter = line.split(": ")[0].lower() 
#             flower = line.split(": ")[1].strip()
#             flower_dict[letter] = flower
#     return flower_dict

# ## Main function that prompts for user input, parses out the first letter
# ## includes function call for create_flowerdict to create dictionary
# def main(): 
#     flower_d = create_flowerdict('flowers.txt')
#     full_name = input("Enter your First [space] Last name only: ")
#     first_name = full_name[0].lower()
#     first_letter = first_name[0]
# ## print command that prints final input with value from corresponding key in dictionary
#     print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

# main()
    