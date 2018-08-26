#! /usr/bin/python3
import socket
if __name__ == '__main__':

    # import socket
    #
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = "localhost"
    # port = 1234
    #
    # s.connect((host,port))
    #
    #
    # # r=input('Enter message   ')
    # # s.send(r.encode())
    # s.send('asdf')
    # # data = ''
    # # data = s.recv(1024).decode()
    # # print (data)
    #
    # s.close ()

    import requests
    r = requests.post("http://localhost:1234", data={'number': 12524, 'type': 'issue', 'action': 'show'})
