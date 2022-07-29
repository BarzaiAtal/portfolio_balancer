
# Main function
def main():
    # Get the number of portfolios
    port_count = int(input("How many funds in the portfolio? "))
    print()

    # dictionary to hold funds
    funds = {}  # Funds and their desired percentages
    actual_position_value = {}  # Dollar value of funds
    actual_percent = {} # Percent value derived from fund values vs total value of portfolio
    fund_sells = [] # Holds funds to sell
    fund_buys = []  # Holds funds to buy
    funds_correct = []  # Holds funds to... hold.

    # start getting fund info and asigning
    count_1 = 0 # Count for control
    # Control loop to add keys and values to both dicts
    while count_1 < port_count:
        # Get fund names
        fund_name = str(input("What is the fund ticker symbol? ")).upper()
        # Get desired percentage
        fund_percentage = (float(input("What percent of you portfolio should it hold? "))/100)
        # Append to funds dicts
        print() # Spacer
        # Create entries for ticker symbols as entered
        funds[fund_name] = (fund_percentage)
        # Assign symbols to secondary dict with initial value set to 0
        actual_position_value[fund_name] = 0
        # Iterate control count
        count_1 += 1        

    # Count to control actual percentage input
    count_2 = 0
    # Value to hold total value of the account
    account_value = 0
    # Control loop to add values to second dict
    while count_2 < port_count:
        # Get key name
        for key in funds.keys():
            # Get percentages
            actual_hold = float(input("What is the current dollar value of " + key + " in your portfolio? $"))
            # Running total to get account value
            account_value += actual_hold
            # Assign actual value to correct key in second dict
            actual_position_value[key] = actual_hold
            # Iterate control count
            count_2 += 1
            
        #assign actual values
        # Work on each value in the dict
        for key in actual_position_value:
            # GEt the actual percentage by dividing the total value of the account into the fund's value
            actual_percent[key] = actual_position_value[key]/account_value

    # Calculate actual account percentages
    sell_count = 0  # Count the number of "sell" positions
    buy_count = 0   # Count the number of "buy" positions
    hold_count = 0  # Count the number of "hold" positions

    # Check through the position values, comparing to desired percentage, then report to the user the appropriate action.
    for key in actual_position_value.keys():
        # Find fund percentage differences
        fund_difference = (funds[key]) - actual_percent[key]
        # What to do if funds need buying
        if fund_difference > 0:
            # Build string, formatting for the proper number of decimals
            buy_entry = ("Buy $" + "{:.2f}".format((fund_difference)*account_value) + " of " + key + ".")
            # Add string to list
            fund_buys.append(buy_entry)
            # Iterate control count
            buy_count += 1
        # What to do if funds need selling.
        elif fund_difference < 0:
            # Build string, formatting for the proper number of decimals
            sell_entry = ("Sell $" + "{:.2f}".format(((fund_difference*-1))*account_value) + " of " + key + ".")
            # Add string to list
            fund_sells.append(sell_entry)
            # Iterate control count
            sell_count += 1
        # If it doesn't need buying or selling
        else:
            # Build string
            hold_entry = ("The value of " +key+ " is correct. Hold.")
            # Add string to list
            funds_correct.append(hold_entry)
            # Iterate control count
            hold_count +=1

    # Return results
    # Holds first
    for i in funds_correct:
        print() # Spacer for fromatting
        print(i)    # Entry
    print() # Spacer
    # Then Sells
    for i in fund_sells:
        print(i) # Entry
    print() # Spacer for fromatting
    # Then buys
    for i in fund_buys:
        print(i) # Entry
    print() # Spacer for formatting

# Run main function
if __name__ == "__main__":
    main()