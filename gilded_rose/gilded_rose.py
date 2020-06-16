class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.maxQuality = 50
    
    def decrement_quality(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros" and item.quality > 0:
            item.quality = item.quality - 1


    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self.decrement_quality(item)
            else:
                if item.quality < self.maxQuality:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < self.maxQuality:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < self.maxQuality:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        self.decrement_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < self.maxQuality:
                        item.quality = item.quality + 1
