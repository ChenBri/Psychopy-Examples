#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on May 09, 2023, at 20:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
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
win_sum = 0
lose_sum = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'pb'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\chenb\\Desktop\\Psychopy Examples\\IOWA Gambling Task Progress Bar\\pb_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='', colorSpace='rgb',
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
header = visual.TextStim(win=win, name='header',
    text='Progress Bar Example',
    font='Open Sans',
    pos=(0, 0.4), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
plus = visual.ButtonStim(win, 
    text='+100 | Win', font='Arvo',
    pos=(0.3, -0.4),
    letterHeight=0.05,
    size=[0.3, 0.15], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='plus'
)
plus.buttonClock = core.Clock()
minus = visual.ButtonStim(win, 
    text='- 100 | Lose', font='Arvo',
    pos=(-0.3, -0.4),
    letterHeight=0.05,
    size=[0.3, 0.15], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='minus'
)
minus.buttonClock = core.Clock()
win_lose = visual.TextStim(win=win, name='win_lose',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
green = visual.Slider(win=win, name='green',
    startValue=0, size=(1.0, 0.1), pos=(0, 0.1), units=None,
    labels=(0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000), ticks=(0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000), granularity=100.0,
    style='slider', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='white', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-5, readOnly=True)
red = visual.Slider(win=win, name='red',
    startValue=0, size=(1.0, 0.1), pos=(0, -0.15), units=None,
    labels=(0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000), ticks=(0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000), granularity=100.0,
    style='slider', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='white', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-6, readOnly=True)
polygon_green = visual.Rect(
    win=win, name='polygon_green',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(-0.5, 0.1), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=[-1.0000, 0.0039, -1.0000],
    opacity=None, depth=-7.0, interpolate=True)
polygon_red = visual.Rect(
    win=win, name='polygon_red',
    width=(1, 0.05)[0], height=(1, 0.05)[1],
    ori=0.0, pos=(-0.5, -0.15), anchor='center-left',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=999.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    #green.startValue= win_sum
    #red.startValue = lose_sum
    
    polygon_green.size = (win_sum/8000, 0.1)
    polygon_red.size = (lose_sum/8000, 0.1)
    
    win_lose.setText(str(win_sum) + " Won | " + str(lose_sum) + " Lost")
    green.reset()
    red.reset()
    # keep track of which components have finished
    trialComponents = [header, plus, minus, win_lose, green, red, polygon_green, polygon_red]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *header* updates
        if header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            header.frameNStart = frameN  # exact frame index
            header.tStart = t  # local t and not account for scr refresh
            header.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(header, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'header.started')
            header.setAutoDraw(True)
        
        # *plus* updates
        if plus.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            plus.frameNStart = frameN  # exact frame index
            plus.tStart = t  # local t and not account for scr refresh
            plus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'plus.started')
            plus.setAutoDraw(True)
        if plus.status == STARTED:
            # check whether plus has been pressed
            if plus.isClicked:
                if not plus.wasClicked:
                    plus.timesOn.append(plus.buttonClock.getTime()) # store time of first click
                    plus.timesOff.append(plus.buttonClock.getTime()) # store time clicked until
                else:
                    plus.timesOff[-1] = plus.buttonClock.getTime() # update time clicked until
                if not plus.wasClicked:
                    continueRoutine = False  # end routine when plus is clicked
                    win_sum += 100
                plus.wasClicked = True  # if plus is still clicked next frame, it is not a new click
            else:
                plus.wasClicked = False  # if plus is clicked next frame, it is a new click
        else:
            plus.wasClicked = False  # if plus is clicked next frame, it is a new click
        
        # *minus* updates
        if minus.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            minus.frameNStart = frameN  # exact frame index
            minus.tStart = t  # local t and not account for scr refresh
            minus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(minus, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'minus.started')
            minus.setAutoDraw(True)
        if minus.status == STARTED:
            # check whether minus has been pressed
            if minus.isClicked:
                if not minus.wasClicked:
                    minus.timesOn.append(minus.buttonClock.getTime()) # store time of first click
                    minus.timesOff.append(minus.buttonClock.getTime()) # store time clicked until
                else:
                    minus.timesOff[-1] = minus.buttonClock.getTime() # update time clicked until
                if not minus.wasClicked:
                    continueRoutine = False  # end routine when minus is clicked
                    lose_sum += 100
                minus.wasClicked = True  # if minus is still clicked next frame, it is not a new click
            else:
                minus.wasClicked = False  # if minus is clicked next frame, it is a new click
        else:
            minus.wasClicked = False  # if minus is clicked next frame, it is a new click
        
        # *win_lose* updates
        if win_lose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            win_lose.frameNStart = frameN  # exact frame index
            win_lose.tStart = t  # local t and not account for scr refresh
            win_lose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(win_lose, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'win_lose.started')
            win_lose.setAutoDraw(True)
        
        # *green* updates
        if green.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            green.frameNStart = frameN  # exact frame index
            green.tStart = t  # local t and not account for scr refresh
            green.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(green, 'tStartRefresh')  # time at next scr refresh
            green.setAutoDraw(True)
        
        # *red* updates
        if red.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red.frameNStart = frameN  # exact frame index
            red.tStart = t  # local t and not account for scr refresh
            red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red, 'tStartRefresh')  # time at next scr refresh
            red.setAutoDraw(True)
        
        # *polygon_green* updates
        if polygon_green.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_green.frameNStart = frameN  # exact frame index
            polygon_green.tStart = t  # local t and not account for scr refresh
            polygon_green.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_green, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_green.started')
            polygon_green.setAutoDraw(True)
        
        # *polygon_red* updates
        if polygon_red.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_red.frameNStart = frameN  # exact frame index
            polygon_red.tStart = t  # local t and not account for scr refresh
            polygon_red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_red, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_red.started')
            polygon_red.setAutoDraw(True)
        
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
    trials.addData('plus.numClicks', plus.numClicks)
    if plus.numClicks:
       trials.addData('plus.timesOn', plus.timesOn)
       trials.addData('plus.timesOff', plus.timesOff)
    else:
       trials.addData('plus.timesOn', "")
       trials.addData('plus.timesOff', "")
    trials.addData('minus.numClicks', minus.numClicks)
    if minus.numClicks:
       trials.addData('minus.timesOn', minus.timesOn)
       trials.addData('minus.timesOff', minus.timesOff)
    else:
       trials.addData('minus.timesOn', "")
       trials.addData('minus.timesOff', "")
    trials.addData('green.response', green.getRating())
    trials.addData('red.response', red.getRating())
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999.0 repeats of 'trials'


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
