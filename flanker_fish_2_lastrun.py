#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on oktober 11, 2021, at 11:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'flanker_fish_2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\rbt369\\Desktop\\NEXS\\IFU_projekt\\Protokoller\\Motorisk indlæring for DS\\Flanker_fish2\\flanker_fish_2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='I det her spil vil du se en masse fisk som dem her.\nDin opgave er at fodre den eller de sultne fisk!\n\nDu skal fodre den rigtige fisk så hurtigt som muligt\n',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_pic = visual.ImageStim(
    win=win,
    name='welcome_pic', 
    image='blue_inc_L.bmp', mask=None,
    ori=0.0, pos=(0, -0.0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
welcome_cont = keyboard.Keyboard()
welcome_pic2 = visual.ImageStim(
    win=win,
    name='welcome_pic2', 
    image='pink_inc_R.bmp', mask=None,
    ori=0.0, pos=(0, -0.3), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Prac1_instr1"
Prac1_instr1Clock = core.Clock()
Prac1_instruc1_text = visual.TextStim(win=win, name='Prac1_instruc1_text',
    text='Når fisken er BLÅ er den sultne fisk i midten\n\nDu fodrer den midterste fisk ved at trykke i den side som fisken kigger mod\nHer kigger den midterste fisk den her vej, så du trykker i venstre side! ',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Prac1_instruc1_pic = visual.ImageStim(
    win=win,
    name='Prac1_instruc1_pic', 
    image='bluedemo.bmp', mask=None,
    ori=0.0, pos=(0, -0.2), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Prac1_instruc2"
Prac1_instruc2Clock = core.Clock()
Prac1_ins_text = visual.TextStim(win=win, name='Prac1_ins_text',
    text='Nogle gange er den MIDTERSTE fisk helt alene!\nDer skal du stadig trykke i den retning som den kigger mod',
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Prac1_instruc_pic1 = visual.ImageStim(
    win=win,
    name='Prac1_instruc_pic1', 
    image='blue_neut_R.bmp', mask=None,
    ori=0.0, pos=(0, 0.2), size=(1.4, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prac1_instruc2_text2 = visual.TextStim(win=win, name='Prac1_instruc2_text2',
    text='Nogle gange er den MIDTERSTE fisk sammen med andre, som svømmer i med andre som svømmer i en anden retning\nDer skal du stadig trykke i den retning som den kigger mod',
    font='Open Sans',
    pos=(0, -0.03), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Prac1_instric2_pic2 = visual.ImageStim(
    win=win,
    name='Prac1_instric2_pic2', 
    image='blue_nod_L.bmp', mask=None,
    ori=0.0, pos=(0, -0.25), size=(1.4, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Prac1_instruc2_text3 = visual.TextStim(win=win, name='Prac1_instruc2_text3',
    text='Du skal fodre den MIDTERSTE fisk! ',
    font='Open Sans',
    pos=(0, -0.4), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Prac1_start"
Prac1_startClock = core.Clock()
Pract1_instr_text = visual.TextStim(win=win, name='Pract1_instr_text',
    text='Lad os træne! ',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Prac1_cont = keyboard.Keyboard()

# Initialize components for Routine "Prac1"
Prac1Clock = core.Clock()
prac1_list = []

jitter = random() * (0.5 - 0.3) + 0.3
jitter = round(jitter, 1) # round to 1 decimal place
Prac1_fix = visual.TextStim(win=win, name='Prac1_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Prac1_stim = visual.ImageStim(
    win=win,
    name='Prac1_stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Prac1_resp = keyboard.Keyboard()

# Initialize components for Routine "Prac1_over"
Prac1_overClock = core.Clock()
Prac1_over_pic = visual.ImageStim(
    win=win,
    name='Prac1_over_pic', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prac1_over_text = visual.TextStim(win=win, name='Prac1_over_text',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Prac1_over_cont = keyboard.Keyboard()

# Initialize components for Routine "Task1_instr"
Task1_instrClock = core.Clock()
Task1_instr_text = visual.TextStim(win=win, name='Task1_instr_text',
    text='FLOT!\nLad os prøve at spille spillet rigtigt',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Task1_instr_cont = keyboard.Keyboard()

# Initialize components for Routine "Task1"
Task1Clock = core.Clock()
Task1_fix = visual.TextStim(win=win, name='Task1_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Task1_stim = visual.ImageStim(
    win=win,
    name='Task1_stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Task1_resp = keyboard.Keyboard()

# Initialize components for Routine "Task1_end"
Task1_endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='FLOT!\nNu kommer der en ny regel',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
task1_end_resp = keyboard.Keyboard()

# Initialize components for Routine "Prac2_instr_1"
Prac2_instr_1Clock = core.Clock()
Pract2_instr_text1 = visual.TextStim(win=win, name='Pract2_instr_text1',
    text='Når fiskene er PINK er de sultne fisk i siderne.\nDu fodrer de yderste fisk ved at trykke i den side de kigger mod.\nHer kigger de yderste fisk den vej, så du skal trykke i højre side! ',
    font='Open Sans',
    pos=(0, 0.35), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pract2_instr_pic = visual.ImageStim(
    win=win,
    name='Pract2_instr_pic', 
    image='pinkdemo.bmp', mask=None,
    ori=0.0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prac2_cont = keyboard.Keyboard()
Prac2_instruc1_text2 = visual.TextStim(win=win, name='Prac2_instruc1_text2',
    text='Lad is spille kun med de PINK fisk \nDu skal fodre de yderste fisk ved at trykke i højre side',
    font='Open Sans',
    pos=(0, -0.35), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Prac2_instr2"
Prac2_instr2Clock = core.Clock()
Prac2_instruc_pic1 = visual.ImageStim(
    win=win,
    name='Prac2_instruc_pic1', 
    image='pink_neut_R.bmp', mask=None,
    ori=0.0, pos=(0, 0.2), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Prac2_instruc2_text1 = visual.TextStim(win=win, name='Prac2_instruc2_text1',
    text='Nogle gange er der ingen fisk i midten! \nDer skal du stadig trikke i den retning de YDERSTE fisk kigger mod',
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Prac2_instr2_pic2 = visual.ImageStim(
    win=win,
    name='Prac2_instr2_pic2', 
    image='pink_nod_L.bmp', mask=None,
    ori=0.0, pos=(0, -0.205), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Prac2_instru2_text2 = visual.TextStim(win=win, name='Prac2_instru2_text2',
    text='Nogle gange svømmer midterste fisk i en helt anden retning\nDer skal du stadig trykke i den retning som de YDERSTE fisk kigger mod',
    font='Open Sans',
    pos=(0, 0.0), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Prac2_instru2_text3 = visual.TextStim(win=win, name='Prac2_instru2_text3',
    text='Du skal fodre de YDERSTE fisk',
    font='Open Sans',
    pos=(0, -0.4), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Prac2_start"
Prac2_startClock = core.Clock()
Parc2_start_text = visual.TextStim(win=win, name='Parc2_start_text',
    text='Lad os træne',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Prac2"
Prac2Clock = core.Clock()
prac2_list = []


Prac2_fix = visual.TextStim(win=win, name='Prac2_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Prac2_stim = visual.ImageStim(
    win=win,
    name='Prac2_stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Prac2_resp = keyboard.Keyboard()

# Initialize components for Routine "Prac2_over"
Prac2_overClock = core.Clock()
Prac2_over_pic = visual.ImageStim(
    win=win,
    name='Prac2_over_pic', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prac2_over_text = visual.TextStim(win=win, name='Prac2_over_text',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Prac2_over_cont = keyboard.Keyboard()

# Initialize components for Routine "Task2_instr"
Task2_instrClock = core.Clock()
Task2_instr_text = visual.TextStim(win=win, name='Task2_instr_text',
    text='FLOT!\nLad os prøve at spille spillet rigtigt',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Task2_instr_cont = keyboard.Keyboard()

# Initialize components for Routine "Task2"
Task2Clock = core.Clock()
Task2_fix = visual.TextStim(win=win, name='Task2_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Task2_stim = visual.ImageStim(
    win=win,
    name='Task2_stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Task2_resp = keyboard.Keyboard()

# Initialize components for Routine "Task2_end"
Task2_endClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Det var SUPER!\n\nNu skal du spille spillet med BEGGE farver\nSå det er vigtigt at du husker reglerne ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Prac3_instr"
Prac3_instrClock = core.Clock()
Pract3_instr_text = visual.TextStim(win=win, name='Pract3_instr_text',
    text='BLÅ betyder at du skal fodre den MIDTERSTE fisk',
    font='Open Sans',
    pos=(0, 0.41), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Pract3_instr_pic1 = visual.ImageStim(
    win=win,
    name='Pract3_instr_pic1', 
    image='blue_nod_R.bmp', mask=None,
    ori=0.0, pos=(0.0, 0.25), size=(1.4, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prac3_pic2 = visual.ImageStim(
    win=win,
    name='Prac3_pic2', 
    image='pink_nod_R.bmp', mask=None,
    ori=0.0, pos=(0.0, -0.15), size=(1.4, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Prac3_cont = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='PINK betyder at du skal fodre de YDERSTE fisk ',
    font='Open Sans',
    pos=(0, 0.015), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='BLÅ - MIDTEN\nPINK - YDERST',
    font='Open Sans',
    pos=(0, -0.37), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Prac3_instr2"
Prac3_instr2Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Lads os træne',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Prac3"
Prac3Clock = core.Clock()
prac3_list = []

Prac3_fix = visual.TextStim(win=win, name='Prac3_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Prac3_pic = visual.ImageStim(
    win=win,
    name='Prac3_pic', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Prac3_resp = keyboard.Keyboard()

# Initialize components for Routine "Prac3_over"
Prac3_overClock = core.Clock()
Prac3_over_pic = visual.ImageStim(
    win=win,
    name='Prac3_over_pic', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.2), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Prac3_over_text = visual.TextStim(win=win, name='Prac3_over_text',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.1, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Prac3_over_cont = keyboard.Keyboard()

# Initialize components for Routine "Task3_instr"
Task3_instrClock = core.Clock()
Task3_instr_text = visual.TextStim(win=win, name='Task3_instr_text',
    text='Lad os prøve at spille spillet rigtgt',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=4.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Task3_instr_cont = keyboard.Keyboard()

# Initialize components for Routine "Task3"
Task3Clock = core.Clock()
Task3_fix = visual.TextStim(win=win, name='Task3_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Task3_stim = visual.ImageStim(
    win=win,
    name='Task3_stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Task3_resp = keyboard.Keyboard()

# Initialize components for Routine "finished"
finishedClock = core.Clock()
Tak_pic = visual.ImageStim(
    win=win,
    name='Tak_pic', 
    image='thank.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
tak_cont = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_cont.keys = []
welcome_cont.rt = []
_welcome_cont_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_pic, welcome_cont, welcome_pic2]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_pic* updates
    if welcome_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_pic.frameNStart = frameN  # exact frame index
        welcome_pic.tStart = t  # local t and not account for scr refresh
        welcome_pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_pic, 'tStartRefresh')  # time at next scr refresh
        welcome_pic.setAutoDraw(True)
    
    # *welcome_cont* updates
    waitOnFlip = False
    if welcome_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_cont.frameNStart = frameN  # exact frame index
        welcome_cont.tStart = t  # local t and not account for scr refresh
        welcome_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_cont, 'tStartRefresh')  # time at next scr refresh
        welcome_cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_cont.status == STARTED and not waitOnFlip:
        theseKeys = welcome_cont.getKeys(keyList=None, waitRelease=False)
        _welcome_cont_allKeys.extend(theseKeys)
        if len(_welcome_cont_allKeys):
            welcome_cont.keys = _welcome_cont_allKeys[-1].name  # just the last key pressed
            welcome_cont.rt = _welcome_cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *welcome_pic2* updates
    if welcome_pic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_pic2.frameNStart = frameN  # exact frame index
        welcome_pic2.tStart = t  # local t and not account for scr refresh
        welcome_pic2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_pic2, 'tStartRefresh')  # time at next scr refresh
        welcome_pic2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
thisExp.addData('welcome_pic.started', welcome_pic.tStartRefresh)
thisExp.addData('welcome_pic.stopped', welcome_pic.tStopRefresh)
# check responses
if welcome_cont.keys in ['', [], None]:  # No response was made
    welcome_cont.keys = None
thisExp.addData('welcome_cont.keys',welcome_cont.keys)
if welcome_cont.keys != None:  # we had a response
    thisExp.addData('welcome_cont.rt', welcome_cont.rt)
thisExp.addData('welcome_cont.started', welcome_cont.tStartRefresh)
thisExp.addData('welcome_cont.stopped', welcome_cont.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('welcome_pic2.started', welcome_pic2.tStartRefresh)
thisExp.addData('welcome_pic2.stopped', welcome_pic2.tStopRefresh)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac1_repeat = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blue_prac_all.xlsx'),
    seed=None, name='prac1_repeat')
thisExp.addLoop(prac1_repeat)  # add the loop to the experiment
thisPrac1_repeat = prac1_repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac1_repeat.rgb)
if thisPrac1_repeat != None:
    for paramName in thisPrac1_repeat:
        exec('{} = thisPrac1_repeat[paramName]'.format(paramName))

for thisPrac1_repeat in prac1_repeat:
    currentLoop = prac1_repeat
    # abbreviate parameter names if possible (e.g. rgb = thisPrac1_repeat.rgb)
    if thisPrac1_repeat != None:
        for paramName in thisPrac1_repeat:
            exec('{} = thisPrac1_repeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Prac1_instr1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    Prac1_instr1Components = [Prac1_instruc1_text, Prac1_instruc1_pic, key_resp_3]
    for thisComponent in Prac1_instr1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac1_instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac1_instr1"-------
    while continueRoutine:
        # get current time
        t = Prac1_instr1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac1_instr1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac1_instruc1_text* updates
        if Prac1_instruc1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_instruc1_text.frameNStart = frameN  # exact frame index
            Prac1_instruc1_text.tStart = t  # local t and not account for scr refresh
            Prac1_instruc1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_instruc1_text, 'tStartRefresh')  # time at next scr refresh
            Prac1_instruc1_text.setAutoDraw(True)
        
        # *Prac1_instruc1_pic* updates
        if Prac1_instruc1_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_instruc1_pic.frameNStart = frameN  # exact frame index
            Prac1_instruc1_pic.tStart = t  # local t and not account for scr refresh
            Prac1_instruc1_pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_instruc1_pic, 'tStartRefresh')  # time at next scr refresh
            Prac1_instruc1_pic.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['lctrl'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac1_instr1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac1_instr1"-------
    for thisComponent in Prac1_instr1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac1_repeat.addData('Prac1_instruc1_text.started', Prac1_instruc1_text.tStartRefresh)
    prac1_repeat.addData('Prac1_instruc1_text.stopped', Prac1_instruc1_text.tStopRefresh)
    prac1_repeat.addData('Prac1_instruc1_pic.started', Prac1_instruc1_pic.tStartRefresh)
    prac1_repeat.addData('Prac1_instruc1_pic.stopped', Prac1_instruc1_pic.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    prac1_repeat.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        prac1_repeat.addData('key_resp_3.rt', key_resp_3.rt)
    prac1_repeat.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    prac1_repeat.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "Prac1_instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Prac1_instruc2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Prac1_instruc2Components = [Prac1_ins_text, Prac1_instruc_pic1, Prac1_instruc2_text2, Prac1_instric2_pic2, Prac1_instruc2_text3, key_resp_2]
    for thisComponent in Prac1_instruc2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac1_instruc2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac1_instruc2"-------
    while continueRoutine:
        # get current time
        t = Prac1_instruc2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac1_instruc2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac1_ins_text* updates
        if Prac1_ins_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_ins_text.frameNStart = frameN  # exact frame index
            Prac1_ins_text.tStart = t  # local t and not account for scr refresh
            Prac1_ins_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_ins_text, 'tStartRefresh')  # time at next scr refresh
            Prac1_ins_text.setAutoDraw(True)
        
        # *Prac1_instruc_pic1* updates
        if Prac1_instruc_pic1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_instruc_pic1.frameNStart = frameN  # exact frame index
            Prac1_instruc_pic1.tStart = t  # local t and not account for scr refresh
            Prac1_instruc_pic1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_instruc_pic1, 'tStartRefresh')  # time at next scr refresh
            Prac1_instruc_pic1.setAutoDraw(True)
        
        # *Prac1_instruc2_text2* updates
        if Prac1_instruc2_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_instruc2_text2.frameNStart = frameN  # exact frame index
            Prac1_instruc2_text2.tStart = t  # local t and not account for scr refresh
            Prac1_instruc2_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_instruc2_text2, 'tStartRefresh')  # time at next scr refresh
            Prac1_instruc2_text2.setAutoDraw(True)
        
        # *Prac1_instric2_pic2* updates
        if Prac1_instric2_pic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_instric2_pic2.frameNStart = frameN  # exact frame index
            Prac1_instric2_pic2.tStart = t  # local t and not account for scr refresh
            Prac1_instric2_pic2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_instric2_pic2, 'tStartRefresh')  # time at next scr refresh
            Prac1_instric2_pic2.setAutoDraw(True)
        
        # *Prac1_instruc2_text3* updates
        if Prac1_instruc2_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_instruc2_text3.frameNStart = frameN  # exact frame index
            Prac1_instruc2_text3.tStart = t  # local t and not account for scr refresh
            Prac1_instruc2_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_instruc2_text3, 'tStartRefresh')  # time at next scr refresh
            Prac1_instruc2_text3.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['lctrl'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac1_instruc2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac1_instruc2"-------
    for thisComponent in Prac1_instruc2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac1_repeat.addData('Prac1_ins_text.started', Prac1_ins_text.tStartRefresh)
    prac1_repeat.addData('Prac1_ins_text.stopped', Prac1_ins_text.tStopRefresh)
    prac1_repeat.addData('Prac1_instruc_pic1.started', Prac1_instruc_pic1.tStartRefresh)
    prac1_repeat.addData('Prac1_instruc_pic1.stopped', Prac1_instruc_pic1.tStopRefresh)
    prac1_repeat.addData('Prac1_instruc2_text2.started', Prac1_instruc2_text2.tStartRefresh)
    prac1_repeat.addData('Prac1_instruc2_text2.stopped', Prac1_instruc2_text2.tStopRefresh)
    prac1_repeat.addData('Prac1_instric2_pic2.started', Prac1_instric2_pic2.tStartRefresh)
    prac1_repeat.addData('Prac1_instric2_pic2.stopped', Prac1_instric2_pic2.tStopRefresh)
    prac1_repeat.addData('Prac1_instruc2_text3.started', Prac1_instruc2_text3.tStartRefresh)
    prac1_repeat.addData('Prac1_instruc2_text3.stopped', Prac1_instruc2_text3.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    prac1_repeat.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        prac1_repeat.addData('key_resp_2.rt', key_resp_2.rt)
    prac1_repeat.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    prac1_repeat.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Prac1_instruc2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Prac1_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    Prac1_cont.keys = []
    Prac1_cont.rt = []
    _Prac1_cont_allKeys = []
    # keep track of which components have finished
    Prac1_startComponents = [Pract1_instr_text, Prac1_cont]
    for thisComponent in Prac1_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac1_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac1_start"-------
    while continueRoutine:
        # get current time
        t = Prac1_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac1_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pract1_instr_text* updates
        if Pract1_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pract1_instr_text.frameNStart = frameN  # exact frame index
            Pract1_instr_text.tStart = t  # local t and not account for scr refresh
            Pract1_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pract1_instr_text, 'tStartRefresh')  # time at next scr refresh
            Pract1_instr_text.setAutoDraw(True)
        
        # *Prac1_cont* updates
        waitOnFlip = False
        if Prac1_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_cont.frameNStart = frameN  # exact frame index
            Prac1_cont.tStart = t  # local t and not account for scr refresh
            Prac1_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_cont, 'tStartRefresh')  # time at next scr refresh
            Prac1_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac1_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac1_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prac1_cont.status == STARTED and not waitOnFlip:
            theseKeys = Prac1_cont.getKeys(keyList=None, waitRelease=False)
            _Prac1_cont_allKeys.extend(theseKeys)
            if len(_Prac1_cont_allKeys):
                Prac1_cont.keys = _Prac1_cont_allKeys[-1].name  # just the last key pressed
                Prac1_cont.rt = _Prac1_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac1_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac1_start"-------
    for thisComponent in Prac1_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac1_repeat.addData('Pract1_instr_text.started', Pract1_instr_text.tStartRefresh)
    prac1_repeat.addData('Pract1_instr_text.stopped', Pract1_instr_text.tStopRefresh)
    # check responses
    if Prac1_cont.keys in ['', [], None]:  # No response was made
        Prac1_cont.keys = None
    prac1_repeat.addData('Prac1_cont.keys',Prac1_cont.keys)
    if Prac1_cont.keys != None:  # we had a response
        prac1_repeat.addData('Prac1_cont.rt', Prac1_cont.rt)
    prac1_repeat.addData('Prac1_cont.started', Prac1_cont.tStartRefresh)
    prac1_repeat.addData('Prac1_cont.stopped', Prac1_cont.tStopRefresh)
    # the Routine "Prac1_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac1_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(prac_file),
        seed=None, name='prac1_trials')
    thisExp.addLoop(prac1_trials)  # add the loop to the experiment
    thisPrac1_trial = prac1_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac1_trial.rgb)
    if thisPrac1_trial != None:
        for paramName in thisPrac1_trial:
            exec('{} = thisPrac1_trial[paramName]'.format(paramName))
    
    for thisPrac1_trial in prac1_trials:
        currentLoop = prac1_trials
        # abbreviate parameter names if possible (e.g. rgb = thisPrac1_trial.rgb)
        if thisPrac1_trial != None:
            for paramName in thisPrac1_trial:
                exec('{} = thisPrac1_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Prac1"-------
        continueRoutine = True
        # update component parameters for each repeat
        Prac1_stim.setImage(blue_stim)
        Prac1_resp.keys = []
        Prac1_resp.rt = []
        _Prac1_resp_allKeys = []
        # keep track of which components have finished
        Prac1Components = [Prac1_fix, Prac1_stim, Prac1_resp]
        for thisComponent in Prac1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Prac1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Prac1"-------
        while continueRoutine:
            # get current time
            t = Prac1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Prac1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Prac1_fix* updates
            if Prac1_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Prac1_fix.frameNStart = frameN  # exact frame index
                Prac1_fix.tStart = t  # local t and not account for scr refresh
                Prac1_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac1_fix, 'tStartRefresh')  # time at next scr refresh
                Prac1_fix.setAutoDraw(True)
            if Prac1_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac1_fix.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac1_fix.tStop = t  # not accounting for scr refresh
                    Prac1_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac1_fix, 'tStopRefresh')  # time at next scr refresh
                    Prac1_fix.setAutoDraw(False)
            
            # *Prac1_stim* updates
            if Prac1_stim.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
                # keep track of start time/frame for later
                Prac1_stim.frameNStart = frameN  # exact frame index
                Prac1_stim.tStart = t  # local t and not account for scr refresh
                Prac1_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac1_stim, 'tStartRefresh')  # time at next scr refresh
                Prac1_stim.setAutoDraw(True)
            if Prac1_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac1_stim.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac1_stim.tStop = t  # not accounting for scr refresh
                    Prac1_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac1_stim, 'tStopRefresh')  # time at next scr refresh
                    Prac1_stim.setAutoDraw(False)
            
            # *Prac1_resp* updates
            waitOnFlip = False
            if Prac1_resp.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
                # keep track of start time/frame for later
                Prac1_resp.frameNStart = frameN  # exact frame index
                Prac1_resp.tStart = t  # local t and not account for scr refresh
                Prac1_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac1_resp, 'tStartRefresh')  # time at next scr refresh
                Prac1_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Prac1_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Prac1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Prac1_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac1_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac1_resp.tStop = t  # not accounting for scr refresh
                    Prac1_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac1_resp, 'tStopRefresh')  # time at next scr refresh
                    Prac1_resp.status = FINISHED
            if Prac1_resp.status == STARTED and not waitOnFlip:
                theseKeys = Prac1_resp.getKeys(keyList=['lctrl', 'return'], waitRelease=False)
                _Prac1_resp_allKeys.extend(theseKeys)
                if len(_Prac1_resp_allKeys):
                    Prac1_resp.keys = _Prac1_resp_allKeys[-1].name  # just the last key pressed
                    Prac1_resp.rt = _Prac1_resp_allKeys[-1].rt
                    # was this correct?
                    if (Prac1_resp.keys == str(corrAns)) or (Prac1_resp.keys == corrAns):
                        Prac1_resp.corr = 1
                    else:
                        Prac1_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Prac1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Prac1"-------
        for thisComponent in Prac1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac1_list.append(Prac1_resp.corr)
        
        prac1_trials.addData('prac1_list', prac1_list)
        
        prac1_trials.addData('Prac1_fix.started', Prac1_fix.tStartRefresh)
        prac1_trials.addData('Prac1_fix.stopped', Prac1_fix.tStopRefresh)
        prac1_trials.addData('Prac1_stim.started', Prac1_stim.tStartRefresh)
        prac1_trials.addData('Prac1_stim.stopped', Prac1_stim.tStopRefresh)
        # check responses
        if Prac1_resp.keys in ['', [], None]:  # No response was made
            Prac1_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               Prac1_resp.corr = 1;  # correct non-response
            else:
               Prac1_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac1_trials (TrialHandler)
        prac1_trials.addData('Prac1_resp.keys',Prac1_resp.keys)
        prac1_trials.addData('Prac1_resp.corr', Prac1_resp.corr)
        if Prac1_resp.keys != None:  # we had a response
            prac1_trials.addData('Prac1_resp.rt', Prac1_resp.rt)
        prac1_trials.addData('Prac1_resp.started', Prac1_resp.tStartRefresh)
        prac1_trials.addData('Prac1_resp.stopped', Prac1_resp.tStopRefresh)
        # the Routine "Prac1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac1_trials'
    
    
    # ------Prepare to start Routine "Prac1_over"-------
    continueRoutine = True
    # update component parameters for each repeat
       
    if sum(prac1_list[-4:]) > 2 :
        pic = 'well_done.jpg'
        msg = 'Træningen er slut. Godt klaret!'
        
    if not sum(prac1_list[-4:]) > 2 :
        pic = 'try_again.jpg'
        msg = 'Lad os træne en gang mere.'
        
    if sum(prac1_list[-4:]) > 2 :
        prac1_repeat.finished = True
        
    if len(prac1_list) > 10 and sum(prac1_list[-4:]) < 3 :
        pic = 'well_done.jpg'
        msg = 'Træningen er slut. Godt klaret!'
        
    Prac1_over_pic.setImage(pic)
    Prac1_over_text.setText(msg)
    Prac1_over_cont.keys = []
    Prac1_over_cont.rt = []
    _Prac1_over_cont_allKeys = []
    # keep track of which components have finished
    Prac1_overComponents = [Prac1_over_pic, Prac1_over_text, Prac1_over_cont]
    for thisComponent in Prac1_overComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac1_overClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac1_over"-------
    while continueRoutine:
        # get current time
        t = Prac1_overClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac1_overClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac1_over_pic* updates
        if Prac1_over_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_over_pic.frameNStart = frameN  # exact frame index
            Prac1_over_pic.tStart = t  # local t and not account for scr refresh
            Prac1_over_pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_over_pic, 'tStartRefresh')  # time at next scr refresh
            Prac1_over_pic.setAutoDraw(True)
        
        # *Prac1_over_text* updates
        if Prac1_over_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_over_text.frameNStart = frameN  # exact frame index
            Prac1_over_text.tStart = t  # local t and not account for scr refresh
            Prac1_over_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_over_text, 'tStartRefresh')  # time at next scr refresh
            Prac1_over_text.setAutoDraw(True)
        
        # *Prac1_over_cont* updates
        waitOnFlip = False
        if Prac1_over_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac1_over_cont.frameNStart = frameN  # exact frame index
            Prac1_over_cont.tStart = t  # local t and not account for scr refresh
            Prac1_over_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac1_over_cont, 'tStartRefresh')  # time at next scr refresh
            Prac1_over_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac1_over_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac1_over_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prac1_over_cont.status == STARTED and not waitOnFlip:
            theseKeys = Prac1_over_cont.getKeys(keyList=None, waitRelease=False)
            _Prac1_over_cont_allKeys.extend(theseKeys)
            if len(_Prac1_over_cont_allKeys):
                Prac1_over_cont.keys = _Prac1_over_cont_allKeys[-1].name  # just the last key pressed
                Prac1_over_cont.rt = _Prac1_over_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac1_overComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac1_over"-------
    for thisComponent in Prac1_overComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac1_repeat.addData('Prac1_over_pic.started', Prac1_over_pic.tStartRefresh)
    prac1_repeat.addData('Prac1_over_pic.stopped', Prac1_over_pic.tStopRefresh)
    prac1_repeat.addData('Prac1_over_text.started', Prac1_over_text.tStartRefresh)
    prac1_repeat.addData('Prac1_over_text.stopped', Prac1_over_text.tStopRefresh)
    # check responses
    if Prac1_over_cont.keys in ['', [], None]:  # No response was made
        Prac1_over_cont.keys = None
    prac1_repeat.addData('Prac1_over_cont.keys',Prac1_over_cont.keys)
    if Prac1_over_cont.keys != None:  # we had a response
        prac1_repeat.addData('Prac1_over_cont.rt', Prac1_over_cont.rt)
    prac1_repeat.addData('Prac1_over_cont.started', Prac1_over_cont.tStartRefresh)
    prac1_repeat.addData('Prac1_over_cont.stopped', Prac1_over_cont.tStopRefresh)
    # the Routine "Prac1_over" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac1_repeat'


# ------Prepare to start Routine "Task1_instr"-------
continueRoutine = True
# update component parameters for each repeat
Task1_instr_cont.keys = []
Task1_instr_cont.rt = []
_Task1_instr_cont_allKeys = []
# keep track of which components have finished
Task1_instrComponents = [Task1_instr_text, Task1_instr_cont]
for thisComponent in Task1_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Task1_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Task1_instr"-------
while continueRoutine:
    # get current time
    t = Task1_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Task1_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task1_instr_text* updates
    if Task1_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task1_instr_text.frameNStart = frameN  # exact frame index
        Task1_instr_text.tStart = t  # local t and not account for scr refresh
        Task1_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task1_instr_text, 'tStartRefresh')  # time at next scr refresh
        Task1_instr_text.setAutoDraw(True)
    
    # *Task1_instr_cont* updates
    waitOnFlip = False
    if Task1_instr_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task1_instr_cont.frameNStart = frameN  # exact frame index
        Task1_instr_cont.tStart = t  # local t and not account for scr refresh
        Task1_instr_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task1_instr_cont, 'tStartRefresh')  # time at next scr refresh
        Task1_instr_cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Task1_instr_cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Task1_instr_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Task1_instr_cont.status == STARTED and not waitOnFlip:
        theseKeys = Task1_instr_cont.getKeys(keyList=None, waitRelease=False)
        _Task1_instr_cont_allKeys.extend(theseKeys)
        if len(_Task1_instr_cont_allKeys):
            Task1_instr_cont.keys = _Task1_instr_cont_allKeys[-1].name  # just the last key pressed
            Task1_instr_cont.rt = _Task1_instr_cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Task1_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task1_instr"-------
for thisComponent in Task1_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Task1_instr_text.started', Task1_instr_text.tStartRefresh)
thisExp.addData('Task1_instr_text.stopped', Task1_instr_text.tStopRefresh)
# check responses
if Task1_instr_cont.keys in ['', [], None]:  # No response was made
    Task1_instr_cont.keys = None
thisExp.addData('Task1_instr_cont.keys',Task1_instr_cont.keys)
if Task1_instr_cont.keys != None:  # we had a response
    thisExp.addData('Task1_instr_cont.rt', Task1_instr_cont.rt)
thisExp.addData('Task1_instr_cont.started', Task1_instr_cont.tStartRefresh)
thisExp.addData('Task1_instr_cont.stopped', Task1_instr_cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "Task1_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
task1_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blue_task.xlsx'),
    seed=None, name='task1_trials')
thisExp.addLoop(task1_trials)  # add the loop to the experiment
thisTask1_trial = task1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask1_trial.rgb)
if thisTask1_trial != None:
    for paramName in thisTask1_trial:
        exec('{} = thisTask1_trial[paramName]'.format(paramName))

for thisTask1_trial in task1_trials:
    currentLoop = task1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTask1_trial.rgb)
    if thisTask1_trial != None:
        for paramName in thisTask1_trial:
            exec('{} = thisTask1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Task1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Task1_stim.setImage(blue_stim)
    Task1_resp.keys = []
    Task1_resp.rt = []
    _Task1_resp_allKeys = []
    # keep track of which components have finished
    Task1Components = [Task1_fix, Task1_stim, Task1_resp]
    for thisComponent in Task1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Task1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Task1"-------
    while continueRoutine:
        # get current time
        t = Task1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Task1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task1_fix* updates
        if Task1_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task1_fix.frameNStart = frameN  # exact frame index
            Task1_fix.tStart = t  # local t and not account for scr refresh
            Task1_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task1_fix, 'tStartRefresh')  # time at next scr refresh
            Task1_fix.setAutoDraw(True)
        if Task1_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task1_fix.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                Task1_fix.tStop = t  # not accounting for scr refresh
                Task1_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task1_fix, 'tStopRefresh')  # time at next scr refresh
                Task1_fix.setAutoDraw(False)
        
        # *Task1_stim* updates
        if Task1_stim.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
            # keep track of start time/frame for later
            Task1_stim.frameNStart = frameN  # exact frame index
            Task1_stim.tStart = t  # local t and not account for scr refresh
            Task1_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task1_stim, 'tStartRefresh')  # time at next scr refresh
            Task1_stim.setAutoDraw(True)
        if Task1_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task1_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Task1_stim.tStop = t  # not accounting for scr refresh
                Task1_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task1_stim, 'tStopRefresh')  # time at next scr refresh
                Task1_stim.setAutoDraw(False)
        
        # *Task1_resp* updates
        waitOnFlip = False
        if Task1_resp.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
            # keep track of start time/frame for later
            Task1_resp.frameNStart = frameN  # exact frame index
            Task1_resp.tStart = t  # local t and not account for scr refresh
            Task1_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task1_resp, 'tStartRefresh')  # time at next scr refresh
            Task1_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Task1_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Task1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Task1_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task1_resp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Task1_resp.tStop = t  # not accounting for scr refresh
                Task1_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task1_resp, 'tStopRefresh')  # time at next scr refresh
                Task1_resp.status = FINISHED
        if Task1_resp.status == STARTED and not waitOnFlip:
            theseKeys = Task1_resp.getKeys(keyList=['lctrl', 'return'], waitRelease=False)
            _Task1_resp_allKeys.extend(theseKeys)
            if len(_Task1_resp_allKeys):
                Task1_resp.keys = _Task1_resp_allKeys[-1].name  # just the last key pressed
                Task1_resp.rt = _Task1_resp_allKeys[-1].rt
                # was this correct?
                if (Task1_resp.keys == str(corrAns)) or (Task1_resp.keys == corrAns):
                    Task1_resp.corr = 1
                else:
                    Task1_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Task1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Task1"-------
    for thisComponent in Task1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task1_trials.addData('Task1_fix.started', Task1_fix.tStartRefresh)
    task1_trials.addData('Task1_fix.stopped', Task1_fix.tStopRefresh)
    task1_trials.addData('Task1_stim.started', Task1_stim.tStartRefresh)
    task1_trials.addData('Task1_stim.stopped', Task1_stim.tStopRefresh)
    # check responses
    if Task1_resp.keys in ['', [], None]:  # No response was made
        Task1_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           Task1_resp.corr = 1;  # correct non-response
        else:
           Task1_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for task1_trials (TrialHandler)
    task1_trials.addData('Task1_resp.keys',Task1_resp.keys)
    task1_trials.addData('Task1_resp.corr', Task1_resp.corr)
    if Task1_resp.keys != None:  # we had a response
        task1_trials.addData('Task1_resp.rt', Task1_resp.rt)
    task1_trials.addData('Task1_resp.started', Task1_resp.tStartRefresh)
    task1_trials.addData('Task1_resp.stopped', Task1_resp.tStopRefresh)
    # the Routine "Task1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task1_trials'


# ------Prepare to start Routine "Task1_end"-------
continueRoutine = True
# update component parameters for each repeat
task1_end_resp.keys = []
task1_end_resp.rt = []
_task1_end_resp_allKeys = []
# keep track of which components have finished
Task1_endComponents = [text_2, task1_end_resp]
for thisComponent in Task1_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Task1_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Task1_end"-------
while continueRoutine:
    # get current time
    t = Task1_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Task1_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *task1_end_resp* updates
    waitOnFlip = False
    if task1_end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        task1_end_resp.frameNStart = frameN  # exact frame index
        task1_end_resp.tStart = t  # local t and not account for scr refresh
        task1_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(task1_end_resp, 'tStartRefresh')  # time at next scr refresh
        task1_end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(task1_end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(task1_end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if task1_end_resp.status == STARTED and not waitOnFlip:
        theseKeys = task1_end_resp.getKeys(keyList=None, waitRelease=False)
        _task1_end_resp_allKeys.extend(theseKeys)
        if len(_task1_end_resp_allKeys):
            task1_end_resp.keys = _task1_end_resp_allKeys[-1].name  # just the last key pressed
            task1_end_resp.rt = _task1_end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Task1_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task1_end"-------
for thisComponent in Task1_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if task1_end_resp.keys in ['', [], None]:  # No response was made
    task1_end_resp.keys = None
thisExp.addData('task1_end_resp.keys',task1_end_resp.keys)
if task1_end_resp.keys != None:  # we had a response
    thisExp.addData('task1_end_resp.rt', task1_end_resp.rt)
thisExp.addData('task1_end_resp.started', task1_end_resp.tStartRefresh)
thisExp.addData('task1_end_resp.stopped', task1_end_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Task1_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac2_repeat = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pink_prac_all.xlsx'),
    seed=None, name='prac2_repeat')
thisExp.addLoop(prac2_repeat)  # add the loop to the experiment
thisPrac2_repeat = prac2_repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac2_repeat.rgb)
if thisPrac2_repeat != None:
    for paramName in thisPrac2_repeat:
        exec('{} = thisPrac2_repeat[paramName]'.format(paramName))

for thisPrac2_repeat in prac2_repeat:
    currentLoop = prac2_repeat
    # abbreviate parameter names if possible (e.g. rgb = thisPrac2_repeat.rgb)
    if thisPrac2_repeat != None:
        for paramName in thisPrac2_repeat:
            exec('{} = thisPrac2_repeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Prac2_instr_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Prac2_cont.keys = []
    Prac2_cont.rt = []
    _Prac2_cont_allKeys = []
    # keep track of which components have finished
    Prac2_instr_1Components = [Pract2_instr_text1, Pract2_instr_pic, Prac2_cont, Prac2_instruc1_text2]
    for thisComponent in Prac2_instr_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac2_instr_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac2_instr_1"-------
    while continueRoutine:
        # get current time
        t = Prac2_instr_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac2_instr_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pract2_instr_text1* updates
        if Pract2_instr_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pract2_instr_text1.frameNStart = frameN  # exact frame index
            Pract2_instr_text1.tStart = t  # local t and not account for scr refresh
            Pract2_instr_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pract2_instr_text1, 'tStartRefresh')  # time at next scr refresh
            Pract2_instr_text1.setAutoDraw(True)
        
        # *Pract2_instr_pic* updates
        if Pract2_instr_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pract2_instr_pic.frameNStart = frameN  # exact frame index
            Pract2_instr_pic.tStart = t  # local t and not account for scr refresh
            Pract2_instr_pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pract2_instr_pic, 'tStartRefresh')  # time at next scr refresh
            Pract2_instr_pic.setAutoDraw(True)
        
        # *Prac2_cont* updates
        waitOnFlip = False
        if Prac2_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_cont.frameNStart = frameN  # exact frame index
            Prac2_cont.tStart = t  # local t and not account for scr refresh
            Prac2_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_cont, 'tStartRefresh')  # time at next scr refresh
            Prac2_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac2_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac2_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prac2_cont.status == STARTED and not waitOnFlip:
            theseKeys = Prac2_cont.getKeys(keyList=['return'], waitRelease=False)
            _Prac2_cont_allKeys.extend(theseKeys)
            if len(_Prac2_cont_allKeys):
                Prac2_cont.keys = _Prac2_cont_allKeys[-1].name  # just the last key pressed
                Prac2_cont.rt = _Prac2_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Prac2_instruc1_text2* updates
        if Prac2_instruc1_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_instruc1_text2.frameNStart = frameN  # exact frame index
            Prac2_instruc1_text2.tStart = t  # local t and not account for scr refresh
            Prac2_instruc1_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_instruc1_text2, 'tStartRefresh')  # time at next scr refresh
            Prac2_instruc1_text2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac2_instr_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac2_instr_1"-------
    for thisComponent in Prac2_instr_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac2_repeat.addData('Pract2_instr_text1.started', Pract2_instr_text1.tStartRefresh)
    prac2_repeat.addData('Pract2_instr_text1.stopped', Pract2_instr_text1.tStopRefresh)
    prac2_repeat.addData('Pract2_instr_pic.started', Pract2_instr_pic.tStartRefresh)
    prac2_repeat.addData('Pract2_instr_pic.stopped', Pract2_instr_pic.tStopRefresh)
    # check responses
    if Prac2_cont.keys in ['', [], None]:  # No response was made
        Prac2_cont.keys = None
    prac2_repeat.addData('Prac2_cont.keys',Prac2_cont.keys)
    if Prac2_cont.keys != None:  # we had a response
        prac2_repeat.addData('Prac2_cont.rt', Prac2_cont.rt)
    prac2_repeat.addData('Prac2_cont.started', Prac2_cont.tStartRefresh)
    prac2_repeat.addData('Prac2_cont.stopped', Prac2_cont.tStopRefresh)
    prac2_repeat.addData('Prac2_instruc1_text2.started', Prac2_instruc1_text2.tStartRefresh)
    prac2_repeat.addData('Prac2_instruc1_text2.stopped', Prac2_instruc1_text2.tStopRefresh)
    # the Routine "Prac2_instr_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Prac2_instr2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Prac2_instr2Components = [Prac2_instruc_pic1, Prac2_instruc2_text1, Prac2_instr2_pic2, Prac2_instru2_text2, Prac2_instru2_text3, key_resp_5]
    for thisComponent in Prac2_instr2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac2_instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac2_instr2"-------
    while continueRoutine:
        # get current time
        t = Prac2_instr2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac2_instr2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac2_instruc_pic1* updates
        if Prac2_instruc_pic1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_instruc_pic1.frameNStart = frameN  # exact frame index
            Prac2_instruc_pic1.tStart = t  # local t and not account for scr refresh
            Prac2_instruc_pic1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_instruc_pic1, 'tStartRefresh')  # time at next scr refresh
            Prac2_instruc_pic1.setAutoDraw(True)
        
        # *Prac2_instruc2_text1* updates
        if Prac2_instruc2_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_instruc2_text1.frameNStart = frameN  # exact frame index
            Prac2_instruc2_text1.tStart = t  # local t and not account for scr refresh
            Prac2_instruc2_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_instruc2_text1, 'tStartRefresh')  # time at next scr refresh
            Prac2_instruc2_text1.setAutoDraw(True)
        
        # *Prac2_instr2_pic2* updates
        if Prac2_instr2_pic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_instr2_pic2.frameNStart = frameN  # exact frame index
            Prac2_instr2_pic2.tStart = t  # local t and not account for scr refresh
            Prac2_instr2_pic2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_instr2_pic2, 'tStartRefresh')  # time at next scr refresh
            Prac2_instr2_pic2.setAutoDraw(True)
        
        # *Prac2_instru2_text2* updates
        if Prac2_instru2_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_instru2_text2.frameNStart = frameN  # exact frame index
            Prac2_instru2_text2.tStart = t  # local t and not account for scr refresh
            Prac2_instru2_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_instru2_text2, 'tStartRefresh')  # time at next scr refresh
            Prac2_instru2_text2.setAutoDraw(True)
        
        # *Prac2_instru2_text3* updates
        if Prac2_instru2_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_instru2_text3.frameNStart = frameN  # exact frame index
            Prac2_instru2_text3.tStart = t  # local t and not account for scr refresh
            Prac2_instru2_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_instru2_text3, 'tStartRefresh')  # time at next scr refresh
            Prac2_instru2_text3.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['lctrl'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac2_instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac2_instr2"-------
    for thisComponent in Prac2_instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac2_repeat.addData('Prac2_instruc_pic1.started', Prac2_instruc_pic1.tStartRefresh)
    prac2_repeat.addData('Prac2_instruc_pic1.stopped', Prac2_instruc_pic1.tStopRefresh)
    prac2_repeat.addData('Prac2_instruc2_text1.started', Prac2_instruc2_text1.tStartRefresh)
    prac2_repeat.addData('Prac2_instruc2_text1.stopped', Prac2_instruc2_text1.tStopRefresh)
    prac2_repeat.addData('Prac2_instr2_pic2.started', Prac2_instr2_pic2.tStartRefresh)
    prac2_repeat.addData('Prac2_instr2_pic2.stopped', Prac2_instr2_pic2.tStopRefresh)
    prac2_repeat.addData('Prac2_instru2_text2.started', Prac2_instru2_text2.tStartRefresh)
    prac2_repeat.addData('Prac2_instru2_text2.stopped', Prac2_instru2_text2.tStopRefresh)
    prac2_repeat.addData('Prac2_instru2_text3.started', Prac2_instru2_text3.tStartRefresh)
    prac2_repeat.addData('Prac2_instru2_text3.stopped', Prac2_instru2_text3.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    prac2_repeat.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        prac2_repeat.addData('key_resp_5.rt', key_resp_5.rt)
    prac2_repeat.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    prac2_repeat.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Prac2_instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Prac2_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Prac2_startComponents = [Parc2_start_text, key_resp_4]
    for thisComponent in Prac2_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac2_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac2_start"-------
    while continueRoutine:
        # get current time
        t = Prac2_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac2_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Parc2_start_text* updates
        if Parc2_start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Parc2_start_text.frameNStart = frameN  # exact frame index
            Parc2_start_text.tStart = t  # local t and not account for scr refresh
            Parc2_start_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Parc2_start_text, 'tStartRefresh')  # time at next scr refresh
            Parc2_start_text.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac2_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac2_start"-------
    for thisComponent in Prac2_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac2_repeat.addData('Parc2_start_text.started', Parc2_start_text.tStartRefresh)
    prac2_repeat.addData('Parc2_start_text.stopped', Parc2_start_text.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    prac2_repeat.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        prac2_repeat.addData('key_resp_4.rt', key_resp_4.rt)
    prac2_repeat.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    prac2_repeat.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Prac2_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac2_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(prac_file),
        seed=None, name='prac2_trials')
    thisExp.addLoop(prac2_trials)  # add the loop to the experiment
    thisPrac2_trial = prac2_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac2_trial.rgb)
    if thisPrac2_trial != None:
        for paramName in thisPrac2_trial:
            exec('{} = thisPrac2_trial[paramName]'.format(paramName))
    
    for thisPrac2_trial in prac2_trials:
        currentLoop = prac2_trials
        # abbreviate parameter names if possible (e.g. rgb = thisPrac2_trial.rgb)
        if thisPrac2_trial != None:
            for paramName in thisPrac2_trial:
                exec('{} = thisPrac2_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Prac2"-------
        continueRoutine = True
        # update component parameters for each repeat
        Prac2_stim.setImage(pink_stim)
        Prac2_resp.keys = []
        Prac2_resp.rt = []
        _Prac2_resp_allKeys = []
        # keep track of which components have finished
        Prac2Components = [Prac2_fix, Prac2_stim, Prac2_resp]
        for thisComponent in Prac2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Prac2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Prac2"-------
        while continueRoutine:
            # get current time
            t = Prac2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Prac2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Prac2_fix* updates
            if Prac2_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Prac2_fix.frameNStart = frameN  # exact frame index
                Prac2_fix.tStart = t  # local t and not account for scr refresh
                Prac2_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac2_fix, 'tStartRefresh')  # time at next scr refresh
                Prac2_fix.setAutoDraw(True)
            if Prac2_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac2_fix.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac2_fix.tStop = t  # not accounting for scr refresh
                    Prac2_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac2_fix, 'tStopRefresh')  # time at next scr refresh
                    Prac2_fix.setAutoDraw(False)
            
            # *Prac2_stim* updates
            if Prac2_stim.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
                # keep track of start time/frame for later
                Prac2_stim.frameNStart = frameN  # exact frame index
                Prac2_stim.tStart = t  # local t and not account for scr refresh
                Prac2_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac2_stim, 'tStartRefresh')  # time at next scr refresh
                Prac2_stim.setAutoDraw(True)
            if Prac2_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac2_stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac2_stim.tStop = t  # not accounting for scr refresh
                    Prac2_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac2_stim, 'tStopRefresh')  # time at next scr refresh
                    Prac2_stim.setAutoDraw(False)
            
            # *Prac2_resp* updates
            waitOnFlip = False
            if Prac2_resp.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
                # keep track of start time/frame for later
                Prac2_resp.frameNStart = frameN  # exact frame index
                Prac2_resp.tStart = t  # local t and not account for scr refresh
                Prac2_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac2_resp, 'tStartRefresh')  # time at next scr refresh
                Prac2_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Prac2_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Prac2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Prac2_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac2_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac2_resp.tStop = t  # not accounting for scr refresh
                    Prac2_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac2_resp, 'tStopRefresh')  # time at next scr refresh
                    Prac2_resp.status = FINISHED
            if Prac2_resp.status == STARTED and not waitOnFlip:
                theseKeys = Prac2_resp.getKeys(keyList=['lctrl', 'return'], waitRelease=False)
                _Prac2_resp_allKeys.extend(theseKeys)
                if len(_Prac2_resp_allKeys):
                    Prac2_resp.keys = _Prac2_resp_allKeys[-1].name  # just the last key pressed
                    Prac2_resp.rt = _Prac2_resp_allKeys[-1].rt
                    # was this correct?
                    if (Prac2_resp.keys == str(corrAns)) or (Prac2_resp.keys == corrAns):
                        Prac2_resp.corr = 1
                    else:
                        Prac2_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Prac2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Prac2"-------
        for thisComponent in Prac2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac2_list.append(Prac2_resp.corr)
        
        prac2_trials.addData('prac2_list', prac2_list)
        
        prac2_trials.addData('Prac2_fix.started', Prac2_fix.tStartRefresh)
        prac2_trials.addData('Prac2_fix.stopped', Prac2_fix.tStopRefresh)
        prac2_trials.addData('Prac2_stim.started', Prac2_stim.tStartRefresh)
        prac2_trials.addData('Prac2_stim.stopped', Prac2_stim.tStopRefresh)
        # check responses
        if Prac2_resp.keys in ['', [], None]:  # No response was made
            Prac2_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               Prac2_resp.corr = 1;  # correct non-response
            else:
               Prac2_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac2_trials (TrialHandler)
        prac2_trials.addData('Prac2_resp.keys',Prac2_resp.keys)
        prac2_trials.addData('Prac2_resp.corr', Prac2_resp.corr)
        if Prac2_resp.keys != None:  # we had a response
            prac2_trials.addData('Prac2_resp.rt', Prac2_resp.rt)
        prac2_trials.addData('Prac2_resp.started', Prac2_resp.tStartRefresh)
        prac2_trials.addData('Prac2_resp.stopped', Prac2_resp.tStopRefresh)
        # the Routine "Prac2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac2_trials'
    
    
    # ------Prepare to start Routine "Prac2_over"-------
    continueRoutine = True
    # update component parameters for each repeat
       
    if sum(prac2_list[-4:]) > 2 :
        pic = 'well_done.jpg'
        msg = 'Træningen er slut. Godt klaret!'
        
    if not sum(prac2_list[-4:]) > 2 :
        pic = 'try_again.jpg'
        msg = 'Lad os træne en gang mere.'
        
    if sum(prac2_list[-4:]) > 2 :
        prac2_repeat.finished = True
        
    if len(prac2_list) > 10 and sum(prac2_list[-4:]) < 3 :
        pic = 'well_done.jpg'
        msg = 'Træningen er slut. Godt klaret!'
    Prac2_over_pic.setImage(pic)
    Prac2_over_text.setText(msg)
    Prac2_over_cont.keys = []
    Prac2_over_cont.rt = []
    _Prac2_over_cont_allKeys = []
    # keep track of which components have finished
    Prac2_overComponents = [Prac2_over_pic, Prac2_over_text, Prac2_over_cont]
    for thisComponent in Prac2_overComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac2_overClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac2_over"-------
    while continueRoutine:
        # get current time
        t = Prac2_overClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac2_overClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac2_over_pic* updates
        if Prac2_over_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_over_pic.frameNStart = frameN  # exact frame index
            Prac2_over_pic.tStart = t  # local t and not account for scr refresh
            Prac2_over_pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_over_pic, 'tStartRefresh')  # time at next scr refresh
            Prac2_over_pic.setAutoDraw(True)
        
        # *Prac2_over_text* updates
        if Prac2_over_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_over_text.frameNStart = frameN  # exact frame index
            Prac2_over_text.tStart = t  # local t and not account for scr refresh
            Prac2_over_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_over_text, 'tStartRefresh')  # time at next scr refresh
            Prac2_over_text.setAutoDraw(True)
        
        # *Prac2_over_cont* updates
        waitOnFlip = False
        if Prac2_over_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac2_over_cont.frameNStart = frameN  # exact frame index
            Prac2_over_cont.tStart = t  # local t and not account for scr refresh
            Prac2_over_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac2_over_cont, 'tStartRefresh')  # time at next scr refresh
            Prac2_over_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac2_over_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac2_over_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prac2_over_cont.status == STARTED and not waitOnFlip:
            theseKeys = Prac2_over_cont.getKeys(keyList=None, waitRelease=False)
            _Prac2_over_cont_allKeys.extend(theseKeys)
            if len(_Prac2_over_cont_allKeys):
                Prac2_over_cont.keys = _Prac2_over_cont_allKeys[-1].name  # just the last key pressed
                Prac2_over_cont.rt = _Prac2_over_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac2_overComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac2_over"-------
    for thisComponent in Prac2_overComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac2_repeat.addData('Prac2_over_pic.started', Prac2_over_pic.tStartRefresh)
    prac2_repeat.addData('Prac2_over_pic.stopped', Prac2_over_pic.tStopRefresh)
    prac2_repeat.addData('Prac2_over_text.started', Prac2_over_text.tStartRefresh)
    prac2_repeat.addData('Prac2_over_text.stopped', Prac2_over_text.tStopRefresh)
    # check responses
    if Prac2_over_cont.keys in ['', [], None]:  # No response was made
        Prac2_over_cont.keys = None
    prac2_repeat.addData('Prac2_over_cont.keys',Prac2_over_cont.keys)
    if Prac2_over_cont.keys != None:  # we had a response
        prac2_repeat.addData('Prac2_over_cont.rt', Prac2_over_cont.rt)
    prac2_repeat.addData('Prac2_over_cont.started', Prac2_over_cont.tStartRefresh)
    prac2_repeat.addData('Prac2_over_cont.stopped', Prac2_over_cont.tStopRefresh)
    # the Routine "Prac2_over" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac2_repeat'


