#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Thu Mar 12 18:36:01 2026
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from memory_sequence_code
import random

random.seed = 1

max_eccen = 0.4

def get_random_path_coord( coords_to_avoid ):
    # Select random x and y values that are different from those in coords_to_avoid
    x = coords_to_avoid[0]
    while abs(x - coords_to_avoid[0]) < 0.2:
       # x = round(max_eccen * random.uniform(-1, 1), 1)
        x = round(max_eccen * random.uniform(-1, 1) * 4, 0) / 4 # does this work?, YES
    y = coords_to_avoid[1]
    while abs(y - coords_to_avoid[1]) < 0.2:
        y = round(max_eccen * random.uniform(-1, 1), 1)
    coord = (x,y)
    return coord
# Run 'Before Experiment' code from memory_sequence_code
import random

random.seed = 1

max_eccen = 0.4

def get_random_path_coord( coords_to_avoid ):
    # Select random x and y values that are different from those in coords_to_avoid
    x = coords_to_avoid[0]
    while abs(x - coords_to_avoid[0]) < 0.2:
       # x = round(max_eccen * random.uniform(-1, 1), 1)
        x = round(max_eccen * random.uniform(-1, 1) * 4, 0) / 4 # does this work?, YES
    y = coords_to_avoid[1]
    while abs(y - coords_to_avoid[1]) < 0.2:
        y = round(max_eccen * random.uniform(-1, 1), 1)
    coord = (x,y)
    return coord
# Run 'Before Experiment' code from memory_sequence_code
import random

random.seed = 1

max_eccen = 0.4

def get_random_path_coord( coords_to_avoid ):
    # Select random x and y values that are different from those in coords_to_avoid
    x = coords_to_avoid[0]
    while abs(x - coords_to_avoid[0]) < 0.2:
       # x = round(max_eccen * random.uniform(-1, 1), 1)
        x = round(max_eccen * random.uniform(-1, 1) * 4, 0) / 4 # does this work?, YES
    y = coords_to_avoid[1]
    while abs(y - coords_to_avoid[1]) < 0.2:
        y = round(max_eccen * random.uniform(-1, 1), 1)
    coord = (x,y)
    return coord
# Run 'Before Experiment' code from memory_sequence_code
import random

random.seed = 1

max_eccen = 0.4

