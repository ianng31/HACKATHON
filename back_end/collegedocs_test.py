from collegedocs_system import CollegeDocs_System

system = CollegeDocs_System()

#create courses
system.addCourse("COMP1511")

#create students
system.addStudent("z5555555", "James")

#get students
student1 = system.getStudent("z5555555")

#get courses
course1 = system.getCourse("COMP1511")

#enrol student in courses
system.enrol(student1, course1)

#create CourseNote
system.addCourseNote("James's Notes", "http/here_are_the_notes", 0, student1, course1)

#get coursenote

note1 = system.getCourseNote("http/here_are_the_notes")

system.upvote(note1)
system.upvote(note1)
system.upvote(note1)
system.upvote(note1)

system.downvote(note1)

print(student1)
print(course1)
print(note1)