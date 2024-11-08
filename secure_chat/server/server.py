import socket
import threading
from client.diffie_hellman import generate_keys, calculate_shared_key
from client.caesar_cipher import caesar_cipher, caesar_decipher

# Configurações do servidor
SERVER_HOST = 'localhost'
SERVER_PORT = 3000

# Inicializa o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

def handle_client(client_socket):
    # Gera chaves Diffie-Hellman do servidor
    private_key, public_key = generate_keys()
    print(f"Servidor - Chave Privada: {private_key}, Chave Pública: {public_key}")

    # Recebe a chave pública do cliente e envia a chave pública do servidor
    client_public_key = int(client_socket.recv(1024).decode())
    client_socket.send(str(public_key).encode())

    # Calcula a chave compartilhada
    shared_key = calculate_shared_key(client_public_key, private_key)
    print(f"Servidor - Chave Compartilhada: {shared_key}")

    # Troca de mensagens
    try:
        while True:
            # Recebe mensagem cifrada, decifra e exibe
            encrypted_message = client_socket.recv(1024).decode()
            decrypted_message = caesar_decipher(encrypted_message, shared_key)
            print(f"Mensagem Recebida Decifrada: {decrypted_message}")

            # Envia resposta cifrada
            response = f"Recebido: {decrypted_message}"
            encrypted_response = caesar_cipher(response, shared_key)
            client_socket.send(encrypted_response.encode())
            print(f"Mensagem Cifrada Enviada: {encrypted_response}")

    finally:
        client_socket.close()

def start_server():
    print("Servidor ouvindo...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Nova conexão: {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
