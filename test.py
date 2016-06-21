import re,os,sys
from switch import Port




class Switch():

	MAC_RE=".*(\w{4}.\w{4}.\w{4})\s+\w+\s+(Fa0/\d+)\s"
	PORT_RE='(Fa0/\d+).*(connected|notconnect|disabled)\s+(\d+)'
	
	def __init__(self,file,dir_path):
		self.name=os.path.splitext(file)[0]
		self.ports=[]
		self.abs_path=dir_path+os.path.altsep+file

	def __repr__(self):
		return self.name
	
	def main(self):
		with open(self.abs_path,"r+") as f:
			while 1:
				line=f.readline()
				args=re.findall(Switch.PORT_RE,line)
				if args != []:
					port=Port(*args[0])
					# print port
					self.ports.append(port)
				if line is '':
					break
					# print line
				
	def get_mac(self):
		with open(self.abs_path,"r+") as f:
			while 1:
				line=f.readline()
				mac_ports=re.findall(Switch.MAC_RE,line)
				if mac_ports != []:
					for port in self.ports:
						if mac_ports[0][1] == port.name:
							port.MacAddress.append(mac_ports[0][0])
				elif line is '':
					break			

					

if __name__ == "__main__":
	try:
		if len(sys.argv) == 2:
			pass
			# print os.listdir(sys.argv[1])
	except WindowsError:
		print "path don't exsit!!!"

	switch_files=os.listdir(sys.argv[1])
	for file in switch_files:
		switch=Switch(file,sys.argv[1])
		switch.main()
		switch.get_mac()
		print switch
		print switch.ports
