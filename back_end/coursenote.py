from back_end.user import User
from back_end.course import Course

class CourseNote:
    def __init__(self, notes, rating, user, course):
        self.__title = title
        self.__noteLink = noteLink
        self.__rating = rating
        self.__user = user
        self.__course = course
    
    def getTitle(self):
        return self.__title

    def getNoteLink(self):
        return self.__noteLink

    def getRating(self):
        return self.__rating

    def getUser(self):
        return self.__user

    def getCourse(self):
        return self.__course

    def Upvote(self):
        self.rating = self.__rating + 1
    
    def Downvote(self):
        if (self.__rating -1 < 0):
            print("can't have negative votes")
        else:
            self.rating = self.__rating - 1
    
    def __str__(self):
        str = "title: " + self.getTitle + "\n"
        str += "noteLink: " + self.getNoteLink + "\n"
        str += "rating: " + self.getRating + "\n"
        str += "user: " + self.getUser + "\n"
        str += "course: " + self.getCourse + "\n"

        return str