# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# we ar using pop for delete the dic.........by nikhil khandelwal
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
##############################end##################################
