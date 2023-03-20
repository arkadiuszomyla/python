class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    #jeżeli ta funcja jest zdefiniowana można wywoływać instancje tak jakby były funkcjami
    def __call__(self, item):
        self.list_of_items.append(item)


mem = MemoryClass([])
print("List of items in memory", mem.list_of_items)

mem.list_of_items.append("but sugar")
print("List of items in memory", mem.list_of_items)

#bez __call__
print('This class is callable:', callable(MemoryClass)) #True
print('This class is callable:', callable(mem))         #False

#po dodaniu __call__
mem('buy milk')

print("List of items in memory", mem.list_of_items)