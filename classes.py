# Prototype for positions data
class PortfolioPosition:
    # Constructor
    def __init__(self, ticker):
        # Set ticker symbol
        self.ticker = ticker
        # Get desired position percentage
        self.desired_perc = float(input("What percentage of the portfolio should this constitute? "))
        # Actual value in portfolio
        self.actual = float(input("What is the value of the position currently? "))
        # Actual percent of portfolio
        self.actual_perc = 0
        # Change required
        self.change = 0
