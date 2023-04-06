import requests
import random
class User:
    def __init__(self, im ="", fam ="", log = "", pas = "" ):
        self.__lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu massa vestibulum lacus accumsan laoreet. Donec aliquet leo sapien, in volutpat est condimentum iaculis. Nam tempor nec nisi ut varius. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras posuere elementum orci, quis finibus metus porttitor ac. In pretium pretium tortor. Aenean luctus tellus non varius interdum. Donec mollis leo dolor, at mollis turpis interdum et. Nam nec commodo metus, at imperdiet risus"
        self.__data = requests.get("https://api.randomdatatools.ru/").json
        self.login = self.__data["Login"]if not log else log
        self.__password= self.__data["Password"]if not pas else pas
        self.imya =self.__data["FirstNano"]if not im else im
        self.familiya = self.__data["LastName"]if not fam else fam
        self. post = [self.__lorem[random.randint(0, 35):random.randint(36, 70)]]

        #x = ""
        # if x:
            #print(5555)   # нельзя если X = "" пустой

print()