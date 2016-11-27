from profile import Profile
from stock import Stock
from graph import Graph
from watchlist import Watchlist


# Methods for each available command
def stockPriceCmd():
    print("Stock price for:", end=" ")
    ticker = input()
    lookedup_stock = Stock(ticker)
    print(lookedup_stock.getPrice())


def watchlistCmd():
    print("1) View watchlist\n2) Add stock to watchlist\n3) Remove stock from watchlist\n")
    print(">", end=" ")
    user_input = input()

    # Displays watchlist
    if user_input == "1":
        user_watchlist.printWatchlist()

    # Adds a stock to the watchlist
    elif user_input == "2":
        print(user_watchlist.addToWatchlist())

    # Removes a stock from the watchlist
    elif user_input == "3":
        print(user_watchlist.removeFromWatchlist())


def portfolioCmd():
    print("1) Portfolio details\n2) Buy stock\n3) Sell stock")
    print(">", end=" ")
    user_input = input()

    if user_input == "1":
        print("Unimplemented")
    elif user_input == "2":
        print("Unimplemented")
    elif user_input == "3":
        print("Unimplemented")


def graphCmd():
    print("Graph stock:", end=" ")
    ticker = input()
    g = Graph(ticker)
    g.start()


def createAccount():
    profile.createUser()

def login():
    profile.login()


# Exits application
# Changes global variable running
# Potentially add code for saving/backing up data here
def exit():
    global running
    running = False
    print("Goodbye")


# starts application and creates loop until exit command
def start():
    global running

    running = True
    print("\n\n\nWelcome to the Rueb Stock Trader\nType the corresponding number to do a command or type 'exit' to exit")

    while running:
        print("\n1) Look up price\n2) Watchlist options\n5) Login\n6) Create Account")
        print(">", end=" ")
        user_input = input()

        # Look up price
        if user_input == "1":
            stockPriceCmd()

        # watch list
        elif user_input == "2":
            watchlistCmd()

        # portfolio
        elif user_input == "3":
            portfolioCmd()

        # graph
        elif user_input == "4":
            graphCmd()

        # login
        elif user_input == "5":
            login()

        # create account
        elif user_input == "6":
            createAccount()

        # exit
        elif user_input == "exit":
            exit()

        # bad input
        else:
            print("That is an invalid command.")

# Creates a profile object
profile = Profile()
# This will be edited when profiles are included.
user_watchlist = Watchlist()
# start application
start()
