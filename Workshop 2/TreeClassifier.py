from sklearn import tree

clf = tree.DecisionTreeClassifier()

height = input("What is your height in centimeters? ")
weight = input("What is your weight in kilograms? ")
gender = input("are you a male or a female? ")

if gender == 'male':
	gender_status = 1
else:
	gender_status = 0
# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [height, weight, gender_status]
X = [[181, 80, 1], [177, 70, 1], [160, 60, 0], [154, 54, 1], [166, 65, 1],
     [190, 90, 1], [175, 64, 0],
     [177, 70, 0], [159, 55, 0], [171, 75, 1], [181, 85, 1]]

Y = [44,43,38,37,40,47,39,40,37,42,43]



# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[height, weight, gender_status]])

# CHALLENGE compare their reusults and print the best one!

print ('Your shoe size is %s' % prediction)
