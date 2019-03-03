from .item_dto import ItemDTO


class CakeDTO:
    name = ''
    description = ''
    items = []

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def add_items(self, items_request):
        for it in items_request:
            item_dto = ItemDTO(it['ingredient'], it['amount'])
            self.items.append(item_dto)

