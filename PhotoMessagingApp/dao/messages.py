
class MessagesDAO:

    def getAllMessages(self):
        result = [[1, 12, 14, "12/feb/2019", "cool message", "cool photo"],
                  [2, 23, 49, "13/aug/2040", "great message", "great photo"]]
        return result

    def getAllMessagesByUser(self, posterid):
        vacio = []
        if posterid == 2:
            result = [[1, 2, 14, "12/feb/2019", "cool message", "cool photo"],
                      [2, 2, 49, "13/aug/2040", "great message", "great photo"]]
        elif posterid == 3:
            result = [[5, 3, 12, "12/feb/2019", "cool message", "cool photo"],
                      [6, 3, 456, "13/aug/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getMessageById(self, mid):
        vacio = []
        if mid == 2:
            result = [2, 2, 14, "12/feb/2019", "cool message", "cool photo"]
        elif mid == 3:
            result = [3, 3, 12, "12/feb/2019", "cool message", "cool photo"]
        else:
            return vacio
        return result

    def getMessagesByDate(self, date):
        vacio = []
        if date == "14/feb/2019":
            result = [[10, 20, 140, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 490, "14/feb/2019", "great message", "great photo"]]
        elif date == "18/feb/2040":
            result = [[11, 21, 1412, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 429, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getMessagesByGroupChat(self, groupchatid):
        vacio = []
        if groupchatid == 25:
            result = [[10, 20, 25, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 25, "14/feb/2019", "great message", "great photo"]]
        elif groupchatid == 190:
            result = [[11, 21, 190, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 190, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getTrendingTopics(self):
        result = "The trending topics are calculated here, and they are #Crazy"
        return result

    def getMessagesPerDayByUser(self, posterid, date):
        vacio = []
        if posterid == 25 & date == "14/feb/2019":
            result = [[10, 20, 25, "14/feb/2019", "cool message", "cool photo"],
                      [20, 20, 25, "14/feb/2019", "great message", "great photo"]]
        elif posterid == 190 & date == "18/feb/2040":
            result = [[11, 21, 190, "18/feb/2040", "cool message", "cool photo"],
                      [243, 25, 190, "18/feb/2040", "great message", "great photo"]]
        else:
            return vacio
        return result

    def getActiveUsers(self):
        result = "These are the most Active Users right now, they post many things every day."
        return result


    def deleteMessage(self, mid):
        result = "MESSAGE TERMINATED"
        return result

    def updateMessage(self, mid):
        result = "Message %d information has been updated" % (mid)
        return result

    def createMessage(self):
        result = "Your message has been created, woohoo"
        return result