class GroupsDAO:

    def getAllGroups(self):
        result = [[30,"Avengers","Steve Rogers"],[11,"Los Extraterrestres","Wisin y Yandel"],[9,"All-Stars","Fulanito"]]
        return result

    def getGroupById(self, gid):
        result=[]
        if gid==30:
            result=[30,"Avengers","Steve Rogers"]

        elif gid==11:
            result=[11,"Los Extraterrestres","Wisin y Yandel"]
        elif gid== 9:
            result=[9,"All-Stars","Fulanito"]

        return result

    def getGroupByGroupName(self, gname):
        result=[]
        if gname=="Avengers":
            result = [[30, "Avengers", "Steve Rogers"]]
        elif gname=="Los Extraterrestres":
            result=[[11,"Los Extraterrestres","Wisin y Yandel"]]
        elif gname=="All-Stars":
            result=[[9,"All-Stars","Fulanito"]]

        return result

    def getAllGroupsByOwnerID(self, ownerID):
        result = [[10,"Basket"],[12,"Playa Sabado"]]
        return result

    def getGroupMembers(self, gid):
        result = [["Pepe","Aguilar"],["Carmen", "Sandiego"]]
        return result

    def createGroup(self):
        result = "Group Succesfully Created."
        return result

    def deleteGroup(self, gid):
        result = "the group %d has been deleted" %(gid)
        return result

    def updateGroup(self, gid):
        result = "the group %d has been updated" %(gid)
        return result
