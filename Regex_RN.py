#
# Student Basic Info - Crawler
# Author: CuongDD
#
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Firefox and goto SIS
driver = webdriver.Firefox()
driver.get("http://sis.hust.edu.vn/ModuleSearch/GroupList.aspx")

# Print message
print("Connected to page! Start crawling")
# Need to have encoding here for Vietnamese characters
output = open('Output/K57.txt', 'a', encoding='utf8')
# Need to wait for some seconds for SIS to be fully loaded
time.sleep(50)

#
start = time.strftime("%c")
print("Start: %s" % start)

# The input box for StudentID
studentCodeFieldID = "MainContent_tbStudentID_I"

for index in range(3000,4000):
	# Coded the student ID to proper format
	if index < 10:
		temp = "000" + str(index)
	elif index < 100:
		temp = "00" + str(index)
	elif index < 1000:
		temp = "0" + str(index)
	else:
		temp = str(index)
	studentID = "2011" + temp

	# Find the input for student ID
	studentCodeElement = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id(studentCodeFieldID))
	# Fill in the student ID and search
	studentCodeElement.clear()
	studentCodeElement.send_keys(studentID)
	time.sleep(0.2)
	studentCodeElement.send_keys(Keys.RETURN)
	# Need to sleep a bit, otherwise SIS will go "shit"
	time.sleep(0.6)

	# Get and extract student detailed info
	studentDetails = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_class_name("dxgv"))
	# for detailField in studentDetails:
	# 	writeData = detailField.text
	# 	# Only store row that is not null
	# 	if dText != 'No data to display':
	# 		output.write(dText+",")
	listLen = len(studentDetails)
	if listLen == 9:
		studentIDValue   = studentDetails[0].text
		lastNameValue	 = studentDetails[1].text
		middleNameValue	 = studentDetails[2].text
		firstNameValue	 = studentDetails[3].text
		dateOfBirthValue = studentDetails[4].text
		classValue 		 = studentDetails[5].text
		programValue 	 = studentDetails[6].text
		statusValue 	 = studentDetails[7].text

		output.write(str(studentIDValue) + "," + \
					     lastNameValue + "," + \
					     middleNameValue + "," + \
					     firstNameValue + "," + \
					     dateOfBirthValue + "," + \
					     classValue + "," + \
					     programValue + "," + \
					 str(statusValue) + ",K56\n")

	studentCodeElement.clear()

output.close()

end = time.strftime("%c")
print("Finish time: %s" % end)
print("Time elapsed: ")