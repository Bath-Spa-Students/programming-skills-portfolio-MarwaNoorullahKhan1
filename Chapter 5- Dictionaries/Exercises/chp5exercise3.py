# Create a dictionary of Python terms and their meanings
python_terms = {
    "list": "A collection of items in a particular order.",
    "dictionary": "A collection of key-value pairs.",
    "tuple": "An immutable list.",
}

# Loop through the dictionary and print each term and its meaning
for term, meaning in python_terms.items():
    print(term.title() + ": " + meaning)

# Add three more terms to the dictionary
python_terms["set"] = "A collection of unique items."
python_terms["function"] = "A named block of code that performs a specific task."
python_terms["module"] = "A file containing Python definitions and statements."