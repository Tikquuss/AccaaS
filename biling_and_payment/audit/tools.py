from .models import CompteUser

class AuthorizationByAccountingTools :
    def isTheUserAuthorized(self, user):
        userAccount = CompteUser.objects.get(userId = user.id)
        if user != None:
            return True
        else :
            return False

            