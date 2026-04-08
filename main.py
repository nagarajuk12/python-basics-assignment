'''Movie Theatre Booking System'''
total_bookings = 0
total_tickets_sold = 0
rejected_bookings = 0
remaining_seats = 0
THEATER_CAPACITY = 350

while True:
    number_of_tickets_required = int(input('Enter the number of tickets (0 to exit):'))
        
    if number_of_tickets_required == 0:
        print(f"Final Report: Total Bookings: {total_bookings}, Total Tickets Sold: {total_tickets_sold}, Rejected Bookings: {rejected_bookings}, Remaining Seats: {THEATER_CAPACITY - total_tickets_sold}")
        break
    if number_of_tickets_required < 0:
        #If the user enters a negative number of tickets, the program will prompt the user that the input is invalid and ask for a positive number of tickets. The total bookings and tickets sold will not be updated, and the remaining seats will remain the same.
        print("Invalid input. Please enter a positive number of tickets.")
        continue
    
    if number_of_tickets_required > (THEATER_CAPACITY - total_tickets_sold):
        # If the number of tickets required exceeds the remaining seats in the theater, the program will prompt the user that there are not enough seats available and ask for a smaller number of tickets. The total bookings and tickets sold will not be updated, and the remaining seats will remain the same.
        print("Not enough seats available. Please enter a smaller number of tickets.")
        continue
        
    ages = []
    if number_of_tickets_required <= 15:
        # The program will ask for the age of each person in the booking. If any person is 12 years old or younger, the booking will be rejected due to age restrictions. If all persons are older than 12, the booking will be confirmed, and the total bookings and tickets sold will be updated accordingly.
        for value in range(number_of_tickets_required):
           person_age = int(input("Enter the age of the person: "))
           ages.append(person_age)
        
        for age in ages:
            if age <= 12:
                # If any person is 12 years old or younger, the booking will be rejected due to age restrictions.  The total bookings and tickets sold will not be updated, and the remaining seats will remain the same.
                print('BOOKING REJECTED - Age restriction')
                rejected_bookings += 1
                total_tickets_sold += 0
                total_bookings += 0
                remaining_seats += 0
                break
            else:
                # If all persons are older than 12, the booking will be confirmed, and the total bookings and tickets sold will be updated accordingly.
                total_bookings += 1
                total_tickets_sold += number_of_tickets_required
                remaining_seats = THEATER_CAPACITY - total_tickets_sold
                print(f'BOOKING CONFIRMED - {total_bookings} tickets')
                break
    elif(number_of_tickets_required > 15):
        print("For each booking: 1-15 tickets only")
        break