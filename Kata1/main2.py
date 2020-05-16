password = "contraseña"

passwordUsuario = input("Introduce la contraseña: ")
passwordUsuario = passwordUsuario.lower()

if password == passwordUsuario :
    print("El password es correcto")
else:
    print("El password no es correcto")