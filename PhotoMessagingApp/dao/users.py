
class UsersDAO:

    def login(self):
        result= "Welcome"
        return result

    def getAllUsers(self):
        result = [[0, "Fulano", "Apellido", 787, "hotmail", "password123"],
                  [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
                 ]
        return result

    def getUserById(self, uid):
        vacio=[]
        if uid== 0:
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        elif uid ==1:
            result=[1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        else:
                return vacio
        return result

    def getUserByFirstName(self, firstName):
        result=[]
        if firstName=="Manuel":
            result=[1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif firstName=="Fulano":
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserByLastName(self, lastName):
        result = []
        if lastName == "Rodriguez":
            result = [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif lastName == "Apellido":
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserByPhone(self, phone):
        result = []
        if phone == 939:
            result = [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif phone == 787:
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserByEmail(self, email):
        result = []
        if email == "gmail":
            result = [1, "Manuel", "Rodriguez", 939, "gmail", "qwerty"]
        elif email == "hotmail":
            result = [0, "Fulano", "Apellido", 787, "hotmail", "password123"]
        return result

    def getUserGroupsById(self, uid):
        result = []
        return result

    def getUserContactsById(self, uid):
        result = [["Jose","Verga",878,"yut@hotmail.com"],["Pepe","Last",878,"lagata@hotmail.com"]]
        return result

    def deleteUser(self, uid):

        result="USER DESTROYED"
        return result

    def updateUser(self, uid):
        result= "User %d information has been updated" %(uid)
        return result
    def createUser(self):
        result="User created,please check yur email to verify"
        return result
