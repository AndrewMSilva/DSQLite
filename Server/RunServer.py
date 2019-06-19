from DSQLiteServer import DSQLiteServer

server = DSQLiteServer("Aa@Si12!", "2fT1@ds?")
server.Bind()
server.Listen()

while server.IsRunning():
    query = input('> ')
    if query.lower() == 'close':
        server.Close()
    else:
        server.QueryRead(query)