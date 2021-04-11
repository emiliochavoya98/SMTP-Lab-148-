from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.mail.yahoo.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mail_from_cmmnd = "MAIL FROM: <emiliochavoya@yahoo.com>\r\n"
clientSocket.send(mail_from_cmmnd.encode())
recv2 = clientSocket.recv(1024).decode()
print("Server response -> MAIL FROM: " + recv2)


# Send RCPT TO command and print server response.
rcpt = "RCPT TO: <pchavoya@gmail.com>\r\n"
clientSocket.send(rcpt.encode())
recv3 =clientSocket.recv(1024).decode()
print("Server response -> RCPT TO: " + recv3)

# Send DATA command and print server response.
data_cmmnd ="DATA\r\n"
clientSocket.send(data_cmmnd.encode())
recv4 = clientSocket.recv(1024).decode()
print("Server response -> DATA: " + recv4)

# Send message data.
clientSocket.send(msg.encode())
recv5 = clientSocket.recv(1024).decode()
print("Server response -> Message: " + recv5)

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

# Send QUIT command and get server response.
quit_cmmd = "QUIT\r\n"
clientSocket.send(quit_cmmd.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
