import socket
from diffie_hellman import generate_keys, calculate_shared_key
from caesar_cipher import caesar_cipher, caesar_decipher

# Configurações
SERVER_HOST = 'localhost'
SERVER_PORT = 3000

# Inicializa o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Gera chaves do Diffie-Hellman
private_key, public_key = generate_keys()
print(f"Chave Privada: {private_key}, Chave Pública: {public_key}")

# Envia a chave pública para o servidor
client_socket.send(str(public_key).encode())

# Recebe a chave pública do servidor e calcula a chave compartilhada
server_public_key = int(client_socket.recv(1024).decode())
shared_key = calculate_shared_key(server_public_key, private_key)
print(f"Chave Compartilhada: {shared_key}")

# Inicia troca de mensagens
try:
    while True:
        # Envia mensagem cifrada
        message = input("Digite sua mensagem: ")
        encrypted_message = caesar_cipher(message, shared_key)
        client_socket.send(encrypted_message.encode())
        print(f"Mensagem Cifrada Enviada: {encrypted_message}")

        # Recebe e decifra a resposta
        encrypted_response = client_socket.recv(1024).decode()
        decrypted_response = caesar_decipher(encrypted_response, shared_key)
        print(f"Mensagem Recebida Decifrada: {decrypted_response}")

finally:
    client_socket.close()