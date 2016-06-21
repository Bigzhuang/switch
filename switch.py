
class Port():

    def __init__(self, Port, Status, Vlan):
        self.name = Port
        self.Status = Status
        self.Vlan = Vlan
        self.MacAddress = []

    def __repr__(self):
        return "Port:%s  Vlan:%s Status:%s  MacAddress:%s\n\n" % (
            self.name, self.Vlan, self.Status, self.MacAddress)
