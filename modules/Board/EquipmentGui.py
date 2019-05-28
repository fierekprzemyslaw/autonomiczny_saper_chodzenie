from modules.Board.EquipmentGuiControl import EquipmentGuiControl


class EquipmentGui:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setEquipment(self, eq):
        self.items = eq

    def getRenderList(self):
        controlList = []
        current_y = 0
        for index, item in enumerate(self.items):
            if(index % 2 == 0):
                control = EquipmentGuiControl(item.sprite, 0, current_y)
            else:
                control = EquipmentGuiControl(item.sprite, 100, current_y)
                current_y += 100
            controlList.append(control)

        return controlList
