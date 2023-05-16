#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on February 27, 2023, at 17:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
def buttonSelector(selectedButton):
    for btn in buttons:
        if btn == selectedButton:
            btn.fillColor = "orange"
        else:
            btn.fillColor = "darkgray"
     



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'selectButton'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\chenb\\Desktop\\Psychopy Examples\\Selected Button Indication (V)\\selectButton_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trial" ---
button_1 = visual.ButtonStim(win, 
    text='Button #1', font='Arvo',
    pos=(-0.5, 0),
    letterHeight=0.05,
    size=(0.35, 0.2), borderWidth=0.0,
    fillColor='darkgray', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_1',
    depth=0
)
button_1.buttonClock = core.Clock()
button_2 = visual.ButtonStim(win, 
    text='Button #2', font='Arvo',
    pos=(0, 0),
    letterHeight=0.05,
    size=(0.35, 0.2), borderWidth=0.0,
    fillColor='darkgray', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_2',
    depth=-1
)
button_2.buttonClock = core.Clock()
button_3 = visual.ButtonStim(win, 
    text='Button #3', font='Arvo',
    pos=(0.5, 0),
    letterHeight=0.05,
    size=(0.35, 0.2), borderWidth=0.0,
    fillColor='darkgray', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_3',
    depth=-2
)
button_3.buttonClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "trial" ---
continueRoutine = True
# update component parameters for each repeat
# reset button_1 to account for continued clicks & clear times on/off
button_1.reset()
# reset button_2 to account for continued clicks & clear times on/off
button_2.reset()
# reset button_3 to account for continued clicks & clear times on/off
button_3.reset()
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [button_1, button_2, button_3, mouse]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *button_1* updates
    
    # if button_1 is starting this frame...
    if button_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_1.frameNStart = frameN  # exact frame index
        button_1.tStart = t  # local t and not account for scr refresh
        button_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'button_1.started')
        # update status
        button_1.status = STARTED
        button_1.setAutoDraw(True)
    
    # if button_1 is active this frame...
    if button_1.status == STARTED:
        # update params
        pass
        # check whether button_1 has been pressed
        if button_1.isClicked:
            if not button_1.wasClicked:
                # if this is a new click, store time of first click and clicked until
                button_1.timesOn.append(button_1.buttonClock.getTime())
                button_1.timesOff.append(button_1.buttonClock.getTime())
            elif len(button_1.timesOff):
                # if click is continuing from last frame, update time of clicked until
                button_1.timesOff[-1] = button_1.buttonClock.getTime()
            if not button_1.wasClicked:
                # run callback code when button_1 is clicked
                pass
    # take note of whether button_1 was clicked, so that next frame we know if clicks are new
    button_1.wasClicked = button_1.isClicked and button_1.status == STARTED
    # *button_2* updates
    
    # if button_2 is starting this frame...
    if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_2.frameNStart = frameN  # exact frame index
        button_2.tStart = t  # local t and not account for scr refresh
        button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'button_2.started')
        # update status
        button_2.status = STARTED
        button_2.setAutoDraw(True)
    
    # if button_2 is active this frame...
    if button_2.status == STARTED:
        # update params
        pass
        # check whether button_2 has been pressed
        if button_2.isClicked:
            if not button_2.wasClicked:
                # if this is a new click, store time of first click and clicked until
                button_2.timesOn.append(button_2.buttonClock.getTime())
                button_2.timesOff.append(button_2.buttonClock.getTime())
            elif len(button_2.timesOff):
                # if click is continuing from last frame, update time of clicked until
                button_2.timesOff[-1] = button_2.buttonClock.getTime()
            if not button_2.wasClicked:
                # run callback code when button_2 is clicked
                pass
    # take note of whether button_2 was clicked, so that next frame we know if clicks are new
    button_2.wasClicked = button_2.isClicked and button_2.status == STARTED
    # *button_3* updates
    
    # if button_3 is starting this frame...
    if button_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_3.frameNStart = frameN  # exact frame index
        button_3.tStart = t  # local t and not account for scr refresh
        button_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'button_3.started')
        # update status
        button_3.status = STARTED
        button_3.setAutoDraw(True)
    
    # if button_3 is active this frame...
    if button_3.status == STARTED:
        # update params
        pass
        # check whether button_3 has been pressed
        if button_3.isClicked:
            if not button_3.wasClicked:
                # if this is a new click, store time of first click and clicked until
                button_3.timesOn.append(button_3.buttonClock.getTime())
                button_3.timesOff.append(button_3.buttonClock.getTime())
            elif len(button_3.timesOff):
                # if click is continuing from last frame, update time of clicked until
                button_3.timesOff[-1] = button_3.buttonClock.getTime()
            if not button_3.wasClicked:
                # run callback code when button_3 is clicked
                pass
    # take note of whether button_3 was clicked, so that next frame we know if clicks are new
    button_3.wasClicked = button_3.isClicked and button_3.status == STARTED
    # *mouse* updates
    
    # if mouse is starting this frame...
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        # update status
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = core.getFromNames([button_1, button_2, button_3])
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    # Run 'Each Frame' code from code
    if len(mouse.clicked_name):
        buttons = [button_1, button_2, button_3]
        
        currentButton = mouse.clicked_name[-1]
        for btn in buttons:
            if currentButton == btn.name:
                currentButton = btn
            
        
        buttonSelector(currentButton)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_1.numClicks', button_1.numClicks)
if button_1.numClicks:
   thisExp.addData('button_1.timesOn', button_1.timesOn)
   thisExp.addData('button_1.timesOff', button_1.timesOff)
else:
   thisExp.addData('button_1.timesOn', "")
   thisExp.addData('button_1.timesOff', "")
thisExp.addData('button_2.numClicks', button_2.numClicks)
if button_2.numClicks:
   thisExp.addData('button_2.timesOn', button_2.timesOn)
   thisExp.addData('button_2.timesOff', button_2.timesOff)
else:
   thisExp.addData('button_2.timesOn', "")
   thisExp.addData('button_2.timesOff', "")
thisExp.addData('button_3.numClicks', button_3.numClicks)
if button_3.numClicks:
   thisExp.addData('button_3.timesOn', button_3.timesOn)
   thisExp.addData('button_3.timesOff', button_3.timesOff)
else:
   thisExp.addData('button_3.timesOn', "")
   thisExp.addData('button_3.timesOff', "")
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
