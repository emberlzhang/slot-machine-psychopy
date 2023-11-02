#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Wed Jul 19 16:09:38 2023
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
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

# Run 'Before Experiment' code from code_practice_reset
card_size = [0.4, 0.4]
cardPositions = [(-0.5, 0.2), (0, 0.2), (0.5, 0.2)]
slotImageLocations = ["stimuli/card_circ_transparent.png", "stimuli/card_pent_transparent.png", 
                      "stimuli/card_sqr_transparent.png", "stimuli/card_star_transparent.png", 
                      "stimuli/card_tri_transparent.png"]

textPosition = [0,-0.1]

intervalAfterSelection = [0.5, 1, 1.5]

arrowSize = [0.20, 0.20]
arrow_loc = [0.50,-0.30]

boxPos = [0,0]

rewardImageSize = [0.30,0.25]
rewardPresentationTime = 0.3
rewardImagePostions = [(-0.530, 0.210), (-0.025, 0.210), (0.475, 0.210)]
rewardImageLocations = ["stimuli/card_100_transparent.png", "stimuli/card_10_transparent.png", 
                        "stimuli/card_0_transparent.png"]
consReward_pos = [[0.2,-0.30],[0,-0.30],[-0.2,-0.30],[-0.4,-0.30],[-0.6,-0.30]]

conditions = [(12,20), (8,20), (7,20), (10,20), (7,14,20), (13,20)]
rewardSeq = [[[2,1,3],[2,3,1]],
             [[1,3,2],[3,2,1]], 
             [[3,1,2],[1,2,3]], 
             [[1,2,3],[3,2,1]], 
             [[2,3,1],[2,1,3],[1,3,2]],
             [[3,2,1],[1,3,2]]]
DictCondRew = {(12,20): [[2,1,3],[2,3,1]], 
                (8,20): [[1,3,2],[3,2,1]], 
                (7,20): [[3,1,2],[1,2,3]], 
                (10,20): [[1,2,3],[3,2,1]], 
                (7,14,20): [[2,3,1],[2,1,3],[1,3,2]],
                (13,20):[[3,2,1],[1,3,2]]}
# Run 'Before Experiment' code from code_practice_rewards
joystickValues = [0,1,2]
keyboardNumbers = ['1', '2', '3']
keyboardArrows = ['left', 'up', 'right']
reward_seq = []
rand_val = 0
currentTrialReward = 0

# Run 'Before Experiment' code from code_reward_presentation
reward_seqs = []


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'slotMachine'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
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
    originPath='/Users/janet/Desktop/Sinai_Projects/Code/Psychopy_slotMachine_updated/slotMachine_updated_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
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

# --- Initialize components for Routine "intro_video" ---
movie = visual.MovieStim(
    win, name='movie',
    filename='stimuli/The Slot Machine Game_FINAL_3.29.23.mp4', movieLib='ffpyplayer',
    loop=False, volume=1.0, noAudio=False,
    pos=(0, 0), size=(0.9, 0.5), units=win.units,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
    depth=0
)

# --- Initialize components for Routine "practice_instruction" ---
# Run 'Begin Experiment' code from code_practice_instruction
#nBlocks = 2
nPracticeTrials = 15
#reversalNo = 3

