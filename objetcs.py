class Ladron:

    def __init__(self,data):
        self.block = data['BLOQUE']
        self.lastName = data['APELLIDO']
        self.name = data['NOMBRE']
        self.province = data['PROVINCIA']
        self.dLegal = data['D_LEGAL']
        self.cLegal = data['C_LEGAL']
        self.dReal = data['D_REAL']
        self.cReal = data['C_REAL']
        self.email = data['EMAIL']
        self.telephone = data['TELEFONO']
        self.facebook = data['FACEBOOK']
        self.twitter = data['TWITTER']
        self.instagram = data['INSTAGRAM']
        self.youtube = data['YOUTUBE']

    def pretty_print(self):
        print('*******************')
        print('name: '+self.name)
        print('lastName: '+self.lastName)
        print('block: '+self.block)
        print('print: '+province)
        print('dLegal: '+self.dLegal)
        print('cLegal: '+self.cLegal)
        print('dReal: '+self.dReal)
        print('cReal: '+self.cReal)
        print('email: '+self.email)
        print('telephone: '+self.telephone)
        print('facebook: '+self.facebook)
        print('twitter: '+self.twitter)
        print('instagram: '+self.instagram)
        print('youtube: '+self.youtube)

