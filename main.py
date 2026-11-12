import json

def add_student():
    with open("data.json", "r+") as file:
        data = json.load(file)

        id = input("Enter student ID: ")
        if id in [student["id"] for student in data["students"]]:
            print("Student ID already exists. Please enter a unique ID.")
            return
        name = input("Enter student name: ")
        if name.isalpha() == False:
            print("Name must contain only letters. Please enter a valid name.")
            return
        exam_times = int(input("Enter number of exam results: "))
        if exam_times <= 0 or not isinstance(exam_times, int) or exam_times>100:
            print("Number of exam results must be a positive integer. Please enter a valid number.")
            return
        exam_results = []
    
        for _ in range(exam_times):
            result = int(input("Enter exam result: "))
            if result <= 0 or not isinstance(result, int) or result > 100:
                print("Exam result must be a positive integer between 1 and 100. Please enter a valid result.")
                return
            exam_results.append(result)
    
        new_data = {
            "id": id,
            "name": name,
            "exam results": exam_results
        }

        data["students"].append(new_data)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def view_student():
    id = input("Enter student ID: ")
    with open("data.json", "r") as file:
        data = json.load(file)
        for student in data["students"]:
            if student["id"] == id:
                print(f"Student ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Exam Results: {student['exam results']}")
                return
    print("Student not found.")

def edit_student():
    id = input("Enter student ID to edit: ")
    with open("data.json", "r+") as file:
        data = json.load(file)
        for student in data["students"]:
            if student["id"] == id:
                new_name = input("Enter new name (leave blank to keep current): ")
                if new_name:
                    student["name"] = new_name
                new_exam_times = input("Enter new number of exam results (leave blank to keep current): ")
                if new_exam_times:
                    exam_results = []
                    for _ in range(int(new_exam_times)):
                        result = int(input("Enter exam result: "))
                        if result <= 0 or not isinstance(result, int) or result > 100:
                            print("Exam result must be a positive integer between 1 and 100. Please enter a valid result.")
                            return
                        exam_results.append(result)
                    student["exam results"] = exam_results
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print("Student updated.")
                return
    print("Student not found.")

def remove_student():
    id = input("Enter student ID to remove: ")
    with open("data.json", "r+") as file:
        data = json.load(file)
        for i, student in enumerate(data["students"]):
            if student["id"] == id:
                info = input(f"Are you sure you want to remove {student['name']}? (yes/no): ")
                if info.lower() != "yes":
                    print("Operation cancelled.")
                    return
                del data["students"][i]
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print("Student removed.")
                return
    print("Student not found.")

def calc_average():
    id = input("Enter student ID to calculate average: ")
    with open("data.json", "r") as file:
        data = json.load(file)
        for student in data["students"]:
            if student["id"] == id:
                if student["exam results"]:
                    average = sum(student["exam results"]) / len(student["exam results"])
                    print(f"Average exam result for {student['name']}: {average}")
                else:
                    print(f"No exam results found for {student['name']}.")
                return
    print("Student not found.")

def ranking():
    with open("data.json", "r") as file:
        data = json.load(file)
        info = {}
        for student in data["students"]:
            if student["exam results"]:
                average = sum(student["exam results"]) / len(student["exam results"])
                info[student["id"]] = average
            else:
                info[student["id"]] = 0

    # Sort students by average in descending order
    sorted_students = sorted(info.items(), key=lambda x: x[1], reverse=True)

    print("Student Rankings:")
    for i, (id, avg) in enumerate(sorted_students, start=1):
        print(f"{i}. {id}: {avg}")

while True:
    action = input("Enter 'add' to add a student or 'view' to view a student or 'edit' to edit a student or 'remove' to remove a student or 'average' to calculate average or 'ranking' to see student rankings: ")
    if action == "add":
        add_student()
    elif action == "view":
        view_student()
    elif action == "edit":
        edit_student()
    elif action == "remove":
        remove_student()
    elif action == "average":
        calc_average()
    elif action == "ranking":
        ranking()
    elif action == "exit":
        break
    else:
        print("Invalid action.")


#with open("data.json", "r") as file:
#    data = json.load(file)

#print(data["students"][0]["id"])