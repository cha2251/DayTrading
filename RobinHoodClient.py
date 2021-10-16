import robin_stocks as rs
import json

class Client():
    def login(self):
        with open('auth.json') as loginFile:
            fields = json.load(loginFile)
            user = fields['username']
            pwd = fields['password']
        rs.robinhood.authentication.login(username=user,
            password=pwd,
            expiresIn=57600)

        print(rs.robinhood.options.find_tradable_options("NYT"))


        

    def logout(self):
        rs.robinhood.authentication.logout()


    def startDay(self):
        pass

    def endDay(self):
        pass

    def buyOption():
        pass

    def sellOption():
        pass

