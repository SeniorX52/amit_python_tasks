thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = dict(name = "John", age = 36, country = "Norway") #{'name': 'John', 'age': 36, 'country': 'Norway'}
print(thisdict["name"])
x = thisdict.get("age") #36
y = thisdict.keys() # dict_keys(['name', 'age', 'country'])
m = thisdict.values() # dict_values(['John', 36, 'Norway'])
z = thisdict.items() #dict_items([('name', 'John'), ('age', 36), ('country', 'Norway')])
thisdict.update({"address": "62a Anton Saefkow Str."}) # add new item
thisdict.pop("age") #deletes age
print(thisdict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child1"]["name"]) # Emil