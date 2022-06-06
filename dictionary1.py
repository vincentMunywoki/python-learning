#dict are used to store data values in value pairs.
#dict items are orderd,changeble and doesnot allow duplicates.
#duplicate values will overwrite the existing one's
dict = {
  "brand": "ford",
  "electric": False,
  "model": "mastang",
  "year": 2014
} 
print(dict["year"])
x = dict["brand"] # accesing item using squre brackets
print(x)
x = dict.get("brand") # using get() to access same item.
print(x)
x = dict.keys()
print(x)
print(len(dict)) #dict length
x = dict.values() # Getting values in the dictionary
print(x)
print(type(dict)) #data type

if "model" in dict: 
  print("Yes! the key is in the dictionary")

dict["year"] = 2017 # changing value of and item.
print(dict["year"])
dict.update({"brand": "toyota"}) #changing using update() method
print(dict["brand"])
dict["color"] = "red" #adding item 
print(dict)
dict.pop("model") # using pop() to remove. 
print(dict)
del dict["electric"]
print(dict)

for x in dict: #looping,,,, printing key names in dict one by one
  print(x) 
for x in dict: #printing values in dict one by one
  print(dict[x]) 

mydict = dict.copy() # coping a dictionary.using copy  () method
print(mydict)

#dictionaries in dictionary
myfamily = {
  "child1" : {
    "name": "Emilly",
    "age": 26,
    "year": 1996
   },
  "child2": {
   "name": "vinny",
   "age": 20,
   "year": 2000
   },
"child3" : {
   "name": "hellen",
   "age": 16,
   "year": 2007
  }
}
print(myfamily)
