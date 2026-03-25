agenda = {}

# Añadir elementos
agenda["Juan"] = "555-1234"
agenda["Maria"] = "555-5678"
print("Diccionario creado:", agenda)

# 2. READ (Leer) - Acceder a un valor
telefono_juan = agenda.get("Juan")
print("Teléfono de Juan:", telefono_juan)

# 3. UPDATE (Actualizar) - Cambiar un valor
agenda["Juan"] = "555-9999"
print("Diccionario actualizado:", agenda)

# 4. DELETE (Borrar) - Eliminar un elemento
del agenda["Maria"]
# O también: agenda.pop("Maria")
print("Diccionario final:", agenda)