# ------Prepare to start Routine "Task2_instr"-------
continueRoutine = True
# update component parameters for each repeat
Task2_instr_cont.keys = []
Task2_instr_cont.rt = []
_Task2_instr_cont_allKeys = []
# keep track of which components have finished
Task2_instrComponents = [Task2_instr_text, Task2_instr_cont]
for thisComponent in Task2_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Task2_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Task2_instr"-------
while continueRoutine:
    # get current time
    t = Task2_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Task2_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task2_instr_text* updates
    if Task2_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task2_instr_text.frameNStart = frameN  # exact frame index
        Task2_instr_text.tStart = t  # local t and not account for scr refresh
        Task2_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task2_instr_text, 'tStartRefresh')  # time at next scr refresh
        Task2_instr_text.setAutoDraw(True)
    
    # *Task2_instr_cont* updates
    waitOnFlip = False
    if Task2_instr_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task2_instr_cont.frameNStart = frameN  # exact frame index
        Task2_instr_cont.tStart = t  # local t and not account for scr refresh
        Task2_instr_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task2_instr_cont, 'tStartRefresh')  # time at next scr refresh
        Task2_instr_cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Task2_instr_cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Task2_instr_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Task2_instr_cont.status == STARTED and not waitOnFlip:
        theseKeys = Task2_instr_cont.getKeys(keyList=None, waitRelease=False)
        _Task2_instr_cont_allKeys.extend(theseKeys)
        if len(_Task2_instr_cont_allKeys):
            Task2_instr_cont.keys = _Task2_instr_cont_allKeys[-1].name  # just the last key pressed
            Task2_instr_cont.rt = _Task2_instr_cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Task2_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task2_instr"-------
