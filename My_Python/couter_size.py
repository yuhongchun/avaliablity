import os 

def size_in_bytes(fname):
    return os.stat(fname).st_size
def cwd_size_in_byes():
    total = 0
    for name in files_cwd():
        totoal = total + size_in_bytes(name)
    return total


cwd_size_in_byes()
