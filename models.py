from sqlalchemy import Column, Integer, String
import db


class Persona(db.Base):
    __tablename__ = "persona"
    __table_args__ = {'sqlite_autoincrement': True}
    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer)
    apellido = Column(String)

    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return "Persona({} {}, {})".format(self.nombre, self.apellido, self.edad)