for thisComponent in Task2_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Task2_instr_text.started', Task2_instr_text.tStartRefresh)
thisExp.addData('Task2_instr_text.stopped', Task2_instr_text.tStopRefresh)
# check responses
if Task2_instr_cont.keys in ['', [], None]:  # No response was made
    Task2_instr_cont.keys = None
thisExp.addData('Task2_instr_cont.keys',Task2_instr_cont.keys)
if Task2_instr_cont.keys != None:  # we had a response
    thisExp.addData('Task2_instr_cont.rt', Task2_instr_cont.rt)
thisExp.addData('Task2_instr_cont.started', Task2_instr_cont.tStartRefresh)
thisExp.addData('Task2_instr_cont.stopped', Task2_instr_cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "Task2_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
task2_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pink_task.xlsx'),
    seed=None, name='task2_trials')
thisExp.addLoop(task2_trials)  # add the loop to the experiment
thisTask2_trial = task2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask2_trial.rgb)
if thisTask2_trial != None:
    for paramName in thisTask2_trial:
        exec('{} = thisTask2_trial[paramName]'.format(paramName))

for thisTask2_trial in task2_trials:
    currentLoop = task2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTask2_trial.rgb)
    if thisTask2_trial != None:
        for paramName in thisTask2_trial:
            exec('{} = thisTask2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Task2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Task2_stim.setImage(pink_stim)
    Task2_resp.keys = []
    Task2_resp.rt = []
    _Task2_resp_allKeys = []
    # keep track of which components have finished
    Task2Components = [Task2_fix, Task2_stim, Task2_resp]
    for thisComponent in Task2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Task2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Task2"-------
    while continueRoutine:
        # get current time
        t = Task2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Task2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task2_fix* updates
        if Task2_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task2_fix.frameNStart = frameN  # exact frame index
            Task2_fix.tStart = t  # local t and not account for scr refresh
            Task2_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task2_fix, 'tStartRefresh')  # time at next scr refresh
            Task2_fix.setAutoDraw(True)
        if Task2_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task2_fix.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                Task2_fix.tStop = t  # not accounting for scr refresh
                Task2_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task2_fix, 'tStopRefresh')  # time at next scr refresh
                Task2_fix.setAutoDraw(False)
        
        # *Task2_stim* updates
        if Task2_stim.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
            # keep track of start time/frame for later
            Task2_stim.frameNStart = frameN  # exact frame index
            Task2_stim.tStart = t  # local t and not account for scr refresh
            Task2_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task2_stim, 'tStartRefresh')  # time at next scr refresh
            Task2_stim.setAutoDraw(True)
        if Task2_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task2_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Task2_stim.tStop = t  # not accounting for scr refresh
                Task2_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task2_stim, 'tStopRefresh')  # time at next scr refresh
                Task2_stim.setAutoDraw(False)
        
        # *Task2_resp* updates
        waitOnFlip = False
        if Task2_resp.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
            # keep track of start time/frame for later
            Task2_resp.frameNStart = frameN  # exact frame index
            Task2_resp.tStart = t  # local t and not account for scr refresh
            Task2_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task2_resp, 'tStartRefresh')  # time at next scr refresh
            Task2_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Task2_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Task2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Task2_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task2_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Task2_resp.tStop = t  # not accounting for scr refresh
                Task2_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task2_resp, 'tStopRefresh')  # time at next scr refresh
                Task2_resp.status = FINISHED
        if Task2_resp.status == STARTED and not waitOnFlip:
            theseKeys = Task2_resp.getKeys(keyList=['lctrl', 'return'], waitRelease=False)
            _Task2_resp_allKeys.extend(theseKeys)
            if len(_Task2_resp_allKeys):
                Task2_resp.keys = _Task2_resp_allKeys[-1].name  # just the last key pressed
                Task2_resp.rt = _Task2_resp_allKeys[-1].rt
                # was this correct?
                if (Task2_resp.keys == str(corrAns)) or (Task2_resp.keys == corrAns):
                    Task2_resp.corr = 1
                else:
                    Task2_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Task2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Task2"-------
    for thisComponent in Task2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task2_trials.addData('Task2_fix.started', Task2_fix.tStartRefresh)
    task2_trials.addData('Task2_fix.stopped', Task2_fix.tStopRefresh)
    task2_trials.addData('Task2_stim.started', Task2_stim.tStartRefresh)
    task2_trials.addData('Task2_stim.stopped', Task2_stim.tStopRefresh)
    # check responses
    if Task2_resp.keys in ['', [], None]:  # No response was made
        Task2_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           Task2_resp.corr = 1;  # correct non-response
        else:
           Task2_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for task2_trials (TrialHandler)
    task2_trials.addData('Task2_resp.keys',Task2_resp.keys)
    task2_trials.addData('Task2_resp.corr', Task2_resp.corr)
    if Task2_resp.keys != None:  # we had a response
        task2_trials.addData('Task2_resp.rt', Task2_resp.rt)
    task2_trials.addData('Task2_resp.started', Task2_resp.tStartRefresh)
    task2_trials.addData('Task2_resp.stopped', Task2_resp.tStopRefresh)
    # the Routine "Task2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task2_trials'


