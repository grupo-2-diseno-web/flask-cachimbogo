import hashlib
password = "d"
m = hashlib.sha256()
m.update(password.encode())
print(m.hexdigest())
