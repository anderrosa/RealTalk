from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Cria a aplicação Flask
app = Flask('__name__')

# Inicializa o SocketIO com suporte a CORS (permitindo conexões de qualquer origem)
socketio = SocketIO(app, cors_allowed_origins="*")

# Define a rota principal para renderizar o arquivo index.html
@app.route('/')
def index():
    return render_template('index.html')  # Retorna a página HTML onde o chat será exibido

# Evento do SocketIO que escuta mensagens enviadas pelos clientes
@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")  # Exibe a mensagem recebida no terminal
    send(msg, broadcast=True)  # Reenvia a mensagem para todos os clientes conectados

# Inicia o servidor Flask com suporte a WebSockets
if __name__ == '__main__':
    # Define o host como '0.0.0.0' para permitir conexões externas
    socketio.run(app, debug=True, host='0.0.0.0')