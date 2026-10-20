# dictionary of students (id -> details)
students_data = {
    "id1": {"name": "sarah", "class": "V", "subjects integration": "english, math, science"},
    "id2": {"name": "david", "class": "V", "subjects integration":"english, math, science"},
    "id3": {"name": "sarah", "class": "V", "subjects integration": "english, math, science"},
    "id4": {"name": "surya", "class": "V", "subjects integration":"english, math, science"},
}
result = {}
seen_keys = [] #using a list instead of a set

for student_id, details in students_data.items():
    unique_key = (details["name"], details["class"], details["subjects integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
#print output line by line
for k, v in result.items():
    print(k, ":", v)