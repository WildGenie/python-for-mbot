from lib.mBot import *
if __name__ == '__main__':
	def onDistance(dist):
		if dist<20 :
			bot.doMove(-100,-100)
			sleep(0.1)
			bot.doMove(100,-100)
			sleep(0.1)
		bot.doMove(100,100)
	bot = mBot()
	bot.startWithSerial("/dev/ttyUSB0")
		
	while(1):
		try:	
			bot.requestUltrasonicSensor(1,3,onDistance)
		except Exception,ex:
			print str(ex)
		sleep(0.5)