from collections import OrderedDict
if __name__=="__main__":
    n = int(input())
    if n > 0 and n <= 100:
        item_list = OrderedDict()
        for _ in range(n):
            item = input()
            *name, price = item.rstrip().split()
            if ' '.join(name) in item_list.keys():
                item_list[' '.join(name)] = item_list.get(' '.join(name)) + int(price)
                continue
            item_list[' '.join(name)] = int(price)
        for x, y in item_list.items():
            print(x, y)