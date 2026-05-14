
STOCK_PRICES = {
    "AAPL":  180.00,
    "TSLA":  250.00,
    "GOOGL": 140.00,
    "AMZN":  185.00,
    "MSFT":  415.00,
    "NVDA":  875.00,
    "META":  505.00,
    "NFLX":  625.00,
    "AMD":   170.00,
    "INTC":   35.00,
}

COMPANY_NAMES = {
    "AAPL": "Apple Inc.",      "TSLA": "Tesla Inc.",
    "GOOGL": "Alphabet",       "AMZN": "Amazon",
    "MSFT": "Microsoft",       "NVDA": "NVIDIA",
    "META": "Meta Platforms",  "NFLX": "Netflix",
    "AMD":  "AMD",             "INTC": "Intel",
}


def show_available_stocks():
    print("\n" + "=" * 45)
    print("  AVAILABLE STOCKS")
    print("=" * 45)
    print(f"  {'Ticker':<8}  {'Company':<22}  {'Price':>8}")
    print("-" * 45)
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<8}  {COMPANY_NAMES[ticker]:<22}  ${price:>7.2f}")
    print("=" * 45)

def get_portfolio():
    portfolio = []
    print("\nEnter your stock holdings.")
    print("Type 'DONE' when finished, 'LIST' to see available stocks.\n")

    while True:
        raw = input("Stock ticker (or DONE): ").strip().upper()

        if raw == "DONE":
            if not portfolio:
                print("  No stocks added yet. Add at least one.\n")
                continue
            break

        if raw == "LIST":
            show_available_stocks()
            continue

        if raw not in STOCK_PRICES:
            print(f"  '{raw}' not found. Type LIST to see valid tickers.\n")
            continue

        # Get quantity
        while True:
            qty_input = input(f"  Quantity of {raw}: ").strip()
            if qty_input.isdigit() and int(qty_input) > 0:
                qty = int(qty_input)
                break
            print("  Please enter a positive whole number.")

        # Calculate value for this holding
        price = STOCK_PRICES[raw]
        value = price * qty                        # Basic arithmetic

        # If ticker already added, merge quantities
        existing = next((h for h in portfolio if h["ticker"] == raw), None)
        if existing:
            existing["qty"]   += qty
            existing["value"] += value
            print(f"  Updated {raw}: total {existing['qty']} shares = ${existing['value']:,.2f}\n")
        else:
            portfolio.append({"ticker": raw, "qty": qty, "price": price, "value": value})
            print(f"  Added {raw}: {qty} x ${price:.2f} = ${value:,.2f}\n")

    return portfolio

def display_summary(portfolio):
    total = sum(h["value"] for h in portfolio)    # Sum all holding values

    print("\n" + "=" * 55)
    print("  PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"  {'Ticker':<8}  {'Qty':>6}  {'Price':>10}  {'Value':>12}")
    print("-" * 55)
    for h in portfolio:
        print(f"  {h['ticker']:<8}  {h['qty']:>6}  ${h['price']:>9.2f}  ${h['value']:>11,.2f}")
    print("=" * 55)
    print(f"  {'TOTAL INVESTMENT':<30}  ${total:>11,.2f}")
    print("=" * 55)

def main():
    print("\n=========================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("=========================================")

    show_available_stocks()
    portfolio = get_portfolio()
    display_summary(portfolio)


if __name__ == "__main__":
    main()
