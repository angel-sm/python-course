lenguagues = "Python Ruby Java Rust C C++"

lenguagues_list = lenguagues.split()
print(lenguagues_list)

# Concat list
all_lenguagues = "-".join(lenguagues_list)
print(all_lenguagues)

full_name = 'Mr. %s %s' %('Angel', 'Sanches')
print(full_name)

full_second_name = 'Mr {} {}'.format('Angel', 'Sanches')
print(full_second_name)

course_title = "Python profetional course Python"
print(course_title.count('Python'))