users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
{'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
{'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
{'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
{'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

for mail in map(lambda u: "남" if u["sex"] == "M" else "여", users):
    print(mail)

temp_1 = list(map(lambda u: u["mail"], users))
temp_2 = tuple(map(lambda u: u["mail"], users))
print(temp_1)
print(temp_2)