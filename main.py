# Creating a list
friends = ["Anar", "Ali", "Eltac", "Yelmar"]

# Printing the list
print(friends)

# To see the length of the list use len()
print(f"The length of friends is: {len(friends)}")

# To print the specific index from the list:
print(friends[0])


# Lists of lists
friends_with_ages = [
  ["Anar", 22],
  ["Ali", 23],
  ["Eltac", 23],
  ["Yelmar", 18]
]
# Printing
print(friends_with_ages)

# Can choos which element to print from the chosen list 
# from the list of the lists
print(friends_with_ages[0])
print(friends_with_ages[0][1])

print(f"{friends_with_ages[0][0]} is {friends_with_ages[0][1]} years old")


# Adding to the list
friends_with_ages.append(["Jalal",23])
print(friends_with_ages)


# Adding to specific index
friends_with_ages.insert(2,["Farid", 22])
print(f"Here is after insertion: {friends_with_ages}")

# Removing from the list
friends_with_ages.remove(["Ali",23])
print(friends_with_ages)


# Removing specific index from the list

friends_with_ages.pop(1)

# To remove the last item from the list
friends_with_ages.pop()


# To clear the items in the list use:
friends_with_ages.clear()


# To sort lists use sort()
# Sort is case sensitive so, Capital Letters will come first
# To make it case-insensitive use: sort(key = str.lower)
friends.sort()

# To sort in descending order use
friends.sort(reverse = True)



# To reverse the existing list use
friends.reverse()

# Lists are type of 'list'
print(type(friends))


# Accessing range of items in list

print(f"Here you can see the first 3 items in the list: {friends[0:2]}")

# Accessing the range without specifying the end
print(f"Here you can see the starting point till end: {friends[1:]}")


# Adding another list to the list
friends2 = ["Rauf", "Rasul", "Rafis"]

friends.extend(friends2)

print(f"Friends list after extending friends2 list is: {friends}")
