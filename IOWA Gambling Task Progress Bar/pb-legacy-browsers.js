/*********** 
 * Pb Test *
 ***********/


// store info about the experiment session:
let expName = 'pb';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code
win_sum = 0;
lose_sum = 0;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color(''),
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
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
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
var header;
var plus;
var minus;
var win_lose;
var green;
var red;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  header = new visual.TextStim({
    win: psychoJS.window,
    name: 'header',
    text: 'Progress Bar Example',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  plus = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'plus',
    text: '+100 | Win',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [0.3, (- 0.4)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  plus.clock = new util.Clock();
  
  minus = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'minus',
    text: '- 100 | Lose',
    fillColor: 'darkgrey',
    borderColor: null,
    color: 'white',
    colorSpace: 'rgb',
    pos: [(- 0.3), (- 0.4)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  minus.clock = new util.Clock();
  
  win_lose = new visual.TextStim({
    win: psychoJS.window,
    name: 'win_lose',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  green = new visual.Slider({
    win: psychoJS.window, name: 'green',
    startValue: 0,
    size: [1.0, 0.1], pos: [0, 0.1], ori: 0.0, units: 'height',
    labels: [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000], fontSize: 0.03, ticks: [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
    granularity: 100.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -5, 
    flip: false,
  });
  
  red = new visual.Slider({
    win: psychoJS.window, name: 'red',
    startValue: 0,
    size: [1.0, 0.1], pos: [0, (- 0.15)], ori: 0.0, units: 'height',
    labels: [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000], fontSize: 0.03, ticks: [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
    granularity: 100.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color([1.0, (- 1.0), (- 1.0)]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -6, 
    flip: false,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 999, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
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
    // Run 'Begin Routine' code from code
    green.startValue = win_sum;
    red.startValue = lose_sum;
    
    win_lose.setText((((win_sum.toString() + " Won | ") + lose_sum.toString()) + " Lost"));
    green.reset()
    red.reset()
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(header);
    trialComponents.push(plus);
    trialComponents.push(minus);
    trialComponents.push(win_lose);
    trialComponents.push(green);
    trialComponents.push(red);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *header* updates
    if (t >= 0.0 && header.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      header.tStart = t;  // (not accounting for frame time here)
      header.frameNStart = frameN;  // exact frame index
      
      header.setAutoDraw(true);
    }

    
    // *plus* updates
    if (t >= 0 && plus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plus.tStart = t;  // (not accounting for frame time here)
      plus.frameNStart = frameN;  // exact frame index
      
      plus.setAutoDraw(true);
    }

    if (plus.status === PsychoJS.Status.STARTED) {
      // check whether plus has been pressed
      if (plus.isClicked) {
        if (!plus.wasClicked) {
          // store time of first click
          plus.timesOn.push(plus.clock.getTime());
          plus.numClicks += 1;
          // store time clicked until
          plus.timesOff.push(plus.clock.getTime());
        } else {
          // update time clicked until;
          plus.timesOff[plus.timesOff.length - 1] = plus.clock.getTime();
        }
        if (!plus.wasClicked) {
          // end routine when plus is clicked
          continueRoutine = false;
          win_sum += 100;
        }
        // if plus is still clicked next frame, it is not a new click
        plus.wasClicked = true;
      } else {
        // if plus is clicked next frame, it is a new click
        plus.wasClicked = false;
      }
    } else {
      // keep clock at 0 if plus hasn't started / has finished
      plus.clock.reset();
      // if plus is clicked next frame, it is a new click
      plus.wasClicked = false;
    }
    
    // *minus* updates
    if (t >= 0 && minus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      minus.tStart = t;  // (not accounting for frame time here)
      minus.frameNStart = frameN;  // exact frame index
      
      minus.setAutoDraw(true);
    }

    if (minus.status === PsychoJS.Status.STARTED) {
      // check whether minus has been pressed
      if (minus.isClicked) {
        if (!minus.wasClicked) {
          // store time of first click
          minus.timesOn.push(minus.clock.getTime());
          minus.numClicks += 1;
          // store time clicked until
          minus.timesOff.push(minus.clock.getTime());
        } else {
          // update time clicked until;
          minus.timesOff[minus.timesOff.length - 1] = minus.clock.getTime();
        }
        if (!minus.wasClicked) {
          // end routine when minus is clicked
          continueRoutine = false;
          lose_sum += 100;
        }
        // if minus is still clicked next frame, it is not a new click
        minus.wasClicked = true;
      } else {
        // if minus is clicked next frame, it is a new click
        minus.wasClicked = false;
      }
    } else {
      // keep clock at 0 if minus hasn't started / has finished
      minus.clock.reset();
      // if minus is clicked next frame, it is a new click
      minus.wasClicked = false;
    }
    
    // *win_lose* updates
    if (t >= 0.0 && win_lose.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      win_lose.tStart = t;  // (not accounting for frame time here)
      win_lose.frameNStart = frameN;  // exact frame index
      
      win_lose.setAutoDraw(true);
    }

    
    // *green* updates
    if (t >= 0.0 && green.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      green.tStart = t;  // (not accounting for frame time here)
      green.frameNStart = frameN;  // exact frame index
      
      green.setAutoDraw(true);
    }

    
    // *red* updates
    if (t >= 0.0 && red.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      red.tStart = t;  // (not accounting for frame time here)
      red.frameNStart = frameN;  // exact frame index
      
      red.setAutoDraw(true);
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
    psychoJS.experiment.addData('plus.numClicks', plus.numClicks);
    psychoJS.experiment.addData('plus.timesOn', plus.timesOn);
    psychoJS.experiment.addData('plus.timesOff', plus.timesOff);
    psychoJS.experiment.addData('minus.numClicks', minus.numClicks);
    psychoJS.experiment.addData('minus.timesOn', minus.timesOn);
    psychoJS.experiment.addData('minus.timesOff', minus.timesOff);
    psychoJS.experiment.addData('green.response', green.getRating());
    psychoJS.experiment.addData('red.response', red.getRating());
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
