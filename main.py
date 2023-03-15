import sys
import db
from models import Persona


def agregarPersonasIniciales():
    p1 = Persona("Cristian", 20, "Galvez")
    p2 = Persona("Manuel", 35, "Lujan")

    # db.session.add(p1)  # añadir uno a uno
    db.session.add_all([p1, p2])
    db.session.commit()  # commit para guardar el cambio
    db.session.close()  # siempre se termina cerrándola
    # print(p1)


def consultasDePrueba():
    print("\n #1 Obtener un objeto a partir de su id (su primary key). Si no lo encuentra nos devuelve none")
    result = db.session.query(Persona).get(1)  # A partir de la version SQLAlchemy 1.4.45 no funciona .get
    print(result)
    print(type(result))
    print(result.edad)


if __name__ == '__main__':
    # Reseteamos la base de datos si existe. Esto se emplea porque una vez la base de datos
    # una vez creada no se cambia. Solo se hace en pruebas.
    db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    # En la siguiente línea estamos indicando a SQLAlchemy que cree si no existen las tablas de todos
    # los modelos que encuentre en model.oy, sin embargo, para que esto ocurra es necesario
    # que cualquier modelo se halla importando previamente antes de llamar a la siguiente funciona (create_all())
    db.Base.metadata.create_all(db.engine)
    while (True):
        print("\n1. Agregar personas iniciales\n"
              "2. Consultas de prueba\n"
              "8. Salir")

        opcion = int(input("Introduzca una opción: "))
        if opcion == 1:
            agregarPersonasIniciales()
        elif opcion == 2:
            consultasDePrueba()
        elif opcion == 8:
            sys.exit(1)
        else:
            print("Opción no válida")
