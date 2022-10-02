# Import class
from classes import *

# Main function
def main():
    # Lists to hold positions
    positions = []  # Portfolio positions
    holds = []      # Positions to hold
    sells = []      # Positions to sell
    buys = []       # Positions to buy
    # Holds portfolio value
    value = 0.00
    # Control number
    control = int(input("How many positions in the portfolio? "))
    print()
    
    # counter
    count = 0
    # Build portfolio positions
    while count < control:
        # Start getting positions
        positions.append(PortfolioPosition(str(input("Enter a ticker symbol: ")).upper()))
        value = value + (positions[count].actual) 
        count += 1
        print()

    # Reset count
    count = 0
    # Calculate and assign actual percentages
    while count < control:
        # access position value and calculate percentage
        positions[count].actual_perc = (positions[count].actual / value) * 100
        count += 1

    # Reset count
    count = 0
    # Calculate change of position
    while count < control:
        positions[count].change = ((positions[count].desired_perc - positions[count].actual_perc)/100) * value
        count += 1

    # Reset count
    count = 0
    # Assign positions based on the needed change
    while count < len(positions):
        # In case the value is already correct
        if positions[count].change == 0:
            holds.append(positions[count].ticker)
            count +=1
        # In case buying is needed
        elif positions[count].change > 0:
            buys.append(positions[count].ticker)
            count += 1
        # In case selling is needed
        else:
            sells.append(positions[count].ticker)
            positions[count].change = (positions[count].change)
            count +=1

    # Reset count
    count =0
    # Begin outputting return to user
    print("Total portfolio value: $" + "{:.2f}".format(value))
    print() # Formatting
    
    # Print positions to hold
    if len(holds) > 0:
        print("Hold the following positions: ")
        while count < len(holds):
            print(holds[count])
            count += 1
    print() # Formatting

    # Print positions to sell
    for i in sells:             # Check positions in items in the 'buys' list
        for j in positions:     # Check tickers in objects
            if j.ticker == i:   # Find matches
                k = j.ticker    # Set value equal to a variable for printing
                print("Sell $" + "{:.2f}".format(j.change * -1) + " of " + k + ".")     # Print output
    print() # Formatting
   
    # Print positions to buy
    for i in buys:              # Check positions in items in the 'buys' list
        for j in positions:     # Check tickers in objects
            if j.ticker == i:   # Find matches
                k = j.ticker    # Set value equal to a variable for printing
                print("Buy $" + "{:.2f}".format(j.change) + " of " + k + ".")   # Print output
    print() # Formatting

if __name__ == "__main__":
    main()