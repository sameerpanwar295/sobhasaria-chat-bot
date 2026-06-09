print("Welcome to the our  Cinema")
print("You know")
print("For the students we have best discout for next 4 days")
STANDARD_PRICE = 10
STUDENT_PRICE = 8

try:
    num_tickets = int(input("How many tickets would you like to buy? "))
    if num_tickets <= 0:
        print("Please enter a valid number of tickets greater than 0.")
except ValueError:
    print("Invalid input. Please enter a whole number.")

student_status = input("Are you a student? (Yes/No or N): ").strip().lower()

if student_status in ['yes', 'y']:
    ticket_price = STUDENT_PRICE
    is_student = True
else:
    ticket_price = STANDARD_PRICE
    is_student = False

total_cost = num_tickets * ticket_price


print(" RECEIPT ")
    

print(f"Ticket Type:  {'Student ($8/each)' if is_student else 'Standard ($10/each)'}")

print(f"Quantity:     {num_tickets}")
    

print(f"TOTAL COST:   ${total_cost:.2f}")
    

print("Thank you for your purchase! Enjoy the movie")
