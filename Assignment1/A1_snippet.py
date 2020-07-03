# Code snippet to read csv file and parse columns without using pandas 

#create list to store csv file
csvfile=[]

#open csv file and store in the list above
with open(filename,"r") as file:
	csvreader=csv.DictReader(file) #using csv.DictReader instead of csv.reader due to ease of manipulating dict for min, max, mean etc.

#for more on using DictReader: https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
#for reader vs DictReader: https://python-forum.io/Thread-csv-reader-vs-csv-dictReader

	for row in csvreader:
		csvfile.append(row) #appends row in the list structure to store the csv file
	columns = csvreader.fieldnames #store columns as a variable



# Code snippet for testing if a column is string or float (returns true for int AND float)
# reference: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float/354130


for column in columns:
	for value in csvfile:
		try:
			float(value[column])  #returns true if value is a float or int
		except ValueError:
			# do something error-like here if value is not float or int




table = [["Columns:", "Min", "Max", "Avg", "Std. Dev.", "Most Common Word"]]

# iteration for 
for column in columns:
	allValues = []
	validValues = []
	hasUnvalid = False
	dataRow = [column]
	for row in csvfile:
		allValues.append(row[column])
		try:
			value = float(row[column])
			validValues.append(value);
		except ValueError:
			hasUnvalid = True

	# Item 1-3
	if hasUnvalid:
		dataRow.append("n/a")
		dataRow.append("n/a")
		dataRow.append("n/a")
	else:
		dataRow.append(min(validValues)) # min value
		dataRow.append(max(validValues)) # max value
		dataRow.append(sum(validValues) / len(validValues)) # average value


	# Item 4
	if len(validValues) >= 2:
		difference = 0
		variance = 0
		standardDeviation = 0
		mean = sum(validValues) / len(validValues)
		for each in validValues:
			difference += (each - mean) ** 2
		variance = difference / len(validValues)
		standardDeviation = variance ** (1 / 2)
		dataRow.append(standardDeviation)
	else:
		dataRow.append('n/a')

	# Item 5
	if len(allValues) > 0:
		mostFrequent = max(set(allValues), key = allValues.count)
		dataRow.append(mostFrequent)
	else:
		dataRow.append("n/a")

	table.append(dataRow)


# graph
for column in columns:
	allValues = []
	hasUnvalid = False;
	for row in csvfile:
		try:
			allValues.append(float(row[column]))
		except ValueError:
			hasUnvalid = True

	if Unvalid is False:
		uniqueValue = dict.fromkeys(sorted(set(allValues)), 0) # unique all values and convert into dictonary - key(value name): value(times of presence)
		for key, value in uniqueValue.items():
			uniqueValue[key] = allValues.count(key) / len(uniqueValue.keys());

		plt.bar(uniqueValue.keys(), uniqueValue.values(), color = "red")
		plt.title(column)
		plt.show()