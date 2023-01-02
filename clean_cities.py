from json import loads, dump

data = loads(open('cities.json', 'r', encoding='utf-8').read())
for i in data:
    del i['coords']
    del i['population']
    del i['district']
    print(i)
print(dump(data, open('cities.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2))
