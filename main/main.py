import engine
import getpass
import socket

Running = True
global instance
instance = engine.Engine()
instance.jsoninit()
instance.pymrk_convert()
instance._autorun()
instance.pymrk_convert()
host = getpass.getuser() + "@" + socket.gethostname() + ": "

while Running:
    c = input(host)
    ext_param = ""
    cmd = c
    
    matching_key = next((key for key in instance.commands if c.startswith(key)), None)
    if matching_key is not None:
        cmd = matching_key
        
        ext_param = (str(c).split())
        ext_param.pop(0)
        
        instance.run(matching_key, {"ext_param":ext_param})
        
    elif not c.isspace() and not c == "":
        print(f"command '{cmd.strip()}' not found")