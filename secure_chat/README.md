# Secure Chat com Troca de Chave Segura

## Hierarquia de Pastas

secure_chat/
├── client/
│   ├── client.py            # Código principal do cliente TCP
│   ├── diffie_hellman.py    # Implementação do algoritmo de Diffie-Hellman
│   └── caesar_cipher.py     # Funções para cifrar e decifrar mensagens com a cifra de César
├── server/
│   └── server.py            # Código principal do servidor TCP
├── logs/
│   └── chat_log.txt         # Arquivo de log das operações (chaves, mensagens cifradas e decifradas)
├── README.md                # Descrição do projeto, instruções de instalação e uso


## Descrição
Este projeto implementa um chat TCP seguro com troca de chave Diffie-Hellman e cifra de César para criptografar as mensagens.

## Estrutura do Projeto
- `client/`: Contém o código do cliente, incluindo o Diffie-Hellman e a cifra de César.
- `server/`: Código do servidor que coordena as conexões e as trocas de mensagens.
- `logs/`: Armazena logs de debug e operações.


## Instruções para Executar
1. Inicie o servidor com `python server/server.py`.
2. Em uma nova janela de terminal, inicie o cliente com `python client/client.py`.
3. Envie mensagens entre cliente e servidor e observe os logs no console.

## Passos para Testar o Projeto
1. Inicializar o Servidor
Abra uma janela de terminal.

Navegue até o diretório secure_chat onde está o projeto.

Execute o comando para iniciar o servidor:

python server/server.py

O servidor estará ouvindo conexões na porta especificada (no exemplo, 12345). Quando ele for iniciado, você deverá ver uma mensagem de confirmação no console:

Servidor ouvindo...


2. Inicializar o Cliente
Abra outra janela de terminal (ou uma aba nova na mesma janela).

Navegue até o diretório secure_chat.

Execute o comando para iniciar o cliente:

python client/client.py

Quando o cliente iniciar, ele deverá conectar-se automaticamente ao servidor. No console do cliente, você deverá ver mensagens como:

Chave Privada: <valor>, Chave Pública: <valor>

No console do servidor, mensagens semelhantes aparecerão para indicar as chaves geradas e a chave pública recebida do cliente.

3. Testar a Troca de Mensagens Cifradas

No console do cliente, digite uma mensagem para enviar ao servidor e pressione Enter. A mensagem será cifrada usando a cifra de César com a chave compartilhada.

No console do servidor, a mensagem será decifrada e exibida em texto claro.

Exemplo de mensagens exibidas no servidor:

Mensagem Recebida Decifrada: Olá, servidor!
Mensagem Cifrada Enviada: Recebido: Olá, servidor!


