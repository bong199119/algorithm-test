def solution(prices):
    answer = []
    dict_prices_idx = {}


    for idx, price in enumerate(prices):
        dict_prices_idx[idx] = {
            'price' : price,
            'len_bull_market' : 0,
            'is_close' : False,
        }

        for dict_price in dict_prices_idx:
            if dict_prices_idx[dict_price]['is_close'] == False:
                if dict_prices_idx[dict_price]['price'] <= price:
                    dict_prices_idx[dict_price]['len_bull_market'] += 1
                else:
                    dict_prices_idx[dict_price]['is_close'] = True

            else:
                pass

    return answer




prices = [1, 2, 3, 2, 3]

answer = solution(prices)
print(answer)

