# напиши здесь код создания и управления картой
class Mapmanager():
    """Managing Map"""
    def __init__(self):
        self.model = 'block' #the cube model is in the block.egg file
        #the following textures are used:
        self.texture = 'wood.png'
        #self.color = (0.2, 0.2, 0.35, 1) #rgba

        #create the main map node:
        self.startNew()
        #create building blocks
        self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        #self.block.setColor(self.color)
        self.block.reparentTo(self.land)
