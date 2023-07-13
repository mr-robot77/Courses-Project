def capitalize(names):
    capitalized_names = []
    for name in names:
        words = name.split()  # Split the name into individual words
        capitalized_words = [word.capitalize() for word in words]  # Capitalize each word
        capitalized_name = ' '.join(capitalized_words)  # Join the capitalized words back together with a space between them
        capitalized_names.append(capitalized_name)  # Add the capitalized name to the list of results
    
    return capitalized_names