# ------Prepare to start Routine "Task2_end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Task2_endComponents = [text_3, key_resp_6]
for thisComponent in Task2_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Task2_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Task2_end"-------
while continueRoutine:
    # get current time
    t = Task2_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Task2_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Task2_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task2_end"-------
for thisComponent in Task2_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "Task2_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac3_repeat = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mix_prac_all.xlsx'),
    seed=None, name='prac3_repeat')
thisExp.addLoop(prac3_repeat)  # add the loop to the experiment
thisPrac3_repeat = prac3_repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac3_repeat.rgb)
if thisPrac3_repeat != None:
    for paramName in thisPrac3_repeat:
        exec('{} = thisPrac3_repeat[paramName]'.format(paramName))

for thisPrac3_repeat in prac3_repeat:
    currentLoop = prac3_repeat
    # abbreviate parameter names if possible (e.g. rgb = thisPrac3_repeat.rgb)
    if thisPrac3_repeat != None:
        for paramName in thisPrac3_repeat:
            exec('{} = thisPrac3_repeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Prac3_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    Prac3_cont.keys = []
    Prac3_cont.rt = []
    _Prac3_cont_allKeys = []
    # keep track of which components have finished
    Prac3_instrComponents = [Pract3_instr_text, Pract3_instr_pic1, Prac3_pic2, Prac3_cont, text_5, text_6]
    for thisComponent in Prac3_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac3_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac3_instr"-------
    while continueRoutine:
        # get current time
        t = Prac3_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac3_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pract3_instr_text* updates
        if Pract3_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pract3_instr_text.frameNStart = frameN  # exact frame index
            Pract3_instr_text.tStart = t  # local t and not account for scr refresh
            Pract3_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pract3_instr_text, 'tStartRefresh')  # time at next scr refresh
            Pract3_instr_text.setAutoDraw(True)
        
        # *Pract3_instr_pic1* updates
        if Pract3_instr_pic1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pract3_instr_pic1.frameNStart = frameN  # exact frame index
            Pract3_instr_pic1.tStart = t  # local t and not account for scr refresh
            Pract3_instr_pic1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pract3_instr_pic1, 'tStartRefresh')  # time at next scr refresh
            Pract3_instr_pic1.setAutoDraw(True)
        
        # *Prac3_pic2* updates
        if Prac3_pic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac3_pic2.frameNStart = frameN  # exact frame index
            Prac3_pic2.tStart = t  # local t and not account for scr refresh
            Prac3_pic2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac3_pic2, 'tStartRefresh')  # time at next scr refresh
            Prac3_pic2.setAutoDraw(True)
        
        # *Prac3_cont* updates
        waitOnFlip = False
        if Prac3_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac3_cont.frameNStart = frameN  # exact frame index
            Prac3_cont.tStart = t  # local t and not account for scr refresh
            Prac3_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac3_cont, 'tStartRefresh')  # time at next scr refresh
            Prac3_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac3_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac3_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prac3_cont.status == STARTED and not waitOnFlip:
            theseKeys = Prac3_cont.getKeys(keyList=None, waitRelease=False)
            _Prac3_cont_allKeys.extend(theseKeys)
            if len(_Prac3_cont_allKeys):
                Prac3_cont.keys = _Prac3_cont_allKeys[-1].name  # just the last key pressed
                Prac3_cont.rt = _Prac3_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac3_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac3_instr"-------
    for thisComponent in Prac3_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac3_repeat.addData('Pract3_instr_text.started', Pract3_instr_text.tStartRefresh)
    prac3_repeat.addData('Pract3_instr_text.stopped', Pract3_instr_text.tStopRefresh)
    prac3_repeat.addData('Pract3_instr_pic1.started', Pract3_instr_pic1.tStartRefresh)
    prac3_repeat.addData('Pract3_instr_pic1.stopped', Pract3_instr_pic1.tStopRefresh)
    prac3_repeat.addData('Prac3_pic2.started', Prac3_pic2.tStartRefresh)
    prac3_repeat.addData('Prac3_pic2.stopped', Prac3_pic2.tStopRefresh)
    # check responses
    if Prac3_cont.keys in ['', [], None]:  # No response was made
        Prac3_cont.keys = None
    prac3_repeat.addData('Prac3_cont.keys',Prac3_cont.keys)
    if Prac3_cont.keys != None:  # we had a response
        prac3_repeat.addData('Prac3_cont.rt', Prac3_cont.rt)
    prac3_repeat.addData('Prac3_cont.started', Prac3_cont.tStartRefresh)
    prac3_repeat.addData('Prac3_cont.stopped', Prac3_cont.tStopRefresh)
    prac3_repeat.addData('text_5.started', text_5.tStartRefresh)
    prac3_repeat.addData('text_5.stopped', text_5.tStopRefresh)
    prac3_repeat.addData('text_6.started', text_6.tStartRefresh)
    prac3_repeat.addData('text_6.stopped', text_6.tStopRefresh)
    # the Routine "Prac3_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Prac3_instr2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    Prac3_instr2Components = [text_4, key_resp_7]
    for thisComponent in Prac3_instr2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac3_instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac3_instr2"-------
    while continueRoutine:
        # get current time
        t = Prac3_instr2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac3_instr2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=None, waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac3_instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac3_instr2"-------
    for thisComponent in Prac3_instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac3_repeat.addData('text_4.started', text_4.tStartRefresh)
    prac3_repeat.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    prac3_repeat.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        prac3_repeat.addData('key_resp_7.rt', key_resp_7.rt)
    prac3_repeat.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    prac3_repeat.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "Prac3_instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac3_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(prac_file),
        seed=None, name='prac3_trials')
    thisExp.addLoop(prac3_trials)  # add the loop to the experiment
    thisPrac3_trial = prac3_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac3_trial.rgb)
    if thisPrac3_trial != None:
        for paramName in thisPrac3_trial:
            exec('{} = thisPrac3_trial[paramName]'.format(paramName))
    
    for thisPrac3_trial in prac3_trials:
        currentLoop = prac3_trials
        # abbreviate parameter names if possible (e.g. rgb = thisPrac3_trial.rgb)
        if thisPrac3_trial != None:
            for paramName in thisPrac3_trial:
                exec('{} = thisPrac3_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Prac3"-------
        continueRoutine = True
        # update component parameters for each repeat
        Prac3_pic.setImage(mix_stim)
        Prac3_resp.keys = []
        Prac3_resp.rt = []
        _Prac3_resp_allKeys = []
        # keep track of which components have finished
        Prac3Components = [Prac3_fix, Prac3_pic, Prac3_resp]
        for thisComponent in Prac3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Prac3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Prac3"-------
        while continueRoutine:
            # get current time
            t = Prac3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Prac3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Prac3_fix* updates
            if Prac3_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Prac3_fix.frameNStart = frameN  # exact frame index
                Prac3_fix.tStart = t  # local t and not account for scr refresh
                Prac3_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac3_fix, 'tStartRefresh')  # time at next scr refresh
                Prac3_fix.setAutoDraw(True)
            if Prac3_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac3_fix.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac3_fix.tStop = t  # not accounting for scr refresh
                    Prac3_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac3_fix, 'tStopRefresh')  # time at next scr refresh
                    Prac3_fix.setAutoDraw(False)
            
            # *Prac3_pic* updates
            if Prac3_pic.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
                # keep track of start time/frame for later
                Prac3_pic.frameNStart = frameN  # exact frame index
                Prac3_pic.tStart = t  # local t and not account for scr refresh
                Prac3_pic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac3_pic, 'tStartRefresh')  # time at next scr refresh
                Prac3_pic.setAutoDraw(True)
            if Prac3_pic.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac3_pic.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac3_pic.tStop = t  # not accounting for scr refresh
                    Prac3_pic.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac3_pic, 'tStopRefresh')  # time at next scr refresh
                    Prac3_pic.setAutoDraw(False)
            
            # *Prac3_resp* updates
            waitOnFlip = False
            if Prac3_resp.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
                # keep track of start time/frame for later
                Prac3_resp.frameNStart = frameN  # exact frame index
                Prac3_resp.tStart = t  # local t and not account for scr refresh
                Prac3_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prac3_resp, 'tStartRefresh')  # time at next scr refresh
                Prac3_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Prac3_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Prac3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Prac3_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Prac3_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Prac3_resp.tStop = t  # not accounting for scr refresh
                    Prac3_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prac3_resp, 'tStopRefresh')  # time at next scr refresh
                    Prac3_resp.status = FINISHED
            if Prac3_resp.status == STARTED and not waitOnFlip:
                theseKeys = Prac3_resp.getKeys(keyList=['lctrl', 'return'], waitRelease=False)
                _Prac3_resp_allKeys.extend(theseKeys)
                if len(_Prac3_resp_allKeys):
                    Prac3_resp.keys = _Prac3_resp_allKeys[-1].name  # just the last key pressed
                    Prac3_resp.rt = _Prac3_resp_allKeys[-1].rt
                    # was this correct?
                    if (Prac3_resp.keys == str(corrAns)) or (Prac3_resp.keys == corrAns):
                        Prac3_resp.corr = 1
                    else:
                        Prac3_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Prac3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Prac3"-------
        for thisComponent in Prac3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac3_list.append(Prac3_resp.corr)
        
        prac3_trials.addData('prac3_list', prac3_list)
        
        prac3_trials.addData('Prac3_fix.started', Prac3_fix.tStartRefresh)
        prac3_trials.addData('Prac3_fix.stopped', Prac3_fix.tStopRefresh)
        prac3_trials.addData('Prac3_pic.started', Prac3_pic.tStartRefresh)
        prac3_trials.addData('Prac3_pic.stopped', Prac3_pic.tStopRefresh)
        # check responses
        if Prac3_resp.keys in ['', [], None]:  # No response was made
            Prac3_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               Prac3_resp.corr = 1;  # correct non-response
            else:
               Prac3_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac3_trials (TrialHandler)
        prac3_trials.addData('Prac3_resp.keys',Prac3_resp.keys)
        prac3_trials.addData('Prac3_resp.corr', Prac3_resp.corr)
        if Prac3_resp.keys != None:  # we had a response
            prac3_trials.addData('Prac3_resp.rt', Prac3_resp.rt)
        prac3_trials.addData('Prac3_resp.started', Prac3_resp.tStartRefresh)
        prac3_trials.addData('Prac3_resp.stopped', Prac3_resp.tStopRefresh)
        # the Routine "Prac3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac3_trials'
    
    
    # ------Prepare to start Routine "Prac3_over"-------
    continueRoutine = True
    # update component parameters for each repeat
       
    if sum(prac3_list[-8:]) > 5 :
        pic = 'well_done.jpg'
        msg = 'Træningen er slut. Godt klaret!'
        
    if not sum(prac3_list[-8:]) > 5 :
        pic = 'try_again.jpg'
        msg = 'Lad os træne en gang mere.'
        
    if sum(prac3_list[-8:]) > 5 :
        prac3_repeat.finished = True
        
    if len(prac3_list) > 20 and sum(prac3_list[-8:]) < 5 :
        pic = 'well_done.jpg'
        msg = 'Træningen er slut. Godt klaret!'
    Prac3_over_pic.setImage(pic)
    Prac3_over_text.setText(msg)
    Prac3_over_cont.keys = []
    Prac3_over_cont.rt = []
    _Prac3_over_cont_allKeys = []
    # keep track of which components have finished
    Prac3_overComponents = [Prac3_over_pic, Prac3_over_text, Prac3_over_cont]
    for thisComponent in Prac3_overComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac3_overClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac3_over"-------
    while continueRoutine:
        # get current time
        t = Prac3_overClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac3_overClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac3_over_pic* updates
        if Prac3_over_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac3_over_pic.frameNStart = frameN  # exact frame index
            Prac3_over_pic.tStart = t  # local t and not account for scr refresh
            Prac3_over_pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac3_over_pic, 'tStartRefresh')  # time at next scr refresh
            Prac3_over_pic.setAutoDraw(True)
        
        # *Prac3_over_text* updates
        if Prac3_over_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac3_over_text.frameNStart = frameN  # exact frame index
            Prac3_over_text.tStart = t  # local t and not account for scr refresh
            Prac3_over_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac3_over_text, 'tStartRefresh')  # time at next scr refresh
            Prac3_over_text.setAutoDraw(True)
        
        # *Prac3_over_cont* updates
        waitOnFlip = False
        if Prac3_over_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Prac3_over_cont.frameNStart = frameN  # exact frame index
            Prac3_over_cont.tStart = t  # local t and not account for scr refresh
            Prac3_over_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac3_over_cont, 'tStartRefresh')  # time at next scr refresh
            Prac3_over_cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac3_over_cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac3_over_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Prac3_over_cont.status == STARTED and not waitOnFlip:
            theseKeys = Prac3_over_cont.getKeys(keyList=None, waitRelease=False)
            _Prac3_over_cont_allKeys.extend(theseKeys)
            if len(_Prac3_over_cont_allKeys):
                Prac3_over_cont.keys = _Prac3_over_cont_allKeys[-1].name  # just the last key pressed
                Prac3_over_cont.rt = _Prac3_over_cont_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac3_overComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac3_over"-------
    for thisComponent in Prac3_overComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac3_repeat.addData('Prac3_over_pic.started', Prac3_over_pic.tStartRefresh)
    prac3_repeat.addData('Prac3_over_pic.stopped', Prac3_over_pic.tStopRefresh)
    prac3_repeat.addData('Prac3_over_text.started', Prac3_over_text.tStartRefresh)
    prac3_repeat.addData('Prac3_over_text.stopped', Prac3_over_text.tStopRefresh)
    # check responses
    if Prac3_over_cont.keys in ['', [], None]:  # No response was made
        Prac3_over_cont.keys = None
    prac3_repeat.addData('Prac3_over_cont.keys',Prac3_over_cont.keys)
    if Prac3_over_cont.keys != None:  # we had a response
        prac3_repeat.addData('Prac3_over_cont.rt', Prac3_over_cont.rt)
    prac3_repeat.addData('Prac3_over_cont.started', Prac3_over_cont.tStartRefresh)
    prac3_repeat.addData('Prac3_over_cont.stopped', Prac3_over_cont.tStopRefresh)
    # the Routine "Prac3_over" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac3_repeat'


