# Start with some designs that need to bee printed.


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design until none are lef
# Move each design to completed_models after printing.

# while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    # Simulate creating a 3D print from the design.
#    print("Printing model: " + current_design)
#    completed_models.append(current_design)

# Display all completed models
#print("\nThe following models have been printed")
#for completed_model in completed_models:
#    print(completed_model)

# Function that makes a copy of the list to do not affect the original

list_copy = unprinted_designs[:]
def print_models(list_copy, completed_models):
    for designs in unprinted_designs:
        print(designs)

def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician)

# Adding phrade the great to each amgicians name
def make_great(magicians_list):
    for magician in magicians_list:
        print("Great: " + magician)


print_models(list_copy, completed_models)