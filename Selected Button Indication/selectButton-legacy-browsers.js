/********************* 
 * Selectbutton Test *
 *********************/


// store info about the experiment session:
let expName = 'selectButton';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(trialRoutineBegin());
flowScheduler.add(trialRoutineEachFrame());
flowScheduler.add(trialRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.0';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var trialClock;
var button_1;
var button_2;
var button_3;
var mouse;
var buttons;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  button_1 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_1',
    text: 'Button #1',
    fillColor: 'darkgray',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.5), 0],
    letterHeight: 0.05,
    size: [0.35, 0.2],
    depth: 0
  });
  button_1.clock = new util.Clock();
  
  button_2 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_2',
    text: 'Button #2',
    fillColor: 'darkgray',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, 0],
    letterHeight: 0.05,
    size: [0.35, 0.2],
    depth: -1
  });
  button_2.clock = new util.Clock();
  
  button_3 = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button_3',
    text: 'Button #3',
    fillColor: 'darkgray',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.5, 0],
    letterHeight: 0.05,
    size: [0.35, 0.2],
    depth: -2
  });
  button_3.clock = new util.Clock();
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  buttons = [button_1, button_2, button_3];
  function buttonSelector(selectedButton) {
      for (var btn, _pj_c = 0, _pj_a = buttons, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
          btn = _pj_a[_pj_c];
          if ((btn === selectedButton)) {
              btn.fillColor = "orange";
          } else {
              btn.fillColor = "darkgray";
          }
      }
  }
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var gotValidClick;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // reset button_1 to account for continued clicks & clear times on/off
    button_1.reset()
    // reset button_2 to account for continued clicks & clear times on/off
    button_2.reset()
    // reset button_3 to account for continued clicks & clear times on/off
    button_3.reset()
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(button_1);
    trialComponents.push(button_2);
    trialComponents.push(button_3);
    trialComponents.push(mouse);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
var currentButton;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *button_1* updates
    if (t >= 0 && button_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_1.tStart = t;  // (not accounting for frame time here)
      button_1.frameNStart = frameN;  // exact frame index
      
      button_1.setAutoDraw(true);
    }

    if (button_1.status === PsychoJS.Status.STARTED) {
      // check whether button_1 has been pressed
      if (button_1.isClicked) {
        if (!button_1.wasClicked) {
          // store time of first click
          button_1.timesOn.push(button_1.clock.getTime());
          button_1.numClicks += 1;
          // store time clicked until
          button_1.timesOff.push(button_1.clock.getTime());
        } else {
          // update time clicked until;
          button_1.timesOff[button_1.timesOff.length - 1] = button_1.clock.getTime();
        }
        if (!button_1.wasClicked) {
        }
        // if button_1 is still clicked next frame, it is not a new click
        button_1.wasClicked = true;
      } else {
        // if button_1 is clicked next frame, it is a new click
        button_1.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_1 hasn't started / has finished
      button_1.clock.reset();
      // if button_1 is clicked next frame, it is a new click
      button_1.wasClicked = false;
    }
    
    // *button_2* updates
    if (t >= 0 && button_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_2.tStart = t;  // (not accounting for frame time here)
      button_2.frameNStart = frameN;  // exact frame index
      
      button_2.setAutoDraw(true);
    }

    if (button_2.status === PsychoJS.Status.STARTED) {
      // check whether button_2 has been pressed
      if (button_2.isClicked) {
        if (!button_2.wasClicked) {
          // store time of first click
          button_2.timesOn.push(button_2.clock.getTime());
          button_2.numClicks += 1;
          // store time clicked until
          button_2.timesOff.push(button_2.clock.getTime());
        } else {
          // update time clicked until;
          button_2.timesOff[button_2.timesOff.length - 1] = button_2.clock.getTime();
        }
        if (!button_2.wasClicked) {
        }
        // if button_2 is still clicked next frame, it is not a new click
        button_2.wasClicked = true;
      } else {
        // if button_2 is clicked next frame, it is a new click
        button_2.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_2 hasn't started / has finished
      button_2.clock.reset();
      // if button_2 is clicked next frame, it is a new click
      button_2.wasClicked = false;
    }
    
    // *button_3* updates
    if (t >= 0 && button_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_3.tStart = t;  // (not accounting for frame time here)
      button_3.frameNStart = frameN;  // exact frame index
      
      button_3.setAutoDraw(true);
    }

    if (button_3.status === PsychoJS.Status.STARTED) {
      // check whether button_3 has been pressed
      if (button_3.isClicked) {
        if (!button_3.wasClicked) {
          // store time of first click
          button_3.timesOn.push(button_3.clock.getTime());
          button_3.numClicks += 1;
          // store time clicked until
          button_3.timesOff.push(button_3.clock.getTime());
        } else {
          // update time clicked until;
          button_3.timesOff[button_3.timesOff.length - 1] = button_3.clock.getTime();
        }
        if (!button_3.wasClicked) {
        }
        // if button_3 is still clicked next frame, it is not a new click
        button_3.wasClicked = true;
      } else {
        // if button_3 is clicked next frame, it is a new click
        button_3.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button_3 hasn't started / has finished
      button_3.clock.reset();
      // if button_3 is clicked next frame, it is a new click
      button_3.wasClicked = false;
    }
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button_1, button_2, button_3]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
        }
      }
    }
    // Run 'Each Frame' code from code
    buttons = [button_1, button_2, button_3];
    if (mouse.clicked_name.length) {
        currentButton = mouse.clicked_name.slice((- 1))[0];
        for (var btn, _pj_c = 0, _pj_a = buttons, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            btn = _pj_a[_pj_c];
            if ((currentButton === btn.name)) {
                currentButton = btn;
            }
        }
        buttonSelector(currentButton);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('button_1.numClicks', button_1.numClicks);
    psychoJS.experiment.addData('button_1.timesOn', button_1.timesOn);
    psychoJS.experiment.addData('button_1.timesOff', button_1.timesOff);
    psychoJS.experiment.addData('button_2.numClicks', button_2.numClicks);
    psychoJS.experiment.addData('button_2.timesOn', button_2.timesOn);
    psychoJS.experiment.addData('button_2.timesOff', button_2.timesOff);
    psychoJS.experiment.addData('button_3.numClicks', button_3.numClicks);
    psychoJS.experiment.addData('button_3.timesOn', button_3.timesOn);
    psychoJS.experiment.addData('button_3.timesOff', button_3.timesOff);
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
