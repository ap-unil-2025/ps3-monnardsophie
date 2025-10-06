

def get_numbers_from_user():
    
   
    numbers = []

    while True:
        text=input("give a number or type done")
        if text == "done":
            break
        if text.replace(".","",1).isdigit():
            numbers.append(float(text))
       
        else : 
            print("invalid input")
            

    print(numbers)
    return numbers



def analyze_numbers(numbers):
    analysis = {}
   
    count_nb = len(numbers)
    sum_nb = sum(numbers)
    average_nb = sum(numbers)/len(numbers)
    minimum_nb = min(numbers)
    maximum_nb = max(numbers)
    list_even = []
    for i in numbers :
        if i % 2 == 0 :
            list_even.append(i)
        
    even_count = len(list_even)
    odd_count = count_nb - even_count

    analysis = { "count": count_nb, "sum": sum_nb, "average": average_nb, 
    "minimum": minimum_nb, "maximum": maximum_nb, "even_count": even_count,
    "odd_count": odd_count}

    return analysis
   
    if not numbers:
        return None  
   





def display_analysis(analysis):

    if not analysis:
        return None

    print("\nAnalysis Results:")
    print("-" * 20)
    for key, value in analysis.items():
        print((f"{key}:{value}"))
        




def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()