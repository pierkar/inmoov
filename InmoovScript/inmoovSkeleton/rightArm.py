# ##############################################################################
#						*** RIGHT ARM ***
# ##############################################################################



  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config

ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isRightArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightArmActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')

except:
	errorSpokenFunc('ConfigParserProblem','rightarm.config')
	pass  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isRightArmActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected:
		talkEvent(lang_startingRightArm)
		rightArm = Runtime.create("i01.rightArm", "InMoovArm")
				
		rightArm.bicep.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'bicep'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'bicep')) 
		rightArm.shoulder.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'shoulder'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'shoulder')) 
		rightArm.rotate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'rotate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rotate')) 
		rightArm.omoplate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'omoplate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'omoplate')) 
		
		rightArm.bicep.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'bicep'))
		rightArm.shoulder.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'shoulder'))
		rightArm.rotate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rotate'))
		rightArm.omoplate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'omoplate'))

		rightArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'bicep'))
		rightArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'shoulder'))
		rightArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rotate'))
		rightArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'omoplate'))
		
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'bicep'):
			rightArm.bicep.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'shoulder'):
			rightArm.shoulder.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rotate'):
			rightArm.rotate.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'omoplate'):
			rightArm.omoplate.setInverted(True)

		i01.startRightArm(MyRightPort)
		
		if autoDetach:
			rightArm.bicep.enableAutoAttach(1)
			rightArm.shoulder.enableAutoAttach(1)
			rightArm.rotate.enableAutoAttach(1)
			rightArm.omoplate.enableAutoAttach(1)

		rightArm.rest()
		sleep(3)
		rightArm.detach()
	else:
		#we force parameter if arduino is off
		isRightArmActivated=0
		
#todo set inverted
