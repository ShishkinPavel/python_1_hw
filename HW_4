from typing import List, Set, Dict, Optional


class Transaction:
    def __init__(self, buyer_id: str,
                 seller_id: str,
                 amount: int,
                 price: int) -> None:
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.amount = amount
        self.price = price


class Order:
    def __init__(self, trader_id: str,
                 amount: int,
                 price: int) -> None:
        self.trader_id = trader_id
        self.amount = amount
        self.price = price


class Stock:
    def __init__(self) -> None:
        self.history: List[Transaction] = []
        self.buyers: List[Order] = []
        self.sellers: List[Order] = []


StockExchange = Dict[str, Stock]


def add_new_stock(stock_exchange: StockExchange, ticker_symbol: str) -> bool:
    if ticker_symbol in stock_exchange:
        return False
    else:
        stock_exchange[ticker_symbol] = Stock()
        return True


def deal(stock_exchange: StockExchange, ticker_symbol: str) -> None:
    s_e = stock_exchange[ticker_symbol]
    len_sellers = len(s_e.sellers)
    len_buyers = len(s_e.buyers)

    if len_sellers > 0:

        for i in range(len_buyers - 1, -1, -1):

            for j in range(len_sellers - 1, -1, -1):
                seller = s_e.sellers[j]
                buyer = s_e.buyers[i]

                if buyer.price >= seller.price \
                        and seller.amount > 0 \
                        and buyer.amount > 0:

                    if seller.amount > buyer.amount:
                        s_e.history.append(Transaction
                                           (buyer.trader_id,
                                            seller.trader_id,
                                            buyer.amount,
                                            buyer.price))
                        seller.amount -= buyer.amount
                        buyer.amount = 0

                    else:
                        s_e.history.append(Transaction
                                           (buyer.trader_id,
                                            seller.trader_id,
                                            seller.amount,
                                            buyer.price))
                        buyer.amount -= seller.amount
                        seller.amount = 0

    for i in range(len_buyers - 1, -1, -1):
        if s_e.buyers[i].amount == 0:
            del s_e.buyers[s_e.buyers.index(s_e.buyers[i])]

    for i in range(len_sellers - 1, -1, -1):
        if s_e.sellers[i].amount == 0:
            del s_e.sellers[s_e.sellers.index(s_e.sellers[i])]


def buy_sell(stock_exchange: StockExchange, ticker_symbol: str,
             trader_id: str, amount: int, price: int, sell: bool) -> None:
    add_new_stock(stock_exchange, ticker_symbol)
    s_e = stock_exchange[ticker_symbol]
    len_buyers = len(s_e.buyers)
    len_sellers = len(s_e.sellers)

    if len_buyers == 0 and sell is False:
        s_e.buyers.append(Order(trader_id, amount, price))
    elif len_sellers == 0 and sell is True:
        s_e.sellers.append(Order(trader_id, amount, price))

    else:
        if sell is False:
            x = s_e.buyers
            ranged = len_buyers
        else:
            x = s_e.sellers
            ranged = len_sellers

        for index in range(ranged):
            if sell is False and x[index].price >= price:
                x.insert(index, Order(trader_id, amount, price))
                break
            if sell is True and x[index].price <= price:
                x.insert(index, Order(trader_id, amount, price))
                break
            if index == ranged - 1:
                x.append(Order(trader_id, amount, price))

    len_sellers = len(s_e.sellers)
    len_buyers = len(s_e.buyers)
    if (len_sellers > 0 and sell is False) \
            or (len_buyers > 0 and sell is True):
        deal(stock_exchange, ticker_symbol)


def place_buy_order(stock_exchange: StockExchange, ticker_symbol: str,
                    trader_id: str, amount: int, price: int) -> None:
    buy_sell(stock_exchange, ticker_symbol, trader_id, amount, price, False)


def place_sell_order(stock_exchange: StockExchange, ticker_symbol: str,
                     trader_id: str, amount: int, price: int) -> None:
    buy_sell(stock_exchange, ticker_symbol, trader_id, amount, price, True)


def stock_owned(stock_exchange: StockExchange, trader_id: str) \
        -> Dict[str, int]:
    s_e = stock_exchange
    dict_result = {}

    for i in s_e.keys():

        actual_amount = 0
        for a in range(len(s_e[i].history)):

            if trader_id == s_e[i].history[a].seller_id:
                actual_amount -= s_e[i].history[a].amount

            if trader_id == s_e[i].history[a].buyer_id:
                actual_amount += s_e[i].history[a].amount

            if actual_amount != 0:
                dict_result[i] = actual_amount

    return dict_result


def all_traders(stock_exchange: StockExchange) -> Set[str]:
    s_e = stock_exchange
    result = []

    for i in s_e.keys():

        for a in range(len(s_e[i].history)):
            result.append(s_e[i].history[a].seller_id)
            result.append(s_e[i].history[a].buyer_id)

        for b in range(len(s_e[i].sellers)):
            result.append(s_e[i].sellers[b].trader_id)

        for c in range(len(s_e[i].buyers)):
            result.append(s_e[i].buyers[c].trader_id)

    return set(result)


