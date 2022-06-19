file_name = "Recipe.txt"


def cat_reader(file_name):
    with open(file_name, encoding='UTF-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish_name = line.strip()
            count = int(file_obj.readline())
            ingr_list = []
            for item in range(count):
                ingr = file_obj.readline().split('|')
                ingr_1 = {"ingr_name": ingr[0].strip(), "ingr_q": ingr[1].strip(), "ingr_measure": ingr[2].strip()}
                ingr_list.append(ingr_1)
            cook_book[dish_name] = ingr_list
            file_obj.readline()

        return cook_book


def new_shop_list(dishes, person):
    dict_1 = cat_reader(file_name)
    shop_list = {}
    for i in dishes:
        for ingredients in dict_1[i]:
            if ingredients['ingr_name'] in shop_list:
                shop_list[ingredients['ingr_name']]['ingr_q'] += int(ingredients['ingr_q']) * person
            else:
                shop_list[ingredients['ingr_name']] = dict(ingr_measure=ingredients['ingr_measure'],
                                                           ingr_q=int(ingredients['ingr_q']) * person)
    print(shop_list)


new_shop_list(['Омлет', 'Омлет', 'Фахитос'], 10)