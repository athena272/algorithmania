def calc_hash(item, item_cout):
    hash = 0
    for c in item:
        hash += ord(c)
    
    return hash % item_cout   