key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
legendary_item = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
legendary_bought = 0
while legendary_bought == 0:
    text_line = input().split(' ')
    quantities = [int(i) for i in text_line[::2]]
    materials = text_line[1::2]
    for material, quantity in zip(materials, quantities):
        material_endname = material.lower()
        if material_endname == 'shards' or material_endname == 'fragments' or material_endname == 'motes':
            key_materials[material_endname] += quantity
            if key_materials[material_endname] >= 250:
                key_materials[material_endname] -= 250

                print(f"{legendary_item[material_endname]} obtained!")
                sorted_key_mat = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
                [print(f"{key}: {value}") for key, value in sorted_key_mat]
                sorted_junk_mat = sorted(junk_materials.items(), key=lambda x: (x[0]))
                [print(f"{key}: {value}") for key, value in sorted_junk_mat]
                legendary_bought = 1
                break
        else:
            if material_endname not in junk_materials:
                junk_materials[material_endname] = 0
            junk_materials[material_endname] += quantity
