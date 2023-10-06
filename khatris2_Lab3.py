import csv
import json
import xml.etree.ElementTree as ET


class DscDataProcessor:
    #constructor function which initializes the filenames
    def __init__(self, csvFilename, jsonFilename, xmlFilename):
        self.csvFilename = csvFilename
        self.jsonFilename = jsonFilename
        self.xmlFilename = xmlFilename

    #method to create a csv file from the student data
    def createCsvFile(self, studentData):
        with open(self.csvFilename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'Program Name'])
            writer.writerows(studentData)

    #Method which count the json object
    def countJsonObjects(self):
        with open(self.jsonFilename, 'r') as file:
            data = json.load(file)
            return len(data)
    #Method which print program infromation by parsing xml file
    def printXmlPrograms(self):
        tree = ET.parse(self.xmlFilename)
        root = tree.getroot()

        print("{:<20} {:<20} {:<15} {:<10} {:<5}".format(
            "Program Name", "College Name", "Student Count", "Year Started", "Type"
        ))
        print("*" * 80)

#for loops to extract different value from root
        for program in root.findall('Program'):
            programName = program.find('Name').text if program.find('Name') is not None else ''
            collegeName = program.find('CollegeName').text if program.find('CollegeName') is not None else ''
            studentNum = program.get('studCount') if 'studCount' in program.attrib else ''
            yearStarted = program.find('YearStarted').text if program.find('YearStarted') is not None else ''
            programType = program.get('type') if 'type' in program.attrib else ''

            if programName or collegeName or studentNum or yearStarted or programType:
                print("{:<20} {:<20} {:<15} {:<10} {:<5}".format(
                    programName, collegeName, studentNum, yearStarted, programType
                ))

#main method
def main():
    csvFilename = 'khatris2.csv'
    jsonFilename = 'sampleData.json'
    xmlFilename = 'NKU_Programs.xml'

    noOfStudents = int(input("Enter the number of students: "))
    studentData = []
#for loop to loop through no of students
    for _ in range(noOfStudents):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        programName = input("Enter Program Name: ")
        studentData.append([first_name, last_name, programName])

    dataProcessor = DscDataProcessor(csvFilename, jsonFilename, xmlFilename)
    dataProcessor.createCsvFile(studentData)

    json_object_count = dataProcessor.countJsonObjects()
    print(f"Number of JSON objects: {json_object_count}")

    dataProcessor.printXmlPrograms()

#calling the main method
if __name__ == "__main__":
    main()
