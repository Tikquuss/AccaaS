#we will use the django rest for these elements
from rest_framework import serializers
from .models import Forfait, CompteUser

class ForfaitSerialiser(serializers.HyperlinkedModelSerializer):
    '''
    here i will create the methods to manipulate forfaits, and in the models, i will write
    the methods to modify forfaits just before database modification
    '''
    class Meta:
        model = Forfait
        fields = ("id","nom","valeur","expire_days")

class CompteUserSerialiser(serializers.HyperlinkedModelSerializer):
    '''
    here i will create the methods to manipulate user accounts (here i will call functions for accounting which will be in the audit package), and in the models, i will write
    the methods to modify userAccounts just before database modification. i don't know the functions actually
    '''
    class Meta:
        model = CompteUser
        fields = ("id","solde","actif","date_creation","date_activation","date_expiration","nom_forfait","userId")
