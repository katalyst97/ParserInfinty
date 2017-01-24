import re


class LogElements:
	def __init__(self):
		self.lineno = ''
		self.time = ''
		self.PID  = ''
		self.TID  = ''
		self.type = ''
		self.proj = ''
		self.msg  = ''


NUM = 1500
'''
Thsi regex filters mm-.. lines and that with module_
'''
# parsel = re.compile(r'\s([0-9]{2}):([0-9]{2}):([0-9]{2})\.([0-9]{3,4})\s*(\d*)\s*(\d*)\s*\w\s(mm-\w{1,8})[\:\s]{2}(module_\w{9,}:\d{1,}).{1,}\n');

#--------------sift=--line.number----- time-------:PID----:TID--:LogType-:msg content
parsel_Logline = r'.{1,4}\s*(\S*)\s*(\S*)\s*(\S*)\s([E|D])\s(mm-[\w\-]*)(.*)' 
# parsel_Logline = r'(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s([E|D])\s(mm-[\w\-]*)'

print("Hello World");
path = 'C:\\Users\\aneelam\\Documents\\Logs\\'
log = open(path+"logFDYUVDefault_YUV.txt",'r');
lines = log.readlines();

LE = LogElements();

lines = [line.replace('\0','') for line in lines if len(line) > 10];

opt = []

TIDs  = set([])
PIDs  = set([])
projs = set([])

log.close()

a = re.finditer(parsel_Logline,line);

i = 0;
	# print(line);
for line in lines:
	opt = re.findall(parsel_Logline,line);
#	i+=1;
#	print    i
	if len(opt):
		print("Inside");
		# print(a);
		print(opt[0]);
		LE.time = opt[0][0];
		LE.PID  = opt[0][1]; PIDs.add(LE.PID);
		LE.TID  = opt[0][2]; TIDs.add(LE.TID);
		LE.type = opt[0][3];
		LE.proj = opt[0][4]; projs.add(LE.proj);
		LE.msg  = opt[0][5];
print("Done");
