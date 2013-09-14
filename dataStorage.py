import os
import pickle,cPickle,json

class dataStorage():
    location = os.getcwd()
    
    def setFileLocation(self, location):
        self.location=location
    def save(self,data,filename):
        raise NotImplementedError("provide concrete implementation")
        return
    def load(self,filename):
        raise NotImplementedError("provide concrete implementation")
        return

class dataStoragePickle(dataStorage):
    def save(self,data,filename):
        if data:
            pickle.dump(data,file(os.path.normpath(self.location+"/"+filename),"w+"))
        else:
            raise TypeError("no data specified")

    def load(self,filename):
        return pickle.load(file(self.location+"/"+filename,"r+"))

class dataStorageCPickle(dataStorage):
    def save(self,data,filename):
        if data:
            cPickle.dump(data,file(os.path.normpath(self.location+"/"+filename),"w+"))
        else:
            raise TypeError("no data specified")

    def load(self,filename):
        return cPickle.load(file(self.location+"/"+filename,"r+"))

class dataStorageJSON(dataStorage):
    def save(self,data,filename):
        if data:
            json.dump(data,file(os.path.normpath(self.location+"/"+filename),"w+"))
        else:
            raise TypeError("no data specified")
    def load(self,filename):
        return json.load(file(self.location+"/"+filename,"r+"))

class dataStorageXML(dataStorage):
    pass
