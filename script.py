last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#List 1
subjects = ["physics", "calculus", "poetry", "history"]
#List 2
grades = [98, 97, 85, 88]
#List 3
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)