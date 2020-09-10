from osrs_api import GrandExchange
from osrs_api import Item

all_items = Item.get_ids('')

for item in all_items:
    # Get the price of each item
    print(int(GrandExchange.item(item).price()))
