with open('years.txt', 'w', encoding='utf-8') as f:
    for i in range(2010, 2021):
        f.write(str(i) + " ")
