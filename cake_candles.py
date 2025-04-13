
def Count_tallest_candles(candles_lengths):
    lengths_list= candles_lengths.split()
    lengths_list= [int(x) for x in lengths_list]
    tallest = max(lengths_list)
    count_tallest= lengths_list.count(tallest)
    return count_tallest

candles_lengths = input('Enter cake candles lengths: ')

print(f'Number of candles tht are tallest: ',Count_tallest_candles(candles_lengths))
