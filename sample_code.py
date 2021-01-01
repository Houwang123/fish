def fish(turn, credit, population, food, pool_level, food_price, fry_price, expand_price, *args, **kwargs):
    def calc_capacity(pool_level):
        return 100 * pool_level ** 2
    fry = 0
    if not turn:
        fry = 20
        credit = credit - fry * fry_price
    capacity = calc_capacity(pool_level)
    harvest = population ** 2 / capacity
    credit = credit + harvest
    feed = max([0, min([capacity * 1.3 - food, credit / food_price])])
    credit = credit - feed * food_price
    expand = 0
    if credit >= expand_price * calc_capacity(pool_level+1) * 1.5:
        expand = 1

    return [harvest, feed, fry, expand], [], {}