# ------Prepare to start Routine "Task3_instr"-------
continueRoutine = True
# update component parameters for each repeat
Task3_instr_cont.keys = []
Task3_instr_cont.rt = []
_Task3_instr_cont_allKeys = []
# keep track of which components have finished
Task3_instrComponents = [Task3_instr_text, Task3_instr_cont]
for thisComponent in Task3_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Task3_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Task3_instr"-------
while continueRoutine:
    # get current time
    t = Task3_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Task3_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task3_instr_text* updates
    if Task3_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task3_instr_text.frameNStart = frameN  # exact frame index
        Task3_instr_text.tStart = t  # local t and not account for scr refresh
        Task3_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task3_instr_text, 'tStartRefresh')  # time at next scr refresh
        Task3_instr_text.setAutoDraw(True)
    
    # *Task3_instr_cont* updates
    waitOnFlip = False
    if Task3_instr_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task3_instr_cont.frameNStart = frameN  # exact frame index
        Task3_instr_cont.tStart = t  # local t and not account for scr refresh
        Task3_instr_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task3_instr_cont, 'tStartRefresh')  # time at next scr refresh
        Task3_instr_cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Task3_instr_cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Task3_instr_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Task3_instr_cont.status == STARTED and not waitOnFlip:
        theseKeys = Task3_instr_cont.getKeys(keyList=None, waitRelease=False)
        _Task3_instr_cont_allKeys.extend(theseKeys)
        if len(_Task3_instr_cont_allKeys):
            Task3_instr_cont.keys = _Task3_instr_cont_allKeys[-1].name  # just the last key pressed
            Task3_instr_cont.rt = _Task3_instr_cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Task3_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task3_instr"-------
