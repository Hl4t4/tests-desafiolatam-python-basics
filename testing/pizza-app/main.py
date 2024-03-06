masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
ingredientes = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamon", "Carne", "Tocino", "Queso"]

from change import change_masa
from change import change_salsa
from timing import pizza_timing
from add import add_ingrediente
from add import add_ingredientes
from remove import remove_ingrediente
from remove import remove_ingredientes
import show
import constructor

# def pizza_constructor(ingredientes = {}):
#     ingredientes_base = ({ingrediente:False for ingrediente in ingredientes})
#     pizza = {"masa": "Masa Tradicional", "salsa": "Salsa de Tomate", "ingredientes": ingredientes_base, "tiempo": 20}
#     return pizza

# def change_masa(pizza, new_masa):
#     global masas
#     new_pizza = pizza
#     if len([True for masa in masas if masa == new_masa]) >= 1:
#         new_pizza["masa"] = new_masa
#     else:
#         print(f"La masa {new_masa} no es una masa valida")
#         print(f"Probar con {masas}")
#     return new_pizza

# def change_salsa(pizza, new_salsa):
#     global salsas
#     new_pizza = pizza
#     new_pizza["salsa"] = new_salsa
#     if len([True for salsa in salsas if salsa == new_salsa]) >= 1:
#         new_pizza["salsa"] = new_salsa
#     else:
#         print(f"La salsa {new_salsa} no es una salsa valida")
#         print(f"Probar con {salsas}")
#     return new_pizza

# def pizza_timing(pizza):
#     new_pizza = pizza
#     new_pizza['tiempo'] = sum([2 for ingrediente, value in new_pizza['ingredientes'].items() if value]) + 20
#     return new_pizza

# def add_ingrediente(pizza, ingrediente):
#     new_pizza = pizza
#     if new_pizza['ingredientes'].get(ingrediente) != None:
#         new_pizza['ingredientes'][ingrediente] = True
#         new_pizza = pizza_timing(new_pizza)
#     else:
#         print(f"{ingrediente} es un ingrediente invalido")
#     return new_pizza

# def add_ingredientes(pizza, ingredientes):
#     new_pizza = pizza
#     for ingrediente in ingredientes:
#         new_pizza = add_ingrediente(new_pizza, ingrediente)
#     return new_pizza

# def remove_ingrediente(pizza, ingrediente):
#     new_pizza = pizza
#     if new_pizza['ingredientes'].get(ingrediente) != None:
#         new_pizza['ingredientes'][ingrediente] = False
#         new_pizza = pizza_timing(new_pizza)
#     else:
#         print(f"{ingrediente} es un ingrediente invalido")
#     return new_pizza

# def remove_ingredientes(pizza, ingredientes):
#     new_pizza = pizza
#     for ingrediente in ingredientes:
#         new_pizza = remove_ingrediente(new_pizza, ingrediente)
#     return new_pizza

# def show_ingredientes (pizza):
#     new_pizza = pizza
#     ingredientes = [ingrediente for ingrediente, value in new_pizza['ingredientes'].items() if value]
#     ingredientes = ", ".join(ingredientes)
#     return ingredientes
#     # print("Los ingredientes actuales son: ", ingredientes)

# def show_menu(ingredientes, salsas, masas):
#     current_command = None
#     print("Bienvenido a la App de Pizzas")
#     current_command = input("Desea ordenar una pizza?\n").lower()
#     if (current_command == 'si'):
#         new_pizza = constructor.pizza_constructor(ingredientes)
#         while(current_command != "5"):
#             print("Tiene las siguientes opciones:")
#             print("Cambiar el tipo de masa [1]")
#             print("Cambiar el tipo de salsa [2]")
#             print("Agregar un ingrediente [3]")
#             print("Quitar un ingrediente [4]")
#             print(f"Confirmar con la masa {new_pizza['masa']} con la salsa {new_pizza['salsa']} {show_ingredientes(new_pizza)} [5]")
#             current_command = input("Elija entre las opciones [1], [2], [3], [4] y [5]\n")
#             match current_command:
#                 case "1":
#                     print(f"Su tipo de masa actual es: {new_pizza['masa']}")
#                     new_masa = input(f"Elija un tipo de masa entre {', '.join(masas)}\n")
#                     new_pizza = change_masa(new_pizza, new_masa, masas)
#                 case "2":
#                     print(f"Su tipo de salsa actual es: {new_pizza['salsa']}")
#                     new_salsa = input(f"Elija un tipo de salsa entre {', '.join(salsas)}\n")
#                     new_pizza = change_salsa(new_pizza, new_salsa, salsas)
#                 case "3":
#                     print(f"Sus ingredientes actuales son: {show_ingredientes(new_pizza)}")
#                     new_ingrediente = input(f"Elija un ingrediente a agregar entre las siguientes opciones: {', '.join(ingredientes)}\n")
#                     new_pizza = add_ingrediente(new_pizza, new_ingrediente)
#                 case "4":
#                     print(f"Sus ingredientes actuales son: {show_ingredientes(new_pizza)}")
#                     new_ingrediente = input("Elija un ingrediente a eliminar\n")
#                     new_pizza = remove_ingrediente(new_pizza, new_ingrediente)
#                 case "5":
#                     print("Gracias por ordenar en App Pizza")
#                     print(f"Su pizza con masa: {new_pizza['masa']}")
#                     print(f"con salsa: {new_pizza['salsa']}")
#                     print(f"con ingredientes: {show_ingredientes(new_pizza)}")
#                     print(f"Estara lista en {new_pizza['tiempo']} minutos")
#                 case _:
#                     print("Solo los comandos [1], [2], [3], [4] y [5] son validos en este menu")
#     else:
#         print("Gracias por venir a la pizzeria")
#         exit()

# new_pizza = pizza_constructor(ingredientes)
# # print(new_pizza)
# new_pizza = change_masa(new_pizza, "Prueba", masas)
# # print(new_pizza)

# new_pizza = add_ingrediente(new_pizza, "Tomate")
# new_pizza = add_ingrediente(new_pizza, "Champiñones")
# new_pizza = add_ingrediente(new_pizza, "Cebolla")
# new_pizza = add_ingrediente(new_pizza, "Tocino")
# new_pizza = add_ingrediente(new_pizza, "Pollo")

# new_pizza = pizza_timing(new_pizza)

# show_ingredientes(new_pizza)


# print(new_pizza['ingredientes'].get("tomate", "no funciona"))
# print(new_pizza)
if __name__ == "__main__":
    show.show_menu(ingredientes, salsas, masas, constructor.pizza_constructor, change_masa, change_salsa, add_ingrediente, remove_ingrediente)
