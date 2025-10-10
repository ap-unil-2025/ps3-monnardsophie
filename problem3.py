def get_numbers_from_user():
    numbers = []
    x = 1
    while x == 1:
        a=input("Type a number")       

        if a == "done":

            x = x-1
        else :
            try : 
                a_float = float(a)
                numbers.append(a_float)

            except ValueError :
                print("Please enter a valid number")

            x=1
            
    return numbers
   

def analyze_numbers(numbers):

    if not numbers :
        return None 

    count = len(numbers)
    sum_var = sum(numbers)
    average_var = sum_var/count 
    min_var = min(numbers) 
    max_var = max(numbers) 
    list_even =[]
    for i in numbers : 
        if i%2 == 0 :
            list_even.append(i)
    even_count = len(list_even)
    odd_count = count - even_count

    analysis = {"count":count, "sum":sum_var, "average":average_var, 
        "minimum": min_var, "maximum": max_var, "even count":even_count, 
        "odd count" : odd_count
        }
    return analysis
  

def display_analysis(analysis):
    

   
    if not analysis:
        return None

    print("\nAnalysis Results:")
    print("-" * 20)
    for key, value in analysis.items():
        print((f"{key}: {value}"))



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