for thisComponent in Task3_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Task3_instr_text.started', Task3_instr_text.tStartRefresh)
thisExp.addData('Task3_instr_text.stopped', Task3_instr_text.tStopRefresh)
# check responses
if Task3_instr_cont.keys in ['', [], None]:  # No response was made
    Task3_instr_cont.keys = None
thisExp.addData('Task3_instr_cont.keys',Task3_instr_cont.keys)
if Task3_instr_cont.keys != None:  # we had a response
    thisExp.addData('Task3_instr_cont.rt', Task3_instr_cont.rt)
thisExp.addData('Task3_instr_cont.started', Task3_instr_cont.tStartRefresh)
thisExp.addData('Task3_instr_cont.stopped', Task3_instr_cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "Task3_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
task3_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mix_task.xlsx'),
    seed=None, name='task3_trials')
thisExp.addLoop(task3_trials)  # add the loop to the experiment
thisTask3_trial = task3_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask3_trial.rgb)
if thisTask3_trial != None:
    for paramName in thisTask3_trial:
        exec('{} = thisTask3_trial[paramName]'.format(paramName))

for thisTask3_trial in task3_trials:
    currentLoop = task3_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTask3_trial.rgb)
    if thisTask3_trial != None:
        for paramName in thisTask3_trial:
            exec('{} = thisTask3_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Task3"-------
    continueRoutine = True
    # update component parameters for each repeat
    Task3_stim.setImage(mix_stim)
    Task3_resp.keys = []
    Task3_resp.rt = []
    _Task3_resp_allKeys = []
    # keep track of which components have finished
    Task3Components = [Task3_fix, Task3_stim, Task3_resp]
    for thisComponent in Task3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Task3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Task3"-------
    while continueRoutine:
        # get current time
        t = Task3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Task3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Task3_fix* updates
        if Task3_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task3_fix.frameNStart = frameN  # exact frame index
            Task3_fix.tStart = t  # local t and not account for scr refresh
            Task3_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task3_fix, 'tStartRefresh')  # time at next scr refresh
            Task3_fix.setAutoDraw(True)
        if Task3_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task3_fix.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                Task3_fix.tStop = t  # not accounting for scr refresh
                Task3_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task3_fix, 'tStopRefresh')  # time at next scr refresh
                Task3_fix.setAutoDraw(False)
        
        # *Task3_stim* updates
        if Task3_stim.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
            # keep track of start time/frame for later
            Task3_stim.frameNStart = frameN  # exact frame index
            Task3_stim.tStart = t  # local t and not account for scr refresh
            Task3_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task3_stim, 'tStartRefresh')  # time at next scr refresh
            Task3_stim.setAutoDraw(True)
        if Task3_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task3_stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Task3_stim.tStop = t  # not accounting for scr refresh
                Task3_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task3_stim, 'tStopRefresh')  # time at next scr refresh
                Task3_stim.setAutoDraw(False)
        
        # *Task3_resp* updates
        waitOnFlip = False
        if Task3_resp.status == NOT_STARTED and tThisFlip >= jitter-frameTolerance:
            # keep track of start time/frame for later
            Task3_resp.frameNStart = frameN  # exact frame index
            Task3_resp.tStart = t  # local t and not account for scr refresh
            Task3_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task3_resp, 'tStartRefresh')  # time at next scr refresh
            Task3_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Task3_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Task3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Task3_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Task3_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Task3_resp.tStop = t  # not accounting for scr refresh
                Task3_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Task3_resp, 'tStopRefresh')  # time at next scr refresh
                Task3_resp.status = FINISHED
        if Task3_resp.status == STARTED and not waitOnFlip:
            theseKeys = Task3_resp.getKeys(keyList=['lctrl', 'return'], waitRelease=False)
            _Task3_resp_allKeys.extend(theseKeys)
            if len(_Task3_resp_allKeys):
                Task3_resp.keys = _Task3_resp_allKeys[-1].name  # just the last key pressed
                Task3_resp.rt = _Task3_resp_allKeys[-1].rt
                # was this correct?
                if (Task3_resp.keys == str(corrAns)) or (Task3_resp.keys == corrAns):
                    Task3_resp.corr = 1
                else:
                    Task3_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Task3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Task3"-------
    for thisComponent in Task3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task3_trials.addData('Task3_fix.started', Task3_fix.tStartRefresh)
    task3_trials.addData('Task3_fix.stopped', Task3_fix.tStopRefresh)
    task3_trials.addData('Task3_stim.started', Task3_stim.tStartRefresh)
    task3_trials.addData('Task3_stim.stopped', Task3_stim.tStopRefresh)
    # check responses
    if Task3_resp.keys in ['', [], None]:  # No response was made
        Task3_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           Task3_resp.corr = 1;  # correct non-response
        else:
           Task3_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for task3_trials (TrialHandler)
    task3_trials.addData('Task3_resp.keys',Task3_resp.keys)
    task3_trials.addData('Task3_resp.corr', Task3_resp.corr)
    if Task3_resp.keys != None:  # we had a response
        task3_trials.addData('Task3_resp.rt', Task3_resp.rt)
    task3_trials.addData('Task3_resp.started', Task3_resp.tStartRefresh)
    task3_trials.addData('Task3_resp.stopped', Task3_resp.tStopRefresh)
    # the Routine "Task3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task3_trials'


