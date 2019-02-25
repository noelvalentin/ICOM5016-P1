from flask import jsonify
from dao.messages import MessagesDAO

class MessageHandler:
    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['posterid'] = row[1]
        result['groupchatid'] = row[2]
        result['date'] = row[3]
        result['message'] = row[4]
        result['photo'] = row[5]
        return result


    #def build_message_attributes(self, mid, posterid, groupchatid, date, message, photo):
        #result = {}
        #result['mid'] = mid
        #result['posterid'] = posterid
        #result['groupchatid'] = groupchatid
        #result['date'] = date
        #result['message'] = message
        #result['photo'] = photo
        #return result

    def getAllMessages(self):
        dao = MessagesDAO()
        messages_list = dao.getAllMessages()
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages=result_list)

    def getAllMessagesByUser(self, posterid):
        dao = MessagesDAO()
        messages_list = dao.getAllMessagesByUser(posterid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages = result_list)

    def getMessageById(self, mid):
        dao = MessagesDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error = "Message Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message = message)

    def getMessagesByDate(self, date):
        dao = MessagesDAO()
        messages_list = dao.getMessagesByDate(date)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages=result_list)


    def getMessagesByGroupChat(self, groupchatid):
        dao = MessagesDAO()
        messages_list = dao.getMessagesByGroupChat(groupchatid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages=result_list)

    def getTrendingTopics(self):
        dao = MessagesDAO()
        result = dao.getTrendingTopics()
        return result

    def getMessagesPerDayByUser(self, posterid, date):
        dao = MessagesDAO()
        messages_list = dao.getMessagesPerDayByUser(posterid, date)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messsages=result_list)

    def getActiveUsers(self):
        dao = MessagesDAO()
        result = dao.getActiveUsers()
        return result

    def createMessage(self):
        dao = MessagesDAO()
        result = dao.createMessage()
        return result

    def deleteMessage(self, mid):
        dao = MessagesDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error = "Message Not Found"), 404
        result = dao.deleteMessage(mid)
        return result

    def updateMessage(self, mid):
        dao = MessagesDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error = "Message Not Found"), 404
        result = dao.updateMessage(mid)
        return result