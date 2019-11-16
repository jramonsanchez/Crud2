import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='pruebapy')
with conn:
    cursors = conn.cursor()
    cursors.execute("SELECT VERSION()")
    version = cursors.fetchone()
    print("Database version: {}".format(version[0]))
    print("Connection successfully done.")

def insertarRegistro():
    print(" --- Insert registers ---")
    #Retrieving data
    id = input("Ingrese ID::")
    name1 = input("Nombre del Trabajador::")
    salary1 = input("Salario del trabajador::")
    sql = "INSERT INTO `trabajadores` (`code`, `nombre`, `sueldo`) VALUES (%s, %s, %s);"
    val = (str(id),str(name1),str(salary1))
    # cursor executes the sentence
    cursors.execute(sql, val)
    # Commit for saving changes
    conn.commit()
    print(cursors.rowcount, "Worker inserted ..")

def cambiarRegistro():
    print(" --- Edit registers ---")
    #Retrieving data
    clavicordio = input("Ingrese el ID del Trabajador:")
    loo = 1
    while loo==1:
        opc = input("1.- Modificar nombre\n 2.-Modificar sueldo")
        loo = 2
        if opc==1:
            nom =  input("Input the new name:")
            sql = "UPDATE Trabajadores Set nombre= " + nom + "WHERE ID = "+ clavicordio+";"
        if opc==2:
            sal = input("Input the new name:")
            sql = "UPDATE Trabajadores Set sueldo= " + sal + "WHERE ID = "+ clavicordio+";"
    # sql sentence again
    cursors.execute(sql)
    conn.commit()
    print("Done update!")

def buscarRegistro():
    print(" --- Search registers ---")
    clavicordio = input("Ingrese el ID del Trabajador::")
    sql = "SELECT * FROM trabajadores(code, nombre, sueldo) WHERE ID = "+ clavicordio+";"
    # sql sentence
    cursors.execute(sql)
    # .fetchall brings all tuples
    fetched = cursors.fetchall()
    # loop to show all
    for i in fetched:
        print(i)
    conn.commit()

def borrarRegistro():
    print(" --- Delete registers ---")
    clavicordio = input("Ingrese el ID del Trabajador::")
    sql = "DELETE FROM `trabajadores` WHERE `trabajadores`.`id` "+ clavicordio+";"
    cursors.execute(sql)
    conn.commit()

def listarRegistros():
    print(" --- All tha slaves ---")
    sql = "SELECT * FROM trabajadores"
    cursors.execute(sql)
    fetched = cursors.fetchall()
    for i in fetched:
        print(i)
    conn.commit()
#Main function
def main():
    print(" --- CRUD with MYSQL ---")
    print("1. Insertar Trabajador\n2. Buscar Trabajador\n3.- Modificar")
    print("4. Elimiar \n5. Lista de Trabajadores \n6. Salir\n")
    opt = input("Select an option between 1 and 6: ")
    print(opt)
    if opt == 1:
        insertarRegistro()
    elif opt == 2:
         buscarRegistro()
    elif opt == 3:
         cambiarRegistro()
    elif opt == 4:
         borrarRegistro()
    elif opt == 5:
         listarRegistros()
    elif opt == 6:
         exit()
if __name__ == "__main__":
    main()
