import socket
import requests

def get_local_ip():
    # Cria um socket e conecta-se a um servidor externo para obter o endereço IP local
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('8.8.8.8', 80))
        local_ip = sock.getsockname()[0]
    finally:
        sock.close()
    return local_ip

def get_public_ip():
    # Faz uma solicitação HTTP para obter o endereço IP público
    response = requests.get('https://api.ipify.org').text
    return response

# Obtém o endereço IP local
local_ip = get_local_ip()
print("Seu endereço IP local é:", local_ip)

# Obtém o endereço IP externo
public_ip = get_public_ip()
print("Seu endereço IP externo é:", public_ip)
