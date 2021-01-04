from flask_login import UserMixin

class Usuario(UserMixin):
    
    def __init__(self, rut):
        self.rut = rut
        self.id = rut
        
    def __repr__(self):
        return f'<Usuario {self.rut}>'