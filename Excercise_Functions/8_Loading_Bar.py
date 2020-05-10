def loading_bar(percentage):
    loading_string = ''
    loading_bars = int(percentage / 10)
    loading_string += f'[{loading_bars * "%"}{(10 - loading_bars) * "."}]'
    if loading_bars == 10:
        print(f'{percentage}% Complete!', f'{loading_string}', sep='\n')
    else:
        print(f'{percentage}% {loading_string}', 'Still loading...', sep='\n')


number = int(input())
loading_bar(number)
