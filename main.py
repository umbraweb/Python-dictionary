word = input("Which word would you like to learn about today\n")
keys = ('apple', 'ape', 'orange')
values ={'apple' :"A sweet, crisp, and refreshing fruit that typically has a red, green, or yellow skin.", 'ape':  "Anthropology, Zoology. any member of the superfamily Hominoidea, the two extant branches of which are the lesser apes (gibbons) and the great apes (humans, chimpanzees, gorillas, and orangutans)"}
if word in keys:
  print(values[word])
else:
  print("Word not found")