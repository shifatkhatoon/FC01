n = int(input().strip())
phone_book = {}
for i in range(n):
    name = str(input())
    num = int(input())
    phone_book[name] = num
      
while True:
    query = str(input())
    if query in phone_book:
        print('{}={}'.format(query,phone_book[query]))
    elif query not in phone_book:
        print('Not found')
    elif query == "":
        break
