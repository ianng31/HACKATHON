from back_end.user import User
from back_end.course import Course
from back_end.CollegeDocs_System import CollegeDocs_System

system = CollegeDocs_System

#create courses
system.addCourse("COMP1511")

#create students
system.addUser("z5555555", "James")

user1 = system.getUser("z5555555")
course1 = system.getCourse("COMP1511")

print(user1)
print(course1)