text_practice_instruction = visual.TextStim(win=win, name='text_practice_instruction',
    text='Welcome to slot machine game.\n\nImagine that you go to a casino to play with three slot machines for six days. Each day you can play 20 rounds on any of these machines. Each round, you can select a machine and you will receive a reward.\n\nPress any key to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_practice_instruction = keyboard.Keyboard()

# --- Initialize components for Routine "instruction2" ---
text = visual.TextStim(win=win, name='text',
    text='But there is something strange about these machines: they are malfunctioning! \n\nThere is always a machine that grants many high rewards (most of the rounds 100 points, but sometimes only 10 or even 0), there is always a machine that grants many low rewards (mostly 10 points, sometimes 100 or 0), and one that grants no reward most of the rounds (mostly 0 points, sometimes 100 or 10). You have to find the appropriate machines to maximise your reward.\n\nPress any key to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "practice_reset" ---
# Run 'Begin Experiment' code from code_practice_reset
#block_reward = []
#
#conditions = [(12,20), (8,20), (7,20), (10,20), (7,14,20)]
#
text_practice_reset = visual.TextStim(win=win, name='text_practice_reset',
    text='Every day, the malfunctioning machines will be different and they also may or may not change within the same day. So the correct selection may become the wrong one after a while. You will have to adapt!\n\nThe game takes approximately 10 minutes to complete and starts with a quick practice.\n\nPress the LEFT, UP or RIGHT arrows on the keyboard to select your slot machine.\n\nPress any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_practice_reset = keyboard.Keyboard()

# --- Initialize components for Routine "practice_slots" ---
card_circ = visual.ImageStim(
    win=win,
    name='card_circ', 
    image=slotImageLocations[0], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[0]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
card_pent = visual.ImageStim(
    win=win,
    name='card_pent', 
    image=slotImageLocations[1], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[1]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
card_sqr = visual.ImageStim(
    win=win,
    name='card_sqr', 
    image=slotImageLocations[2], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[2]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
arrow_4 = visual.ImageStim(
    win=win,
    name='arrow_4', 
    image='stimuli/arrow_transparent.png', mask=None, anchor='center',
    ori=0.0, pos=arrow_loc, size=arrowSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_21 = visual.ImageStim(
    win=win,
    name='image_21', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
text_practice_slots = visual.TextStim(win=win, name='text_practice_slots',
    text='',
    font='Open Sans',
    pos=textPosition, height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
text_practice_slots_2 = visual.TextStim(win=win, name='text_practice_slots_2',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.17, 0.17)[0], height=(0.17, 0.17)[1],
    ori=0.0, pos=[consReward_pos[0]], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=None,
    opacity=0.5, depth=-12.0, interpolate=True)
key_resp_practice_slots = keyboard.Keyboard()

# --- Initialize components for Routine "practice_interval" ---
card_circ_6 = visual.ImageStim(
    win=win,
    name='card_circ_6', 
    image=slotImageLocations[0], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[0]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
card_pent_6 = visual.ImageStim(
    win=win,
    name='card_pent_6', 
    image=slotImageLocations[1], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[1]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
card_sqr_6 = visual.ImageStim(
    win=win,
    name='card_sqr_6', 
    image=slotImageLocations[2], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[2]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
arrow_5 = visual.ImageStim(
    win=win,
    name='arrow_5', 
    image='stimuli/arrow_transparent.png', mask=None, anchor='center',
    ori=0.0, pos=arrow_loc, size=arrowSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
text_practice_interval = visual.TextStim(win=win, name='text_practice_interval',
    text='',
    font='Open Sans',
    pos=textPosition, height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-10.0);
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.17, 0.17)[0], height=(0.17, 0.17)[1],
    ori=0.0, pos=[consReward_pos[0]], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=None,
    opacity=0.5, depth=-11.0, interpolate=True)
polygon_practice_interval = visual.Rect(
    win=win, name='polygon_practice_interval',
    width=card_size[0], height=card_size[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[-0.0667, 0.0667, 0.2000],
    opacity=0.5, depth=-12.0, interpolate=True)

# --- Initialize components for Routine "practice_rewards" ---
# Run 'Begin Experiment' code from code_practice_rewards

rewPos = [0,0]
rewImg = "stimuli/blank_transparent.png"

card_circ_7 = visual.ImageStim(
    win=win,
    name='card_circ_7', 
    image=slotImageLocations[0], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[0]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
card_pent_7 = visual.ImageStim(
    win=win,
    name='card_pent_7', 
    image=slotImageLocations[1], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[1]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
card_sqr_7 = visual.ImageStim(
    win=win,
    name='card_sqr_7', 
    image=slotImageLocations[2], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[2]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
arrow_6 = visual.ImageStim(
    win=win,
    name='arrow_6', 
    image='stimuli/arrow_transparent.png', mask=None, anchor='center',
    ori=0.0, pos=arrow_loc, size=arrowSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_27 = visual.ImageStim(
    win=win,
    name='image_27', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=rewardImageSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_28 = visual.ImageStim(
    win=win,
    name='image_28', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[0]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_29 = visual.ImageStim(
    win=win,
    name='image_29', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[1]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_30 = visual.ImageStim(
    win=win,
    name='image_30', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[2]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_31 = visual.ImageStim(
    win=win,
    name='image_31', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[3]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
image_32 = visual.ImageStim(
    win=win,
    name='image_32', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[4]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.17, 0.17)[0], height=(0.17, 0.17)[1],
    ori=0.0, pos=[consReward_pos[0]], anchor='center',
    lineWidth=20.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=None,
    opacity=0.5, depth=-11.0, interpolate=True)
text_practice_rewards = visual.TextStim(win=win, name='text_practice_rewards',
    text='',
    font='Open Sans',
    pos=textPosition, height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0039, 0.0039, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# --- Initialize components for Routine "practice_end" ---
text_practice_end = visual.TextStim(win=win, name='text_practice_end',
    text='You have successfully completed the practice.\n\nNow you are ready to start the game.\n\nPress SPACE key to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_practice_end = keyboard.Keyboard()

# --- Initialize components for Routine "Main_Instruction" ---
# Run 'Begin Experiment' code from code_main_instruction
nBlocks = 10
nTrials = 15
#reversalNo = 3

text_main_instruction = visual.TextStim(win=win, name='text_main_instruction',
    text='Press one of the following arrows on the keyboard to select your slot machine\n\nLEFT, UP, RIGHT\n\n\nPress SPACE key to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_main_instruction = keyboard.Keyboard()

# --- Initialize components for Routine "reward_reset" ---
# Run 'Begin Experiment' code from code_reward_reset
block_reward = []


# --- Initialize components for Routine "slots_presentation" ---
card_circ_3 = visual.ImageStim(
    win=win,
    name='card_circ_3', 
    image=slotImageLocations[0], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[0]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
card_pent_3 = visual.ImageStim(
    win=win,
    name='card_pent_3', 
    image=slotImageLocations[1], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[1]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
card_sqr_3 = visual.ImageStim(
    win=win,
    name='card_sqr_3', 
    image=slotImageLocations[2], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[2]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image='stimuli/arrow_transparent.png', mask=None, anchor='center',
    ori=0.0, pos=arrow_loc, size=arrowSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
text_slots_presentation = visual.TextStim(win=win, name='text_slots_presentation',
    text='',
    font='Open Sans',
    pos=textPosition, height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
text_slots_presentation_2 = visual.TextStim(win=win, name='text_slots_presentation_2',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(0.17, 0.17)[0], height=(0.17, 0.17)[1],
    ori=0.0, pos=[consReward_pos[0]], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=None,
    opacity=0.5, depth=-12.0, interpolate=True)
key_resp_slots_presentation = keyboard.Keyboard()

# --- Initialize components for Routine "selection_interval" ---
card_circ_5 = visual.ImageStim(
    win=win,
    name='card_circ_5', 
    image=slotImageLocations[0], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[0]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
card_pent_5 = visual.ImageStim(
    win=win,
    name='card_pent_5', 
    image=slotImageLocations[1], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[1]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
card_sqr_5 = visual.ImageStim(
    win=win,
    name='card_sqr_5', 
    image=slotImageLocations[2], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[2]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
arrow_2 = visual.ImageStim(
    win=win,
    name='arrow_2', 
    image='stimuli/arrow_transparent.png', mask=None, anchor='center',
    ori=0.0, pos=arrow_loc, size=arrowSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
polygon_selection_interval = visual.Rect(
    win=win, name='polygon_selection_interval',
    width=card_size[0], height=card_size[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[-0.0667, 0.0667, 0.2000],
    opacity=0.5, depth=-10.0, interpolate=True)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(0.17, 0.17)[0], height=(0.17, 0.17)[1],
    ori=0.0, pos=[consReward_pos[0]], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=None,
    opacity=0.5, depth=-11.0, interpolate=True)
text_selection_interval = visual.TextStim(win=win, name='text_selection_interval',
    text='',
    font='Open Sans',
    pos=textPosition, height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-12.0);

# --- Initialize components for Routine "reward_presentation" ---
# Run 'Begin Experiment' code from code_reward_presentation
'''
shuffle(conditions)
thisExp.addData('Main_conditions',conditions)
thisExp.nextEntry()

currentCondition = conditions[0]
thisExp.addData('Main_currentCondition',currentCondition)
thisExp.nextEntry()

conditions.remove(currentCondition) ## Check if this works
thisExp.addData('Main_conditionsAfterRemoval',conditions)
thisExp.nextEntry()
'''
rewPos = [0,0]
rewImg = "stimuli/blank_transparent.png"

card_circ_4 = visual.ImageStim(
    win=win,
    name='card_circ_4', 
    image=slotImageLocations[0], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[0]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
card_pent_4 = visual.ImageStim(
    win=win,
    name='card_pent_4', 
    image=slotImageLocations[1], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[1]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
card_sqr_4 = visual.ImageStim(
    win=win,
    name='card_sqr_4', 
    image=slotImageLocations[2], mask=None, anchor='center',
    ori=0.0, pos=[cardPositions[2]], size=card_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
arrow_3 = visual.ImageStim(
    win=win,
    name='arrow_3', 
    image='stimuli/arrow_transparent.png', mask=None, anchor='center',
    ori=0.0, pos=arrow_loc, size=arrowSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=rewardImageSize,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[0]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[1]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[2]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[3]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[consReward_pos[4]], size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.17, 0.17)[0], height=(0.17, 0.17)[1],
    ori=0.0, pos=[consReward_pos[0]], anchor='center',
    lineWidth=20.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=None,
    opacity=0.5, depth=-11.0, interpolate=True)
text_reward_presentation = visual.TextStim(win=win, name='text_reward_presentation',
    text='',
    font='Open Sans',
    pos=textPosition, height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0039, 0.0039, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# --- Initialize components for Routine "Block_break" ---
text_block_break = visual.TextStim(win=win, name='text_block_break',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "End_ins" ---
text_end_ins = visual.TextStim(win=win, name='text_end_ins',
    text='\nYou have successfully completed the task.\n\nPlease let our researcher know.\n\nThank you.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro_video" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
intro_videoComponents = [movie]
for thisComponent in intro_videoComponents:
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

# --- Run Routine "intro_video" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    
    # if movie is starting this frame...
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movie.started')
        # update status
        movie.status = STARTED
        movie.setAutoDraw(True)
        movie.play()
    if movie.isFinished:  # force-end the routine
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_video" ---
for thisComponent in intro_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()
# the Routine "intro_video" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "practice_instruction" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code_practice_instruction
thisExp.addData('key_resp_practice_instruction.started', globalClock.getTime())

key_resp_practice_instruction.keys = []
key_resp_practice_instruction.rt = []
_key_resp_practice_instruction_allKeys = []
# keep track of which components have finished
practice_instructionComponents = [text_practice_instruction, key_resp_practice_instruction]
for thisComponent in practice_instructionComponents:
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

# --- Run Routine "practice_instruction" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_practice_instruction* updates
    
    # if text_practice_instruction is starting this frame...
    if text_practice_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_practice_instruction.frameNStart = frameN  # exact frame index
        text_practice_instruction.tStart = t  # local t and not account for scr refresh
        text_practice_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_practice_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_practice_instruction.started')
        # update status
        text_practice_instruction.status = STARTED
        text_practice_instruction.setAutoDraw(True)
    
    # if text_practice_instruction is active this frame...
    if text_practice_instruction.status == STARTED:
        # update params
        pass
    
    # *key_resp_practice_instruction* updates
    waitOnFlip = False
    
    # if key_resp_practice_instruction is starting this frame...
    if key_resp_practice_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_practice_instruction.frameNStart = frameN  # exact frame index
        key_resp_practice_instruction.tStart = t  # local t and not account for scr refresh
        key_resp_practice_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_practice_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_practice_instruction.started')
        # update status
        key_resp_practice_instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_practice_instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_practice_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_practice_instruction.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_practice_instruction.getKeys(keyList=None, waitRelease=False)
        _key_resp_practice_instruction_allKeys.extend(theseKeys)
        if len(_key_resp_practice_instruction_allKeys):
            key_resp_practice_instruction.keys = _key_resp_practice_instruction_allKeys[-1].name  # just the last key pressed
            key_resp_practice_instruction.rt = _key_resp_practice_instruction_allKeys[-1].rt
            key_resp_practice_instruction.duration = _key_resp_practice_instruction_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_instruction" ---
for thisComponent in practice_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_practice_instruction.keys in ['', [], None]:  # No response was made
    key_resp_practice_instruction.keys = None
thisExp.addData('key_resp_practice_instruction.keys',key_resp_practice_instruction.keys)
if key_resp_practice_instruction.keys != None:  # we had a response
    thisExp.addData('key_resp_practice_instruction.rt', key_resp_practice_instruction.rt)
    thisExp.addData('key_resp_practice_instruction.duration', key_resp_practice_instruction.duration)
thisExp.nextEntry()
# the Routine "practice_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# Run 'Begin Routine' code from code_2
thisExp.addData('key_resp.started', globalClock.getTime())

# keep track of which components have finished
instruction2Components = [text, key_resp]
for thisComponent in instruction2Components:
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

# --- Run Routine "instruction2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            key_resp.duration = _key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction2" ---
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.duration', key_resp.duration)
thisExp.nextEntry()
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "practice_reset" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code_practice_reset
'''
conditions = [(12,20), (8,20), (7,20), (10,20), (7,14,20), (13,20)]
shuffle(conditions)
thisExp.addData('conditions',conditions)
thisExp.nextEntry()

currentCondition = conditions[0]
thisExp.addData('currentCondition',currentCondition)
thisExp.nextEntry()

conditions.remove(currentCondition) ## Check if this works
thisExp.addData('conditionsAfterRemoval',conditions)
thisExp.nextEntry()
'''
thisExp.addData('key_resp_practice_reset.started', globalClock.getTime())

nCorr = 0

consRewardImgs = ["stimuli/blank_transparent.png", "stimuli/blank_transparent.png", "stimuli/blank_transparent.png", "stimuli/blank_transparent.png", "stimuli/blank_transparent.png"]

#thisExp.addData('key_resp_practice_reset.started', practice_resetClock.getTime())

key_resp_practice_reset.keys = []
key_resp_practice_reset.rt = []
_key_resp_practice_reset_allKeys = []
# keep track of which components have finished
practice_resetComponents = [text_practice_reset, key_resp_practice_reset]
for thisComponent in practice_resetComponents:
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

# --- Run Routine "practice_reset" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_practice_reset* updates
    
    # if text_practice_reset is starting this frame...
    if text_practice_reset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_practice_reset.frameNStart = frameN  # exact frame index
        text_practice_reset.tStart = t  # local t and not account for scr refresh
        text_practice_reset.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_practice_reset, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_practice_reset.started')
        # update status
        text_practice_reset.status = STARTED
        text_practice_reset.setAutoDraw(True)
    
    # if text_practice_reset is active this frame...
    if text_practice_reset.status == STARTED:
        # update params
        pass
    
    # *key_resp_practice_reset* updates
    waitOnFlip = False
    
    # if key_resp_practice_reset is starting this frame...
    if key_resp_practice_reset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_practice_reset.frameNStart = frameN  # exact frame index
        key_resp_practice_reset.tStart = t  # local t and not account for scr refresh
        key_resp_practice_reset.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_practice_reset, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_practice_reset.started')
        # update status
        key_resp_practice_reset.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_practice_reset.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_practice_reset.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_practice_reset.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_practice_reset.getKeys(keyList=None, waitRelease=False)
        _key_resp_practice_reset_allKeys.extend(theseKeys)
        if len(_key_resp_practice_reset_allKeys):
            key_resp_practice_reset.keys = _key_resp_practice_reset_allKeys[-1].name  # just the last key pressed
            key_resp_practice_reset.rt = _key_resp_practice_reset_allKeys[-1].rt
            key_resp_practice_reset.duration = _key_resp_practice_reset_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_resetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_reset" ---
for thisComponent in practice_resetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_practice_reset.keys in ['', [], None]:  # No response was made
    key_resp_practice_reset.keys = None
thisExp.addData('key_resp_practice_reset.keys',key_resp_practice_reset.keys)
if key_resp_practice_reset.keys != None:  # we had a response
    thisExp.addData('key_resp_practice_reset.rt', key_resp_practice_reset.rt)
    thisExp.addData('key_resp_practice_reset.duration', key_resp_practice_reset.duration)
thisExp.nextEntry()
# the Routine "practice_reset" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=nPracticeTrials, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "practice_slots" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Code_practice_slots
    thisExp.addData('key_resp_practice_slots.started', globalClock.getTime())
    
    textMsg = "Total reward: " + str(nCorr)
    endMsg = " "
    
    endTrial = False
    image.setPos([consReward_pos[0]])
    image.setImage(consRewardImgs[4])
    image_18.setPos([consReward_pos[1]])
    image_18.setImage(consRewardImgs[3])
    image_19.setPos([consReward_pos[2]])
    image_19.setImage(consRewardImgs[2])
    image_20.setPos([consReward_pos[3]])
    image_20.setImage(consRewardImgs[1])
    image_21.setPos([consReward_pos[4]])
    image_21.setImage(consRewardImgs[0])
    text_practice_slots.setText(textMsg)
    key_resp_practice_slots.keys = []
    key_resp_practice_slots.rt = []
    _key_resp_practice_slots_allKeys = []
    # keep track of which components have finished
    practice_slotsComponents = [card_circ, card_pent, card_sqr, arrow_4, image, image_18, image_19, image_20, image_21, text_practice_slots, text_practice_slots_2, polygon, key_resp_practice_slots]
    for thisComponent in practice_slotsComponents:
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
    
    # --- Run Routine "practice_slots" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Code_practice_slots
        
        if t > 5.0 and len(key_resp_practice_slots.getKeys()) == 0:
            endMsg = "Too slow"
            endTrial = True
            if t > 5.5 and len(key_resp_practice_slots.getKeys()) == 0:
                continueRoutine = False
        
        
        # *card_circ* updates
        
        # if card_circ is starting this frame...
        if card_circ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_circ.frameNStart = frameN  # exact frame index
            card_circ.tStart = t  # local t and not account for scr refresh
            card_circ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_circ, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_circ.status = STARTED
            card_circ.setAutoDraw(True)
        
        # if card_circ is active this frame...
        if card_circ.status == STARTED:
            # update params
            pass
        
        # *card_pent* updates
        
        # if card_pent is starting this frame...
        if card_pent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_pent.frameNStart = frameN  # exact frame index
            card_pent.tStart = t  # local t and not account for scr refresh
            card_pent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_pent, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_pent.status = STARTED
            card_pent.setAutoDraw(True)
        
        # if card_pent is active this frame...
        if card_pent.status == STARTED:
            # update params
            pass
        
        # *card_sqr* updates
        
        # if card_sqr is starting this frame...
        if card_sqr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_sqr.frameNStart = frameN  # exact frame index
            card_sqr.tStart = t  # local t and not account for scr refresh
            card_sqr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_sqr, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_sqr.status = STARTED
            card_sqr.setAutoDraw(True)
        
        # if card_sqr is active this frame...
        if card_sqr.status == STARTED:
            # update params
            pass
        
        # *arrow_4* updates
        
        # if arrow_4 is starting this frame...
        if arrow_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow_4.frameNStart = frameN  # exact frame index
            arrow_4.tStart = t  # local t and not account for scr refresh
            arrow_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            arrow_4.status = STARTED
            arrow_4.setAutoDraw(True)
        
        # if arrow_4 is active this frame...
        if arrow_4.status == STARTED:
            # update params
            pass
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # *image_18* updates
        
        # if image_18 is starting this frame...
        if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_18.frameNStart = frameN  # exact frame index
            image_18.tStart = t  # local t and not account for scr refresh
            image_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_18.status = STARTED
            image_18.setAutoDraw(True)
        
        # if image_18 is active this frame...
        if image_18.status == STARTED:
            # update params
            pass
        
        # *image_19* updates
        
        # if image_19 is starting this frame...
        if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_19.frameNStart = frameN  # exact frame index
            image_19.tStart = t  # local t and not account for scr refresh
            image_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_19.status = STARTED
            image_19.setAutoDraw(True)
        
        # if image_19 is active this frame...
        if image_19.status == STARTED:
            # update params
            pass
        
        # *image_20* updates
        
        # if image_20 is starting this frame...
        if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_20.frameNStart = frameN  # exact frame index
            image_20.tStart = t  # local t and not account for scr refresh
            image_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_20.status = STARTED
            image_20.setAutoDraw(True)
        
        # if image_20 is active this frame...
        if image_20.status == STARTED:
            # update params
            pass
        
        # *image_21* updates
        
        # if image_21 is starting this frame...
        if image_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_21.frameNStart = frameN  # exact frame index
            image_21.tStart = t  # local t and not account for scr refresh
            image_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_21.status = STARTED
            image_21.setAutoDraw(True)
        
        # if image_21 is active this frame...
        if image_21.status == STARTED:
            # update params
            pass
        
        # *text_practice_slots* updates
        
        # if text_practice_slots is starting this frame...
        if text_practice_slots.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_slots.frameNStart = frameN  # exact frame index
            text_practice_slots.tStart = t  # local t and not account for scr refresh
            text_practice_slots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_slots, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_practice_slots.started')
            # update status
            text_practice_slots.status = STARTED
            text_practice_slots.setAutoDraw(True)
        
        # if text_practice_slots is active this frame...
        if text_practice_slots.status == STARTED:
            # update params
            pass
        
        # *text_practice_slots_2* updates
        
        # if text_practice_slots_2 is starting this frame...
        if text_practice_slots_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_slots_2.frameNStart = frameN  # exact frame index
            text_practice_slots_2.tStart = t  # local t and not account for scr refresh
            text_practice_slots_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_slots_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_practice_slots_2.started')
            # update status
            text_practice_slots_2.status = STARTED
            text_practice_slots_2.setAutoDraw(True)
        
        # if text_practice_slots_2 is active this frame...
        if text_practice_slots_2.status == STARTED:
            # update params
            text_practice_slots_2.setText(endMsg, log=False)
        
        # *polygon* updates
        
        # if polygon is starting this frame...
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # update status
            polygon.status = STARTED
            polygon.setAutoDraw(True)
        
        # if polygon is active this frame...
        if polygon.status == STARTED:
            # update params
            pass
        
        # *key_resp_practice_slots* updates
        waitOnFlip = False
        
        # if key_resp_practice_slots is starting this frame...
        if key_resp_practice_slots.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice_slots.frameNStart = frameN  # exact frame index
            key_resp_practice_slots.tStart = t  # local t and not account for scr refresh
            key_resp_practice_slots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice_slots, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_practice_slots.started')
            # update status
            key_resp_practice_slots.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice_slots.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice_slots.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice_slots.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice_slots.getKeys(keyList=['1','2','3','left','up','right'], waitRelease=False)
            _key_resp_practice_slots_allKeys.extend(theseKeys)
            if len(_key_resp_practice_slots_allKeys):
                key_resp_practice_slots.keys = _key_resp_practice_slots_allKeys[-1].name  # just the last key pressed
                key_resp_practice_slots.rt = _key_resp_practice_slots_allKeys[-1].rt
                key_resp_practice_slots.duration = _key_resp_practice_slots_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_slotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_slots" ---
    for thisComponent in practice_slotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_practice_slots.keys in ['', [], None]:  # No response was made
        key_resp_practice_slots.keys = None
    practice_trials.addData('key_resp_practice_slots.keys',key_resp_practice_slots.keys)
    if key_resp_practice_slots.keys != None:  # we had a response
        practice_trials.addData('key_resp_practice_slots.rt', key_resp_practice_slots.rt)
        practice_trials.addData('key_resp_practice_slots.duration', key_resp_practice_slots.duration)
    # the Routine "practice_slots" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_interval" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Code_practice_interval
    
    if endTrial:
        continueRoutine = False
    
    presentationInterval = randchoice(intervalAfterSelection)
    
    thisExp.addData('presentationInterval',presentationInterval)
    #thisExp.nextEntry()
    
    #presentationInterval = random.choice(intervalAfterSelection)
    
    if key_resp_practice_slots.keys == keyboardNumbers[0] or key_resp_practice_slots.keys == keyboardArrows[0]:
        boxPos = cardPositions[0]
    elif key_resp_practice_slots.keys == keyboardNumbers[1] or key_resp_practice_slots.keys == keyboardArrows[1]:
        boxPos = cardPositions[1]
    elif key_resp_practice_slots.keys == keyboardNumbers[2] or key_resp_practice_slots.keys == keyboardArrows[2]:
        boxPos = cardPositions[2]
    
    image_22.setPos([consReward_pos[0]])
    image_22.setImage(consRewardImgs[4])
    image_23.setPos([consReward_pos[1]])
    image_23.setImage(consRewardImgs[3])
    image_24.setPos([consReward_pos[2]])
    image_24.setImage(consRewardImgs[2])
    image_25.setPos([consReward_pos[3]])
    image_25.setImage(consRewardImgs[1])
    image_26.setPos([consReward_pos[4]])
    image_26.setImage(consRewardImgs[0])
    text_practice_interval.setText(textMsg)
    polygon_practice_interval.setPos(boxPos)
    # keep track of which components have finished
    practice_intervalComponents = [card_circ_6, card_pent_6, card_sqr_6, arrow_5, image_22, image_23, image_24, image_25, image_26, text_practice_interval, polygon_2, polygon_practice_interval]
    for thisComponent in practice_intervalComponents:
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
    
    # --- Run Routine "practice_interval" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *card_circ_6* updates
        
        # if card_circ_6 is starting this frame...
        if card_circ_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_circ_6.frameNStart = frameN  # exact frame index
            card_circ_6.tStart = t  # local t and not account for scr refresh
            card_circ_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_circ_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_circ_6.status = STARTED
            card_circ_6.setAutoDraw(True)
        
        # if card_circ_6 is active this frame...
        if card_circ_6.status == STARTED:
            # update params
            pass
        
        # if card_circ_6 is stopping this frame...
        if card_circ_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card_circ_6.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                card_circ_6.tStop = t  # not accounting for scr refresh
                card_circ_6.frameNStop = frameN  # exact frame index
                # update status
                card_circ_6.status = FINISHED
                card_circ_6.setAutoDraw(False)
        
        # *card_pent_6* updates
        
        # if card_pent_6 is starting this frame...
        if card_pent_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_pent_6.frameNStart = frameN  # exact frame index
            card_pent_6.tStart = t  # local t and not account for scr refresh
            card_pent_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_pent_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_pent_6.status = STARTED
            card_pent_6.setAutoDraw(True)
        
        # if card_pent_6 is active this frame...
        if card_pent_6.status == STARTED:
            # update params
            pass
        
        # if card_pent_6 is stopping this frame...
        if card_pent_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card_pent_6.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                card_pent_6.tStop = t  # not accounting for scr refresh
                card_pent_6.frameNStop = frameN  # exact frame index
                # update status
                card_pent_6.status = FINISHED
                card_pent_6.setAutoDraw(False)
        
        # *card_sqr_6* updates
        
        # if card_sqr_6 is starting this frame...
        if card_sqr_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_sqr_6.frameNStart = frameN  # exact frame index
            card_sqr_6.tStart = t  # local t and not account for scr refresh
            card_sqr_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_sqr_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_sqr_6.status = STARTED
            card_sqr_6.setAutoDraw(True)
        
        # if card_sqr_6 is active this frame...
        if card_sqr_6.status == STARTED:
            # update params
            pass
        
        # if card_sqr_6 is stopping this frame...
        if card_sqr_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card_sqr_6.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                card_sqr_6.tStop = t  # not accounting for scr refresh
                card_sqr_6.frameNStop = frameN  # exact frame index
                # update status
                card_sqr_6.status = FINISHED
                card_sqr_6.setAutoDraw(False)
        
        # *arrow_5* updates
        
        # if arrow_5 is starting this frame...
        if arrow_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow_5.frameNStart = frameN  # exact frame index
            arrow_5.tStart = t  # local t and not account for scr refresh
            arrow_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            arrow_5.status = STARTED
            arrow_5.setAutoDraw(True)
        
        # if arrow_5 is active this frame...
        if arrow_5.status == STARTED:
            # update params
            pass
        
        # if arrow_5 is stopping this frame...
        if arrow_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow_5.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                arrow_5.tStop = t  # not accounting for scr refresh
                arrow_5.frameNStop = frameN  # exact frame index
                # update status
                arrow_5.status = FINISHED
                arrow_5.setAutoDraw(False)
        
        # *image_22* updates
        
        # if image_22 is starting this frame...
        if image_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_22.frameNStart = frameN  # exact frame index
            image_22.tStart = t  # local t and not account for scr refresh
            image_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_22.status = STARTED
            image_22.setAutoDraw(True)
        
        # if image_22 is active this frame...
        if image_22.status == STARTED:
            # update params
            pass
        
        # if image_22 is stopping this frame...
        if image_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_22.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                image_22.tStop = t  # not accounting for scr refresh
                image_22.frameNStop = frameN  # exact frame index
                # update status
                image_22.status = FINISHED
                image_22.setAutoDraw(False)
        
        # *image_23* updates
        
        # if image_23 is starting this frame...
        if image_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_23.frameNStart = frameN  # exact frame index
            image_23.tStart = t  # local t and not account for scr refresh
            image_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_23.status = STARTED
            image_23.setAutoDraw(True)
        
        # if image_23 is active this frame...
        if image_23.status == STARTED:
            # update params
            pass
        
        # if image_23 is stopping this frame...
        if image_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_23.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                image_23.tStop = t  # not accounting for scr refresh
                image_23.frameNStop = frameN  # exact frame index
                # update status
                image_23.status = FINISHED
                image_23.setAutoDraw(False)
        
        # *image_24* updates
        
        # if image_24 is starting this frame...
        if image_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_24.frameNStart = frameN  # exact frame index
            image_24.tStart = t  # local t and not account for scr refresh
            image_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_24.status = STARTED
            image_24.setAutoDraw(True)
        
        # if image_24 is active this frame...
        if image_24.status == STARTED:
            # update params
            pass
        
        # if image_24 is stopping this frame...
        if image_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_24.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                image_24.tStop = t  # not accounting for scr refresh
                image_24.frameNStop = frameN  # exact frame index
                # update status
                image_24.status = FINISHED
                image_24.setAutoDraw(False)
        
        # *image_25* updates
        
        # if image_25 is starting this frame...
        if image_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_25.frameNStart = frameN  # exact frame index
            image_25.tStart = t  # local t and not account for scr refresh
            image_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_25.status = STARTED
            image_25.setAutoDraw(True)
        
        # if image_25 is active this frame...
        if image_25.status == STARTED:
            # update params
            pass
        
        # if image_25 is stopping this frame...
        if image_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_25.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                image_25.tStop = t  # not accounting for scr refresh
                image_25.frameNStop = frameN  # exact frame index
                # update status
                image_25.status = FINISHED
                image_25.setAutoDraw(False)
        
        # *image_26* updates
        
        # if image_26 is starting this frame...
        if image_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_26.frameNStart = frameN  # exact frame index
            image_26.tStart = t  # local t and not account for scr refresh
            image_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_26.status = STARTED
            image_26.setAutoDraw(True)
        
        # if image_26 is active this frame...
        if image_26.status == STARTED:
            # update params
            pass
        
        # if image_26 is stopping this frame...
        if image_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_26.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                image_26.tStop = t  # not accounting for scr refresh
                image_26.frameNStop = frameN  # exact frame index
                # update status
                image_26.status = FINISHED
                image_26.setAutoDraw(False)
        
        # *text_practice_interval* updates
        
        # if text_practice_interval is starting this frame...
        if text_practice_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_interval.frameNStart = frameN  # exact frame index
            text_practice_interval.tStart = t  # local t and not account for scr refresh
            text_practice_interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_interval, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_practice_interval.status = STARTED
            text_practice_interval.setAutoDraw(True)
        
        # if text_practice_interval is active this frame...
        if text_practice_interval.status == STARTED:
            # update params
            pass
        
        # if text_practice_interval is stopping this frame...
        if text_practice_interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_practice_interval.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                text_practice_interval.tStop = t  # not accounting for scr refresh
                text_practice_interval.frameNStop = frameN  # exact frame index
                # update status
                text_practice_interval.status = FINISHED
                text_practice_interval.setAutoDraw(False)
        
        # *polygon_2* updates
        
        # if polygon_2 is starting this frame...
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            polygon_2.status = STARTED
            polygon_2.setAutoDraw(True)
        
        # if polygon_2 is active this frame...
        if polygon_2.status == STARTED:
            # update params
            pass
        
        # if polygon_2 is stopping this frame...
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                # update status
                polygon_2.status = FINISHED
                polygon_2.setAutoDraw(False)
        
        # *polygon_practice_interval* updates
        
        # if polygon_practice_interval is starting this frame...
        if polygon_practice_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_practice_interval.frameNStart = frameN  # exact frame index
            polygon_practice_interval.tStart = t  # local t and not account for scr refresh
            polygon_practice_interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_practice_interval, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_practice_interval.started')
            # update status
            polygon_practice_interval.status = STARTED
            polygon_practice_interval.setAutoDraw(True)
        
        # if polygon_practice_interval is active this frame...
        if polygon_practice_interval.status == STARTED:
            # update params
            pass
        
        # if polygon_practice_interval is stopping this frame...
        if polygon_practice_interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_practice_interval.tStartRefresh + presentationInterval-frameTolerance:
                # keep track of stop time/frame for later
                polygon_practice_interval.tStop = t  # not accounting for scr refresh
                polygon_practice_interval.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_practice_interval.stopped')
                # update status
                polygon_practice_interval.status = FINISHED
                polygon_practice_interval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_interval" ---
    for thisComponent in practice_intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice_interval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_rewards" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_practice_rewards
    
    if endTrial:
        consRewardImgs.append('stimuli/blank_transparent.png')
        if len(consRewardImgs) > 5:
            del consRewardImgs[0]
        continueRoutine = False
    else:
    #    reward_seqs = DictCondRew[currentCondition]
    #    reward_seq = reward_seqs[0]
        reward_seq = [2, 1, 3]
        thisExp.addData('reward_seq',reward_seq)
        #thisExp.nextEntry()
    
    #    for i in enumerate(currentCondition):
        if practice_trials.thisN+1 > 10:
    #        reward_seqs = DictCondRew[currentCondition]
            reward_seq = [3,2,1]
            thisExp.addData('reward_seq',reward_seq)
    #        thisExp.nextEntry()
    
        rand_val = random()
        currentTrialReward = 0
        
        x = reward_seq.index(1)
        y = reward_seq.index(2)
        z = reward_seq.index(3)
        
        #reward_seq[0]-1
        
        #Reward selection and presentation
        if key_resp_practice_slots.keys == keyboardNumbers[x] or key_resp_practice_slots.keys == keyboardArrows[x]:
            #time = core.getTime()
            if rand_val >= 0.2:
                currentTrialReward = 100
                nCorr+= 100
                rewPos = rewardImagePostions[x]
                rewImg = rewardImageLocations[0]
            elif rand_val >= 0.1:
                currentTrialReward = 10
                nCorr+= 10
                rewPos = rewardImagePostions[x]
                rewImg = rewardImageLocations[1]
            else:
                currentTrialReward = 0
                nCorr+= 0
                rewPos = rewardImagePostions[x]
                rewImg = rewardImageLocations[2]
                
        elif key_resp_practice_slots.keys == keyboardNumbers[y] or key_resp_practice_slots.keys == keyboardArrows[y]:
            #time = core.getTime()
            if rand_val >= 0.2:
                currentTrialReward = 10
                nCorr+= 10
                rewPos = rewardImagePostions[y]
                rewImg = rewardImageLocations[1]
            elif rand_val >= 0.1:
                currentTrialReward = 100
                nCorr+= 100
                rewPos = rewardImagePostions[y]
                rewImg = rewardImageLocations[0]
            else:
                currentTrialReward = 0
                nCorr+= 0
                rewPos = rewardImagePostions[y]
                rewImg = rewardImageLocations[2]
    
        elif key_resp_practice_slots.keys == keyboardNumbers[z] or key_resp_practice_slots.keys == keyboardArrows[z]:
            #time = core.getTime()
            if rand_val >= 0.2:
                currentTrialReward = 0
                nCorr+= 0
                rewPos = rewardImagePostions[z]
                rewImg = rewardImageLocations[2]
            elif rand_val >= 0.1:
                currentTrialReward = 10
                nCorr+= 10
                rewPos = rewardImagePostions[z]
                rewImg = rewardImageLocations[1]
            else:
                currentTrialReward = 100
                nCorr+= 100
                rewPos = rewardImagePostions[z]
                rewImg = rewardImageLocations[0]
        
        thisExp.addData('reward_Img',rewImg)
        #thisExp.nextEntry()
        thisExp.addData('Cuml_rew',nCorr)
        #thisExp.nextEntry()
        thisExp.addData('currentTrialReward',currentTrialReward)
        #thisExp.nextEntry()
    
        #Storing 5 consecutive reward images to display.
        consRewardImgs.append(rewImg)
        if len(consRewardImgs) > 5:
            del consRewardImgs[0]
            
    
    
    textMsg = "Total reward: " + str(nCorr) #+ "\nTrail number: " + str(practice_trials.thisN+1)
    image_27.setPos(rewPos)
    image_27.setImage(rewImg)
    image_28.setImage(consRewardImgs[4])
    image_29.setImage(consRewardImgs[3])
    image_30.setImage(consRewardImgs[2])
    image_31.setImage(consRewardImgs[1])
    image_32.setImage(consRewardImgs[0])
    text_practice_rewards.setText(textMsg)
    # keep track of which components have finished
    practice_rewardsComponents = [card_circ_7, card_pent_7, card_sqr_7, arrow_6, image_27, image_28, image_29, image_30, image_31, image_32, polygon_3, text_practice_rewards]
    for thisComponent in practice_rewardsComponents:
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
    
    # --- Run Routine "practice_rewards" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *card_circ_7* updates
        
        # if card_circ_7 is starting this frame...
        if card_circ_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            card_circ_7.frameNStart = frameN  # exact frame index
            card_circ_7.tStart = t  # local t and not account for scr refresh
            card_circ_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_circ_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_circ_7.status = STARTED
            card_circ_7.setAutoDraw(True)
        
        # if card_circ_7 is active this frame...
        if card_circ_7.status == STARTED:
            # update params
            pass
        
        # if card_circ_7 is stopping this frame...
        if card_circ_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card_circ_7.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                card_circ_7.tStop = t  # not accounting for scr refresh
                card_circ_7.frameNStop = frameN  # exact frame index
                # update status
                card_circ_7.status = FINISHED
                card_circ_7.setAutoDraw(False)
        
        # *card_pent_7* updates
        
        # if card_pent_7 is starting this frame...
        if card_pent_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            card_pent_7.frameNStart = frameN  # exact frame index
            card_pent_7.tStart = t  # local t and not account for scr refresh
            card_pent_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_pent_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_pent_7.status = STARTED
            card_pent_7.setAutoDraw(True)
        
        # if card_pent_7 is active this frame...
        if card_pent_7.status == STARTED:
            # update params
            pass
        
        # if card_pent_7 is stopping this frame...
        if card_pent_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card_pent_7.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                card_pent_7.tStop = t  # not accounting for scr refresh
                card_pent_7.frameNStop = frameN  # exact frame index
                # update status
                card_pent_7.status = FINISHED
                card_pent_7.setAutoDraw(False)
        
        # *card_sqr_7* updates
        
        # if card_sqr_7 is starting this frame...
        if card_sqr_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            card_sqr_7.frameNStart = frameN  # exact frame index
            card_sqr_7.tStart = t  # local t and not account for scr refresh
            card_sqr_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_sqr_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            card_sqr_7.status = STARTED
            card_sqr_7.setAutoDraw(True)
        
        # if card_sqr_7 is active this frame...
        if card_sqr_7.status == STARTED:
            # update params
            pass
        
        # if card_sqr_7 is stopping this frame...
        if card_sqr_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card_sqr_7.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                card_sqr_7.tStop = t  # not accounting for scr refresh
                card_sqr_7.frameNStop = frameN  # exact frame index
                # update status
                card_sqr_7.status = FINISHED
                card_sqr_7.setAutoDraw(False)
        
        # *arrow_6* updates
        
        # if arrow_6 is starting this frame...
        if arrow_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow_6.frameNStart = frameN  # exact frame index
            arrow_6.tStart = t  # local t and not account for scr refresh
            arrow_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            arrow_6.status = STARTED
            arrow_6.setAutoDraw(True)
        
        # if arrow_6 is active this frame...
        if arrow_6.status == STARTED:
            # update params
            pass
        
        # if arrow_6 is stopping this frame...
        if arrow_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow_6.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                arrow_6.tStop = t  # not accounting for scr refresh
                arrow_6.frameNStop = frameN  # exact frame index
                # update status
                arrow_6.status = FINISHED
                arrow_6.setAutoDraw(False)
        
        # *image_27* updates
        
        # if image_27 is starting this frame...
        if image_27.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_27.frameNStart = frameN  # exact frame index
            image_27.tStart = t  # local t and not account for scr refresh
            image_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_27, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_27.status = STARTED
            image_27.setAutoDraw(True)
        
        # if image_27 is active this frame...
        if image_27.status == STARTED:
            # update params
            pass
        
        # if image_27 is stopping this frame...
        if image_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_27.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                image_27.tStop = t  # not accounting for scr refresh
                image_27.frameNStop = frameN  # exact frame index
                # update status
                image_27.status = FINISHED
                image_27.setAutoDraw(False)
        
        # *image_28* updates
        
        # if image_28 is starting this frame...
        if image_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_28.frameNStart = frameN  # exact frame index
            image_28.tStart = t  # local t and not account for scr refresh
            image_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_28, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_28.status = STARTED
            image_28.setAutoDraw(True)
        
        # if image_28 is active this frame...
        if image_28.status == STARTED:
            # update params
            pass
        
        # if image_28 is stopping this frame...
        if image_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_28.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                image_28.tStop = t  # not accounting for scr refresh
                image_28.frameNStop = frameN  # exact frame index
                # update status
                image_28.status = FINISHED
                image_28.setAutoDraw(False)
        
        # *image_29* updates
        
        # if image_29 is starting this frame...
        if image_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_29.frameNStart = frameN  # exact frame index
            image_29.tStart = t  # local t and not account for scr refresh
            image_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_29, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_29.status = STARTED
            image_29.setAutoDraw(True)
        
        # if image_29 is active this frame...
        if image_29.status == STARTED:
            # update params
            pass
        
        # if image_29 is stopping this frame...
        if image_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_29.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                image_29.tStop = t  # not accounting for scr refresh
                image_29.frameNStop = frameN  # exact frame index
                # update status
                image_29.status = FINISHED
                image_29.setAutoDraw(False)
        
        # *image_30* updates
        
        # if image_30 is starting this frame...
        if image_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_30.frameNStart = frameN  # exact frame index
            image_30.tStart = t  # local t and not account for scr refresh
            image_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_30, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_30.status = STARTED
            image_30.setAutoDraw(True)
        
        # if image_30 is active this frame...
        if image_30.status == STARTED:
            # update params
            pass
        
        # if image_30 is stopping this frame...
        if image_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_30.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                image_30.tStop = t  # not accounting for scr refresh
                image_30.frameNStop = frameN  # exact frame index
                # update status
                image_30.status = FINISHED
                image_30.setAutoDraw(False)
        
        # *image_31* updates
        
        # if image_31 is starting this frame...
        if image_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_31.frameNStart = frameN  # exact frame index
            image_31.tStart = t  # local t and not account for scr refresh
            image_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_31, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_31.status = STARTED
            image_31.setAutoDraw(True)
        
        # if image_31 is active this frame...
        if image_31.status == STARTED:
            # update params
            pass
        
        # if image_31 is stopping this frame...
        if image_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_31.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                image_31.tStop = t  # not accounting for scr refresh
                image_31.frameNStop = frameN  # exact frame index
                # update status
                image_31.status = FINISHED
                image_31.setAutoDraw(False)
        
        # *image_32* updates
        
        # if image_32 is starting this frame...
        if image_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_32.frameNStart = frameN  # exact frame index
            image_32.tStart = t  # local t and not account for scr refresh
            image_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_32, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_32.status = STARTED
            image_32.setAutoDraw(True)
        
        # if image_32 is active this frame...
        if image_32.status == STARTED:
            # update params
            pass
        
        # if image_32 is stopping this frame...
        if image_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_32.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                image_32.tStop = t  # not accounting for scr refresh
                image_32.frameNStop = frameN  # exact frame index
                # update status
                image_32.status = FINISHED
                image_32.setAutoDraw(False)
        
        # *polygon_3* updates
        
        # if polygon_3 is starting this frame...
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            polygon_3.status = STARTED
            polygon_3.setAutoDraw(True)
        
        # if polygon_3 is active this frame...
        if polygon_3.status == STARTED:
            # update params
            pass
        
        # if polygon_3 is stopping this frame...
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                # update status
                polygon_3.status = FINISHED
                polygon_3.setAutoDraw(False)
        
        # *text_practice_rewards* updates
        
        # if text_practice_rewards is starting this frame...
        if text_practice_rewards.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_rewards.frameNStart = frameN  # exact frame index
            text_practice_rewards.tStart = t  # local t and not account for scr refresh
            text_practice_rewards.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_rewards, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_practice_rewards.started')
            # update status
            text_practice_rewards.status = STARTED
            text_practice_rewards.setAutoDraw(True)
        
        # if text_practice_rewards is active this frame...
        if text_practice_rewards.status == STARTED:
            # update params
            pass
        
        # if text_practice_rewards is stopping this frame...
        if text_practice_rewards.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_practice_rewards.tStartRefresh + rewardPresentationTime-frameTolerance:
                # keep track of stop time/frame for later
                text_practice_rewards.tStop = t  # not accounting for scr refresh
                text_practice_rewards.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_practice_rewards.stopped')
                # update status
                text_practice_rewards.status = FINISHED
                text_practice_rewards.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_rewardsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_rewards" ---
    for thisComponent in practice_rewardsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice_rewards" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed nPracticeTrials repeats of 'practice_trials'


# --- Prepare to start Routine "practice_end" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_practice_end.keys = []
key_resp_practice_end.rt = []
_key_resp_practice_end_allKeys = []
# Run 'Begin Routine' code from code_3
thisExp.addData('key_resp_practice_end.started', globalClock.getTime())

# keep track of which components have finished
practice_endComponents = [text_practice_end, key_resp_practice_end]
for thisComponent in practice_endComponents:
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

# --- Run Routine "practice_end" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_practice_end* updates
    
    # if text_practice_end is starting this frame...
    if text_practice_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_practice_end.frameNStart = frameN  # exact frame index
        text_practice_end.tStart = t  # local t and not account for scr refresh
        text_practice_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_practice_end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_practice_end.started')
        # update status
        text_practice_end.status = STARTED
        text_practice_end.setAutoDraw(True)
    
    # if text_practice_end is active this frame...
    if text_practice_end.status == STARTED:
        # update params
        pass
    
    # *key_resp_practice_end* updates
    waitOnFlip = False
    
    # if key_resp_practice_end is starting this frame...
    if key_resp_practice_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_practice_end.frameNStart = frameN  # exact frame index
        key_resp_practice_end.tStart = t  # local t and not account for scr refresh
        key_resp_practice_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_practice_end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_practice_end.started')
        # update status
        key_resp_practice_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_practice_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_practice_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_practice_end.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_practice_end.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_practice_end_allKeys.extend(theseKeys)
        if len(_key_resp_practice_end_allKeys):
            key_resp_practice_end.keys = _key_resp_practice_end_allKeys[-1].name  # just the last key pressed
            key_resp_practice_end.rt = _key_resp_practice_end_allKeys[-1].rt
            key_resp_practice_end.duration = _key_resp_practice_end_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_end" ---
for thisComponent in practice_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_practice_end.keys in ['', [], None]:  # No response was made
    key_resp_practice_end.keys = None
thisExp.addData('key_resp_practice_end.keys',key_resp_practice_end.keys)
if key_resp_practice_end.keys != None:  # we had a response
    thisExp.addData('key_resp_practice_end.rt', key_resp_practice_end.rt)
    thisExp.addData('key_resp_practice_end.duration', key_resp_practice_end.duration)
thisExp.nextEntry()
# the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Main_Instruction" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code_main_instruction
#thisExp.addData('Main_Instruction_onset',t)
#thisExp.nextEntry()
thisExp.addData('text_main_instruction.started', globalClock.getTime())

conditions = [(12,20), (8,20), (7,20), (10,20), (7,14,20), (13,20)]
thisExp.addData('key_resp_main_instruction.started', globalClock.getTime())

key_resp_main_instruction.keys = []
key_resp_main_instruction.rt = []
_key_resp_main_instruction_allKeys = []
# keep track of which components have finished
Main_InstructionComponents = [text_main_instruction, key_resp_main_instruction]
for thisComponent in Main_InstructionComponents:
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

# --- Run Routine "Main_Instruction" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_main_instruction* updates
    
    # if text_main_instruction is starting this frame...
    if text_main_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_main_instruction.frameNStart = frameN  # exact frame index
        text_main_instruction.tStart = t  # local t and not account for scr refresh
        text_main_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_main_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_main_instruction.started')
        # update status
        text_main_instruction.status = STARTED
        text_main_instruction.setAutoDraw(True)
    
    # if text_main_instruction is active this frame...
    if text_main_instruction.status == STARTED:
        # update params
        pass
    
    # *key_resp_main_instruction* updates
    waitOnFlip = False
    
    # if key_resp_main_instruction is starting this frame...
    if key_resp_main_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_main_instruction.frameNStart = frameN  # exact frame index
        key_resp_main_instruction.tStart = t  # local t and not account for scr refresh
        key_resp_main_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_main_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_main_instruction.started')
        # update status
        key_resp_main_instruction.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_main_instruction.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_main_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_main_instruction.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_main_instruction.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_main_instruction_allKeys.extend(theseKeys)
        if len(_key_resp_main_instruction_allKeys):
            key_resp_main_instruction.keys = _key_resp_main_instruction_allKeys[-1].name  # just the last key pressed
            key_resp_main_instruction.rt = _key_resp_main_instruction_allKeys[-1].rt
            key_resp_main_instruction.duration = _key_resp_main_instruction_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Main_InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Main_Instruction" ---
for thisComponent in Main_InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_main_instruction.keys in ['', [], None]:  # No response was made
    key_resp_main_instruction.keys = None
thisExp.addData('key_resp_main_instruction.keys',key_resp_main_instruction.keys)
if key_resp_main_instruction.keys != None:  # we had a response
    thisExp.addData('key_resp_main_instruction.rt', key_resp_main_instruction.rt)
    thisExp.addData('key_resp_main_instruction.duration', key_resp_main_instruction.duration)
thisExp.nextEntry()
# the Routine "Main_Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=nBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "reward_reset" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_reward_reset
    
    # shuffle(conditions) # old code - should not randomize order of block conditions
    thisExp.addData('conditions',conditions)
    #thisExp.nextEntry()
    
    currentCondition = conditions[0]
    thisExp.addData('currentCondition',currentCondition)
    #thisExp.nextEntry()
    
    conditions.remove(currentCondition) ## Check if this works
    thisExp.addData('conditionsAfterRemoval',conditions)
    #thisExp.nextEntry()
    
    nCorr = 0
    
    consRewardImgs = ["stimuli/blank_transparent.png", "stimuli/blank_transparent.png", "stimuli/blank_transparent.png", "stimuli/blank_transparent.png", "stimuli/blank_transparent.png"]
    # keep track of which components have finished
    reward_resetComponents = []
    for thisComponent in reward_resetComponents:
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
    
    # --- Run Routine "reward_reset" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reward_resetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reward_reset" ---
    for thisComponent in reward_resetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "reward_reset" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    main_trials = data.TrialHandler(nReps=nTrials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='main_trials')
    thisExp.addLoop(main_trials)  # add the loop to the experiment
    thisMain_trial = main_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
    if thisMain_trial != None:
        for paramName in thisMain_trial:
            exec('{} = thisMain_trial[paramName]'.format(paramName))
    
    for thisMain_trial in main_trials:
        currentLoop = main_trials
        # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
        if thisMain_trial != None:
            for paramName in thisMain_trial:
                exec('{} = thisMain_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "slots_presentation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Code_slots_presentation
        #routineTimer = core.CountdownTimer(8)
        #routineTimer.add(6.000000)
        thisExp.addData('key_resp_slots_presentation.started', globalClock.getTime())
        
        textMsg = "Total reward: " + str(nCorr)
        endMsg = " "
        
        endTrial = False
        image_3.setPos([consReward_pos[0]])
        image_3.setImage(consRewardImgs[4])
        image_6.setPos([consReward_pos[1]])
        image_6.setImage(consRewardImgs[3])
        image_9.setPos([consReward_pos[2]])
        image_9.setImage(consRewardImgs[2])
        image_12.setPos([consReward_pos[3]])
        image_12.setImage(consRewardImgs[1])
        image_15.setPos([consReward_pos[4]])
        image_15.setImage(consRewardImgs[0])
        text_slots_presentation.setText(textMsg)
        key_resp_slots_presentation.keys = []
        key_resp_slots_presentation.rt = []
        _key_resp_slots_presentation_allKeys = []
        # keep track of which components have finished
        slots_presentationComponents = [card_circ_3, card_pent_3, card_sqr_3, arrow, image_3, image_6, image_9, image_12, image_15, text_slots_presentation, text_slots_presentation_2, polygon_4, key_resp_slots_presentation]
        for thisComponent in slots_presentationComponents:
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
        
        # --- Run Routine "slots_presentation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from Code_slots_presentation
            
            if t>5.0 and len(key_resp_slots_presentation.getKeys()) == 0:
                endMsg = "Too Slow"
                endTrial = True
                if t>5.5 and len(key_resp_slots_presentation.getKeys()) == 0:
                    continueRoutine = False
            
            
            # *card_circ_3* updates
            
            # if card_circ_3 is starting this frame...
            if card_circ_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_circ_3.frameNStart = frameN  # exact frame index
                card_circ_3.tStart = t  # local t and not account for scr refresh
                card_circ_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_circ_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_circ_3.status = STARTED
                card_circ_3.setAutoDraw(True)
            
            # if card_circ_3 is active this frame...
            if card_circ_3.status == STARTED:
                # update params
                pass
            
            # *card_pent_3* updates
            
            # if card_pent_3 is starting this frame...
            if card_pent_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_pent_3.frameNStart = frameN  # exact frame index
                card_pent_3.tStart = t  # local t and not account for scr refresh
                card_pent_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_pent_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_pent_3.status = STARTED
                card_pent_3.setAutoDraw(True)
            
            # if card_pent_3 is active this frame...
            if card_pent_3.status == STARTED:
                # update params
                pass
            
            # *card_sqr_3* updates
            
            # if card_sqr_3 is starting this frame...
            if card_sqr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_sqr_3.frameNStart = frameN  # exact frame index
                card_sqr_3.tStart = t  # local t and not account for scr refresh
                card_sqr_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_sqr_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_sqr_3.status = STARTED
                card_sqr_3.setAutoDraw(True)
            
            # if card_sqr_3 is active this frame...
            if card_sqr_3.status == STARTED:
                # update params
                pass
            
            # *arrow* updates
            
            # if arrow is starting this frame...
            if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow.frameNStart = frameN  # exact frame index
                arrow.tStart = t  # local t and not account for scr refresh
                arrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                # update status
                arrow.status = STARTED
                arrow.setAutoDraw(True)
            
            # if arrow is active this frame...
            if arrow.status == STARTED:
                # update params
                pass
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # *image_6* updates
            
            # if image_6 is starting this frame...
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_6.status = STARTED
                image_6.setAutoDraw(True)
            
            # if image_6 is active this frame...
            if image_6.status == STARTED:
                # update params
                pass
            
            # *image_9* updates
            
            # if image_9 is starting this frame...
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_9.status = STARTED
                image_9.setAutoDraw(True)
            
            # if image_9 is active this frame...
            if image_9.status == STARTED:
                # update params
                pass
            
            # *image_12* updates
            
            # if image_12 is starting this frame...
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_12.status = STARTED
                image_12.setAutoDraw(True)
            
            # if image_12 is active this frame...
            if image_12.status == STARTED:
                # update params
                pass
            
            # *image_15* updates
            
            # if image_15 is starting this frame...
            if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_15.frameNStart = frameN  # exact frame index
                image_15.tStart = t  # local t and not account for scr refresh
                image_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_15.status = STARTED
                image_15.setAutoDraw(True)
            
            # if image_15 is active this frame...
            if image_15.status == STARTED:
                # update params
                pass
            
            # *text_slots_presentation* updates
            
            # if text_slots_presentation is starting this frame...
            if text_slots_presentation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_slots_presentation.frameNStart = frameN  # exact frame index
                text_slots_presentation.tStart = t  # local t and not account for scr refresh
                text_slots_presentation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_slots_presentation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_slots_presentation.started')
                # update status
                text_slots_presentation.status = STARTED
                text_slots_presentation.setAutoDraw(True)
            
            # if text_slots_presentation is active this frame...
            if text_slots_presentation.status == STARTED:
                # update params
                pass
            
            # *text_slots_presentation_2* updates
            
            # if text_slots_presentation_2 is starting this frame...
            if text_slots_presentation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_slots_presentation_2.frameNStart = frameN  # exact frame index
                text_slots_presentation_2.tStart = t  # local t and not account for scr refresh
                text_slots_presentation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_slots_presentation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_slots_presentation_2.started')
                # update status
                text_slots_presentation_2.status = STARTED
                text_slots_presentation_2.setAutoDraw(True)
            
            # if text_slots_presentation_2 is active this frame...
            if text_slots_presentation_2.status == STARTED:
                # update params
                text_slots_presentation_2.setText(endMsg, log=False)
            
            # *polygon_4* updates
            
            # if polygon_4 is starting this frame...
            if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_4.frameNStart = frameN  # exact frame index
                polygon_4.tStart = t  # local t and not account for scr refresh
                polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_4.status = STARTED
                polygon_4.setAutoDraw(True)
            
            # if polygon_4 is active this frame...
            if polygon_4.status == STARTED:
                # update params
                pass
            
            # *key_resp_slots_presentation* updates
            waitOnFlip = False
            
            # if key_resp_slots_presentation is starting this frame...
            if key_resp_slots_presentation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_slots_presentation.frameNStart = frameN  # exact frame index
                key_resp_slots_presentation.tStart = t  # local t and not account for scr refresh
                key_resp_slots_presentation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_slots_presentation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_slots_presentation.started')
                # update status
                key_resp_slots_presentation.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_slots_presentation.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_slots_presentation.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_slots_presentation.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_slots_presentation.getKeys(keyList=['1','2','3','left','up','right'], waitRelease=False)
                _key_resp_slots_presentation_allKeys.extend(theseKeys)
                if len(_key_resp_slots_presentation_allKeys):
                    key_resp_slots_presentation.keys = _key_resp_slots_presentation_allKeys[-1].name  # just the last key pressed
                    key_resp_slots_presentation.rt = _key_resp_slots_presentation_allKeys[-1].rt
                    key_resp_slots_presentation.duration = _key_resp_slots_presentation_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in slots_presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "slots_presentation" ---
        for thisComponent in slots_presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_slots_presentation.keys in ['', [], None]:  # No response was made
            key_resp_slots_presentation.keys = None
        main_trials.addData('key_resp_slots_presentation.keys',key_resp_slots_presentation.keys)
        if key_resp_slots_presentation.keys != None:  # we had a response
            main_trials.addData('key_resp_slots_presentation.rt', key_resp_slots_presentation.rt)
            main_trials.addData('key_resp_slots_presentation.duration', key_resp_slots_presentation.duration)
        # the Routine "slots_presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "selection_interval" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Code_selection_interval
        if endTrial:
            continueRoutine = False
        
        presentationInterval = randchoice(intervalAfterSelection)
        
        thisExp.addData('Main_presentationInterval',presentationInterval)
        #thisExp.nextEntry()
        
        #presentationInterval = random.choice(intervalAfterSelection)
        
        #textMsg = "Reward obtained so far: " + str(nCorr)
        if key_resp_slots_presentation.keys == keyboardNumbers[0] or key_resp_slots_presentation.keys == keyboardArrows[0]:
            boxPos = cardPositions[0]
        elif key_resp_slots_presentation.keys == keyboardNumbers[1] or key_resp_slots_presentation.keys == keyboardArrows[1]:
            boxPos = cardPositions[1]
        elif key_resp_slots_presentation.keys == keyboardNumbers[2] or key_resp_slots_presentation.keys == keyboardArrows[2]:
            boxPos = cardPositions[2]
        
        image_4.setPos([consReward_pos[0]])
        image_4.setImage(consRewardImgs[4])
        image_7.setPos([consReward_pos[1]])
        image_7.setImage(consRewardImgs[3])
        image_10.setPos([consReward_pos[2]])
        image_10.setImage(consRewardImgs[2])
        image_13.setPos([consReward_pos[3]])
        image_13.setImage(consRewardImgs[1])
        image_16.setPos([consReward_pos[4]])
        image_16.setImage(consRewardImgs[0])
        polygon_selection_interval.setPos(boxPos)
        text_selection_interval.setText(textMsg)
        # keep track of which components have finished
        selection_intervalComponents = [card_circ_5, card_pent_5, card_sqr_5, arrow_2, image_4, image_7, image_10, image_13, image_16, polygon_selection_interval, polygon_5, text_selection_interval]
        for thisComponent in selection_intervalComponents:
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
        
        # --- Run Routine "selection_interval" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *card_circ_5* updates
            
            # if card_circ_5 is starting this frame...
            if card_circ_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_circ_5.frameNStart = frameN  # exact frame index
                card_circ_5.tStart = t  # local t and not account for scr refresh
                card_circ_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_circ_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_circ_5.status = STARTED
                card_circ_5.setAutoDraw(True)
            
            # if card_circ_5 is active this frame...
            if card_circ_5.status == STARTED:
                # update params
                pass
            
            # if card_circ_5 is stopping this frame...
            if card_circ_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > card_circ_5.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    card_circ_5.tStop = t  # not accounting for scr refresh
                    card_circ_5.frameNStop = frameN  # exact frame index
                    # update status
                    card_circ_5.status = FINISHED
                    card_circ_5.setAutoDraw(False)
            
            # *card_pent_5* updates
            
            # if card_pent_5 is starting this frame...
            if card_pent_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_pent_5.frameNStart = frameN  # exact frame index
                card_pent_5.tStart = t  # local t and not account for scr refresh
                card_pent_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_pent_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_pent_5.status = STARTED
                card_pent_5.setAutoDraw(True)
            
            # if card_pent_5 is active this frame...
            if card_pent_5.status == STARTED:
                # update params
                pass
            
            # if card_pent_5 is stopping this frame...
            if card_pent_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > card_pent_5.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    card_pent_5.tStop = t  # not accounting for scr refresh
                    card_pent_5.frameNStop = frameN  # exact frame index
                    # update status
                    card_pent_5.status = FINISHED
                    card_pent_5.setAutoDraw(False)
            
            # *card_sqr_5* updates
            
            # if card_sqr_5 is starting this frame...
            if card_sqr_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_sqr_5.frameNStart = frameN  # exact frame index
                card_sqr_5.tStart = t  # local t and not account for scr refresh
                card_sqr_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_sqr_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_sqr_5.status = STARTED
                card_sqr_5.setAutoDraw(True)
            
            # if card_sqr_5 is active this frame...
            if card_sqr_5.status == STARTED:
                # update params
                pass
            
            # if card_sqr_5 is stopping this frame...
            if card_sqr_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > card_sqr_5.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    card_sqr_5.tStop = t  # not accounting for scr refresh
                    card_sqr_5.frameNStop = frameN  # exact frame index
                    # update status
                    card_sqr_5.status = FINISHED
                    card_sqr_5.setAutoDraw(False)
            
            # *arrow_2* updates
            
            # if arrow_2 is starting this frame...
            if arrow_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_2.frameNStart = frameN  # exact frame index
                arrow_2.tStart = t  # local t and not account for scr refresh
                arrow_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                arrow_2.status = STARTED
                arrow_2.setAutoDraw(True)
            
            # if arrow_2 is active this frame...
            if arrow_2.status == STARTED:
                # update params
                pass
            
            # if arrow_2 is stopping this frame...
            if arrow_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow_2.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow_2.tStop = t  # not accounting for scr refresh
                    arrow_2.frameNStop = frameN  # exact frame index
                    # update status
                    arrow_2.status = FINISHED
                    arrow_2.setAutoDraw(False)
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            
            # if image_4 is stopping this frame...
            if image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_4.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    # update status
                    image_4.status = FINISHED
                    image_4.setAutoDraw(False)
            
            # *image_7* updates
            
            # if image_7 is starting this frame...
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_7.status = STARTED
                image_7.setAutoDraw(True)
            
            # if image_7 is active this frame...
            if image_7.status == STARTED:
                # update params
                pass
            
            # if image_7 is stopping this frame...
            if image_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_7.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    image_7.tStop = t  # not accounting for scr refresh
                    image_7.frameNStop = frameN  # exact frame index
                    # update status
                    image_7.status = FINISHED
                    image_7.setAutoDraw(False)
            
            # *image_10* updates
            
            # if image_10 is starting this frame...
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_10.status = STARTED
                image_10.setAutoDraw(True)
            
            # if image_10 is active this frame...
            if image_10.status == STARTED:
                # update params
                pass
            
            # if image_10 is stopping this frame...
            if image_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_10.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    image_10.tStop = t  # not accounting for scr refresh
                    image_10.frameNStop = frameN  # exact frame index
                    # update status
                    image_10.status = FINISHED
                    image_10.setAutoDraw(False)
            
            # *image_13* updates
            
            # if image_13 is starting this frame...
            if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_13.frameNStart = frameN  # exact frame index
                image_13.tStart = t  # local t and not account for scr refresh
                image_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_13.status = STARTED
                image_13.setAutoDraw(True)
            
            # if image_13 is active this frame...
            if image_13.status == STARTED:
                # update params
                pass
            
            # if image_13 is stopping this frame...
            if image_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_13.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    image_13.tStop = t  # not accounting for scr refresh
                    image_13.frameNStop = frameN  # exact frame index
                    # update status
                    image_13.status = FINISHED
                    image_13.setAutoDraw(False)
            
            # *image_16* updates
            
            # if image_16 is starting this frame...
            if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_16.frameNStart = frameN  # exact frame index
                image_16.tStart = t  # local t and not account for scr refresh
                image_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_16.status = STARTED
                image_16.setAutoDraw(True)
            
            # if image_16 is active this frame...
            if image_16.status == STARTED:
                # update params
                pass
            
            # if image_16 is stopping this frame...
            if image_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_16.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    image_16.tStop = t  # not accounting for scr refresh
                    image_16.frameNStop = frameN  # exact frame index
                    # update status
                    image_16.status = FINISHED
                    image_16.setAutoDraw(False)
            
            # *polygon_selection_interval* updates
            
            # if polygon_selection_interval is starting this frame...
            if polygon_selection_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_selection_interval.frameNStart = frameN  # exact frame index
                polygon_selection_interval.tStart = t  # local t and not account for scr refresh
                polygon_selection_interval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_selection_interval, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_selection_interval.started')
                # update status
                polygon_selection_interval.status = STARTED
                polygon_selection_interval.setAutoDraw(True)
            
            # if polygon_selection_interval is active this frame...
            if polygon_selection_interval.status == STARTED:
                # update params
                pass
            
            # if polygon_selection_interval is stopping this frame...
            if polygon_selection_interval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_selection_interval.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_selection_interval.tStop = t  # not accounting for scr refresh
                    polygon_selection_interval.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_selection_interval.stopped')
                    # update status
                    polygon_selection_interval.status = FINISHED
                    polygon_selection_interval.setAutoDraw(False)
            
            # *polygon_5* updates
            
            # if polygon_5 is starting this frame...
            if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_5.frameNStart = frameN  # exact frame index
                polygon_5.tStart = t  # local t and not account for scr refresh
                polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_5.status = STARTED
                polygon_5.setAutoDraw(True)
            
            # if polygon_5 is active this frame...
            if polygon_5.status == STARTED:
                # update params
                pass
            
            # if polygon_5 is stopping this frame...
            if polygon_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_5.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_5.tStop = t  # not accounting for scr refresh
                    polygon_5.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_5.status = FINISHED
                    polygon_5.setAutoDraw(False)
            
            # *text_selection_interval* updates
            
            # if text_selection_interval is starting this frame...
            if text_selection_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_selection_interval.frameNStart = frameN  # exact frame index
                text_selection_interval.tStart = t  # local t and not account for scr refresh
                text_selection_interval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_selection_interval, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_selection_interval.started')
                # update status
                text_selection_interval.status = STARTED
                text_selection_interval.setAutoDraw(True)
            
            # if text_selection_interval is active this frame...
            if text_selection_interval.status == STARTED:
                # update params
                pass
            
            # if text_selection_interval is stopping this frame...
            if text_selection_interval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_selection_interval.tStartRefresh + presentationInterval-frameTolerance:
                    # keep track of stop time/frame for later
                    text_selection_interval.tStop = t  # not accounting for scr refresh
                    text_selection_interval.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_selection_interval.stopped')
                    # update status
                    text_selection_interval.status = FINISHED
                    text_selection_interval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in selection_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "selection_interval" ---
        for thisComponent in selection_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "selection_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "reward_presentation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_reward_presentation
        
        if endTrial:
            consRewardImgs.append('stimuli/blank_transparent.png')
            if len(consRewardImgs) > 5:
                del consRewardImgs[0]
            continueRoutine = False
        else:
            reward_seqs = DictCondRew[currentCondition]
            reward_seq = reward_seqs[0]
        #    thisExp.addData('Main_reward_seq',reward_seq)
        #    thisExp.nextEntry()
        
            for i in enumerate(currentCondition):
                if main_trials.thisN+1 > i[1]:
                    reward_seqs = DictCondRew[currentCondition]
                    reward_seq = reward_seqs[i[0]+1]
            thisExp.addData('Main_reward_seq',reward_seq)
            #thisExp.nextEntry()
        
            rand_val = random()
            thisExp.addData('Random value generated',rand_val)
            currentTrialReward = 0
        
            x = reward_seq.index(1)
            y = reward_seq.index(2)
            z = reward_seq.index(3)
            
        
            #Reward selection and presentation
            if key_resp_slots_presentation.keys == keyboardNumbers[x] or key_resp_slots_presentation.keys == keyboardArrows[x]:
        #        time = core.getTime()
                if rand_val >= 0.2:
                    currentTrialReward = 100
                    nCorr+= 100
                    rewPos = rewardImagePostions[x]
                    rewImg = rewardImageLocations[0]
                elif rand_val >= 0.1:
                    nCorr+= 10
                    currentTrialReward = 10
                    rewPos = rewardImagePostions[x]
                    rewImg = rewardImageLocations[1]
                else:
                    currentTrialReward = 0
                    nCorr+= 0
                    rewPos = rewardImagePostions[x]
                    rewImg = rewardImageLocations[2]
                    
            elif key_resp_slots_presentation.keys == keyboardNumbers[y] or key_resp_slots_presentation.keys == keyboardArrows[y]:
        #        time = core.getTime()
                if rand_val >= 0.2:
                    currentTrialReward = 10
                    nCorr+= 10
                    rewPos = rewardImagePostions[y]
                    rewImg = rewardImageLocations[1]
                elif rand_val >= 0.1:
                    currentTrialReward = 100
                    nCorr+= 100
                    rewPos = rewardImagePostions[y]
                    rewImg = rewardImageLocations[0]
                else:
                    currentTrialReward = 0
                    nCorr+= 0
                    rewPos = rewardImagePostions[y]
                    rewImg = rewardImageLocations[2]
        
            elif key_resp_slots_presentation.keys == keyboardNumbers[z] or key_resp_slots_presentation.keys == keyboardArrows[z]:
        #        time = core.getTime()
                if rand_val >= 0.2:
                    currentTrialReward = 0
                    nCorr+= 0
                    rewPos = rewardImagePostions[z]
                    rewImg = rewardImageLocations[2]
                elif rand_val >= 0.1:
                    currentTrialReward = 10
                    nCorr+= 10
                    rewPos = rewardImagePostions[z]
                    rewImg = rewardImageLocations[1]
                else:
                    currentTrialReward = 100
                    nCorr+= 100
                    rewPos = rewardImagePostions[z]
                    rewImg = rewardImageLocations[0]
            
            thisExp.addData('Main_reward_Img',rewImg)
            #thisExp.nextEntry()
            thisExp.addData('Main_Cuml_rew',nCorr)
            #thisExp.nextEntry()
            thisExp.addData('Main_currentTrialReward',currentTrialReward)
            #thisExp.nextEntry()
        
            #Storing 5 consecutive reward images to display.
            consRewardImgs.append(rewImg)
            if len(consRewardImgs) > 5:
                del consRewardImgs[0]
                
        
        
        textMsg = "Total reward: " + str(nCorr) #+ "\nTrail number: " + str(practice_trials.thisN+1)
        image_2.setPos(rewPos)
        image_2.setImage(rewImg)
        image_5.setImage(consRewardImgs[4])
        image_8.setImage(consRewardImgs[3])
        image_11.setImage(consRewardImgs[2])
        image_14.setImage(consRewardImgs[1])
        image_17.setImage(consRewardImgs[0])
        text_reward_presentation.setText(textMsg)
        # keep track of which components have finished
        reward_presentationComponents = [card_circ_4, card_pent_4, card_sqr_4, arrow_3, image_2, image_5, image_8, image_11, image_14, image_17, polygon_6, text_reward_presentation]
        for thisComponent in reward_presentationComponents:
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
        
        # --- Run Routine "reward_presentation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *card_circ_4* updates
            
            # if card_circ_4 is starting this frame...
            if card_circ_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                card_circ_4.frameNStart = frameN  # exact frame index
                card_circ_4.tStart = t  # local t and not account for scr refresh
                card_circ_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_circ_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_circ_4.status = STARTED
                card_circ_4.setAutoDraw(True)
            
            # if card_circ_4 is active this frame...
            if card_circ_4.status == STARTED:
                # update params
                pass
            
            # if card_circ_4 is stopping this frame...
            if card_circ_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > card_circ_4.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    card_circ_4.tStop = t  # not accounting for scr refresh
                    card_circ_4.frameNStop = frameN  # exact frame index
                    # update status
                    card_circ_4.status = FINISHED
                    card_circ_4.setAutoDraw(False)
            
            # *card_pent_4* updates
            
            # if card_pent_4 is starting this frame...
            if card_pent_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                card_pent_4.frameNStart = frameN  # exact frame index
                card_pent_4.tStart = t  # local t and not account for scr refresh
                card_pent_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_pent_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_pent_4.status = STARTED
                card_pent_4.setAutoDraw(True)
            
            # if card_pent_4 is active this frame...
            if card_pent_4.status == STARTED:
                # update params
                pass
            
            # if card_pent_4 is stopping this frame...
            if card_pent_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > card_pent_4.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    card_pent_4.tStop = t  # not accounting for scr refresh
                    card_pent_4.frameNStop = frameN  # exact frame index
                    # update status
                    card_pent_4.status = FINISHED
                    card_pent_4.setAutoDraw(False)
            
            # *card_sqr_4* updates
            
            # if card_sqr_4 is starting this frame...
            if card_sqr_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                card_sqr_4.frameNStart = frameN  # exact frame index
                card_sqr_4.tStart = t  # local t and not account for scr refresh
                card_sqr_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_sqr_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                card_sqr_4.status = STARTED
                card_sqr_4.setAutoDraw(True)
            
            # if card_sqr_4 is active this frame...
            if card_sqr_4.status == STARTED:
                # update params
                pass
            
            # if card_sqr_4 is stopping this frame...
            if card_sqr_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > card_sqr_4.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    card_sqr_4.tStop = t  # not accounting for scr refresh
                    card_sqr_4.frameNStop = frameN  # exact frame index
                    # update status
                    card_sqr_4.status = FINISHED
                    card_sqr_4.setAutoDraw(False)
            
            # *arrow_3* updates
            
            # if arrow_3 is starting this frame...
            if arrow_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow_3.frameNStart = frameN  # exact frame index
                arrow_3.tStart = t  # local t and not account for scr refresh
                arrow_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                arrow_3.status = STARTED
                arrow_3.setAutoDraw(True)
            
            # if arrow_3 is active this frame...
            if arrow_3.status == STARTED:
                # update params
                pass
            
            # if arrow_3 is stopping this frame...
            if arrow_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow_3.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow_3.tStop = t  # not accounting for scr refresh
                    arrow_3.frameNStop = frameN  # exact frame index
                    # update status
                    arrow_3.status = FINISHED
                    arrow_3.setAutoDraw(False)
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            
            # if image_2 is stopping this frame...
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    # update status
                    image_2.status = FINISHED
                    image_2.setAutoDraw(False)
            
            # *image_5* updates
            
            # if image_5 is starting this frame...
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_5.status = STARTED
                image_5.setAutoDraw(True)
            
            # if image_5 is active this frame...
            if image_5.status == STARTED:
                # update params
                pass
            
            # if image_5 is stopping this frame...
            if image_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_5.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    image_5.tStop = t  # not accounting for scr refresh
                    image_5.frameNStop = frameN  # exact frame index
                    # update status
                    image_5.status = FINISHED
                    image_5.setAutoDraw(False)
            
            # *image_8* updates
            
            # if image_8 is starting this frame...
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_8.status = STARTED
                image_8.setAutoDraw(True)
            
            # if image_8 is active this frame...
            if image_8.status == STARTED:
                # update params
                pass
            
            # if image_8 is stopping this frame...
            if image_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_8.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    image_8.tStop = t  # not accounting for scr refresh
                    image_8.frameNStop = frameN  # exact frame index
                    # update status
                    image_8.status = FINISHED
                    image_8.setAutoDraw(False)
            
            # *image_11* updates
            
            # if image_11 is starting this frame...
            if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_11.status = STARTED
                image_11.setAutoDraw(True)
            
            # if image_11 is active this frame...
            if image_11.status == STARTED:
                # update params
                pass
            
            # if image_11 is stopping this frame...
            if image_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_11.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    image_11.tStop = t  # not accounting for scr refresh
                    image_11.frameNStop = frameN  # exact frame index
                    # update status
                    image_11.status = FINISHED
                    image_11.setAutoDraw(False)
            
            # *image_14* updates
            
            # if image_14 is starting this frame...
            if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_14.frameNStart = frameN  # exact frame index
                image_14.tStart = t  # local t and not account for scr refresh
                image_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_14.status = STARTED
                image_14.setAutoDraw(True)
            
            # if image_14 is active this frame...
            if image_14.status == STARTED:
                # update params
                pass
            
            # if image_14 is stopping this frame...
            if image_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_14.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    image_14.tStop = t  # not accounting for scr refresh
                    image_14.frameNStop = frameN  # exact frame index
                    # update status
                    image_14.status = FINISHED
                    image_14.setAutoDraw(False)
            
            # *image_17* updates
            
            # if image_17 is starting this frame...
            if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_17.frameNStart = frameN  # exact frame index
                image_17.tStart = t  # local t and not account for scr refresh
                image_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_17.status = STARTED
                image_17.setAutoDraw(True)
            
            # if image_17 is active this frame...
            if image_17.status == STARTED:
                # update params
                pass
            
            # if image_17 is stopping this frame...
            if image_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_17.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    image_17.tStop = t  # not accounting for scr refresh
                    image_17.frameNStop = frameN  # exact frame index
                    # update status
                    image_17.status = FINISHED
                    image_17.setAutoDraw(False)
            
            # *polygon_6* updates
            
            # if polygon_6 is starting this frame...
            if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_6.frameNStart = frameN  # exact frame index
                polygon_6.tStart = t  # local t and not account for scr refresh
                polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_6.status = STARTED
                polygon_6.setAutoDraw(True)
            
            # if polygon_6 is active this frame...
            if polygon_6.status == STARTED:
                # update params
                pass
            
            # if polygon_6 is stopping this frame...
            if polygon_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_6.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_6.tStop = t  # not accounting for scr refresh
                    polygon_6.frameNStop = frameN  # exact frame index
                    # update status
                    polygon_6.status = FINISHED
                    polygon_6.setAutoDraw(False)
            
            # *text_reward_presentation* updates
            
            # if text_reward_presentation is starting this frame...
            if text_reward_presentation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_reward_presentation.frameNStart = frameN  # exact frame index
                text_reward_presentation.tStart = t  # local t and not account for scr refresh
                text_reward_presentation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_reward_presentation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_reward_presentation.started')
                # update status
                text_reward_presentation.status = STARTED
                text_reward_presentation.setAutoDraw(True)
            
            # if text_reward_presentation is active this frame...
            if text_reward_presentation.status == STARTED:
                # update params
                pass
            
            # if text_reward_presentation is stopping this frame...
            if text_reward_presentation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_reward_presentation.tStartRefresh + rewardPresentationTime-frameTolerance:
                    # keep track of stop time/frame for later
                    text_reward_presentation.tStop = t  # not accounting for scr refresh
                    text_reward_presentation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_reward_presentation.stopped')
                    # update status
                    text_reward_presentation.status = FINISHED
                    text_reward_presentation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reward_presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reward_presentation" ---
        for thisComponent in reward_presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "reward_presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nTrials repeats of 'main_trials'
    
    
    # --- Prepare to start Routine "Block_break" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_block_break
    thisExp.addData('text_block_break.started', globalClock.getTime())
    
    block_reward.append(nCorr)
    
    blockMsg = "Total reward for this day: " + str(nCorr) + "\n Next day starts soon"
    text_block_break.setText(blockMsg)
    # keep track of which components have finished
    Block_breakComponents = [text_block_break]
    for thisComponent in Block_breakComponents:
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
    
    # --- Run Routine "Block_break" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_block_break* updates
        
        # if text_block_break is starting this frame...
        if text_block_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_block_break.frameNStart = frameN  # exact frame index
            text_block_break.tStart = t  # local t and not account for scr refresh
            text_block_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_block_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_block_break.started')
            # update status
            text_block_break.status = STARTED
            text_block_break.setAutoDraw(True)
        
        # if text_block_break is active this frame...
        if text_block_break.status == STARTED:
            # update params
            pass
        
        # if text_block_break is stopping this frame...
        if text_block_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_block_break.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text_block_break.tStop = t  # not accounting for scr refresh
                text_block_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_block_break.stopped')
                # update status
                text_block_break.status = FINISHED
                text_block_break.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Block_break" ---
    for thisComponent in Block_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
# completed nBlocks repeats of 'block'


# --- Prepare to start Routine "End_ins" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
End_insComponents = [text_end_ins]
for thisComponent in End_insComponents:
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

# --- Run Routine "End_ins" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end_ins* updates
    
    # if text_end_ins is starting this frame...
    if text_end_ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end_ins.frameNStart = frameN  # exact frame index
        text_end_ins.tStart = t  # local t and not account for scr refresh
        text_end_ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end_ins, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_end_ins.started')
        # update status
        text_end_ins.status = STARTED
        text_end_ins.setAutoDraw(True)
    
    # if text_end_ins is active this frame...
    if text_end_ins.status == STARTED:
        # update params
        pass
    
    # if text_end_ins is stopping this frame...
    if text_end_ins.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end_ins.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            text_end_ins.tStop = t  # not accounting for scr refresh
            text_end_ins.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_end_ins.stopped')
            # update status
            text_end_ins.status = FINISHED
            text_end_ins.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End_ins" ---
for thisComponent in End_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)
# Run 'End Experiment' code from code
final_pay = randchoice(range(len(block_reward)))
blockID = final_pay + 1 

#print("correct per block", block_correct)
#print('block number: ', blockID)
#print('You earned: ', block_correct[final_pay])
thisExp.addData('reward_block_chosen', blockID)

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
