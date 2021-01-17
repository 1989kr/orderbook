from src.order import Order
from orderBook import OrderBook


#exemplary standard input
order_list=[{"type": "Iceberg", "order": {"direction": "Sell", "id": 1, "price": 100, "quantity": 200,
"peak": 100}},
{"type": "Iceberg", "order": {"direction": "Sell", "id": 2, "price": 100, "quantity": 300,
"peak": 100}},
{"type": "Iceberg", "order": {"direction": "Sell", "id": 3, "price": 100, "quantity": 200,
"peak": 100}},
{"type": "Iceberg", "order": {"direction": "Buy", "id": 4, "price": 100, "quantity": 500,
"peak": 100}}]
order_list_revised=[Order("S" if ord["order"]["direction"]=='Sell' else "B",ord["order"]["id"],ord["order"]["price"],ord["order"]["quantity"], ord["order"]["peak"] if ord["type"]=="Iceberg" else None ) for ord in order_list]     

od_book=OrderBook()    
for ord in order_list_revised:
    od_book.process_order(ord)
