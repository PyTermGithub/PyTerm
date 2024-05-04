import engine

instance = engine.Engine()
instance.pymrk_convert()
Running = True

while Running:
    inp = input("key: ")
    if inp=='!$quit':
        Running = False
    else:
        try:
            print(instance.commands[inp])
        except Exception as error:
            print(error)