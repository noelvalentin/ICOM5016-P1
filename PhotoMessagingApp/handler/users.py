from flask import jsonify
from dao.users import UsersDAO

class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]
        result['phone'] = row[3]
        result['email'] = row[4]
        result['password'] = row[5]
        return result

    def build_user_contact_dict(self, row):
        result = {}
        result['firstName'] = row[0]
        result['lastName'] = row[1]
        result['phone'] = row[2]
        result['email'] = row[3]
        return result

    def build_user_groups_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['ownerID'] = row[2]
        return result

    #def build_user_attributes(self, uid, firstName, lastName, phone, email, password):
        #result = {}
        #result['uid'] = uid
        #result['firstName'] = firstName
        #result['lastName'] = lastName
        #result['phone'] = phone
        #result['email'] = email
        #result['password'] = password
        #return result

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)

    def getUserById(self, uid):
        dao = UsersDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByFirstName(self, firstName):
        dao = UsersDAO()
        row = dao.getUserByFirstName(firstName)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByLastName(self, lastName):
        dao = UsersDAO()
        row = dao.getUserByLastName(lastName)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByPhone(self, phone):
        dao = UsersDAO()
        row = dao.getUserByPhone(phone)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserByEmail(self, email):
        dao = UsersDAO()
        row = dao.getUserByEmail(email)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def getUserGroupsById(self, uid):
        dao = UsersDAO()
        group_list = dao.getUserGroupsById(uid)
        result_list = []
        for row in group_list:
            result = self.build_user_groups_dict(row)
            result_list.append(row)
        return jsonify(Groups = result_list)

    def getUserContactsById(self, uid):
        dao = UsersDAO()
        contact_list = dao.getUserContactsById(uid)
        result_list = []
        for row in contact_list:
            result = self.build_user_contact_dict(row)
            result_list.append(result)
        return jsonify(Contacts = result_list)

    def createUser(self):
        dao = UsersDAO()
        result = dao.insert(firstName, lastName, phone, email, password)
        return result

    def deleteUser(self, uid):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User Not Found"), 404
        result = dao.delete(uid)
        return result

    def updateUser(self, uid):
        dao = UsersDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User Not Found"), 404
        result = dao.update(uid)
        return result