def transactions_by_amount(stock_exchange: StockExchange,
                           ticker_symbol: str) -> List[Transaction]:
    s_e = stock_exchange[ticker_symbol]
    result_tr: List[Transaction] = list(s_e.history)
    result_tr.sort(key=lambda x: x.amount, reverse=True)
    return result_tr


def process_batch_commands(stock_exchange: StockExchange,
                           commands: List[str]) -> Optional[int]:
    num = 0
    for i in commands:

        check_add = check = False
        if 'ADD ' in i and len(i.split()) == 2:
            new_stock = i.split()
            if len(new_stock) == 2 \
                    and new_stock[0] == 'ADD':
                if add_new_stock(stock_exchange, new_stock[1]) is False:
                    return num
                num += 1
                check_add = True

        list_of_i = i.split(':', maxsplit=1)
        if len(list_of_i) == 2 \
                and len(list_of_i[0]) > 0 \
                and check_add is False:
            action = list_of_i[1].split(' ')
            if len(action) == 6 \
                    and action[0] == '' \
                    and action[2].isdigit() \
                    and action[5].isdigit():
                check = True

            if check is True \
                    and action[1] == 'BUY' \
                    and action[4] == 'AT':
                place_buy_order(stock_exchange, action[3], list_of_i[0],
                                int(action[2]), int(action[5]))

            elif check is True \
                    and action[1] == 'SELL' \
                    and action[4] == 'AT':
                place_sell_order(stock_exchange, action[3], list_of_i[0],
                                 int(action[2]), int(action[5]))

            else:
                return num
            num += 1
        if check == check_add is False:
            return num
    return None


def print_stock(stock_exchange: StockExchange, ticker_symbol: str) -> None:
    assert ticker_symbol in stock_exchange

    stock = stock_exchange[ticker_symbol]
    print(f"=== {ticker_symbol} ===")
    print("     price amount  trader")
    print("  -------------------------------------------------------------")

    for order in stock.sellers:
        print(f"    {order.price:6d} {order.amount:6d} ({order.trader_id})")
    print("  -------------------------------------------------------------")

    for order in reversed(stock.buyers):
        print(f"    {order.price:6d} {order.amount:6d} ({order.trader_id})")
    print("  -------------------------------------------------------------")

    for transaction in stock.history:
        print(f"    {transaction.seller_id} -> {transaction.buyer_id}: "
              f"{transaction.amount} at {transaction.price}")


def check_order(order: Order, trader_id: str, amount: int, price: int) -> None:
    assert order.trader_id == trader_id
    assert order.amount == amount
    assert order.price == price


def check_transaction(transaction: Transaction, buyer_id: str, seller_id: str,
                      amount: int, price: int) -> None:
    assert transaction.buyer_id == buyer_id
    assert transaction.seller_id == seller_id
    assert transaction.amount == amount
    assert transaction.price == price


def test_scenario1() -> None:
    duckburg_se: StockExchange = {}
    add_new_stock(duckburg_se, 'ACME')

    place_sell_order(duckburg_se, 'ACME', 'Strýček Skrblík', 50, 120)
    place_buy_order(duckburg_se, 'ACME', 'Rampa McKvák', 100, 90)
    place_sell_order(duckburg_se, 'ACME', 'Hamoun Držgrešle', 70, 110)
    place_sell_order(duckburg_se, 'ACME', 'Kačer Donald', 20, 120)

    acme = duckburg_se['ACME']
    assert acme.history == []

    assert len(acme.buyers) == 1
    check_order(acme.buyers[0], 'Rampa McKvák', 100, 90)

    assert len(acme.sellers) == 3
    check_order(acme.sellers[0], 'Kačer Donald', 20, 120)
    check_order(acme.sellers[1], 'Strýček Skrblík', 50, 120)
    check_order(acme.sellers[2], 'Hamoun Držgrešle', 70, 110)

    place_buy_order(duckburg_se, 'ACME', 'Paní Čvachtová', 90, 110)

    assert len(acme.history) == 1
    check_transaction(acme.history[0], 'Paní Čvachtová', 'Hamoun Držgrešle',
                      70, 110)

    assert len(acme.buyers) == 2
    check_order(acme.buyers[0], 'Rampa McKvák', 100, 90)
    check_order(acme.buyers[1], 'Paní Čvachtová', 20, 110)

    assert len(acme.sellers) == 2
    check_order(acme.sellers[0], 'Kačer Donald', 20, 120)
    check_order(acme.sellers[1], 'Strýček Skrblík', 50, 120)

    place_buy_order(duckburg_se, 'ACME', 'Magika von Čáry', 60, 130)

    assert len(acme.history) == 3
    check_transaction(acme.history[0], 'Paní Čvachtová', 'Hamoun Držgrešle',
                      70, 110)
    check_transaction(acme.history[1], 'Magika von Čáry', 'Strýček Skrblík',
                      50, 130)
    check_transaction(acme.history[2], 'Magika von Čáry', 'Kačer Donald',
                      10, 130)

    assert len(acme.buyers) == 2
    check_order(acme.buyers[0], 'Rampa McKvák', 100, 90)
    check_order(acme.buyers[1], 'Paní Čvachtová', 20, 110)

    assert len(acme.sellers) == 1
    check_order(acme.sellers[0], 'Kačer Donald', 10, 120)

    for name, amount in [
        ('Kačer Donald', -10),
        ('Strýček Skrblík', -50),
        ('Hamoun Držgrešle', -70),
        ('Paní Čvachtová', 70),
        ('Magika von Čáry', 60),
    ]:
        assert stock_owned(duckburg_se, name) == {'ACME': amount}

    assert stock_owned(duckburg_se, 'Rampa McKvák') == {}
    assert stock_owned(duckburg_se, 'Šikula') == {}

    assert all_traders(duckburg_se) == {
        'Kačer Donald',
        'Strýček Skrblík',
        'Hamoun Držgrešle',
        'Paní Čvachtová',
        'Magika von Čáry',
        'Rampa McKvák',
    }

    all_transactions = transactions_by_amount(duckburg_se, 'ACME')
    check_transaction(all_transactions[0],
                      'Paní Čvachtová', 'Hamoun Držgrešle',
                      70, 110)
    check_transaction(all_transactions[1],
                      'Magika von Čáry', 'Strýček Skrblík',
                      50, 130)
    check_transaction(all_transactions[2],
                      'Magika von Čáry', 'Kačer Donald',
                      10, 130)


