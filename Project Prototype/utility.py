import os

class Utility():
    def getFile(file: str) -> str:
        return os.path.join(os.getcwd(), file)
    
    def getSoundFile(file: str) -> str:
        return Utility.getFile(os.path.join("sound", file))
    
    def getGambarFile(file: str) -> str:
        return Utility.getFile(os.path.join("Gambar", file))
    
    def getBackgroundFile(file: str) -> str:
        return Utility.getFile(os.path.join("Background", file))
    
    def getWidgetFile(file: str) -> str:
        return Utility.getFile(os.path.join("Widget", file))