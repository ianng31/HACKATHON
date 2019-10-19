class course:
    def __init__(self, courseCode, users):
        self.__courseCode = courseCode
        self.__users = users

    def getCourseCode(self):
        return self.__courseCode

    def getZID(self):
        return self.__users