def test_scenario2() -> None:
    duckburg_se: StockExchange = {}
    result = process_batch_commands(duckburg_se, [
        "ADD ACME",
        "Uncle Scrooge: SELL 50 ACME AT 120",
        "Launchpad McQuack: BUY 100 ACME AT 90",
        "Flintheart Glomgold: SELL 70 ACME AT 110",
        "Donald Duck: SELL 20 ACME AT 120",
        "Mrs. Beakley: BUY 90 ACME AT 110",
        "Magica De Spell: BUY 60 ACME AT 130",
    ])
    assert result is None
    assert 'ACME' in duckburg_se
    acme = duckburg_se['ACME']

    assert len(acme.history) == 3
    check_transaction(acme.history[0], 'Mrs. Beakley', 'Flintheart Glomgold',
                      70, 110)
    check_transaction(acme.history[1], 'Magica De Spell', 'Uncle Scrooge',
                      50, 130)
    check_transaction(acme.history[2], 'Magica De Spell', 'Donald Duck',
                      10, 130)

    assert len(acme.buyers) == 2
    check_order(acme.buyers[0], 'Launchpad McQuack', 100, 90)
    check_order(acme.buyers[1], 'Mrs. Beakley', 20, 110)

    assert len(acme.sellers) == 1
    check_order(acme.sellers[0], 'Donald Duck', 10, 120)


def test_scenario3() -> None:
    nnyse: StockExchange = {}
    result = process_batch_commands(nnyse, [
        "ADD Momcorp",
        "Mom: SELL 1000 Momcorp AT 5000",
        "Walt: BUY 10 Momcorp AT 5600",
        "Larry: BUY 7 Momcorp AT 5000",
        "Igner: BUY 1 Momcorp AT 4000",
        "ADD PlanetExpress",
        "Mom: BUY 1000 PlanetExpress AT 100",
        "Zoidberg: BUY 1000 PlanetExpress AT 199",
        "Professor Farnsworth: SELL 1020 PlanetExpress AT 100",
        "Bender B. Rodriguez: BUY 20 Momcorp AT 100",
        "Fry: INVALID COMMAND",
        "Leela: BUY 500 PlanetExpress AT 150",
    ])

    assert result == 10

    assert set(nnyse) == {'Momcorp', 'PlanetExpress'}

    momcorp = nnyse['Momcorp']
    pe = nnyse['PlanetExpress']

    assert len(momcorp.history) == 2
    check_transaction(momcorp.history[0], 'Walt', 'Mom', 10, 5600)
    check_transaction(momcorp.history[1], 'Larry', 'Mom', 7, 5000)

    assert len(momcorp.sellers) == 1
    check_order(momcorp.sellers[0], 'Mom', 983, 5000)

    assert len(momcorp.buyers) == 2
    check_order(momcorp.buyers[0], 'Bender B. Rodriguez', 20, 100)
    check_order(momcorp.buyers[1], 'Igner', 1, 4000)

    assert len(pe.history) == 2
    check_transaction(pe.history[0], 'Zoidberg', 'Professor Farnsworth',
                      1000, 199)
    check_transaction(pe.history[1], 'Mom', 'Professor Farnsworth',
                      20, 100)

    assert pe.sellers == []
    assert len(pe.buyers) == 1
    check_order(pe.buyers[0], 'Mom', 980, 100)


if __name__ == '__main__':
    test_scenario1()
    test_scenario2()
    test_scenario3()
