"""Escribe una clase Python llamada Restaurante"""
"""Las mesas estaran numeradas y tendran el nombre de la persona que reserva, estado de la mesa (si esta reservada o no)"""
"""Las ordenes tendran el nombre del cliente y los items deseados"""
"""Anhadir items al menu"""
"""Reservar mesas"""
"""Tomar pedidos del cliente"""
from flask import Flask, request, jsonify

app = Flask(__name__)

class Restaurante:
    def __init__(self):
        self.menu = {}
        self.mesas = []
        self.mesas_reservadas = {}
        self.ordenes = {}

    def add_item(self, item, precio):
        self.menu [item] = precio 

    def reservas_mesas(self, numero, nombre_cliente ):
        if numero not in self. mesas_reservadas:
            self.mesas_reservadas[numero] = nombre_cliente
        else:
            print(f"Lo sentimos, la mesa {numero} esta reservada")

    def cancelar_reserva(self, numero):
        if numero in self.mesas_reservadas:
            del self.mesas_reservadas[numero]
            return f"La reserva de la mesa {numero} ha sido cancelada"
        else:
            return f"No hay una reserva para la mesa {numero}"
        
    def pedidos (self, numero, items):
        if numero not in self.ordenes:
           self.ordenes[numero] = items
        else:
            self.ordenes[numero].append(items)
    def imprimir_menu(self):
        print(self.menu)

    def imprimir_reservas(self):
        print(self.mesas_reservadas)

    def imprimir_pedidos(self):
        print(self.ordenes)


    


restaurante = Restaurante()
restaurante.add_item("Pizza napolitana", 75000)
restaurante.add_item("Tamaño familiar", 100000)
restaurante.reservas_mesas(15, "Lorena Sanabria")
restaurante.reservas_mesas(9, "Cecilia Cabral")
restaurante.pedidos(15, ["Pizza napolitana", "Tamaño familiar"])
restaurante.pedidos(15, "Pizza napolitana")

@app.route('/cancelar_reserva', methods=['POST'])
def cancelar_reserva():
    numero_mesa = int(request.form['numero_mesa'])
    mensaje = restaurante.cancelar_reserva(numero_mesa)
    return jsonify({'mensaje': mensaje})

@app.route('/reservas')
def obtener_reservas():
    reservas = restaurante.obtener_reservas()
    return jsonify(reservas)

if __name__ == '__main__':
    app.run(debug=True)

"""print(restaurante.mesas_reservadas)
print(restaurante.menu)
print(restaurante.pedidos)
print(restaurante.ordenes)"""

restaurante.imprimir_menu()
restaurante.imprimir_reservas()
restaurante.imprimir_ordenes()



