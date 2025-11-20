# Importa o módulo socket
from socket import *
import sys # Necessário para encerrar o programa
# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepara o socket do servidor
serverSocket.bind(('127.0.0.1', 6789))
serverSocket.listen()
while True:
# Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = connectionSocket.recv(1024).decode('utf-8')
        filename = message.split()[1]
        f = open(filename[1:], "r", encoding="utf-8")
        file = f.read()
        outputdata = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Content-Length: 13\r\n"
            "\r\n"
            "Hello, world!" +
            file
        )
        #
# Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            # Fecha a conexão com o cliente
            connectionSocket.close()
    except IOError:
# Envia mensagem de erro 404 se o arquivo não for encontrado
        noFileError = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 9\r\n"
            "\r\n"
            "Not Found"
        )
        # Fecha o socket do cliente
        connectionSocket.close()

serverSocket.close()
sys.exit() # Encerra o programa

"""
Questão 2:
(OBS: Carreguei o arquivo http-ethereal-trace pois a captura por algum motivo não estava dando certo no Wireshark.)

a. A versão do HTTP usada é a 1.1
b. Linguagem: en-us
c. De acordo com o ipconfig do prompt de comando do Windows, o IP do meu PC é 192.168.0.6. O IP do servidor/host é 128.119.245.12.
d. 200 OK, ou, no navegador, 304 Not Modified.
e. A partir do momento em que ele foi baixado.
f. De acordo com a Lista de Arquivos do Wireshark, 4443 bytes. No entanto, de acordo com a função "inspecionar" do navegador, 0.3kb.
g. Não. Ao inspecionar o navegador, nada é encontrado.
h. No navegador em Inspecionar -> Network -> HTTP-wireshark-file2.html e clicando em "Response", o código do HTML está presente, mas, com algumas tags faltando.

Infelizmente apenas consegui uma requisição HTTP em vez de duas, portanto, não poderei responder a I e a J.

"""

