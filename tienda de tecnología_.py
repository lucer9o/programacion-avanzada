print("Bienvenid@ a Luz Tecnology")
#The following code represents the process of a virtual technology store.
#Copyright (C) 2024  Lucero Riaño Gómez <dlrg@udistrital.edu.co>
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

# The code snippet you provided is defining two dictionaries in Python.
Catalogo ={
    "accesorios",
    "repuestos",
    "servicio tecnico"
}
Accesorios = {
    "Cargadores": 30000,
    "Hadware": 70000,
    "Formateo": 75000,
    "Seguridad": 130000
}


# The line `carrito = []` is initializing an empty list named `carrito`. This list will be used to
# store the products that the user adds to their shopping cart while interacting with the program.
carrito = []
#
# The `while True` loop is creating an infinite loop that continuously displays a menu to the user and
# prompts them to select an option. The menu options are:
while True:
    # The code snippet `print("\nMenú:")`, `print("1. Agregar productos al carrito")`, `print("2. Ver
    # carrito")`, and `print("3. Realizar el pago y salir")` is displaying a menu to the user with
    # three options:
    print("\nMenú:")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Realizar el pago y salir")

    # The line `opcion = input("Seleccione una opción: ")` is prompting the user to input their choice
    # from the menu options displayed. The user is expected to enter a number corresponding to the
    # action they want to perform within the program. This input is stored in the variable `opcion`
    # and is later used to determine which block of code should be executed based on the user's
    # selection.
    opcion = input("Seleccione una opción: ")

    # This block of code is executed when the user selects option "1" from the menu. It displays the
    # available products from the `Accesorios` dictionary along with their prices. The user is then
    # prompted to enter the name of the product they wish to add to their shopping cart. If the
    # entered product is found in the `Accesorios` dictionary, it is added to the `carrito` list,
    # representing the user's shopping cart. Finally, a message is displayed confirming that the
    # product has been successfully added to the cart.
    if opcion == "1":
        print("\nProductos disponibles Accesorios.Repuestos.Tecnico:")
        [print(f"• {producto} ${precio}") for producto, precio in Accesorios.items()]
        producto = input("Ingrese el nombre del producto que desea agregar: ").title()

        if producto in Accesorios:
            carrito.append(producto)
            print(f"Producto '{producto}' agregado al carrito.")
            

    # This block of code is executed when the user selects option "2" from the menu. 'elif' is responsible
    # for displaying the contents of the user's shopping cart.
    elif opcion == "2":
        print("\nCarrito:")
        for producto in  set(carrito):
            cantidad = carrito.count(producto)
            precio_unitario = Accesorios[producto]
            

            print(f"{cantidad} {producto} - ${precio_unitario} c/u")

   # The code block you provided is the functionality for when the user selects option "3" from the
   # menu. Here's a breakdown of what it does:
    elif opcion == "3":
        total_a_pagar = sum(Accesorios[producto] for producto in carrito)
        print(f"Total a pagar: ${total_a_pagar}")

        # The code snippet you provided within the `try` block is prompting the user to input specific
        # information related to the delivery address and contact details for a purchase. Here's a
        # breakdown of what each line is doing:
        try:
            domicilio = input("Ingrese nombre del receptor:")
            documento = input("Ingrese cedula de ciudadanía:")
            direccion = input("Ingrese su direccion:")
            telefono = input("ingrese su numero de celular:")

            # The code snippet `monto_pagado = float(input("Ingrese el monto con el que pagará: "))`
            # is prompting the user to input the amount they will pay for their purchase. The input is
            # converted to a floating-point number using `float()` to handle decimal values.
            monto_pagado = float(input("Ingrese el monto con el que pagará: "))
            cambio = monto_pagado - total_a_pagar
            
           # This code block is handling the scenario where the user has selected option "3" to
           # proceed with the payment and exit the program. It checks if the change (cambio)
           # calculated after the user has paid is greater than or equal to zero.
            if cambio >= 0:
                mensaje_cambio = f"Su cambio es: ${round(cambio, 2)}" if cambio > 0 else "¡Exacto! No se requiere cambio."
                print(f"Gracias por su compra. {mensaje_cambio}")
                break
            else:
                print("El monto ingresado es insuficiente. Por favor, ingrese un monto válido.")

        # The code snippet `except Exception as e:` is a part of a try-except block in Python. In this
        # context, it is used to catch any exception that might occur within the try block. If an
        # exception is raised during the execution of the code within the try block, the except block
        # will handle it.
        except Exception as e:
            print("Monto inválido. Por favor, ingrese un monto válido.")

    # The `else` block with `print("Opción no válida. Por favor, seleccione una opción válida.")` is
    # handling the scenario where the user inputs an option that is not recognized or valid. If the
    # user enters an option that is not "1", "2", or "3" from the menu, this block will execute and
    # display a message informing the user that the selected option is not valid. This helps guide the
    # user to choose a valid option from the menu presented to them.
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")