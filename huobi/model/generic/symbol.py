class Symbol:
    """
    The Huobi supported symbols.

    :member
        base_currency: The base currency in a trading symbol.
        quote_currency: The quote currency in a trading symbol.
        price_precision: The quote currency precision when quote price (decimal places).
        amount_precision: The base currency precision when quote amount (decimal places).
        symbol_partition: The trading section, possible values: [main，innovation，bifurcation].
        symbol: The symbol, like "btcusdt".
        state : trade status, maybe one in [online，offline,suspend]
        value_precision : value precision
        min_order_amt : minimum volume limit only used in limit-order and sell-market order
        max_order_amt : Maximum volume
        min_order_value : Minimum order amount
        leverage_ratio : Leverage ratio for symbol
    """

    def __init__(self):
        self.base_currency = ""
        self.quote_currency = ""
        self.price_precision = 0
        self.amount_precision = 0
        self.symbol_partition = ""
        self.symbol = ""
        self.state = ""
        self.value_precision = 0
        self.min_order_amt = ""
        self.max_order_amt = ""
        self.min_order_value = ""
        self.leverage_ratio = 0


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.base_currency, format_data + "Base Currency")
        PrintBasic.print_basic(self.quote_currency, format_data + "Quote Currency")
        PrintBasic.print_basic(self.price_precision, format_data + "Price Precision")
        PrintBasic.print_basic(self.amount_precision, format_data + "Amount Precision")
        PrintBasic.print_basic(self.symbol_partition, format_data + "Symbol Partition")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.state, format_data + "State")
        PrintBasic.print_basic(self.value_precision, format_data + "Value Precision")
        PrintBasic.print_basic(self.min_order_amt, format_data + "Min Order Amount")
        PrintBasic.print_basic(self.max_order_amt, format_data + "Max Order Amount")
        PrintBasic.print_basic(self.min_order_value, format_data + "Min Order Value")
        PrintBasic.print_basic(self.leverage_ratio, format_data + "Leverage Ratio")
