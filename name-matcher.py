import argparse

def get_matching_names(names, letter):
    matches = []

    # Calculate staisfaction score
    for name in names:
        if name[0].upper() == letter.upper():
            matches.append(name)
    return matches

if __name__ == "__main__":
    # Parse input argument (opinion)
    parser = argparse.ArgumentParser(description=   'Provide a list of names, and \
                                                    the letter you want to filter them by.')
    parser.add_argument('names', metavar='names', type=str,
                        help='List of names, separated by a comma and space. ex: "Jack, jerome, bob, Chris"')
    parser.add_argument('letter', metavar='letter', type=str,
                    help='Letter to match the first character of those in your list.')
    args = parser.parse_args()
    names = args.names
    letter = args.letter
    
    print("Letter:              '" + letter + "'")
    print("Matched Names:       ", get_matching_names(names.split(", ", -1), letter))
    
    
