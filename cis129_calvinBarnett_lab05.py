# Calvin Barnett
# March 11
# Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"
 
# Step 2: Loop to run program again
while keep_going.lower() == "y":
    # Step 3: Code to set value of variables
    # code to set value of variable total_bottles
    # code to set value of variable total_payout
    # code to print the number of total bottles and total payout
        
    # getBottles code
    NBR_OF_DAYS = 7
    # Declare and initialize total_bottles, today_bottles, counter to 0
    total_bottles = 0
    today_bottles = 0
    counter = 1
    
    while counter <= NBR_OF_DAYS:
        # Display "Enter number of bottles returned for day #", counter, ":"
        print(f"Enter number of bottles for day #{counter}: ", end="")
        # Input today_bottles
        today_bottles = int(input())
        # total_bottles += today_bottles
        total_bottles = total_bottles + today_bottles
        # Increment counter
        counter += 1
    
    # calcPayout code
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE
    
    # printInfo code
    # Display "The total number of bottles collected is", total_bottles
    print(f"The total number of bottles collected is {total_bottles}")
    # Display "The total paid out is $", total_payout
    print(f"The total paid out is $ {total_payout:.2f}")
    
    # Display "Do you want to enter another week’s worth of data?"
    # Display "(Enter y or n)"
    print("Do you want to enter another week’s worth of data?")
    print("(Enter y or n)")
    # Input keep_going
    keep_going = input()
