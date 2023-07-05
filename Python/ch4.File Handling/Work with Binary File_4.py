with open('src.png', 'rb') as src:
    data = src.read()
    with open('dst.png', 'wb') as dst:
        dst.write(data)