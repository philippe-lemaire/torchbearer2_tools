class Character:
    def init(self, name, class_):
        self.name = name
        self.class_ = class_
        class_to_stock_dict = {
            "Burglar": "Halfling",
            "Magician": "Human",
            "Outcast": "Dwarf",
            "Ranger": "Elf",
            "Theurge": "Human",
            "Warrior": "Human",
        }
        self.stock = class_to_stock_dict[self.class_]
