import argparse

def get_satisfaction_score(opinionWords):
    satisfactionScore = 0

    # Calculate staisfaction score
    for word in opinionWords:
        if word in positiveKeywords:
            satisfactionScore = satisfactionScore + 1
        if word in negativeKeywords:
            satisfactionScore = satisfactionScore - 1
    return satisfactionScore

if __name__ == "__main__":
    positiveKeywords = ["good", "nice", "beautiful", "charm"]
    negativeKeywords = ["boring", "horrible", "unsatisfied", "bad"]

    # Parse input argument (opinion)
    parser = argparse.ArgumentParser(description=   'Provide your opinion \
                                                    as an argument and we will \
                                                    give you a satisfaction score.')
    parser.add_argument('opinion', metavar='opinion', type=str,
                        help='Your opinion')
    opinion = parser.parse_args().opinion
    
    print("Satisfaction score:  ", get_satisfaction_score(opinion.split()))
    print("Input:               '" + opinion + "'")
    