# ------Prepare to start Routine "finished"-------
continueRoutine = True
# update component parameters for each repeat
tak_cont.keys = []
tak_cont.rt = []
_tak_cont_allKeys = []
# keep track of which components have finished
finishedComponents = [Tak_pic, tak_cont]
for thisComponent in finishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finished"-------
while continueRoutine:
    # get current time
    t = finishedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Tak_pic* updates
    if Tak_pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Tak_pic.frameNStart = frameN  # exact frame index
        Tak_pic.tStart = t  # local t and not account for scr refresh
        Tak_pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Tak_pic, 'tStartRefresh')  # time at next scr refresh
        Tak_pic.setAutoDraw(True)
    
    # *tak_cont* updates
    waitOnFlip = False
    if tak_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tak_cont.frameNStart = frameN  # exact frame index
        tak_cont.tStart = t  # local t and not account for scr refresh
        tak_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tak_cont, 'tStartRefresh')  # time at next scr refresh
        tak_cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(tak_cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(tak_cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if tak_cont.status == STARTED and not waitOnFlip:
        theseKeys = tak_cont.getKeys(keyList=None, waitRelease=False)
        _tak_cont_allKeys.extend(theseKeys)
        if len(_tak_cont_allKeys):
            tak_cont.keys = _tak_cont_allKeys[-1].name  # just the last key pressed
            tak_cont.rt = _tak_cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finished"-------
for thisComponent in finishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Tak_pic.started', Tak_pic.tStartRefresh)
thisExp.addData('Tak_pic.stopped', Tak_pic.tStopRefresh)
# check responses
if tak_cont.keys in ['', [], None]:  # No response was made
    tak_cont.keys = None
thisExp.addData('tak_cont.keys',tak_cont.keys)
if tak_cont.keys != None:  # we had a response
    thisExp.addData('tak_cont.rt', tak_cont.rt)
thisExp.addData('tak_cont.started', tak_cont.tStartRefresh)
thisExp.addData('tak_cont.stopped', tak_cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "finished" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
