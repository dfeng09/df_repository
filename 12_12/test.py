from student import Student

s1 = Student('keqing', 'female')
s2 = Student.from_string('shogun female')
print(f"student_num:{Student.student_num}")
print(f"s1_name: {s1.name}, s2_sex: {s2.sex}")