def submit_data(data, client, address):
    client.connect(address)
    client.send(data.encode())
    client.close()