def get_random_path_coord( coords_to_avoid ):
    # Select random x and y values that are different from those in coords_to_avoid
    x = coords_to_avoid[0]
    while abs(x - coords_to_avoid[0]) < 0.2:
       # x = round(max_eccen * random.uniform(-1, 1), 1)
        x = round(max_eccen * random.uniform(-1, 1) * 4, 0) / 4 # does this work?, YES
    y = coords_to_avoid[1]
    while abs(y - coords_to_avoid[1]) < 0.2:
        y = round(max_eccen * random.uniform(-1, 1), 1)
    coord = (x,y)
    return coord
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'grouping-vwm-task'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': 'test',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1470, 956]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/rainaalam/Downloads/psych of aging/reseach 2/Visuospatial-Working-Memory-Task-main/grouping-vwm-task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color='', colorSpace='rgb',
            backgroundImage='abstract-art-3840x2160-23159.jpg', backgroundFit='fill',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = ''
        win.colorSpace = 'rgb'
        win.backgroundImage = 'abstract-art-3840x2160-23159.jpg'
        win.backgroundFit = 'fill'
        win.units = 'height'
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_single_instructions') is None:
        # initialise key_resp_single_instructions
        key_resp_single_instructions = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_single_instructions',
        )
    if deviceManager.getDevice('key_resp_VWM') is None:
        # initialise key_resp_VWM
        key_resp_VWM = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_VWM',
        )
    if deviceManager.getDevice('break_resp') is None:
        # initialise break_resp
        break_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='break_resp',
        )
    if deviceManager.getDevice('key_resp_seq_instructions') is None:
        # initialise key_resp_seq_instructions
        key_resp_seq_instructions = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_seq_instructions',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "set_block_order" ---
    
    # --- Initialize components for Routine "advance_block" ---
    # Run 'Begin Experiment' code from code_2
    current_block_idx = 0
    
    # --- Initialize components for Routine "single_probe_instructions" ---
    text_single_instructions = visual.TextStim(win=win, name='text_single_instructions',
        text='In this task, you will remember the locations of a disc. On some trials, the disc will move from place to place, pausing at each corner. On other trials, the disc will "jump" to different locations.\n\nAfter the disc returns to the cross, there will be a brief pause, and then the disc will appear at a single location. Your task is to determine whether that location is one of you\'ve seen the disc at before (press "F") or is different (press "J").\n\nPress space to continue to this part of the experiment.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_single_instructions = keyboard.Keyboard(deviceName='key_resp_single_instructions')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_display" ---
    # Run 'Begin Experiment' code from memory_sequence_code
    # Set path parameters
    path_length = 5
    pause_duration = 0.6 # in seconds
    retention_interval = 3.0 # 1000 ms
    
    # Movement speed (adjust for smoothness)
    #step_size = 0.01 # speeding up for debugging
    step_size = 0.1
    
    # colors 
    #white = [1,1,1]
    #gray = [0,0,0]
    disc_color = [1,1,1]
    mem_disc = visual.ShapeStim(
        win=win, name='mem_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    mem_fix = visual.ShapeStim(
        win=win, name='mem_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "retention" ---
    retention_fix = visual.ShapeStim(
        win=win, name='retention_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_probe" ---
    probe_disc = visual.ShapeStim(
        win=win, name='probe_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    probe_fix = visual.ShapeStim(
        win=win, name='probe_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_response" ---
    response_cue = visual.TextStim(win=win, name='response_cue',
        text='?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    response_instructions = visual.TextStim(win=win, name='response_instructions',
        text='',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_VWM = keyboard.Keyboard(deviceName='key_resp_VWM')
    
    # --- Initialize components for Routine "break_2" ---
    break_txt = visual.TextStim(win=win, name='break_txt',
        text='press space to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    break_resp = keyboard.Keyboard(deviceName='break_resp')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "sequence_probe_instructions" ---
    text_seq_instructions = visual.TextStim(win=win, name='text_seq_instructions',
        text='In this task, you will remember the locations of a disc. On some trials, the disc will move from place to place, pausing at each corner. On other trials, the disc will appear at individual locations, but you will not see it move.\n\nAfter the series of locations, there will be a brief pause, and then the disc will move again. Your task is to determine whether sequence of locations is the same as previously (press "F") or is different (press "J").\n\nPress space to continue to this part of the experiment.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_seq_instructions = keyboard.Keyboard(deviceName='key_resp_seq_instructions')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_display" ---
    # Run 'Begin Experiment' code from memory_sequence_code
    # Set path parameters
    path_length = 5
    pause_duration = 0.6 # in seconds
    retention_interval = 3.0 # 1000 ms
    
    # Movement speed (adjust for smoothness)
    #step_size = 0.01 # speeding up for debugging
    step_size = 0.1
    
    # colors 
    #white = [1,1,1]
    #gray = [0,0,0]
    disc_color = [1,1,1]
    mem_disc = visual.ShapeStim(
        win=win, name='mem_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    mem_fix = visual.ShapeStim(
        win=win, name='mem_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "retention" ---
    retention_fix = visual.ShapeStim(
        win=win, name='retention_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_probe" ---
    probe_disc = visual.ShapeStim(
        win=win, name='probe_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    probe_fix = visual.ShapeStim(
        win=win, name='probe_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_response" ---
    response_cue = visual.TextStim(win=win, name='response_cue',
        text='?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    response_instructions = visual.TextStim(win=win, name='response_instructions',
        text='',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_VWM = keyboard.Keyboard(deviceName='key_resp_VWM')
    
    # --- Initialize components for Routine "break_2" ---
    break_txt = visual.TextStim(win=win, name='break_txt',
        text='press space to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    break_resp = keyboard.Keyboard(deviceName='break_resp')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "advance_block" ---
    # Run 'Begin Experiment' code from code_2
    current_block_idx = 0
    
    # --- Initialize components for Routine "single_probe_instructions" ---
    text_single_instructions = visual.TextStim(win=win, name='text_single_instructions',
        text='In this task, you will remember the locations of a disc. On some trials, the disc will move from place to place, pausing at each corner. On other trials, the disc will "jump" to different locations.\n\nAfter the disc returns to the cross, there will be a brief pause, and then the disc will appear at a single location. Your task is to determine whether that location is one of you\'ve seen the disc at before (press "F") or is different (press "J").\n\nPress space to continue to this part of the experiment.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_single_instructions = keyboard.Keyboard(deviceName='key_resp_single_instructions')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_display" ---
    # Run 'Begin Experiment' code from memory_sequence_code
    # Set path parameters
    path_length = 5
    pause_duration = 0.6 # in seconds
    retention_interval = 3.0 # 1000 ms
    
    # Movement speed (adjust for smoothness)
    #step_size = 0.01 # speeding up for debugging
    step_size = 0.1
    
    # colors 
    #white = [1,1,1]
    #gray = [0,0,0]
    disc_color = [1,1,1]
    mem_disc = visual.ShapeStim(
        win=win, name='mem_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    mem_fix = visual.ShapeStim(
        win=win, name='mem_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "retention" ---
    retention_fix = visual.ShapeStim(
        win=win, name='retention_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_probe" ---
    probe_disc = visual.ShapeStim(
        win=win, name='probe_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    probe_fix = visual.ShapeStim(
        win=win, name='probe_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_response" ---
    response_cue = visual.TextStim(win=win, name='response_cue',
        text='?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    response_instructions = visual.TextStim(win=win, name='response_instructions',
        text='',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_VWM = keyboard.Keyboard(deviceName='key_resp_VWM')
    
    # --- Initialize components for Routine "break_2" ---
    break_txt = visual.TextStim(win=win, name='break_txt',
        text='press space to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    break_resp = keyboard.Keyboard(deviceName='break_resp')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "sequence_probe_instructions" ---
    text_seq_instructions = visual.TextStim(win=win, name='text_seq_instructions',
        text='In this task, you will remember the locations of a disc. On some trials, the disc will move from place to place, pausing at each corner. On other trials, the disc will appear at individual locations, but you will not see it move.\n\nAfter the series of locations, there will be a brief pause, and then the disc will move again. Your task is to determine whether sequence of locations is the same as previously (press "F") or is different (press "J").\n\nPress space to continue to this part of the experiment.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_seq_instructions = keyboard.Keyboard(deviceName='key_resp_seq_instructions')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_display" ---
    # Run 'Begin Experiment' code from memory_sequence_code
    # Set path parameters
    path_length = 5
    pause_duration = 0.6 # in seconds
    retention_interval = 3.0 # 1000 ms
    
    # Movement speed (adjust for smoothness)
    #step_size = 0.01 # speeding up for debugging
    step_size = 0.1
    
    # colors 
    #white = [1,1,1]
    #gray = [0,0,0]
    disc_color = [1,1,1]
    mem_disc = visual.ShapeStim(
        win=win, name='mem_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    mem_fix = visual.ShapeStim(
        win=win, name='mem_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "retention" ---
    retention_fix = visual.ShapeStim(
        win=win, name='retention_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_memory_probe" ---
    probe_disc = visual.ShapeStim(
        win=win, name='probe_disc',
        size=(0.1,0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    probe_fix = visual.ShapeStim(
        win=win, name='probe_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "VWM_response" ---
    response_cue = visual.TextStim(win=win, name='response_cue',
        text='?',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    response_instructions = visual.TextStim(win=win, name='response_instructions',
        text='',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_VWM = keyboard.Keyboard(deviceName='key_resp_VWM')
    
    # --- Initialize components for Routine "break_2" ---
    break_txt = visual.TextStim(win=win, name='break_txt',
        text='press space to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    break_resp = keyboard.Keyboard(deviceName='break_resp')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_fix = visual.ShapeStim(
        win=win, name='ITI_fix', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor='gray', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "thank_you" ---
    ty = visual.TextStim(win=win, name='ty',
        text='The experiment is now complete.\n\n\nThank you for your participation!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "set_block_order" ---
    # create an object to store info about Routine set_block_order
    set_block_order = data.Routine(
        name='set_block_order',
        components=[],
    )
    set_block_order.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    block_order = random.sample(['single', 'sequence'], 2)
    # e.g. ['sequence', 'single'] or ['single', 'sequence']
    thisExp.addData('block_order', block_order)  # saved to data file
    # store start times for set_block_order
    set_block_order.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    set_block_order.tStart = globalClock.getTime(format='float')
    set_block_order.status = STARTED
    thisExp.addData('set_block_order.started', set_block_order.tStart)
    set_block_order.maxDuration = None
    # keep track of which components have finished
    set_block_orderComponents = set_block_order.components
    for thisComponent in set_block_order.components:
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
    
    # --- Run Routine "set_block_order" ---
    set_block_order.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=set_block_order,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            set_block_order.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in set_block_order.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "set_block_order" ---
    for thisComponent in set_block_order.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for set_block_order
    set_block_order.tStop = globalClock.getTime(format='float')
    set_block_order.tStopRefresh = tThisFlipGlobal
    thisExp.addData('set_block_order.stopped', set_block_order.tStop)
    thisExp.nextEntry()
    # the Routine "set_block_order" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "advance_block" ---
    # create an object to store info about Routine advance_block
    advance_block = data.Routine(
        name='advance_block',
        components=[],
    )
    advance_block.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    current_block = block_order[current_block_idx]
    current_block_idx += 1
    single_nreps = 10 if current_block == 'single' else 0
    seq_nreps = 10 if current_block == 'sequence' else 0
    continueRoutine = False
    # store start times for advance_block
    advance_block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    advance_block.tStart = globalClock.getTime(format='float')
    advance_block.status = STARTED
    thisExp.addData('advance_block.started', advance_block.tStart)
    advance_block.maxDuration = None
    # keep track of which components have finished
    advance_blockComponents = advance_block.components
    for thisComponent in advance_block.components:
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
    
    # --- Run Routine "advance_block" ---
    advance_block.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=advance_block,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            advance_block.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in advance_block.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "advance_block" ---
    for thisComponent in advance_block.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for advance_block
    advance_block.tStop = globalClock.getTime(format='float')
    advance_block.tStopRefresh = tThisFlipGlobal
    thisExp.addData('advance_block.stopped', advance_block.tStop)
    thisExp.nextEntry()
    # the Routine "advance_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "single_probe_instructions" ---
    # create an object to store info about Routine single_probe_instructions
    single_probe_instructions = data.Routine(
        name='single_probe_instructions',
        components=[text_single_instructions, key_resp_single_instructions],
    )
    single_probe_instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_single_instructions
    key_resp_single_instructions.keys = []
    key_resp_single_instructions.rt = []
    _key_resp_single_instructions_allKeys = []
    # store start times for single_probe_instructions
    single_probe_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    single_probe_instructions.tStart = globalClock.getTime(format='float')
    single_probe_instructions.status = STARTED
    thisExp.addData('single_probe_instructions.started', single_probe_instructions.tStart)
    single_probe_instructions.maxDuration = None
    # skip Routine single_probe_instructions if its 'Skip if' condition is True
    single_probe_instructions.skipped = continueRoutine and not (current_block != 'single')
    continueRoutine = single_probe_instructions.skipped
    win.color = [0.0000, 0.0000, 0.0000]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    single_probe_instructionsComponents = single_probe_instructions.components
    for thisComponent in single_probe_instructions.components:
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
    
    # --- Run Routine "single_probe_instructions" ---
    single_probe_instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_single_instructions* updates
        
        # if text_single_instructions is starting this frame...
        if text_single_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_single_instructions.frameNStart = frameN  # exact frame index
            text_single_instructions.tStart = t  # local t and not account for scr refresh
            text_single_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_single_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_single_instructions.started')
            # update status
            text_single_instructions.status = STARTED
            text_single_instructions.setAutoDraw(True)
        
        # if text_single_instructions is active this frame...
        if text_single_instructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_single_instructions* updates
        waitOnFlip = False
        
        # if key_resp_single_instructions is starting this frame...
        if key_resp_single_instructions.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_single_instructions.frameNStart = frameN  # exact frame index
            key_resp_single_instructions.tStart = t  # local t and not account for scr refresh
            key_resp_single_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_single_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_single_instructions.started')
            # update status
            key_resp_single_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_single_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_single_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_single_instructions.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_single_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_single_instructions_allKeys.extend(theseKeys)
            if len(_key_resp_single_instructions_allKeys):
                key_resp_single_instructions.keys = _key_resp_single_instructions_allKeys[-1].name  # just the last key pressed
                key_resp_single_instructions.rt = _key_resp_single_instructions_allKeys[-1].rt
                key_resp_single_instructions.duration = _key_resp_single_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=single_probe_instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            single_probe_instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in single_probe_instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "single_probe_instructions" ---
    for thisComponent in single_probe_instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for single_probe_instructions
    single_probe_instructions.tStop = globalClock.getTime(format='float')
    single_probe_instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('single_probe_instructions.stopped', single_probe_instructions.tStop)
    setupWindow(expInfo=expInfo, win=win)
    # check responses
    if key_resp_single_instructions.keys in ['', [], None]:  # No response was made
        key_resp_single_instructions.keys = None
    thisExp.addData('key_resp_single_instructions.keys',key_resp_single_instructions.keys)
    if key_resp_single_instructions.keys != None:  # we had a response
        thisExp.addData('key_resp_single_instructions.rt', key_resp_single_instructions.rt)
        thisExp.addData('key_resp_single_instructions.duration', key_resp_single_instructions.duration)
    thisExp.nextEntry()
    # the Routine "single_probe_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    # create an object to store info about Routine ITI
    ITI = data.Routine(
        name='ITI',
        components=[ITI_fix],
    )
    ITI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI
    ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI.tStart = globalClock.getTime(format='float')
    ITI.status = STARTED
    thisExp.addData('ITI.started', ITI.tStart)
    ITI.maxDuration = 1
    # keep track of which components have finished
    ITIComponents = ITI.components
    for thisComponent in ITI.components:
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
    
    # --- Run Routine "ITI" ---
    ITI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ITI.maxDuration-frameTolerance:
            ITI.maxDurationReached = True
            continueRoutine = False
        
        # *ITI_fix* updates
        
        # if ITI_fix is starting this frame...
        if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ITI_fix.frameNStart = frameN  # exact frame index
            ITI_fix.tStart = t  # local t and not account for scr refresh
            ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_fix.started')
            # update status
            ITI_fix.status = STARTED
            ITI_fix.setAutoDraw(True)
        
        # if ITI_fix is active this frame...
        if ITI_fix.status == STARTED:
            # update params
            pass
        
        # if ITI_fix is stopping this frame...
        if ITI_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ITI_fix.tStop = t  # not accounting for scr refresh
                ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                ITI_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                # update status
                ITI_fix.status = FINISHED
                ITI_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ITI,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ITI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI
    ITI.tStop = globalClock.getTime(format='float')
    ITI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI.stopped', ITI.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI.maxDurationReached:
        routineTimer.addTime(-ITI.maxDuration)
    elif ITI.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_single_probe = data.TrialHandler2(
        name='trials_single_probe',
        nReps=single_nreps, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('experiment_control_files/trial-types_single-probe_2025-12-09.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials_single_probe)  # add the loop to the experiment
    thisTrials_single_probe = trials_single_probe.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_single_probe.rgb)
    if thisTrials_single_probe != None:
        for paramName in thisTrials_single_probe:
            globals()[paramName] = thisTrials_single_probe[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_single_probe in trials_single_probe:
        trials_single_probe.status = STARTED
        if hasattr(thisTrials_single_probe, 'status'):
            thisTrials_single_probe.status = STARTED
        currentLoop = trials_single_probe
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_single_probe.rgb)
        if thisTrials_single_probe != None:
            for paramName in thisTrials_single_probe:
                globals()[paramName] = thisTrials_single_probe[paramName]
        
        # --- Prepare to start Routine "VWM_memory_display" ---
        # create an object to store info about Routine VWM_memory_display
        VWM_memory_display = data.Routine(
            name='VWM_memory_display',
            components=[mem_disc, mem_fix],
        )
        VWM_memory_display.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from memory_sequence_code
        # Get locations for this trial
        path_coords = []
        ## path coords is a list of (x,y) tuples
        for segment in range(path_length):
            if segment == 0:
                segment_coord = (0,0)
            else:
                segment_coord = get_random_path_coord(path_coords[segment-1])
        
            path_coords.append(segment_coord)
        #print(path_coords)
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position
        disc_position = path_coords[segment]
        
        disc_alpha = 1
        path_end = path_coords[segment + 1]
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        # add data to output
        thisExp.addData('path_coords', path_coords)
        
        
        # store start times for VWM_memory_display
        VWM_memory_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_display.tStart = globalClock.getTime(format='float')
        VWM_memory_display.status = STARTED
        thisExp.addData('VWM_memory_display.started', VWM_memory_display.tStart)
        VWM_memory_display.maxDuration = None
        win.color = ''
        win.colorSpace = 'rgb'
        win.backgroundImage = 'abstract-art-3840x2160-23159.jpg'
        win.backgroundFit = 'none'
        # keep track of which components have finished
        VWM_memory_displayComponents = VWM_memory_display.components
        for thisComponent in VWM_memory_display.components:
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
        
        # --- Run Routine "VWM_memory_display" ---
        VWM_memory_display.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe, 'status') and thisTrials_single_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from memory_sequence_code
            
            if pause_timer.getTime() <= 0 and segment < path_length - 1:
                path_end = path_coords[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1        
                disc_position = (new_x, new_y)    
            elif segment >= path_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
            
            
            
            # *mem_disc* updates
            
            # if mem_disc is starting this frame...
            if mem_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_disc.frameNStart = frameN  # exact frame index
                mem_disc.tStart = t  # local t and not account for scr refresh
                mem_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_disc.started')
                # update status
                mem_disc.status = STARTED
                mem_disc.setAutoDraw(True)
            
            # if mem_disc is active this frame...
            if mem_disc.status == STARTED:
                # update params
                mem_disc.setFillColor(disc_alpha, log=False)
                mem_disc.setOpacity(disc_alpha, log=False)
                mem_disc.setPos(disc_position, log=False)
                mem_disc.setLineColor(disc_alpha, log=False)
            
            # *mem_fix* updates
            
            # if mem_fix is starting this frame...
            if mem_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_fix.frameNStart = frameN  # exact frame index
                mem_fix.tStart = t  # local t and not account for scr refresh
                mem_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_fix.started')
                # update status
                mem_fix.status = STARTED
                mem_fix.setAutoDraw(True)
            
            # if mem_fix is active this frame...
            if mem_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_display,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_display.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_display.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_display" ---
        for thisComponent in VWM_memory_display.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_display
        VWM_memory_display.tStop = globalClock.getTime(format='float')
        VWM_memory_display.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_display.stopped', VWM_memory_display.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # the Routine "VWM_memory_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "retention" ---
        # create an object to store info about Routine retention
        retention = data.Routine(
            name='retention',
            components=[retention_fix],
        )
        retention.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for retention
        retention.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        retention.tStart = globalClock.getTime(format='float')
        retention.status = STARTED
        thisExp.addData('retention.started', retention.tStart)
        retention.maxDuration = None
        # keep track of which components have finished
        retentionComponents = retention.components
        for thisComponent in retention.components:
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
        
        # --- Run Routine "retention" ---
        retention.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe, 'status') and thisTrials_single_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *retention_fix* updates
            
            # if retention_fix is starting this frame...
            if retention_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                retention_fix.frameNStart = frameN  # exact frame index
                retention_fix.tStart = t  # local t and not account for scr refresh
                retention_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(retention_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'retention_fix.started')
                # update status
                retention_fix.status = STARTED
                retention_fix.setAutoDraw(True)
            
            # if retention_fix is active this frame...
            if retention_fix.status == STARTED:
                # update params
                pass
            
            # if retention_fix is stopping this frame...
            if retention_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > retention_fix.tStartRefresh + retention_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    retention_fix.tStop = t  # not accounting for scr refresh
                    retention_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    retention_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'retention_fix.stopped')
                    # update status
                    retention_fix.status = FINISHED
                    retention_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=retention,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                retention.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in retention.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "retention" ---
        for thisComponent in retention.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for retention
        retention.tStop = globalClock.getTime(format='float')
        retention.tStopRefresh = tThisFlipGlobal
        thisExp.addData('retention.stopped', retention.tStop)
        # the Routine "retention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_memory_probe" ---
        # create an object to store info about Routine VWM_memory_probe
        VWM_memory_probe = data.Routine(
            name='VWM_memory_probe',
            components=[probe_disc, probe_fix],
        )
        VWM_memory_probe.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from probe_sequence_code
        # Get locations for this trial
        
        # by default, we reprise the prior coords
        path_coords_probe = path_coords.copy() # PYTHON VARIABLES ARE DUMB
        probe_length = path_length # Int, don't need to copy.
        
        print(memory_type)
        print(probe_type)
        print(probe_validity)
        
        if probe_validity == "lure":
            if probe_type == "sequence":
                print('generating a sequence lure')
                # pick a position — range 1 to path_length-1 so center (index 0) can be swapped
                lure_pos = int(round(random.uniform(1, path_length - 1),0))
                # swap lure_pos with lure_pos-1
                path_coords_probe[lure_pos] = path_coords[lure_pos - 1]
                path_coords_probe[lure_pos - 1] = path_coords[lure_pos]
        
            elif probe_type == "single":
                print('generating a single lure')
                probe_length = 1
                x = round(max_eccen * random.uniform(-1, 1), 1)
                y = round(max_eccen * random.uniform(-1, 1), 1)
                lure_coords = (x,y)
                a = 1
                while a:
                    for loc in path_coords:
                        x_distance = abs(loc[0] - lure_coords[0])
                        y_distance = abs(loc[1] - lure_coords[1])
                        if x_distance < 0.2 and y_distance < 0.2:
                            x = round(max_eccen * random.uniform(-1, 1), 1)
                            y = round(max_eccen * random.uniform(-1, 1), 1)
                            lure_coords = (x,y)
                            break
                        a = 0
                path_coords_probe = [lure_coords]
        
        else: # probe_validity == target
            if probe_type == "single":
                print('generating a single target')
                probe_pos = int(round(random.uniform(1, path_length-1),0))
                path_coords_probe = [path_coords_probe[probe_pos]]
                probe_length = 1
        
        # For sequence probes: prepend (0,0) as the travel-to-start step.
        # The disc always starts at center, AND center can appear as a
        # mid-sequence location when lure_pos=1 swaps index 0 into position 1.
        if probe_type == "sequence":
            path_coords_probe = [(0,0)] + path_coords_probe
            probe_length = path_length + 1
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position — always (0,0) for sequence (prepended above)
        disc_position = path_coords_probe[segment]
        disc_alpha = 1
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        if probe_type == "sequence":
            path_end = path_coords_probe[segment + 1]
        
        if probe_type == "sequence":
            response_string = "F same                           J different"
        else:
            response_string = "F old                                  J new"
        
        thisExp.addData('path_coords_probe', path_coords_probe)
        # store start times for VWM_memory_probe
        VWM_memory_probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_probe.tStart = globalClock.getTime(format='float')
        VWM_memory_probe.status = STARTED
        thisExp.addData('VWM_memory_probe.started', VWM_memory_probe.tStart)
        VWM_memory_probe.maxDuration = None
        # keep track of which components have finished
        VWM_memory_probeComponents = VWM_memory_probe.components
        for thisComponent in VWM_memory_probe.components:
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
        
        # --- Run Routine "VWM_memory_probe" ---
        VWM_memory_probe.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe, 'status') and thisTrials_single_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from probe_sequence_code
            if pause_timer.getTime() <= 0 and probe_type == "sequence" and segment < probe_length - 1:
                #path_end = path_coords[segment + 1]
                path_end = path_coords_probe[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1
                disc_position = (new_x, new_y)
            elif segment >= probe_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
                
            
            
            
            # *probe_disc* updates
            
            # if probe_disc is starting this frame...
            if probe_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_disc.frameNStart = frameN  # exact frame index
                probe_disc.tStart = t  # local t and not account for scr refresh
                probe_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_disc.started')
                # update status
                probe_disc.status = STARTED
                probe_disc.setAutoDraw(True)
            
            # if probe_disc is active this frame...
            if probe_disc.status == STARTED:
                # update params
                probe_disc.setFillColor(disc_alpha, log=False)
                probe_disc.setOpacity(disc_alpha, log=False)
                probe_disc.setPos(disc_position, log=False)
                probe_disc.setLineColor(disc_alpha, log=False)
            
            # *probe_fix* updates
            
            # if probe_fix is starting this frame...
            if probe_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_fix.frameNStart = frameN  # exact frame index
                probe_fix.tStart = t  # local t and not account for scr refresh
                probe_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_fix.started')
                # update status
                probe_fix.status = STARTED
                probe_fix.setAutoDraw(True)
            
            # if probe_fix is active this frame...
            if probe_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_probe,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_probe.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_probe.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_probe" ---
        for thisComponent in VWM_memory_probe.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_probe
        VWM_memory_probe.tStop = globalClock.getTime(format='float')
        VWM_memory_probe.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_probe.stopped', VWM_memory_probe.tStop)
        # the Routine "VWM_memory_probe" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_response" ---
        # create an object to store info about Routine VWM_response
        VWM_response = data.Routine(
            name='VWM_response',
            components=[response_cue, response_instructions, key_resp_VWM],
        )
        VWM_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        response_instructions.setText(response_string)
        # create starting attributes for key_resp_VWM
        key_resp_VWM.keys = []
        key_resp_VWM.rt = []
        _key_resp_VWM_allKeys = []
        # store start times for VWM_response
        VWM_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_response.tStart = globalClock.getTime(format='float')
        VWM_response.status = STARTED
        thisExp.addData('VWM_response.started', VWM_response.tStart)
        VWM_response.maxDuration = None
        # keep track of which components have finished
        VWM_responseComponents = VWM_response.components
        for thisComponent in VWM_response.components:
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
        
        # --- Run Routine "VWM_response" ---
        VWM_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe, 'status') and thisTrials_single_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_cue* updates
            
            # if response_cue is starting this frame...
            if response_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_cue.frameNStart = frameN  # exact frame index
                response_cue.tStart = t  # local t and not account for scr refresh
                response_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_cue.started')
                # update status
                response_cue.status = STARTED
                response_cue.setAutoDraw(True)
            
            # if response_cue is active this frame...
            if response_cue.status == STARTED:
                # update params
                pass
            
            # *response_instructions* updates
            
            # if response_instructions is starting this frame...
            if response_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_instructions.frameNStart = frameN  # exact frame index
                response_instructions.tStart = t  # local t and not account for scr refresh
                response_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_instructions.started')
                # update status
                response_instructions.status = STARTED
                response_instructions.setAutoDraw(True)
            
            # if response_instructions is active this frame...
            if response_instructions.status == STARTED:
                # update params
                pass
            
            # *key_resp_VWM* updates
            waitOnFlip = False
            
            # if key_resp_VWM is starting this frame...
            if key_resp_VWM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_VWM.frameNStart = frameN  # exact frame index
                key_resp_VWM.tStart = t  # local t and not account for scr refresh
                key_resp_VWM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_VWM, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_VWM.started')
                # update status
                key_resp_VWM.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_VWM.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_VWM.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_VWM.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_VWM.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_VWM_allKeys.extend(theseKeys)
                if len(_key_resp_VWM_allKeys):
                    key_resp_VWM.keys = _key_resp_VWM_allKeys[-1].name  # just the last key pressed
                    key_resp_VWM.rt = _key_resp_VWM_allKeys[-1].rt
                    key_resp_VWM.duration = _key_resp_VWM_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_response,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_response" ---
        for thisComponent in VWM_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_response
        VWM_response.tStop = globalClock.getTime(format='float')
        VWM_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_response.stopped', VWM_response.tStop)
        # check responses
        if key_resp_VWM.keys in ['', [], None]:  # No response was made
            key_resp_VWM.keys = None
        trials_single_probe.addData('key_resp_VWM.keys',key_resp_VWM.keys)
        if key_resp_VWM.keys != None:  # we had a response
            trials_single_probe.addData('key_resp_VWM.rt', key_resp_VWM.rt)
            trials_single_probe.addData('key_resp_VWM.duration', key_resp_VWM.duration)
        # the Routine "VWM_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_2" ---
        # create an object to store info about Routine break_2
        break_2 = data.Routine(
            name='break_2',
            components=[break_txt, break_resp],
        )
        break_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for break_resp
        break_resp.keys = []
        break_resp.rt = []
        _break_resp_allKeys = []
        # store start times for break_2
        break_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        break_2.tStart = globalClock.getTime(format='float')
        break_2.status = STARTED
        thisExp.addData('break_2.started', break_2.tStart)
        break_2.maxDuration = None
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        # keep track of which components have finished
        break_2Components = break_2.components
        for thisComponent in break_2.components:
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
        
        # --- Run Routine "break_2" ---
        break_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe, 'status') and thisTrials_single_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *break_txt* updates
            
            # if break_txt is starting this frame...
            if break_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_txt.frameNStart = frameN  # exact frame index
                break_txt.tStart = t  # local t and not account for scr refresh
                break_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_txt.started')
                # update status
                break_txt.status = STARTED
                break_txt.setAutoDraw(True)
            
            # if break_txt is active this frame...
            if break_txt.status == STARTED:
                # update params
                pass
            
            # *break_resp* updates
            waitOnFlip = False
            
            # if break_resp is starting this frame...
            if break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_resp.frameNStart = frameN  # exact frame index
                break_resp.tStart = t  # local t and not account for scr refresh
                break_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_resp.started')
                # update status
                break_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(break_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if break_resp.status == STARTED and not waitOnFlip:
                theseKeys = break_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _break_resp_allKeys.extend(theseKeys)
                if len(_break_resp_allKeys):
                    break_resp.keys = _break_resp_allKeys[-1].name  # just the last key pressed
                    break_resp.rt = _break_resp_allKeys[-1].rt
                    break_resp.duration = _break_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=break_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for break_2
        break_2.tStop = globalClock.getTime(format='float')
        break_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('break_2.stopped', break_2.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # check responses
        if break_resp.keys in ['', [], None]:  # No response was made
            break_resp.keys = None
        trials_single_probe.addData('break_resp.keys',break_resp.keys)
        if break_resp.keys != None:  # we had a response
            trials_single_probe.addData('break_resp.rt', break_resp.rt)
            trials_single_probe.addData('break_resp.duration', break_resp.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_fix],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = 1
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
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
        
        # --- Run Routine "ITI" ---
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe, 'status') and thisTrials_single_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ITI.maxDuration-frameTolerance:
                ITI.maxDurationReached = True
                continueRoutine = False
            
            # *ITI_fix* updates
            
            # if ITI_fix is starting this frame...
            if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                ITI_fix.frameNStart = frameN  # exact frame index
                ITI_fix.tStart = t  # local t and not account for scr refresh
                ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.started')
                # update status
                ITI_fix.status = STARTED
                ITI_fix.setAutoDraw(True)
            
            # if ITI_fix is active this frame...
            if ITI_fix.status == STARTED:
                # update params
                pass
            
            # if ITI_fix is stopping this frame...
            if ITI_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_fix.tStop = t  # not accounting for scr refresh
                    ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                    # update status
                    ITI_fix.status = FINISHED
                    ITI_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrials_single_probe as finished
        if hasattr(thisTrials_single_probe, 'status'):
            thisTrials_single_probe.status = FINISHED
        # if awaiting a pause, pause now
        if trials_single_probe.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_single_probe.status = STARTED
        thisExp.nextEntry()
        
    # completed single_nreps repeats of 'trials_single_probe'
    trials_single_probe.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "sequence_probe_instructions" ---
    # create an object to store info about Routine sequence_probe_instructions
    sequence_probe_instructions = data.Routine(
        name='sequence_probe_instructions',
        components=[text_seq_instructions, key_resp_seq_instructions],
    )
    sequence_probe_instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_seq_instructions
    key_resp_seq_instructions.keys = []
    key_resp_seq_instructions.rt = []
    _key_resp_seq_instructions_allKeys = []
    # store start times for sequence_probe_instructions
    sequence_probe_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    sequence_probe_instructions.tStart = globalClock.getTime(format='float')
    sequence_probe_instructions.status = STARTED
    thisExp.addData('sequence_probe_instructions.started', sequence_probe_instructions.tStart)
    sequence_probe_instructions.maxDuration = None
    # skip Routine sequence_probe_instructions if its 'Skip if' condition is True
    sequence_probe_instructions.skipped = continueRoutine and not (current_block != 'sequence' )
    continueRoutine = sequence_probe_instructions.skipped
    win.color = [0,0,0]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    sequence_probe_instructionsComponents = sequence_probe_instructions.components
    for thisComponent in sequence_probe_instructions.components:
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
    
    # --- Run Routine "sequence_probe_instructions" ---
    sequence_probe_instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_seq_instructions* updates
        
        # if text_seq_instructions is starting this frame...
        if text_seq_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_seq_instructions.frameNStart = frameN  # exact frame index
            text_seq_instructions.tStart = t  # local t and not account for scr refresh
            text_seq_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_seq_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_seq_instructions.started')
            # update status
            text_seq_instructions.status = STARTED
            text_seq_instructions.setAutoDraw(True)
        
        # if text_seq_instructions is active this frame...
        if text_seq_instructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_seq_instructions* updates
        waitOnFlip = False
        
        # if key_resp_seq_instructions is starting this frame...
        if key_resp_seq_instructions.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_seq_instructions.frameNStart = frameN  # exact frame index
            key_resp_seq_instructions.tStart = t  # local t and not account for scr refresh
            key_resp_seq_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_seq_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_seq_instructions.started')
            # update status
            key_resp_seq_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_seq_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_seq_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_seq_instructions.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_seq_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_seq_instructions_allKeys.extend(theseKeys)
            if len(_key_resp_seq_instructions_allKeys):
                key_resp_seq_instructions.keys = _key_resp_seq_instructions_allKeys[-1].name  # just the last key pressed
                key_resp_seq_instructions.rt = _key_resp_seq_instructions_allKeys[-1].rt
                key_resp_seq_instructions.duration = _key_resp_seq_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=sequence_probe_instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            sequence_probe_instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sequence_probe_instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sequence_probe_instructions" ---
    for thisComponent in sequence_probe_instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for sequence_probe_instructions
    sequence_probe_instructions.tStop = globalClock.getTime(format='float')
    sequence_probe_instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('sequence_probe_instructions.stopped', sequence_probe_instructions.tStop)
    setupWindow(expInfo=expInfo, win=win)
    # check responses
    if key_resp_seq_instructions.keys in ['', [], None]:  # No response was made
        key_resp_seq_instructions.keys = None
    thisExp.addData('key_resp_seq_instructions.keys',key_resp_seq_instructions.keys)
    if key_resp_seq_instructions.keys != None:  # we had a response
        thisExp.addData('key_resp_seq_instructions.rt', key_resp_seq_instructions.rt)
        thisExp.addData('key_resp_seq_instructions.duration', key_resp_seq_instructions.duration)
    thisExp.nextEntry()
    # the Routine "sequence_probe_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    # create an object to store info about Routine ITI
    ITI = data.Routine(
        name='ITI',
        components=[ITI_fix],
    )
    ITI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI
    ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI.tStart = globalClock.getTime(format='float')
    ITI.status = STARTED
    thisExp.addData('ITI.started', ITI.tStart)
    ITI.maxDuration = 1
    # keep track of which components have finished
    ITIComponents = ITI.components
    for thisComponent in ITI.components:
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
    
    # --- Run Routine "ITI" ---
    ITI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ITI.maxDuration-frameTolerance:
            ITI.maxDurationReached = True
            continueRoutine = False
        
        # *ITI_fix* updates
        
        # if ITI_fix is starting this frame...
        if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ITI_fix.frameNStart = frameN  # exact frame index
            ITI_fix.tStart = t  # local t and not account for scr refresh
            ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_fix.started')
            # update status
            ITI_fix.status = STARTED
            ITI_fix.setAutoDraw(True)
        
        # if ITI_fix is active this frame...
        if ITI_fix.status == STARTED:
            # update params
            pass
        
        # if ITI_fix is stopping this frame...
        if ITI_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ITI_fix.tStop = t  # not accounting for scr refresh
                ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                ITI_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                # update status
                ITI_fix.status = FINISHED
                ITI_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ITI,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ITI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI
    ITI.tStop = globalClock.getTime(format='float')
    ITI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI.stopped', ITI.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI.maxDurationReached:
        routineTimer.addTime(-ITI.maxDuration)
    elif ITI.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_sequence_probe = data.TrialHandler2(
        name='trials_sequence_probe',
        nReps=seq_nreps, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('experiment_control_files/trial-types_sequence-probe_2025-12-09.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials_sequence_probe)  # add the loop to the experiment
    thisTrials_sequence_probe = trials_sequence_probe.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sequence_probe.rgb)
    if thisTrials_sequence_probe != None:
        for paramName in thisTrials_sequence_probe:
            globals()[paramName] = thisTrials_sequence_probe[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_sequence_probe in trials_sequence_probe:
        trials_sequence_probe.status = STARTED
        if hasattr(thisTrials_sequence_probe, 'status'):
            thisTrials_sequence_probe.status = STARTED
        currentLoop = trials_sequence_probe
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sequence_probe.rgb)
        if thisTrials_sequence_probe != None:
            for paramName in thisTrials_sequence_probe:
                globals()[paramName] = thisTrials_sequence_probe[paramName]
        
        # --- Prepare to start Routine "VWM_memory_display" ---
        # create an object to store info about Routine VWM_memory_display
        VWM_memory_display = data.Routine(
            name='VWM_memory_display',
            components=[mem_disc, mem_fix],
        )
        VWM_memory_display.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from memory_sequence_code
        # Get locations for this trial
        path_coords = []
        ## path coords is a list of (x,y) tuples
        for segment in range(path_length):
            if segment == 0:
                segment_coord = (0,0)
            else:
                segment_coord = get_random_path_coord(path_coords[segment-1])
        
            path_coords.append(segment_coord)
        #print(path_coords)
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position
        disc_position = path_coords[segment]
        
        disc_alpha = 1
        path_end = path_coords[segment + 1]
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        # add data to output
        thisExp.addData('path_coords', path_coords)
        
        
        # store start times for VWM_memory_display
        VWM_memory_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_display.tStart = globalClock.getTime(format='float')
        VWM_memory_display.status = STARTED
        thisExp.addData('VWM_memory_display.started', VWM_memory_display.tStart)
        VWM_memory_display.maxDuration = None
        win.color = ''
        win.colorSpace = 'rgb'
        win.backgroundImage = 'abstract-art-3840x2160-23159.jpg'
        win.backgroundFit = 'none'
        # keep track of which components have finished
        VWM_memory_displayComponents = VWM_memory_display.components
        for thisComponent in VWM_memory_display.components:
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
        
        # --- Run Routine "VWM_memory_display" ---
        VWM_memory_display.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe, 'status') and thisTrials_sequence_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from memory_sequence_code
            
            if pause_timer.getTime() <= 0 and segment < path_length - 1:
                path_end = path_coords[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1        
                disc_position = (new_x, new_y)    
            elif segment >= path_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
            
            
            
            # *mem_disc* updates
            
            # if mem_disc is starting this frame...
            if mem_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_disc.frameNStart = frameN  # exact frame index
                mem_disc.tStart = t  # local t and not account for scr refresh
                mem_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_disc.started')
                # update status
                mem_disc.status = STARTED
                mem_disc.setAutoDraw(True)
            
            # if mem_disc is active this frame...
            if mem_disc.status == STARTED:
                # update params
                mem_disc.setFillColor(disc_alpha, log=False)
                mem_disc.setOpacity(disc_alpha, log=False)
                mem_disc.setPos(disc_position, log=False)
                mem_disc.setLineColor(disc_alpha, log=False)
            
            # *mem_fix* updates
            
            # if mem_fix is starting this frame...
            if mem_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_fix.frameNStart = frameN  # exact frame index
                mem_fix.tStart = t  # local t and not account for scr refresh
                mem_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_fix.started')
                # update status
                mem_fix.status = STARTED
                mem_fix.setAutoDraw(True)
            
            # if mem_fix is active this frame...
            if mem_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_display,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_display.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_display.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_display" ---
        for thisComponent in VWM_memory_display.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_display
        VWM_memory_display.tStop = globalClock.getTime(format='float')
        VWM_memory_display.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_display.stopped', VWM_memory_display.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # the Routine "VWM_memory_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "retention" ---
        # create an object to store info about Routine retention
        retention = data.Routine(
            name='retention',
            components=[retention_fix],
        )
        retention.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for retention
        retention.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        retention.tStart = globalClock.getTime(format='float')
        retention.status = STARTED
        thisExp.addData('retention.started', retention.tStart)
        retention.maxDuration = None
        # keep track of which components have finished
        retentionComponents = retention.components
        for thisComponent in retention.components:
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
        
        # --- Run Routine "retention" ---
        retention.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe, 'status') and thisTrials_sequence_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *retention_fix* updates
            
            # if retention_fix is starting this frame...
            if retention_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                retention_fix.frameNStart = frameN  # exact frame index
                retention_fix.tStart = t  # local t and not account for scr refresh
                retention_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(retention_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'retention_fix.started')
                # update status
                retention_fix.status = STARTED
                retention_fix.setAutoDraw(True)
            
            # if retention_fix is active this frame...
            if retention_fix.status == STARTED:
                # update params
                pass
            
            # if retention_fix is stopping this frame...
            if retention_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > retention_fix.tStartRefresh + retention_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    retention_fix.tStop = t  # not accounting for scr refresh
                    retention_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    retention_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'retention_fix.stopped')
                    # update status
                    retention_fix.status = FINISHED
                    retention_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=retention,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                retention.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in retention.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "retention" ---
        for thisComponent in retention.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for retention
        retention.tStop = globalClock.getTime(format='float')
        retention.tStopRefresh = tThisFlipGlobal
        thisExp.addData('retention.stopped', retention.tStop)
        # the Routine "retention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_memory_probe" ---
        # create an object to store info about Routine VWM_memory_probe
        VWM_memory_probe = data.Routine(
            name='VWM_memory_probe',
            components=[probe_disc, probe_fix],
        )
        VWM_memory_probe.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from probe_sequence_code
        # Get locations for this trial
        
        # by default, we reprise the prior coords
        path_coords_probe = path_coords.copy() # PYTHON VARIABLES ARE DUMB
        probe_length = path_length # Int, don't need to copy.
        
        print(memory_type)
        print(probe_type)
        print(probe_validity)
        
        if probe_validity == "lure":
            if probe_type == "sequence":
                print('generating a sequence lure')
                # pick a position — range 1 to path_length-1 so center (index 0) can be swapped
                lure_pos = int(round(random.uniform(1, path_length - 1),0))
                # swap lure_pos with lure_pos-1
                path_coords_probe[lure_pos] = path_coords[lure_pos - 1]
                path_coords_probe[lure_pos - 1] = path_coords[lure_pos]
        
            elif probe_type == "single":
                print('generating a single lure')
                probe_length = 1
                x = round(max_eccen * random.uniform(-1, 1), 1)
                y = round(max_eccen * random.uniform(-1, 1), 1)
                lure_coords = (x,y)
                a = 1
                while a:
                    for loc in path_coords:
                        x_distance = abs(loc[0] - lure_coords[0])
                        y_distance = abs(loc[1] - lure_coords[1])
                        if x_distance < 0.2 and y_distance < 0.2:
                            x = round(max_eccen * random.uniform(-1, 1), 1)
                            y = round(max_eccen * random.uniform(-1, 1), 1)
                            lure_coords = (x,y)
                            break
                        a = 0
                path_coords_probe = [lure_coords]
        
        else: # probe_validity == target
            if probe_type == "single":
                print('generating a single target')
                probe_pos = int(round(random.uniform(1, path_length-1),0))
                path_coords_probe = [path_coords_probe[probe_pos]]
                probe_length = 1
        
        # For sequence probes: prepend (0,0) as the travel-to-start step.
        # The disc always starts at center, AND center can appear as a
        # mid-sequence location when lure_pos=1 swaps index 0 into position 1.
        if probe_type == "sequence":
            path_coords_probe = [(0,0)] + path_coords_probe
            probe_length = path_length + 1
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position — always (0,0) for sequence (prepended above)
        disc_position = path_coords_probe[segment]
        disc_alpha = 1
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        if probe_type == "sequence":
            path_end = path_coords_probe[segment + 1]
        
        if probe_type == "sequence":
            response_string = "F same                           J different"
        else:
            response_string = "F old                                  J new"
        
        thisExp.addData('path_coords_probe', path_coords_probe)
        # store start times for VWM_memory_probe
        VWM_memory_probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_probe.tStart = globalClock.getTime(format='float')
        VWM_memory_probe.status = STARTED
        thisExp.addData('VWM_memory_probe.started', VWM_memory_probe.tStart)
        VWM_memory_probe.maxDuration = None
        # keep track of which components have finished
        VWM_memory_probeComponents = VWM_memory_probe.components
        for thisComponent in VWM_memory_probe.components:
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
        
        # --- Run Routine "VWM_memory_probe" ---
        VWM_memory_probe.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe, 'status') and thisTrials_sequence_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from probe_sequence_code
            if pause_timer.getTime() <= 0 and probe_type == "sequence" and segment < probe_length - 1:
                #path_end = path_coords[segment + 1]
                path_end = path_coords_probe[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1
                disc_position = (new_x, new_y)
            elif segment >= probe_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
                
            
            
            
            # *probe_disc* updates
            
            # if probe_disc is starting this frame...
            if probe_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_disc.frameNStart = frameN  # exact frame index
                probe_disc.tStart = t  # local t and not account for scr refresh
                probe_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_disc.started')
                # update status
                probe_disc.status = STARTED
                probe_disc.setAutoDraw(True)
            
            # if probe_disc is active this frame...
            if probe_disc.status == STARTED:
                # update params
                probe_disc.setFillColor(disc_alpha, log=False)
                probe_disc.setOpacity(disc_alpha, log=False)
                probe_disc.setPos(disc_position, log=False)
                probe_disc.setLineColor(disc_alpha, log=False)
            
            # *probe_fix* updates
            
            # if probe_fix is starting this frame...
            if probe_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_fix.frameNStart = frameN  # exact frame index
                probe_fix.tStart = t  # local t and not account for scr refresh
                probe_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_fix.started')
                # update status
                probe_fix.status = STARTED
                probe_fix.setAutoDraw(True)
            
            # if probe_fix is active this frame...
            if probe_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_probe,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_probe.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_probe.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_probe" ---
        for thisComponent in VWM_memory_probe.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_probe
        VWM_memory_probe.tStop = globalClock.getTime(format='float')
        VWM_memory_probe.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_probe.stopped', VWM_memory_probe.tStop)
        # the Routine "VWM_memory_probe" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_response" ---
        # create an object to store info about Routine VWM_response
        VWM_response = data.Routine(
            name='VWM_response',
            components=[response_cue, response_instructions, key_resp_VWM],
        )
        VWM_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        response_instructions.setText(response_string)
        # create starting attributes for key_resp_VWM
        key_resp_VWM.keys = []
        key_resp_VWM.rt = []
        _key_resp_VWM_allKeys = []
        # store start times for VWM_response
        VWM_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_response.tStart = globalClock.getTime(format='float')
        VWM_response.status = STARTED
        thisExp.addData('VWM_response.started', VWM_response.tStart)
        VWM_response.maxDuration = None
        # keep track of which components have finished
        VWM_responseComponents = VWM_response.components
        for thisComponent in VWM_response.components:
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
        
        # --- Run Routine "VWM_response" ---
        VWM_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe, 'status') and thisTrials_sequence_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_cue* updates
            
            # if response_cue is starting this frame...
            if response_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_cue.frameNStart = frameN  # exact frame index
                response_cue.tStart = t  # local t and not account for scr refresh
                response_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_cue.started')
                # update status
                response_cue.status = STARTED
                response_cue.setAutoDraw(True)
            
            # if response_cue is active this frame...
            if response_cue.status == STARTED:
                # update params
                pass
            
            # *response_instructions* updates
            
            # if response_instructions is starting this frame...
            if response_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_instructions.frameNStart = frameN  # exact frame index
                response_instructions.tStart = t  # local t and not account for scr refresh
                response_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_instructions.started')
                # update status
                response_instructions.status = STARTED
                response_instructions.setAutoDraw(True)
            
            # if response_instructions is active this frame...
            if response_instructions.status == STARTED:
                # update params
                pass
            
            # *key_resp_VWM* updates
            waitOnFlip = False
            
            # if key_resp_VWM is starting this frame...
            if key_resp_VWM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_VWM.frameNStart = frameN  # exact frame index
                key_resp_VWM.tStart = t  # local t and not account for scr refresh
                key_resp_VWM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_VWM, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_VWM.started')
                # update status
                key_resp_VWM.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_VWM.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_VWM.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_VWM.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_VWM.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_VWM_allKeys.extend(theseKeys)
                if len(_key_resp_VWM_allKeys):
                    key_resp_VWM.keys = _key_resp_VWM_allKeys[-1].name  # just the last key pressed
                    key_resp_VWM.rt = _key_resp_VWM_allKeys[-1].rt
                    key_resp_VWM.duration = _key_resp_VWM_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_response,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_response" ---
        for thisComponent in VWM_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_response
        VWM_response.tStop = globalClock.getTime(format='float')
        VWM_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_response.stopped', VWM_response.tStop)
        # check responses
        if key_resp_VWM.keys in ['', [], None]:  # No response was made
            key_resp_VWM.keys = None
        trials_sequence_probe.addData('key_resp_VWM.keys',key_resp_VWM.keys)
        if key_resp_VWM.keys != None:  # we had a response
            trials_sequence_probe.addData('key_resp_VWM.rt', key_resp_VWM.rt)
            trials_sequence_probe.addData('key_resp_VWM.duration', key_resp_VWM.duration)
        # the Routine "VWM_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_2" ---
        # create an object to store info about Routine break_2
        break_2 = data.Routine(
            name='break_2',
            components=[break_txt, break_resp],
        )
        break_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for break_resp
        break_resp.keys = []
        break_resp.rt = []
        _break_resp_allKeys = []
        # store start times for break_2
        break_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        break_2.tStart = globalClock.getTime(format='float')
        break_2.status = STARTED
        thisExp.addData('break_2.started', break_2.tStart)
        break_2.maxDuration = None
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        # keep track of which components have finished
        break_2Components = break_2.components
        for thisComponent in break_2.components:
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
        
        # --- Run Routine "break_2" ---
        break_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe, 'status') and thisTrials_sequence_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *break_txt* updates
            
            # if break_txt is starting this frame...
            if break_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_txt.frameNStart = frameN  # exact frame index
                break_txt.tStart = t  # local t and not account for scr refresh
                break_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_txt.started')
                # update status
                break_txt.status = STARTED
                break_txt.setAutoDraw(True)
            
            # if break_txt is active this frame...
            if break_txt.status == STARTED:
                # update params
                pass
            
            # *break_resp* updates
            waitOnFlip = False
            
            # if break_resp is starting this frame...
            if break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_resp.frameNStart = frameN  # exact frame index
                break_resp.tStart = t  # local t and not account for scr refresh
                break_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_resp.started')
                # update status
                break_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(break_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if break_resp.status == STARTED and not waitOnFlip:
                theseKeys = break_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _break_resp_allKeys.extend(theseKeys)
                if len(_break_resp_allKeys):
                    break_resp.keys = _break_resp_allKeys[-1].name  # just the last key pressed
                    break_resp.rt = _break_resp_allKeys[-1].rt
                    break_resp.duration = _break_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=break_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for break_2
        break_2.tStop = globalClock.getTime(format='float')
        break_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('break_2.stopped', break_2.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # check responses
        if break_resp.keys in ['', [], None]:  # No response was made
            break_resp.keys = None
        trials_sequence_probe.addData('break_resp.keys',break_resp.keys)
        if break_resp.keys != None:  # we had a response
            trials_sequence_probe.addData('break_resp.rt', break_resp.rt)
            trials_sequence_probe.addData('break_resp.duration', break_resp.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_fix],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = 1
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
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
        
        # --- Run Routine "ITI" ---
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe, 'status') and thisTrials_sequence_probe.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ITI.maxDuration-frameTolerance:
                ITI.maxDurationReached = True
                continueRoutine = False
            
            # *ITI_fix* updates
            
            # if ITI_fix is starting this frame...
            if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                ITI_fix.frameNStart = frameN  # exact frame index
                ITI_fix.tStart = t  # local t and not account for scr refresh
                ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.started')
                # update status
                ITI_fix.status = STARTED
                ITI_fix.setAutoDraw(True)
            
            # if ITI_fix is active this frame...
            if ITI_fix.status == STARTED:
                # update params
                pass
            
            # if ITI_fix is stopping this frame...
            if ITI_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_fix.tStop = t  # not accounting for scr refresh
                    ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                    # update status
                    ITI_fix.status = FINISHED
                    ITI_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrials_sequence_probe as finished
        if hasattr(thisTrials_sequence_probe, 'status'):
            thisTrials_sequence_probe.status = FINISHED
        # if awaiting a pause, pause now
        if trials_sequence_probe.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_sequence_probe.status = STARTED
        thisExp.nextEntry()
        
    # completed seq_nreps repeats of 'trials_sequence_probe'
    trials_sequence_probe.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "advance_block" ---
    # create an object to store info about Routine advance_block
    advance_block = data.Routine(
        name='advance_block',
        components=[],
    )
    advance_block.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    current_block = block_order[current_block_idx]
    current_block_idx += 1
    single_nreps = 10 if current_block == 'single' else 0
    seq_nreps = 10 if current_block == 'sequence' else 0
    continueRoutine = False
    # store start times for advance_block
    advance_block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    advance_block.tStart = globalClock.getTime(format='float')
    advance_block.status = STARTED
    thisExp.addData('advance_block.started', advance_block.tStart)
    advance_block.maxDuration = None
    # keep track of which components have finished
    advance_blockComponents = advance_block.components
    for thisComponent in advance_block.components:
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
    
    # --- Run Routine "advance_block" ---
    advance_block.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=advance_block,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            advance_block.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in advance_block.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "advance_block" ---
    for thisComponent in advance_block.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for advance_block
    advance_block.tStop = globalClock.getTime(format='float')
    advance_block.tStopRefresh = tThisFlipGlobal
    thisExp.addData('advance_block.stopped', advance_block.tStop)
    thisExp.nextEntry()
    # the Routine "advance_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "single_probe_instructions" ---
    # create an object to store info about Routine single_probe_instructions
    single_probe_instructions = data.Routine(
        name='single_probe_instructions',
        components=[text_single_instructions, key_resp_single_instructions],
    )
    single_probe_instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_single_instructions
    key_resp_single_instructions.keys = []
    key_resp_single_instructions.rt = []
    _key_resp_single_instructions_allKeys = []
    # store start times for single_probe_instructions
    single_probe_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    single_probe_instructions.tStart = globalClock.getTime(format='float')
    single_probe_instructions.status = STARTED
    thisExp.addData('single_probe_instructions.started', single_probe_instructions.tStart)
    single_probe_instructions.maxDuration = None
    # skip Routine single_probe_instructions if its 'Skip if' condition is True
    single_probe_instructions.skipped = continueRoutine and not (current_block != 'single')
    continueRoutine = single_probe_instructions.skipped
    win.color = [0.0000, 0.0000, 0.0000]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    single_probe_instructionsComponents = single_probe_instructions.components
    for thisComponent in single_probe_instructions.components:
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
    
    # --- Run Routine "single_probe_instructions" ---
    single_probe_instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_single_instructions* updates
        
        # if text_single_instructions is starting this frame...
        if text_single_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_single_instructions.frameNStart = frameN  # exact frame index
            text_single_instructions.tStart = t  # local t and not account for scr refresh
            text_single_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_single_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_single_instructions.started')
            # update status
            text_single_instructions.status = STARTED
            text_single_instructions.setAutoDraw(True)
        
        # if text_single_instructions is active this frame...
        if text_single_instructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_single_instructions* updates
        waitOnFlip = False
        
        # if key_resp_single_instructions is starting this frame...
        if key_resp_single_instructions.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_single_instructions.frameNStart = frameN  # exact frame index
            key_resp_single_instructions.tStart = t  # local t and not account for scr refresh
            key_resp_single_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_single_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_single_instructions.started')
            # update status
            key_resp_single_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_single_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_single_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_single_instructions.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_single_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_single_instructions_allKeys.extend(theseKeys)
            if len(_key_resp_single_instructions_allKeys):
                key_resp_single_instructions.keys = _key_resp_single_instructions_allKeys[-1].name  # just the last key pressed
                key_resp_single_instructions.rt = _key_resp_single_instructions_allKeys[-1].rt
                key_resp_single_instructions.duration = _key_resp_single_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=single_probe_instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            single_probe_instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in single_probe_instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "single_probe_instructions" ---
    for thisComponent in single_probe_instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for single_probe_instructions
    single_probe_instructions.tStop = globalClock.getTime(format='float')
    single_probe_instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('single_probe_instructions.stopped', single_probe_instructions.tStop)
    setupWindow(expInfo=expInfo, win=win)
    # check responses
    if key_resp_single_instructions.keys in ['', [], None]:  # No response was made
        key_resp_single_instructions.keys = None
    thisExp.addData('key_resp_single_instructions.keys',key_resp_single_instructions.keys)
    if key_resp_single_instructions.keys != None:  # we had a response
        thisExp.addData('key_resp_single_instructions.rt', key_resp_single_instructions.rt)
        thisExp.addData('key_resp_single_instructions.duration', key_resp_single_instructions.duration)
    thisExp.nextEntry()
    # the Routine "single_probe_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    # create an object to store info about Routine ITI
    ITI = data.Routine(
        name='ITI',
        components=[ITI_fix],
    )
    ITI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI
    ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI.tStart = globalClock.getTime(format='float')
    ITI.status = STARTED
    thisExp.addData('ITI.started', ITI.tStart)
    ITI.maxDuration = 1
    # keep track of which components have finished
    ITIComponents = ITI.components
    for thisComponent in ITI.components:
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
    
    # --- Run Routine "ITI" ---
    ITI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ITI.maxDuration-frameTolerance:
            ITI.maxDurationReached = True
            continueRoutine = False
        
        # *ITI_fix* updates
        
        # if ITI_fix is starting this frame...
        if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ITI_fix.frameNStart = frameN  # exact frame index
            ITI_fix.tStart = t  # local t and not account for scr refresh
            ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_fix.started')
            # update status
            ITI_fix.status = STARTED
            ITI_fix.setAutoDraw(True)
        
        # if ITI_fix is active this frame...
        if ITI_fix.status == STARTED:
            # update params
            pass
        
        # if ITI_fix is stopping this frame...
        if ITI_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ITI_fix.tStop = t  # not accounting for scr refresh
                ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                ITI_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                # update status
                ITI_fix.status = FINISHED
                ITI_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ITI,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ITI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI
    ITI.tStop = globalClock.getTime(format='float')
    ITI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI.stopped', ITI.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI.maxDurationReached:
        routineTimer.addTime(-ITI.maxDuration)
    elif ITI.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_single_probe2 = data.TrialHandler2(
        name='trials_single_probe2',
        nReps=single_nreps, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('experiment_control_files/trial-types_single-probe_2025-12-09.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials_single_probe2)  # add the loop to the experiment
    thisTrials_single_probe2 = trials_single_probe2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_single_probe2.rgb)
    if thisTrials_single_probe2 != None:
        for paramName in thisTrials_single_probe2:
            globals()[paramName] = thisTrials_single_probe2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_single_probe2 in trials_single_probe2:
        trials_single_probe2.status = STARTED
        if hasattr(thisTrials_single_probe2, 'status'):
            thisTrials_single_probe2.status = STARTED
        currentLoop = trials_single_probe2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_single_probe2.rgb)
        if thisTrials_single_probe2 != None:
            for paramName in thisTrials_single_probe2:
                globals()[paramName] = thisTrials_single_probe2[paramName]
        
        # --- Prepare to start Routine "VWM_memory_display" ---
        # create an object to store info about Routine VWM_memory_display
        VWM_memory_display = data.Routine(
            name='VWM_memory_display',
            components=[mem_disc, mem_fix],
        )
        VWM_memory_display.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from memory_sequence_code
        # Get locations for this trial
        path_coords = []
        ## path coords is a list of (x,y) tuples
        for segment in range(path_length):
            if segment == 0:
                segment_coord = (0,0)
            else:
                segment_coord = get_random_path_coord(path_coords[segment-1])
        
            path_coords.append(segment_coord)
        #print(path_coords)
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position
        disc_position = path_coords[segment]
        
        disc_alpha = 1
        path_end = path_coords[segment + 1]
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        # add data to output
        thisExp.addData('path_coords', path_coords)
        
        
        # store start times for VWM_memory_display
        VWM_memory_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_display.tStart = globalClock.getTime(format='float')
        VWM_memory_display.status = STARTED
        thisExp.addData('VWM_memory_display.started', VWM_memory_display.tStart)
        VWM_memory_display.maxDuration = None
        win.color = ''
        win.colorSpace = 'rgb'
        win.backgroundImage = 'abstract-art-3840x2160-23159.jpg'
        win.backgroundFit = 'none'
        # keep track of which components have finished
        VWM_memory_displayComponents = VWM_memory_display.components
        for thisComponent in VWM_memory_display.components:
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
        
        # --- Run Routine "VWM_memory_display" ---
        VWM_memory_display.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe2, 'status') and thisTrials_single_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from memory_sequence_code
            
            if pause_timer.getTime() <= 0 and segment < path_length - 1:
                path_end = path_coords[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1        
                disc_position = (new_x, new_y)    
            elif segment >= path_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
            
            
            
            # *mem_disc* updates
            
            # if mem_disc is starting this frame...
            if mem_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_disc.frameNStart = frameN  # exact frame index
                mem_disc.tStart = t  # local t and not account for scr refresh
                mem_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_disc.started')
                # update status
                mem_disc.status = STARTED
                mem_disc.setAutoDraw(True)
            
            # if mem_disc is active this frame...
            if mem_disc.status == STARTED:
                # update params
                mem_disc.setFillColor(disc_alpha, log=False)
                mem_disc.setOpacity(disc_alpha, log=False)
                mem_disc.setPos(disc_position, log=False)
                mem_disc.setLineColor(disc_alpha, log=False)
            
            # *mem_fix* updates
            
            # if mem_fix is starting this frame...
            if mem_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_fix.frameNStart = frameN  # exact frame index
                mem_fix.tStart = t  # local t and not account for scr refresh
                mem_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_fix.started')
                # update status
                mem_fix.status = STARTED
                mem_fix.setAutoDraw(True)
            
            # if mem_fix is active this frame...
            if mem_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_display,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_display.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_display.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_display" ---
        for thisComponent in VWM_memory_display.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_display
        VWM_memory_display.tStop = globalClock.getTime(format='float')
        VWM_memory_display.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_display.stopped', VWM_memory_display.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # the Routine "VWM_memory_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "retention" ---
        # create an object to store info about Routine retention
        retention = data.Routine(
            name='retention',
            components=[retention_fix],
        )
        retention.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for retention
        retention.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        retention.tStart = globalClock.getTime(format='float')
        retention.status = STARTED
        thisExp.addData('retention.started', retention.tStart)
        retention.maxDuration = None
        # keep track of which components have finished
        retentionComponents = retention.components
        for thisComponent in retention.components:
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
        
        # --- Run Routine "retention" ---
        retention.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe2, 'status') and thisTrials_single_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *retention_fix* updates
            
            # if retention_fix is starting this frame...
            if retention_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                retention_fix.frameNStart = frameN  # exact frame index
                retention_fix.tStart = t  # local t and not account for scr refresh
                retention_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(retention_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'retention_fix.started')
                # update status
                retention_fix.status = STARTED
                retention_fix.setAutoDraw(True)
            
            # if retention_fix is active this frame...
            if retention_fix.status == STARTED:
                # update params
                pass
            
            # if retention_fix is stopping this frame...
            if retention_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > retention_fix.tStartRefresh + retention_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    retention_fix.tStop = t  # not accounting for scr refresh
                    retention_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    retention_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'retention_fix.stopped')
                    # update status
                    retention_fix.status = FINISHED
                    retention_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=retention,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                retention.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in retention.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "retention" ---
        for thisComponent in retention.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for retention
        retention.tStop = globalClock.getTime(format='float')
        retention.tStopRefresh = tThisFlipGlobal
        thisExp.addData('retention.stopped', retention.tStop)
        # the Routine "retention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_memory_probe" ---
        # create an object to store info about Routine VWM_memory_probe
        VWM_memory_probe = data.Routine(
            name='VWM_memory_probe',
            components=[probe_disc, probe_fix],
        )
        VWM_memory_probe.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from probe_sequence_code
        # Get locations for this trial
        
        # by default, we reprise the prior coords
        path_coords_probe = path_coords.copy() # PYTHON VARIABLES ARE DUMB
        probe_length = path_length # Int, don't need to copy.
        
        print(memory_type)
        print(probe_type)
        print(probe_validity)
        
        if probe_validity == "lure":
            if probe_type == "sequence":
                print('generating a sequence lure')
                # pick a position — range 1 to path_length-1 so center (index 0) can be swapped
                lure_pos = int(round(random.uniform(1, path_length - 1),0))
                # swap lure_pos with lure_pos-1
                path_coords_probe[lure_pos] = path_coords[lure_pos - 1]
                path_coords_probe[lure_pos - 1] = path_coords[lure_pos]
        
            elif probe_type == "single":
                print('generating a single lure')
                probe_length = 1
                x = round(max_eccen * random.uniform(-1, 1), 1)
                y = round(max_eccen * random.uniform(-1, 1), 1)
                lure_coords = (x,y)
                a = 1
                while a:
                    for loc in path_coords:
                        x_distance = abs(loc[0] - lure_coords[0])
                        y_distance = abs(loc[1] - lure_coords[1])
                        if x_distance < 0.2 and y_distance < 0.2:
                            x = round(max_eccen * random.uniform(-1, 1), 1)
                            y = round(max_eccen * random.uniform(-1, 1), 1)
                            lure_coords = (x,y)
                            break
                        a = 0
                path_coords_probe = [lure_coords]
        
        else: # probe_validity == target
            if probe_type == "single":
                print('generating a single target')
                probe_pos = int(round(random.uniform(1, path_length-1),0))
                path_coords_probe = [path_coords_probe[probe_pos]]
                probe_length = 1
        
        # For sequence probes: prepend (0,0) as the travel-to-start step.
        # The disc always starts at center, AND center can appear as a
        # mid-sequence location when lure_pos=1 swaps index 0 into position 1.
        if probe_type == "sequence":
            path_coords_probe = [(0,0)] + path_coords_probe
            probe_length = path_length + 1
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position — always (0,0) for sequence (prepended above)
        disc_position = path_coords_probe[segment]
        disc_alpha = 1
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        if probe_type == "sequence":
            path_end = path_coords_probe[segment + 1]
        
        if probe_type == "sequence":
            response_string = "F same                           J different"
        else:
            response_string = "F old                                  J new"
        
        thisExp.addData('path_coords_probe', path_coords_probe)
        # store start times for VWM_memory_probe
        VWM_memory_probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_probe.tStart = globalClock.getTime(format='float')
        VWM_memory_probe.status = STARTED
        thisExp.addData('VWM_memory_probe.started', VWM_memory_probe.tStart)
        VWM_memory_probe.maxDuration = None
        # keep track of which components have finished
        VWM_memory_probeComponents = VWM_memory_probe.components
        for thisComponent in VWM_memory_probe.components:
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
        
        # --- Run Routine "VWM_memory_probe" ---
        VWM_memory_probe.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe2, 'status') and thisTrials_single_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from probe_sequence_code
            if pause_timer.getTime() <= 0 and probe_type == "sequence" and segment < probe_length - 1:
                #path_end = path_coords[segment + 1]
                path_end = path_coords_probe[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1
                disc_position = (new_x, new_y)
            elif segment >= probe_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
                
            
            
            
            # *probe_disc* updates
            
            # if probe_disc is starting this frame...
            if probe_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_disc.frameNStart = frameN  # exact frame index
                probe_disc.tStart = t  # local t and not account for scr refresh
                probe_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_disc.started')
                # update status
                probe_disc.status = STARTED
                probe_disc.setAutoDraw(True)
            
            # if probe_disc is active this frame...
            if probe_disc.status == STARTED:
                # update params
                probe_disc.setFillColor(disc_alpha, log=False)
                probe_disc.setOpacity(disc_alpha, log=False)
                probe_disc.setPos(disc_position, log=False)
                probe_disc.setLineColor(disc_alpha, log=False)
            
            # *probe_fix* updates
            
            # if probe_fix is starting this frame...
            if probe_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_fix.frameNStart = frameN  # exact frame index
                probe_fix.tStart = t  # local t and not account for scr refresh
                probe_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_fix.started')
                # update status
                probe_fix.status = STARTED
                probe_fix.setAutoDraw(True)
            
            # if probe_fix is active this frame...
            if probe_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_probe,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_probe.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_probe.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_probe" ---
        for thisComponent in VWM_memory_probe.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_probe
        VWM_memory_probe.tStop = globalClock.getTime(format='float')
        VWM_memory_probe.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_probe.stopped', VWM_memory_probe.tStop)
        # the Routine "VWM_memory_probe" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_response" ---
        # create an object to store info about Routine VWM_response
        VWM_response = data.Routine(
            name='VWM_response',
            components=[response_cue, response_instructions, key_resp_VWM],
        )
        VWM_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        response_instructions.setText(response_string)
        # create starting attributes for key_resp_VWM
        key_resp_VWM.keys = []
        key_resp_VWM.rt = []
        _key_resp_VWM_allKeys = []
        # store start times for VWM_response
        VWM_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_response.tStart = globalClock.getTime(format='float')
        VWM_response.status = STARTED
        thisExp.addData('VWM_response.started', VWM_response.tStart)
        VWM_response.maxDuration = None
        # keep track of which components have finished
        VWM_responseComponents = VWM_response.components
        for thisComponent in VWM_response.components:
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
        
        # --- Run Routine "VWM_response" ---
        VWM_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe2, 'status') and thisTrials_single_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_cue* updates
            
            # if response_cue is starting this frame...
            if response_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_cue.frameNStart = frameN  # exact frame index
                response_cue.tStart = t  # local t and not account for scr refresh
                response_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_cue.started')
                # update status
                response_cue.status = STARTED
                response_cue.setAutoDraw(True)
            
            # if response_cue is active this frame...
            if response_cue.status == STARTED:
                # update params
                pass
            
            # *response_instructions* updates
            
            # if response_instructions is starting this frame...
            if response_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_instructions.frameNStart = frameN  # exact frame index
                response_instructions.tStart = t  # local t and not account for scr refresh
                response_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_instructions.started')
                # update status
                response_instructions.status = STARTED
                response_instructions.setAutoDraw(True)
            
            # if response_instructions is active this frame...
            if response_instructions.status == STARTED:
                # update params
                pass
            
            # *key_resp_VWM* updates
            waitOnFlip = False
            
            # if key_resp_VWM is starting this frame...
            if key_resp_VWM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_VWM.frameNStart = frameN  # exact frame index
                key_resp_VWM.tStart = t  # local t and not account for scr refresh
                key_resp_VWM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_VWM, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_VWM.started')
                # update status
                key_resp_VWM.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_VWM.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_VWM.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_VWM.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_VWM.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_VWM_allKeys.extend(theseKeys)
                if len(_key_resp_VWM_allKeys):
                    key_resp_VWM.keys = _key_resp_VWM_allKeys[-1].name  # just the last key pressed
                    key_resp_VWM.rt = _key_resp_VWM_allKeys[-1].rt
                    key_resp_VWM.duration = _key_resp_VWM_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_response,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_response" ---
        for thisComponent in VWM_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_response
        VWM_response.tStop = globalClock.getTime(format='float')
        VWM_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_response.stopped', VWM_response.tStop)
        # check responses
        if key_resp_VWM.keys in ['', [], None]:  # No response was made
            key_resp_VWM.keys = None
        trials_single_probe2.addData('key_resp_VWM.keys',key_resp_VWM.keys)
        if key_resp_VWM.keys != None:  # we had a response
            trials_single_probe2.addData('key_resp_VWM.rt', key_resp_VWM.rt)
            trials_single_probe2.addData('key_resp_VWM.duration', key_resp_VWM.duration)
        # the Routine "VWM_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_2" ---
        # create an object to store info about Routine break_2
        break_2 = data.Routine(
            name='break_2',
            components=[break_txt, break_resp],
        )
        break_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for break_resp
        break_resp.keys = []
        break_resp.rt = []
        _break_resp_allKeys = []
        # store start times for break_2
        break_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        break_2.tStart = globalClock.getTime(format='float')
        break_2.status = STARTED
        thisExp.addData('break_2.started', break_2.tStart)
        break_2.maxDuration = None
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        # keep track of which components have finished
        break_2Components = break_2.components
        for thisComponent in break_2.components:
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
        
        # --- Run Routine "break_2" ---
        break_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe2, 'status') and thisTrials_single_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *break_txt* updates
            
            # if break_txt is starting this frame...
            if break_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_txt.frameNStart = frameN  # exact frame index
                break_txt.tStart = t  # local t and not account for scr refresh
                break_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_txt.started')
                # update status
                break_txt.status = STARTED
                break_txt.setAutoDraw(True)
            
            # if break_txt is active this frame...
            if break_txt.status == STARTED:
                # update params
                pass
            
            # *break_resp* updates
            waitOnFlip = False
            
            # if break_resp is starting this frame...
            if break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_resp.frameNStart = frameN  # exact frame index
                break_resp.tStart = t  # local t and not account for scr refresh
                break_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_resp.started')
                # update status
                break_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(break_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if break_resp.status == STARTED and not waitOnFlip:
                theseKeys = break_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _break_resp_allKeys.extend(theseKeys)
                if len(_break_resp_allKeys):
                    break_resp.keys = _break_resp_allKeys[-1].name  # just the last key pressed
                    break_resp.rt = _break_resp_allKeys[-1].rt
                    break_resp.duration = _break_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=break_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for break_2
        break_2.tStop = globalClock.getTime(format='float')
        break_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('break_2.stopped', break_2.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # check responses
        if break_resp.keys in ['', [], None]:  # No response was made
            break_resp.keys = None
        trials_single_probe2.addData('break_resp.keys',break_resp.keys)
        if break_resp.keys != None:  # we had a response
            trials_single_probe2.addData('break_resp.rt', break_resp.rt)
            trials_single_probe2.addData('break_resp.duration', break_resp.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_fix],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = 1
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
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
        
        # --- Run Routine "ITI" ---
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_single_probe2, 'status') and thisTrials_single_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ITI.maxDuration-frameTolerance:
                ITI.maxDurationReached = True
                continueRoutine = False
            
            # *ITI_fix* updates
            
            # if ITI_fix is starting this frame...
            if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                ITI_fix.frameNStart = frameN  # exact frame index
                ITI_fix.tStart = t  # local t and not account for scr refresh
                ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.started')
                # update status
                ITI_fix.status = STARTED
                ITI_fix.setAutoDraw(True)
            
            # if ITI_fix is active this frame...
            if ITI_fix.status == STARTED:
                # update params
                pass
            
            # if ITI_fix is stopping this frame...
            if ITI_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_fix.tStop = t  # not accounting for scr refresh
                    ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                    # update status
                    ITI_fix.status = FINISHED
                    ITI_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrials_single_probe2 as finished
        if hasattr(thisTrials_single_probe2, 'status'):
            thisTrials_single_probe2.status = FINISHED
        # if awaiting a pause, pause now
        if trials_single_probe2.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_single_probe2.status = STARTED
        thisExp.nextEntry()
        
    # completed single_nreps repeats of 'trials_single_probe2'
    trials_single_probe2.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "sequence_probe_instructions" ---
    # create an object to store info about Routine sequence_probe_instructions
    sequence_probe_instructions = data.Routine(
        name='sequence_probe_instructions',
        components=[text_seq_instructions, key_resp_seq_instructions],
    )
    sequence_probe_instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_seq_instructions
    key_resp_seq_instructions.keys = []
    key_resp_seq_instructions.rt = []
    _key_resp_seq_instructions_allKeys = []
    # store start times for sequence_probe_instructions
    sequence_probe_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    sequence_probe_instructions.tStart = globalClock.getTime(format='float')
    sequence_probe_instructions.status = STARTED
    thisExp.addData('sequence_probe_instructions.started', sequence_probe_instructions.tStart)
    sequence_probe_instructions.maxDuration = None
    # skip Routine sequence_probe_instructions if its 'Skip if' condition is True
    sequence_probe_instructions.skipped = continueRoutine and not (current_block != 'sequence' )
    continueRoutine = sequence_probe_instructions.skipped
    win.color = [0,0,0]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    sequence_probe_instructionsComponents = sequence_probe_instructions.components
    for thisComponent in sequence_probe_instructions.components:
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
    
    # --- Run Routine "sequence_probe_instructions" ---
    sequence_probe_instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_seq_instructions* updates
        
        # if text_seq_instructions is starting this frame...
        if text_seq_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_seq_instructions.frameNStart = frameN  # exact frame index
            text_seq_instructions.tStart = t  # local t and not account for scr refresh
            text_seq_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_seq_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_seq_instructions.started')
            # update status
            text_seq_instructions.status = STARTED
            text_seq_instructions.setAutoDraw(True)
        
        # if text_seq_instructions is active this frame...
        if text_seq_instructions.status == STARTED:
            # update params
            pass
        
        # *key_resp_seq_instructions* updates
        waitOnFlip = False
        
        # if key_resp_seq_instructions is starting this frame...
        if key_resp_seq_instructions.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_seq_instructions.frameNStart = frameN  # exact frame index
            key_resp_seq_instructions.tStart = t  # local t and not account for scr refresh
            key_resp_seq_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_seq_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_seq_instructions.started')
            # update status
            key_resp_seq_instructions.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_seq_instructions.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_seq_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_seq_instructions.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_seq_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_seq_instructions_allKeys.extend(theseKeys)
            if len(_key_resp_seq_instructions_allKeys):
                key_resp_seq_instructions.keys = _key_resp_seq_instructions_allKeys[-1].name  # just the last key pressed
                key_resp_seq_instructions.rt = _key_resp_seq_instructions_allKeys[-1].rt
                key_resp_seq_instructions.duration = _key_resp_seq_instructions_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=sequence_probe_instructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            sequence_probe_instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sequence_probe_instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sequence_probe_instructions" ---
    for thisComponent in sequence_probe_instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for sequence_probe_instructions
    sequence_probe_instructions.tStop = globalClock.getTime(format='float')
    sequence_probe_instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('sequence_probe_instructions.stopped', sequence_probe_instructions.tStop)
    setupWindow(expInfo=expInfo, win=win)
    # check responses
    if key_resp_seq_instructions.keys in ['', [], None]:  # No response was made
        key_resp_seq_instructions.keys = None
    thisExp.addData('key_resp_seq_instructions.keys',key_resp_seq_instructions.keys)
    if key_resp_seq_instructions.keys != None:  # we had a response
        thisExp.addData('key_resp_seq_instructions.rt', key_resp_seq_instructions.rt)
        thisExp.addData('key_resp_seq_instructions.duration', key_resp_seq_instructions.duration)
    thisExp.nextEntry()
    # the Routine "sequence_probe_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    # create an object to store info about Routine ITI
    ITI = data.Routine(
        name='ITI',
        components=[ITI_fix],
    )
    ITI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ITI
    ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ITI.tStart = globalClock.getTime(format='float')
    ITI.status = STARTED
    thisExp.addData('ITI.started', ITI.tStart)
    ITI.maxDuration = 1
    # keep track of which components have finished
    ITIComponents = ITI.components
    for thisComponent in ITI.components:
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
    
    # --- Run Routine "ITI" ---
    ITI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > ITI.maxDuration-frameTolerance:
            ITI.maxDurationReached = True
            continueRoutine = False
        
        # *ITI_fix* updates
        
        # if ITI_fix is starting this frame...
        if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            ITI_fix.frameNStart = frameN  # exact frame index
            ITI_fix.tStart = t  # local t and not account for scr refresh
            ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_fix.started')
            # update status
            ITI_fix.status = STARTED
            ITI_fix.setAutoDraw(True)
        
        # if ITI_fix is active this frame...
        if ITI_fix.status == STARTED:
            # update params
            pass
        
        # if ITI_fix is stopping this frame...
        if ITI_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ITI_fix.tStop = t  # not accounting for scr refresh
                ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                ITI_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                # update status
                ITI_fix.status = FINISHED
                ITI_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ITI,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ITI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ITI
    ITI.tStop = globalClock.getTime(format='float')
    ITI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ITI.stopped', ITI.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ITI.maxDurationReached:
        routineTimer.addTime(-ITI.maxDuration)
    elif ITI.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_sequence_probe2 = data.TrialHandler2(
        name='trials_sequence_probe2',
        nReps=seq_nreps, 
        method='fullRandom', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('experiment_control_files/trial-types_sequence-probe_2025-12-09.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials_sequence_probe2)  # add the loop to the experiment
    thisTrials_sequence_probe2 = trials_sequence_probe2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sequence_probe2.rgb)
    if thisTrials_sequence_probe2 != None:
        for paramName in thisTrials_sequence_probe2:
            globals()[paramName] = thisTrials_sequence_probe2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_sequence_probe2 in trials_sequence_probe2:
        trials_sequence_probe2.status = STARTED
        if hasattr(thisTrials_sequence_probe2, 'status'):
            thisTrials_sequence_probe2.status = STARTED
        currentLoop = trials_sequence_probe2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sequence_probe2.rgb)
        if thisTrials_sequence_probe2 != None:
            for paramName in thisTrials_sequence_probe2:
                globals()[paramName] = thisTrials_sequence_probe2[paramName]
        
        # --- Prepare to start Routine "VWM_memory_display" ---
        # create an object to store info about Routine VWM_memory_display
        VWM_memory_display = data.Routine(
            name='VWM_memory_display',
            components=[mem_disc, mem_fix],
        )
        VWM_memory_display.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from memory_sequence_code
        # Get locations for this trial
        path_coords = []
        ## path coords is a list of (x,y) tuples
        for segment in range(path_length):
            if segment == 0:
                segment_coord = (0,0)
            else:
                segment_coord = get_random_path_coord(path_coords[segment-1])
        
            path_coords.append(segment_coord)
        #print(path_coords)
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position
        disc_position = path_coords[segment]
        
        disc_alpha = 1
        path_end = path_coords[segment + 1]
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        # add data to output
        thisExp.addData('path_coords', path_coords)
        
        
        # store start times for VWM_memory_display
        VWM_memory_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_display.tStart = globalClock.getTime(format='float')
        VWM_memory_display.status = STARTED
        thisExp.addData('VWM_memory_display.started', VWM_memory_display.tStart)
        VWM_memory_display.maxDuration = None
        win.color = ''
        win.colorSpace = 'rgb'
        win.backgroundImage = 'abstract-art-3840x2160-23159.jpg'
        win.backgroundFit = 'none'
        # keep track of which components have finished
        VWM_memory_displayComponents = VWM_memory_display.components
        for thisComponent in VWM_memory_display.components:
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
        
        # --- Run Routine "VWM_memory_display" ---
        VWM_memory_display.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe2, 'status') and thisTrials_sequence_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from memory_sequence_code
            
            if pause_timer.getTime() <= 0 and segment < path_length - 1:
                path_end = path_coords[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1        
                disc_position = (new_x, new_y)    
            elif segment >= path_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
            
            
            
            # *mem_disc* updates
            
            # if mem_disc is starting this frame...
            if mem_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_disc.frameNStart = frameN  # exact frame index
                mem_disc.tStart = t  # local t and not account for scr refresh
                mem_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_disc.started')
                # update status
                mem_disc.status = STARTED
                mem_disc.setAutoDraw(True)
            
            # if mem_disc is active this frame...
            if mem_disc.status == STARTED:
                # update params
                mem_disc.setFillColor(disc_alpha, log=False)
                mem_disc.setOpacity(disc_alpha, log=False)
                mem_disc.setPos(disc_position, log=False)
                mem_disc.setLineColor(disc_alpha, log=False)
            
            # *mem_fix* updates
            
            # if mem_fix is starting this frame...
            if mem_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mem_fix.frameNStart = frameN  # exact frame index
                mem_fix.tStart = t  # local t and not account for scr refresh
                mem_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mem_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mem_fix.started')
                # update status
                mem_fix.status = STARTED
                mem_fix.setAutoDraw(True)
            
            # if mem_fix is active this frame...
            if mem_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_display,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_display.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_display.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_display" ---
        for thisComponent in VWM_memory_display.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_display
        VWM_memory_display.tStop = globalClock.getTime(format='float')
        VWM_memory_display.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_display.stopped', VWM_memory_display.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # the Routine "VWM_memory_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "retention" ---
        # create an object to store info about Routine retention
        retention = data.Routine(
            name='retention',
            components=[retention_fix],
        )
        retention.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for retention
        retention.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        retention.tStart = globalClock.getTime(format='float')
        retention.status = STARTED
        thisExp.addData('retention.started', retention.tStart)
        retention.maxDuration = None
        # keep track of which components have finished
        retentionComponents = retention.components
        for thisComponent in retention.components:
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
        
        # --- Run Routine "retention" ---
        retention.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe2, 'status') and thisTrials_sequence_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *retention_fix* updates
            
            # if retention_fix is starting this frame...
            if retention_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                retention_fix.frameNStart = frameN  # exact frame index
                retention_fix.tStart = t  # local t and not account for scr refresh
                retention_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(retention_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'retention_fix.started')
                # update status
                retention_fix.status = STARTED
                retention_fix.setAutoDraw(True)
            
            # if retention_fix is active this frame...
            if retention_fix.status == STARTED:
                # update params
                pass
            
            # if retention_fix is stopping this frame...
            if retention_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > retention_fix.tStartRefresh + retention_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    retention_fix.tStop = t  # not accounting for scr refresh
                    retention_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    retention_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'retention_fix.stopped')
                    # update status
                    retention_fix.status = FINISHED
                    retention_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=retention,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                retention.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in retention.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "retention" ---
        for thisComponent in retention.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for retention
        retention.tStop = globalClock.getTime(format='float')
        retention.tStopRefresh = tThisFlipGlobal
        thisExp.addData('retention.stopped', retention.tStop)
        # the Routine "retention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_memory_probe" ---
        # create an object to store info about Routine VWM_memory_probe
        VWM_memory_probe = data.Routine(
            name='VWM_memory_probe',
            components=[probe_disc, probe_fix],
        )
        VWM_memory_probe.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from probe_sequence_code
        # Get locations for this trial
        
        # by default, we reprise the prior coords
        path_coords_probe = path_coords.copy() # PYTHON VARIABLES ARE DUMB
        probe_length = path_length # Int, don't need to copy.
        
        print(memory_type)
        print(probe_type)
        print(probe_validity)
        
        if probe_validity == "lure":
            if probe_type == "sequence":
                print('generating a sequence lure')
                # pick a position — range 1 to path_length-1 so center (index 0) can be swapped
                lure_pos = int(round(random.uniform(1, path_length - 1),0))
                # swap lure_pos with lure_pos-1
                path_coords_probe[lure_pos] = path_coords[lure_pos - 1]
                path_coords_probe[lure_pos - 1] = path_coords[lure_pos]
        
            elif probe_type == "single":
                print('generating a single lure')
                probe_length = 1
                x = round(max_eccen * random.uniform(-1, 1), 1)
                y = round(max_eccen * random.uniform(-1, 1), 1)
                lure_coords = (x,y)
                a = 1
                while a:
                    for loc in path_coords:
                        x_distance = abs(loc[0] - lure_coords[0])
                        y_distance = abs(loc[1] - lure_coords[1])
                        if x_distance < 0.2 and y_distance < 0.2:
                            x = round(max_eccen * random.uniform(-1, 1), 1)
                            y = round(max_eccen * random.uniform(-1, 1), 1)
                            lure_coords = (x,y)
                            break
                        a = 0
                path_coords_probe = [lure_coords]
        
        else: # probe_validity == target
            if probe_type == "single":
                print('generating a single target')
                probe_pos = int(round(random.uniform(1, path_length-1),0))
                path_coords_probe = [path_coords_probe[probe_pos]]
                probe_length = 1
        
        # For sequence probes: prepend (0,0) as the travel-to-start step.
        # The disc always starts at center, AND center can appear as a
        # mid-sequence location when lure_pos=1 swaps index 0 into position 1.
        if probe_type == "sequence":
            path_coords_probe = [(0,0)] + path_coords_probe
            probe_length = path_length + 1
        
        # Initialize path steps
        segment = 0
        
        # set initial disc position — always (0,0) for sequence (prepended above)
        disc_position = path_coords_probe[segment]
        disc_alpha = 1
        
        # start pause timer
        pause_timer = core.CountdownTimer(pause_duration)
        
        if probe_type == "sequence":
            path_end = path_coords_probe[segment + 1]
        
        if probe_type == "sequence":
            response_string = "F same                           J different"
        else:
            response_string = "F old                                  J new"
        
        thisExp.addData('path_coords_probe', path_coords_probe)
        # store start times for VWM_memory_probe
        VWM_memory_probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_memory_probe.tStart = globalClock.getTime(format='float')
        VWM_memory_probe.status = STARTED
        thisExp.addData('VWM_memory_probe.started', VWM_memory_probe.tStart)
        VWM_memory_probe.maxDuration = None
        # keep track of which components have finished
        VWM_memory_probeComponents = VWM_memory_probe.components
        for thisComponent in VWM_memory_probe.components:
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
        
        # --- Run Routine "VWM_memory_probe" ---
        VWM_memory_probe.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe2, 'status') and thisTrials_sequence_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from probe_sequence_code
            if pause_timer.getTime() <= 0 and probe_type == "sequence" and segment < probe_length - 1:
                #path_end = path_coords[segment + 1]
                path_end = path_coords_probe[segment + 1]
                # get euclidean distance
                dx = path_end[0] - disc_position[0]
                dy = path_end[1] - disc_position[1]
            
                distance = (dx**2 + dy**2) ** 0.5
                if distance > step_size:
                    # move a small step toward the target
                    new_x = disc_position[0] + dx * ( step_size / distance )
                    new_y = disc_position[1] + dy * ( step_size / distance )
                    if memory_type == "continuous":
                        #disc_color = white
                        disc_alpha = 1
                    else:
                        #disc_color = gray
                        disc_alpha = 0
                else:
                    # we've reached the target, snap to position and update segment counter
                    new_x = path_end[0]
                    new_y = path_end[1]
                    #disc_color = white
                    disc_alpha = 1
                    # start pause timer
                    pause_timer = core.CountdownTimer(pause_duration)    
                    segment = segment + 1
                disc_position = (new_x, new_y)
            elif segment >= probe_length - 1 and pause_timer.getTime() <= 0:
                #disc_color = gray
                disc_alpha = 0
                continueRoutine = False  # reached last point
                
            
            
            
            # *probe_disc* updates
            
            # if probe_disc is starting this frame...
            if probe_disc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_disc.frameNStart = frameN  # exact frame index
                probe_disc.tStart = t  # local t and not account for scr refresh
                probe_disc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_disc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_disc.started')
                # update status
                probe_disc.status = STARTED
                probe_disc.setAutoDraw(True)
            
            # if probe_disc is active this frame...
            if probe_disc.status == STARTED:
                # update params
                probe_disc.setFillColor(disc_alpha, log=False)
                probe_disc.setOpacity(disc_alpha, log=False)
                probe_disc.setPos(disc_position, log=False)
                probe_disc.setLineColor(disc_alpha, log=False)
            
            # *probe_fix* updates
            
            # if probe_fix is starting this frame...
            if probe_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_fix.frameNStart = frameN  # exact frame index
                probe_fix.tStart = t  # local t and not account for scr refresh
                probe_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_fix.started')
                # update status
                probe_fix.status = STARTED
                probe_fix.setAutoDraw(True)
            
            # if probe_fix is active this frame...
            if probe_fix.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_memory_probe,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_memory_probe.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_memory_probe.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_memory_probe" ---
        for thisComponent in VWM_memory_probe.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_memory_probe
        VWM_memory_probe.tStop = globalClock.getTime(format='float')
        VWM_memory_probe.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_memory_probe.stopped', VWM_memory_probe.tStop)
        # the Routine "VWM_memory_probe" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "VWM_response" ---
        # create an object to store info about Routine VWM_response
        VWM_response = data.Routine(
            name='VWM_response',
            components=[response_cue, response_instructions, key_resp_VWM],
        )
        VWM_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        response_instructions.setText(response_string)
        # create starting attributes for key_resp_VWM
        key_resp_VWM.keys = []
        key_resp_VWM.rt = []
        _key_resp_VWM_allKeys = []
        # store start times for VWM_response
        VWM_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        VWM_response.tStart = globalClock.getTime(format='float')
        VWM_response.status = STARTED
        thisExp.addData('VWM_response.started', VWM_response.tStart)
        VWM_response.maxDuration = None
        # keep track of which components have finished
        VWM_responseComponents = VWM_response.components
        for thisComponent in VWM_response.components:
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
        
        # --- Run Routine "VWM_response" ---
        VWM_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe2, 'status') and thisTrials_sequence_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_cue* updates
            
            # if response_cue is starting this frame...
            if response_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_cue.frameNStart = frameN  # exact frame index
                response_cue.tStart = t  # local t and not account for scr refresh
                response_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_cue.started')
                # update status
                response_cue.status = STARTED
                response_cue.setAutoDraw(True)
            
            # if response_cue is active this frame...
            if response_cue.status == STARTED:
                # update params
                pass
            
            # *response_instructions* updates
            
            # if response_instructions is starting this frame...
            if response_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_instructions.frameNStart = frameN  # exact frame index
                response_instructions.tStart = t  # local t and not account for scr refresh
                response_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response_instructions.started')
                # update status
                response_instructions.status = STARTED
                response_instructions.setAutoDraw(True)
            
            # if response_instructions is active this frame...
            if response_instructions.status == STARTED:
                # update params
                pass
            
            # *key_resp_VWM* updates
            waitOnFlip = False
            
            # if key_resp_VWM is starting this frame...
            if key_resp_VWM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_VWM.frameNStart = frameN  # exact frame index
                key_resp_VWM.tStart = t  # local t and not account for scr refresh
                key_resp_VWM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_VWM, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_VWM.started')
                # update status
                key_resp_VWM.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_VWM.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_VWM.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_VWM.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_VWM.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_VWM_allKeys.extend(theseKeys)
                if len(_key_resp_VWM_allKeys):
                    key_resp_VWM.keys = _key_resp_VWM_allKeys[-1].name  # just the last key pressed
                    key_resp_VWM.rt = _key_resp_VWM_allKeys[-1].rt
                    key_resp_VWM.duration = _key_resp_VWM_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=VWM_response,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                VWM_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VWM_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "VWM_response" ---
        for thisComponent in VWM_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for VWM_response
        VWM_response.tStop = globalClock.getTime(format='float')
        VWM_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('VWM_response.stopped', VWM_response.tStop)
        # check responses
        if key_resp_VWM.keys in ['', [], None]:  # No response was made
            key_resp_VWM.keys = None
        trials_sequence_probe2.addData('key_resp_VWM.keys',key_resp_VWM.keys)
        if key_resp_VWM.keys != None:  # we had a response
            trials_sequence_probe2.addData('key_resp_VWM.rt', key_resp_VWM.rt)
            trials_sequence_probe2.addData('key_resp_VWM.duration', key_resp_VWM.duration)
        # the Routine "VWM_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_2" ---
        # create an object to store info about Routine break_2
        break_2 = data.Routine(
            name='break_2',
            components=[break_txt, break_resp],
        )
        break_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for break_resp
        break_resp.keys = []
        break_resp.rt = []
        _break_resp_allKeys = []
        # store start times for break_2
        break_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        break_2.tStart = globalClock.getTime(format='float')
        break_2.status = STARTED
        thisExp.addData('break_2.started', break_2.tStart)
        break_2.maxDuration = None
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        # keep track of which components have finished
        break_2Components = break_2.components
        for thisComponent in break_2.components:
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
        
        # --- Run Routine "break_2" ---
        break_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe2, 'status') and thisTrials_sequence_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *break_txt* updates
            
            # if break_txt is starting this frame...
            if break_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_txt.frameNStart = frameN  # exact frame index
                break_txt.tStart = t  # local t and not account for scr refresh
                break_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_txt.started')
                # update status
                break_txt.status = STARTED
                break_txt.setAutoDraw(True)
            
            # if break_txt is active this frame...
            if break_txt.status == STARTED:
                # update params
                pass
            
            # *break_resp* updates
            waitOnFlip = False
            
            # if break_resp is starting this frame...
            if break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_resp.frameNStart = frameN  # exact frame index
                break_resp.tStart = t  # local t and not account for scr refresh
                break_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_resp.started')
                # update status
                break_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(break_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if break_resp.status == STARTED and not waitOnFlip:
                theseKeys = break_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _break_resp_allKeys.extend(theseKeys)
                if len(_break_resp_allKeys):
                    break_resp.keys = _break_resp_allKeys[-1].name  # just the last key pressed
                    break_resp.rt = _break_resp_allKeys[-1].rt
                    break_resp.duration = _break_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=break_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for break_2
        break_2.tStop = globalClock.getTime(format='float')
        break_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('break_2.stopped', break_2.tStop)
        setupWindow(expInfo=expInfo, win=win)
        # check responses
        if break_resp.keys in ['', [], None]:  # No response was made
            break_resp.keys = None
        trials_sequence_probe2.addData('break_resp.keys',break_resp.keys)
        if break_resp.keys != None:  # we had a response
            trials_sequence_probe2.addData('break_resp.rt', break_resp.rt)
            trials_sequence_probe2.addData('break_resp.duration', break_resp.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_fix],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = 1
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
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
        
        # --- Run Routine "ITI" ---
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sequence_probe2, 'status') and thisTrials_sequence_probe2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > ITI.maxDuration-frameTolerance:
                ITI.maxDurationReached = True
                continueRoutine = False
            
            # *ITI_fix* updates
            
            # if ITI_fix is starting this frame...
            if ITI_fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                ITI_fix.frameNStart = frameN  # exact frame index
                ITI_fix.tStart = t  # local t and not account for scr refresh
                ITI_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_fix.started')
                # update status
                ITI_fix.status = STARTED
                ITI_fix.setAutoDraw(True)
            
            # if ITI_fix is active this frame...
            if ITI_fix.status == STARTED:
                # update params
                pass
            
            # if ITI_fix is stopping this frame...
            if ITI_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_fix.tStop = t  # not accounting for scr refresh
                    ITI_fix.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_fix.stopped')
                    # update status
                    ITI_fix.status = FINISHED
                    ITI_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisTrials_sequence_probe2 as finished
        if hasattr(thisTrials_sequence_probe2, 'status'):
            thisTrials_sequence_probe2.status = FINISHED
        # if awaiting a pause, pause now
        if trials_sequence_probe2.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_sequence_probe2.status = STARTED
        thisExp.nextEntry()
        
    # completed seq_nreps repeats of 'trials_sequence_probe2'
    trials_sequence_probe2.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "thank_you" ---
    # create an object to store info about Routine thank_you
    thank_you = data.Routine(
        name='thank_you',
        components=[ty],
    )
    thank_you.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for thank_you
    thank_you.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thank_you.tStart = globalClock.getTime(format='float')
    thank_you.status = STARTED
    thisExp.addData('thank_you.started', thank_you.tStart)
    thank_you.maxDuration = None
    win.color = [0,0,0]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    thank_youComponents = thank_you.components
    for thisComponent in thank_you.components:
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
    
    # --- Run Routine "thank_you" ---
    thank_you.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ty* updates
        
        # if ty is starting this frame...
        if ty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ty.frameNStart = frameN  # exact frame index
            ty.tStart = t  # local t and not account for scr refresh
            ty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ty, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ty.started')
            # update status
            ty.status = STARTED
            ty.setAutoDraw(True)
        
        # if ty is active this frame...
        if ty.status == STARTED:
            # update params
            pass
        
        # if ty is stopping this frame...
        if ty.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ty.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                ty.tStop = t  # not accounting for scr refresh
                ty.tStopRefresh = tThisFlipGlobal  # on global time
                ty.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ty.stopped')
                # update status
                ty.status = FINISHED
                ty.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thank_you,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            thank_you.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thank_you.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thank_you" ---
    for thisComponent in thank_you.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thank_you
    thank_you.tStop = globalClock.getTime(format='float')
    thank_you.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thank_you.stopped', thank_you.tStop)
    setupWindow(expInfo=expInfo, win=win)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thank_you.maxDurationReached:
        routineTimer.addTime(-thank_you.maxDuration)
    elif thank_you.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
