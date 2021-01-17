import sys
from src.priceTree import PriceTree
from src.ptreeIterator import ComplexIterator


class OrderBook(object):
    def __init__(self):
        self.bids = PriceTree('Bids')
        self.asks = PriceTree('Asks')

    def process_order(self, curr_order):
        """
        Generic method to process a Bid or Ask order
        :param curr_order:
        """
        opposite_tree = self.bids if not curr_order.is_bid else self.asks
        # we are assuming thar order can not be modified or canceled
        # Try first to match this order with the opposite tree
        trades = opposite_tree.match_price_order(curr_order)
        # If there is remaining order size add it to the matching tree
        if curr_order.peak_size is not 0:
            curr_order.restore_peak_size()
            matching_tree = self.bids if curr_order.is_bid else self.asks
            matching_tree.insert_price_order(curr_order)
        # First print all trades
        for order in trades:
            order.print_trade_result(curr_order.id)
        curr_order.trade_size = 0
        # And then the LOB state
        self.print_book()
        return trades

    def print_book(self):        
        bids_it = ComplexIterator(self.bids.tree.values(reverse=True))
        asks_it = ComplexIterator(self.asks.tree.values())
        
        book_dict={"buyOrders" : [],"sellOrders" : []}
        
        while bids_it.hasnext():
            current_bid=next(bids_it)
            book_dict["buyOrders"].append({'id': current_bid.id, 'price' : current_bid.price, 'quantity' :current_bid.peak_size})
            
        while asks_it.hasnext():
            current_ask=next(asks_it)
            book_dict["sellOrders"].append({'id': current_ask.id, 'price' : current_ask.price, 'quantity' :current_ask.peak_size})
        

        print(book_dict)    
        

if __name__=='__main__':
    pass
    # from orderbook.src.common.order import Order
    
    # order_list=[{"type": "Iceberg", "order": {"direction": "Sell", "id": 1, "price": 100, "quantity": 200,
    # "peak": 100}},
    # {"type": "Iceberg", "order": {"direction": "Sell", "id": 2, "price": 100, "quantity": 300,
    # "peak": 100}},
    # {"type": "Iceberg", "order": {"direction": "Sell", "id": 3, "price": 100, "quantity": 200,
    # "peak": 100}},
    # {"type": "Iceberg", "order": {"direction": "Buy", "id": 4, "price": 100, "quantity": 500,
    # "peak": 100}}]
    # order_list_revised=[Order("S" if ord["order"]["direction"]=='Sell' else "B",ord["order"]["id"],ord["order"]["price"],ord["order"]["quantity"], ord["order"]["peak"] if ord["type"]=="Iceberg" else None ) for ord in order_list]     
    
    # od_book=OrderBook()    
    # for ord in order_list_revised:
    #     od_book.process_order(ord)
