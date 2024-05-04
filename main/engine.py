import os
import multiprocessing
import json

class Engine:
    def __init__(self) -> None:
        self.autorun = []
        self.dat = ""
        self.commands = {}
        self.docs = {}
        self.pymrk_initialize()
            
    def pymrk_convert(self):
        try:
            files = os.listdir("./PyMrk/Snippets/")

            for i in range(len(files)):
                file_path = "./PyMrk/Snippets/" + files[i]
        
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    self.commands[files[i]] = file_content
                file.close()
                
        except Exception as error:
            return error
            
    def pymrk_initialize(self):
        print("Welcome to pyterm")
        if not os.path.exists("PyMrk/Data"):
            cwd = os.getcwd()
            path = os.path.join(cwd, "PyMrk/Data")
            os.makedirs(f"{path}")
        if not os.path.exists("PyMrk/Snippets"):
            cwd = os.getcwd()
            path = os.path.join(cwd, "PyMrk/Snippets")
            os.makedirs(f"{path}")
        if not os.path.exists("PyMrk/Docs"):
            cwd = os.getcwd()
            path = os.path.join(cwd, "PyMrk/Docs")
            os.makedirs(f"{path}")
    
    def _autorun(self):
        processes = []

        for autokey in self.autorun:
            process = multiprocessing.Process(target=self.run, args=(autokey, None))
            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()
    
    def jsoninit(self):
        if not os.path.exists("./PyMrk/Data/autorun.json"):
            try:
                with open("./PyMrk/Data/autorun.json", 'w') as file:
                    json.dump([""], file, indent=2)
            except Exception as e:
                pass
        
        if os.path.exists("./PyMrk/Data/autorun.json"):
            with open("./PyMrk/Data/autorun.json", 'r') as file:
                self.dat = file.read()
            file.close()
    
        self.autorun = json.loads(self.dat)
    
    def run(self, cmd, glob):
        try:
            self.word = self.commands[f"{cmd}"]
            exec(str(self.word), glob)
        
            return str(self.word)

        except Exception as error:
            return error