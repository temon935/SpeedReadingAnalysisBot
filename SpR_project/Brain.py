import csv


list = ['Точка обмана 4', 'https://cv1.litres.ru/pub/c/elektronnaya-kniga/cover_415/126614-den-braun-tochka-obmana-126614.jpg',
        '8900', '505']


def rec(list_of_data):
    books = open('books.csv', 'a')
    for row in list_of_data:
        books.write(row)
        books.write('\n')
    books.close()


rec(list)