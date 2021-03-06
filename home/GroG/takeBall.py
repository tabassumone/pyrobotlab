import random
leftPort = "vleft"
rightPort = "vright"

###########################################################################
### special virtual blender handling - not in "regular" scripts - begin ###

# start blender service
blender = Runtime.start("blender", "Blender")

# connect blender service to running Blender (2.72b) instance
if (not blender.connect()):
	print("could not connect")

# get Blender.py version 
# FIXME - compare expected version !
blender.getVersion()

# pre-create Arduinos 
i01_left = Runtime.start("i01.left", "Arduino")
i01_right = Runtime.start("i01.right", "Arduino")

# blender "attach" will connect Arduinos with serial ports running
# over tcp/ip sockets to Blender.py
blender.attach(i01_left)
sleep(6)
blender.attach(i01_right)

### special virtual blender handling - not in "regular" scripts - end  ###
##########################################################################

i01 = Runtime.start("i01", "InMoov")
i01.startHead(leftPort)

i01.startLeftArm(leftPort)
i01.startRightArm(leftPort)
i01.startMouthControl(leftPort)
i01.startMouth()

#to tweak the default voice
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")

# tweaking default settings of eyes
i01.head.eyeY.setMinMax(0,180)
i01.head.eyeY.map(0,180,75,95)
i01.head.eyeY.setRest(85)
i01.head.eyeX.setMinMax(0,180)
i01.head.eyeX.map(0,180,70,100)
i01.head.eyeX.setRest(85)
i01.head.neck.setMinMax(0,180)
i01.head.neck.map(0,180,15,155)
i01.head.neck.setRest(70)
i01.head.rothead.setMinMax(0,180)
i01.head.rothead.map(0,180,30,150)
i01.head.rothead.setRest(86)

# tweaking default settings of jaw
i01.head.jaw.setMinMax(6,25)
#i01.head.jaw.map(0,180,10,35)
i01.mouthControl.setmouth(6,25)
##############
i01.startEar()
##############
torso = i01.startTorso(leftPort)
# tweaking default torso settings
torso.topStom.setMinMax(0,180)
torso.topStom.map(0,180,67,110)
torso.midStom.setMinMax(0,180)
torso.topStom.map(0,180,60,120)
#torso.lowStom.setMinMax(0,180)
#torso.topStom.setRest(90)
#torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
##############
i01.startLeftHand(leftPort)
# tweaking default settings of left hand
i01.leftHand.thumb.setMinMax(0,180)
i01.leftHand.index.setMinMax(0,180)
i01.leftHand.majeure.setMinMax(0,180)
i01.leftHand.ringFinger.setMinMax(0,180)
i01.leftHand.pinky.setMinMax(0,180)
i01.leftHand.thumb.map(0,180,45,140)
i01.leftHand.index.map(0,180,40,140)
i01.leftHand.majeure.map(0,180,30,176)
i01.leftHand.ringFinger.map(0,180,25,175)
i01.leftHand.pinky.map(0,180,15,112)
################
i01.startLeftArm(leftPort)
#tweak defaults LeftArm
#i01.leftArm.bicep.setMinMax(0,90)
#i01.leftArm.rotate.setMinMax(46,160)
#i01.leftArm.shoulder.setMinMax(30,100)
#i01.leftArm.omoplate.setMinMax(10,75)
################
i01.startRightHand(rightPort,"atmega2560")
# tweaking defaults settings of right hand
i01.rightHand.thumb.setMinMax(0,180)
i01.rightHand.index.setMinMax(0,180)
i01.rightHand.majeure.setMinMax(0,180)
i01.rightHand.ringFinger.setMinMax(0,180)
i01.rightHand.pinky.setMinMax(0,180)
i01.rightHand.thumb.map(0,180,55,135)
i01.rightHand.index.map(0,180,35,140)
i01.rightHand.majeure.map(0,180,8,120)
i01.rightHand.ringFinger.map(0,180,40,125)
i01.rightHand.pinky.map(0,180,10,110)
#################
i01.startRightArm(rightPort)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)

def takeball():
  rest()
  i01.setHandSpeed("right", 0.85, 0.75, 0.75, 0.75, 0.85, 0.75)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(30,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,76,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,140,140,3,0,11)
  i01.moveTorso(120,100,90)


def studyball():
##keepball():
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(3)
##approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,84)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
##uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(10,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,61,50,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,140,145,3,0,11)
  sleep(4)
##more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.80, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(13,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",80,114,114,3,0,11)
  sleep(3)
##handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.setArmSpeed("right", 0.85, 0.65, 0.65, 0.65)
  i01.moveHead(18,75)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",54,95,66,0,0,11)
  sleep(2)
#isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 0.8, 0.8, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(70,82)
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  i01.mouth.speakBlocking("I will start tracking the object")
  sleep(2)
  i01.mouth.speakBlocking("you need to set the point")

i01.speakBlocking("I think I am ready")
