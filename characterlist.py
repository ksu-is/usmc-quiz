character_names = open('charaters.txt','w+')

character_names.write("Homer","Marge","Bart","Lisa","Maggie","Santa’s little helper","Snowball", "Abraham","Apu", "Barney","Chief Wiggum","Itchy","Scratchy","Kent Brockman","Krusty the Clown","Lenny","Uter","Millhouse","Moe","Mr.Burns","Ned Flanders","Otto Man","Patty","Selma","Ralph Wiggum","Seymour Skinner","Waylon Smithers", "Mayor Joe Quimby","Nelson Muntz", "Groundskeeper Willie")

character_names.seek(0)

character_list = character_names.read()

print(character_list)
