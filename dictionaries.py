#DICTIONARIES 
# In python the dictionaries stores the information as "key-value" pairs

# KEY VALUE PAIRS 
# A key value pair is item in dictionary, a key used to identify item , and that value stored under that key
# member = {"name":"dinesh","grade":12}
# here name and grade are keys , values are dinesh and 12

member = {"name":"dinesh","grade":12}
print(member["name"])
print(member["grade"])

#METHODS
#dictionary methods are built in actions 
# we call it dictionary using dot notation , such as my_dict.method_name()
member = {"name":"dinesh","age":22}
print(member.keys()) # method for key
print(member.values()) # method to call values 
print(member.items())  # method to call items in dict
print(member.get("name")) # method to call value of name

member.update({"age": 12}) # method to add or update
print(member)

age = member.pop("age")
print(member)

#ITERATION 
#iteration means it goes through each item in dict one ny one from starting to ending

person = {"name":"chintu","score":31}
for key,value in person.items():
    print(key,value)
    
#NESTED DICTIONARY
# A dictionary which is stored inside a dictionary is called nested dictionary

members = {
    "members1":{"name":"yogi","age":22},
    "members2":{"name":"prakash","age":21}
}

print(members)
