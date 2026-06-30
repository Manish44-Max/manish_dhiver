import csv

def main():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 330,
        "AMZN": 145,
        "META": 350,
        "NVDA": 480,
        "JPM": 155,
        "V": 270,
        "JNJ": 160
    }
    
    print("=" * 50)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    
    print("\nAvailable stocks and their prices:")
    print("-" * 35)
    for stock, price in stock_prices.items():
        print(f"{stock:6} : ${price:.2f}")
    
    print("\n" + "-" * 50)
    print("Enter your stock holdings (type 'done' when finished)")
    print("-" * 50)
    
    portfolio = {}
    
    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock == 'DONE':
            break
        
        if stock not in stock_prices:
            print(f"Error: '{stock}' not found in available stocks. Please try again.")
            continue
        
        try:
            quantity = float(input(f"Enter quantity of {stock} shares: "))
            if quantity <= 0:
                print("Quantity must be positive. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity
        
        print(f"✓ Added {quantity} shares of {stock}")
    
    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return
    
    print("\n" + "=" * 50)
    print("YOUR PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<10} {'Quantity':<10} {'Price':<10} {'Value':<12}")
    print("-" * 50)
    
    total_investment = 0
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total_investment += value
        print(f"{stock:<10} {quantity:<10.2f} ${price:<9.2f} ${value:<11.2f}")
    
    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':<30} ${total_investment:,.2f}")
    print("=" * 50)
    
    print("\n" + "-" * 50)
    save_option = input("Would you like to save the results to a file? (y/n): ").lower().strip()
    
    if save_option == 'y':
        filename = input("Enter filename (default: portfolio_summary.txt): ").strip()
        if not filename:
            filename = "portfolio_summary.txt"
        
        if not filename.endswith(('.txt', '.csv')):
            filename += '.txt'
        
        save_to_file(portfolio, stock_prices, total_investment, filename)
    
    print("\nThank you for using the Stock Portfolio Tracker!")


def save_to_file(portfolio, stock_prices, total_investment, filename):
    try:
        if filename.endswith('.csv'):
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Stock', 'Quantity', 'Price', 'Value'])
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    value = quantity * price
                    writer.writerow([stock, quantity, price, value])
                writer.writerow([])
                writer.writerow(['TOTAL INVESTMENT', '', '', total_investment])
        else:
            with open(filename, 'w') as file:
                file.write("=" * 50 + "\n")
                file.write("STOCK PORTFOLIO SUMMARY\n")
                file.write("=" * 50 + "\n\n")
                file.write(f"{'Stock':<10} {'Quantity':<10} {'Price':<10} {'Value':<12}\n")
                file.write("-" * 50 + "\n")
                
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    value = quantity * price
                    file.write(f"{stock:<10} {quantity:<10.2f} ${price:<9.2f} ${value:<11.2f}\n")
                
                file.write("-" * 50 + "\n")
                file.write(f"{'TOTAL INVESTMENT':<30} ${total_investment:,.2f}\n")
                file.write("=" * 50)
        
        print(f"✓ Results saved to '{filename}'")
    except Exception as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":
    main()
