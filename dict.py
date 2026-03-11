engineeringstudents = {
    'computer': {
        'student1': {
            'name': 'yusufa',
            'matric_no': 'CSC001',
            'level': 300,
            'gpa': 3.72,
            'age': 22,
            'email': 'yusufa@uni.edu',
            'year_of_admission': 2022
        },
        'student2': {
            'name': 'bilal',
            'matric_no': 'CSC002',
            'level': 200,
            'gpa': 3.45,
            'age': 21,
            'email': 'bilal@uni.edu',
            'year_of_admission': 2023
        },
        'student3': {
            'name': 'auwal',
            'matric_no': 'CSC003',
            'level': 400,
            'gpa': 3.88,
            'age': 24,
            'email': 'auwal@uni.edu',
            'year_of_admission': 2021
        },
        'student4': {
            'name': 'shamo',
            'matric_no': 'CSC004',
            'level': 100,
            'gpa': 3.10,
            'age': 19,
            'email': 'shamo@uni.edu',
            'year_of_admission': 2024
        },
        'student5': {
            'name': 'umar jako',
            'matric_no': 'CSC005',
            'level': 300,
            'gpa': 3.56,
            'age': 23,
            'email': 'umarjako@uni.edu',
            'year_of_admission': 2022
        }
    },

    'electrical': {
        'student1': {
            'name': 'muhammad',
            'matric_no': 'EEE001',
            'level': 400,
            'gpa': 3.91,
            'age': 25,
            'email': 'muhammad@uni.edu',
            'year_of_admission': 2021
        },
        'student2': {
            'name': 'khalifa',
            'matric_no': 'EEE002',
            'level': 200,
            'gpa': 3.33,
            'age': 20,
            'email': 'khalifa@uni.edu',
            'year_of_admission': 2023
        },
        'student3': {
            'name': 'ado',
            'matric_no': 'EEE003',
            'level': 300,
            'gpa': 3.60,
            'age': 22,
            'email': 'ado@uni.edu',
            'year_of_admission': 2022
        },
        'student4': {
            'name': 'yusuf',
            'matric_no': 'EEE004',
            'level': 100,
            'gpa': 3.05,
            'age': 18,
            'email': 'yusuf@uni.edu',
            'year_of_admission': 2024
        },
        'student5': {
            'name': 'baballe',
            'matric_no': 'EEE005',
            'level': 400,
            'gpa': 3.70,
            'age': 24,
            'email': 'baballe@uni.edu',
            'year_of_admission': 2021
        }
    },

    'mechanical': {
        'student1': {
            'name': 'muallim',
            'matric_no': 'MEC001',
            'level': 300,
            'gpa': 3.48,
            'age': 23,
            'email': 'muallim@uni.edu',
            'year_of_admission': 2022
        },
        'student2': {
            'name': 'abdulbasit',
            'matric_no': 'MEC002',
            'level': 200,
            'gpa': 3.29,
            'age': 21,
            'email': 'abdulbasit@uni.edu',
            'year_of_admission': 2023
        },
        'student3': {
            'name': 'john',
            'matric_no': 'MEC003',
            'level': 400,
            'gpa': 3.95,
            'age': 26,
            'email': 'john@uni.edu',
            'year_of_admission': 2021
        },
        'student4': {
            'name': 'ahmad',
            'matric_no': 'MEC004',
            'level': 100,
            'gpa': 2.98,
            'age': 19,
            'email': 'ahmad@uni.edu',
            'year_of_admission': 2024
        },
        'student5': {
            'name': 'abubakar',
            'matric_no': 'MEC005',
            'level': 300,
            'gpa': 3.67,
            'age': 22,
            'email': 'abubakar@uni.edu',
            'year_of_admission': 2022
        }
    }
}


# random student data generation
import random

generated_students = {}

for dept, names in engineeringstudents.items():
    generated_students[dept] = {}
    
    for index, name in enumerate(names, start=1):
        student_id = f"{dept[:3].upper()}{index:03}"
        
        generated_students[dept][student_id] = {
            "name": name,
            "level": random.choice([100, 200, 300, 400]),
            "gpa": round(random.uniform(2.0, 4.0), 2),
            "age": random.randint(18, 26),
            "year_of_admission": random.randint(2020, 2024),
            "email": f"{name.replace(' ', '').lower()}@uni.edu"
        }

print(generated_students)

for dept, students in generated_students.items():
    # print("Department:", dept)
    for id, info in students.items():
        name = info["name"]
        gpa = info['gpa']
        matric_no = info['matric_no']
        if gpa >= 3.5:
            # print(f"List of all first class student in {dept}\n")
            print(id, matric_no, "-", name, "-", gpa)
        # elif gpa >= 3.0:
        #     # print("List of all second class upper student in each department :\n")
        #     print(matric_no, "-", name, "-", gpa)
        # elif gpa >= 2.5:
        #     # print("List of all secod class lower student in each department :\n")
        #     print(matric_no, "-", name, "-", gpa)
        # elif gpa >= 1.5:
        #     # print("List of all pass class student in each department :\n")
        #     print(matric_no, "-", name, "-", gpa)
        # else:
        #     # print("List of all withdrawn student (with gpa < 1.5) in each department :\n")
        #     print(matric_no, "-", name, "-", gpa)
            #print(dept, "-", matric_no, "-", name, "-", gpa)
        # if name and name.lower().startswith("a"):
        #     print(dept, "-", student_id, "-", name)
        

# for dept, students in engineeringstudents.items():
#     print("Department:", dept)
    
#     for student_id, info in students.items():
#         name = info['name']

#         # if name.lower().startswith('a'):
#         #     print("   ", student_id, "-", info["name"])

# print(engineeringstudents['electrical'])