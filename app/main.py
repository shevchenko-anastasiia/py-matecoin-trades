import json
import decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as f:
        trades_data = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for trade in trades_data:
        if trade["bought"] is not None:
            earned_money += decimal.Decimal(trade["bought"])\
                * decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += decimal.Decimal(trade["sold"])\
                * decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
