skinning  = {}
first_lvl = int(1 / 10 + 10)
skinning[f"{first_lvl}"] = [1]

for i in range(2, 300 + 1):
    if i <= 99:
        second_lvl = int(i / 10 + 10)
        if second_lvl == first_lvl:
            pass
        else:
            skinning[f"{first_lvl}"].append(i - 1)
            skinning[f"{second_lvl}"] = [i]
        first_lvl = second_lvl
    else:
        second_lvl = int(i / 5)
        if second_lvl == first_lvl:
            pass
        else:
            skinning[f"{first_lvl}"].append(i - 1)
            skinning[f"{second_lvl}"] = [i]
        first_lvl = second_lvl

skinning10_34 = {}
skinning35_59 = {}

for key in skinning:
    if int(key) <= 34:
        skinning10_34[key] = skinning[key]
    elif int(key) <= 59:
        skinning35_59[key] = skinning[key]
    else:
        pass

skinning_lvl = "Skinning lvl:"
mob_lvl      = "Mob lvl:"
print(f"{skinning_lvl}    {mob_lvl}       {skinning_lvl}   {mob_lvl}")
print("--------------------------------------------------------")

for i in range(10, 34 + 1):
    a = f"{i}"
    b = f"{i + 25}"
    print(f"{skinning10_34[a][0]: 4d}-{skinning10_34[a][1]: <4d} {int(a): 9d}\
            {skinning35_59[b][0]: 4d}-{skinning35_59[b][1]: <4d} {int(b): 9d}")