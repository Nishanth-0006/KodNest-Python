fruits = {"apple", "banana", "kiwi"}
print(fruits, type(fruits)) 
# # set constructer
info = set(("Ram", "a", "90"))
print(info, type(info))
# Set Methods
# add()
# ADD Method (only 1 thing avn be added )
fruits = {"apple", "banana", "kiwi"}
fruits.add("orange")
print(fruits)
# UPDATE method (Multiple things can be added )
fruits = {"apple", "banana", "Kiwi", "apple"}
nfruits = {"Orange", "mango"}
fruits.update(nfruits)
print(fruits)
# Remove method 
fruits.remove("banana")
print(fruits)
# Discard()
fruits.discard("apple")
print(fruits)
# pop()
fruits.pop()
print(fruits)
# clear()
fruits.clear()
print(fruits)
# del 
del fruits
print(fruits)
# use Loops
name = {"Nishanth", "Akhil" , "Vinay"}
for i in name:
    print(i)
# Frozen set is uded to completeley make set immutabel , no methods can be used on it 
game = frozenset({"GTA3", "GTA5", "GTA6"})
print(game, type(game))
for i in game:
    print(i)
# game.add("MineCraft") ///'frozenset' object has no attribute 'add'
print(game )