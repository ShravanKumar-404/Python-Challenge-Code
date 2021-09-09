"""
Write a Python program that adds a new key-value pair
to a dictionary only if the key doesn't exist already.

If the key-value pair exists in the dictionary, do not update the existing value.
The dictionary should not be modified in this case.

Store the new key in the new_key variable and the new value in the new_value variable.

Print the final value of the dictionary.

"""


dicts = {"January": 45, "February": 56, "March": 67}

new_key = "April"
new_value = "69"

if new_key not in dicts:
    dicts[new_key] = new_value
    print(dicts)
else:
    print(dicts)
