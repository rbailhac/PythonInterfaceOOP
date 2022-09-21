#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
# -*- coding: utf-8 -*-

# Copyright 2019-2020 CERN and copyright holders of ALICE O2.
# See https://alice-o2.web.cern.ch/copyright for details of the copyright holders.
# All rights not expressly granted are reserved.
#
# This software is distributed under the terms of the GNU General Public
# License v3 (GPL Version 3), copied verbatim in the file "COPYING".
#
# In applying this license CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

# \Author: ionut.cristian.arsene@cern.ch
# \Interface:  cevat.batuhan.tolon@cern.ch

# Orginal Task: https://github.com/AliceO2Group/O2Physics/blob/master/PWGDQ/Tasks/tableReader.cxx

import json
import sys
import logging
import logging.config
import os
from extramodules.configGetter import configGetter
from extramodules.monitoring import dispArgs
from extramodules.dqTranscations import MandatoryArgAdder, aodFileChecker, depsChecker, forgettedArgsChecker, jsonTypeChecker, mainTaskChecker, oneToMultiDepsChecker
from extramodules.configSetter import CONFIG_SET, NOT_CONFIGURED_SET_FALSE, PROCESS_SWITCH, SELECTION_SET, PROCESS_DUMMY, debugSettings
from extramodules.pycacheRemover import runPycacheRemover
from dqtasks.tableReader import TableReader

# Predefined selections for PROCESS_SWITCH function
sepParameters = [
    "processJpsiToEESkimmed", "processJpsiToMuMuSkimmed", "processJpsiToMuMuVertexingSkimmed", "processVnJpsiToEESkimmed",
    "processVnJpsiToMuMuSkimmed", "processElectronMuonSkimmed", "processAllSkimmed"
    ]

mixingParameters = [
    "processBarrelSkimmed", "processMuonSkimmed", "processBarrelMuonSkimmed", "processBarrelVnSkimmed", "processMuonVnSkimmed"
    ]

# All Dependencies
analysisSelectionDeps = {
    "trackSelection": ["analysis-track-selection", "processSkimmed"],
    "eventSelection": ["analysis-event-selection", "processSkimmed"],
    "muonSelection": ["analysis-muon-selection", "processSkimmed"],
    "dileptonHadron": ["analysis-dilepton-hadron", "processSkimmed"]
    }
sepKey = "analysis-same-event-pairing"
sepDeps = {
    "processJpsiToEESkimmed": ["analysis-track-selection", "processSkimmed"],
    "processJpsiToMuMuSkimmed": ["analysis-muon-selection", "processSkimmed"],
    "processJpsiToMuMuVertexingSkimmed": ["analysis-muon-selection", "processSkimmed"],
    "processVnJpsiToEESkimmed": ["analysis-track-selection", "processSkimmed"],
    "processVnJpsiToMuMuSkimmed": ["analysis-muon-selection", "processSkimmed"],
    "processElectronMuonSkimmed": ["analysis-track-selection", "processSkimmed"],
    "processElectronMuonSkimmed": ["analysis-muon-selection", "processSkimmed"], # two deps for electron muon skimming
    "processAllSkimmed": ["analysis-track-selection", "processSkimmed"],
    "processAllSkimmed": ["analysis-muon-selection", "processSkimmed"], # two deps for all skimmed
    }
mixingKey = "analysis-event-mixing"
mixingDeps = {
    "processBarrelSkimmed": ["analysis-track-selection", "processSkimmed"],
    "processMuonSkimmed": ["analysis-muon-selection", "processSkimmed"],
    "processBarrelMuonSkimmed": ["analysis-track-selection", "processSkimmed"],
    "processBarrelMuonSkimmed": ["analysis-muon-selection", "processSkimmed"], # two deps for barrel muon mixing
    "processBarrelVnSkimmed": ["analysis-track-selection", "processSkimmed"],
    "processMuonVnSkimmed": ["analysis-muon-selection", "processSkimmed"]
    }

# init args manually
initArgs = TableReader()
initArgs.mergeArgs()
initArgs.parseArgs()
args = initArgs.parseArgs()
allArgs = vars(args) # for get args

# Debug settings
debugSettings(args.debug, args.logFile, fileName = "tableReader.log")

# if cliMode true, Overrider mode else additional mode
cliMode = args.onlySelect

# Transaction
forgettedArgsChecker(allArgs) # Transaction Management

prefix_process = "process"
suffix_skimmed = "Skimmed"
# adding prefix for PROCESS_SWITCH function (for no kFlag True situations)
if args.process is not None:
    args.process = [prefix_process + sub for sub in args.process]
    args.process = [sub + suffix_skimmed for sub in args.process]

# add prefix and suffix for args.mixing
if args.mixing is not None:
    args.mixing = [prefix_process + sub for sub in args.mixing]
    args.mixing = [sub + suffix_skimmed for sub in args.mixing]

analysisCfg = configGetter(allArgs, "analysis") # get all analysis parameters
analysisArgName = configGetter(allArgs, "analysis", True) # get analysis arg name
processCfg = configGetter(allArgs, "process") # get all process parameters
processArgName = configGetter(allArgs, "process", True) # get process arg name

# Load the configuration file provided as the first parameter
config = {}
with open(args.cfgFileName) as configFile:
    config = json.load(configFile)

# Transaction
jsonTypeChecker(args.cfgFileName)

taskNameInCommandLine = "o2-analysis-dq-table-reader"
taskNameInConfig = "analysis-event-selection"

# Transaction
mainTaskChecker(config, taskNameInConfig)

# Interface Process
logging.info("Only Select Configured as %s", args.onlySelect)
if args.onlySelect == "true":
    logging.info("INTERFACE MODE : JSON Overrider")
if args.onlySelect == "false":
    logging.info("INTERFACE MODE : JSON Additional")

SELECTION_SET(config, analysisSelectionDeps, analysisCfg, cliMode) # Set selections

# Iterating in JSON config file
for key, value in config.items():
    if isinstance(value, dict):
        for value, value2 in value.items():
            
            # aod
            if value == "aod-file" and args.aod:
                config[key][value] = args.aod
                logging.debug(" - [%s] %s : %s", key, value, args.aod)
            # reader
            if value == "aod-reader-json" and args.reader:
                config[key][value] = args.reader
                logging.debug(" - [%s] %s : %s", key, value, args.reader)
            
            # Interface Logic
            CONFIG_SET(config, key, value, allArgs, cliMode)
            PROCESS_SWITCH(config, key, value, allArgs, cliMode, "process", sepParameters, "true/false")
            PROCESS_SWITCH(config, key, value, allArgs, cliMode, "mixing", mixingParameters, "true/false")
            NOT_CONFIGURED_SET_FALSE(config, key, value, args.process, sepParameters, cliMode)
            NOT_CONFIGURED_SET_FALSE(config, key, value, args.mixing, mixingParameters, cliMode)
            MandatoryArgAdder(config, key, value, "analysis-event-selection", "processSkimmed")

PROCESS_DUMMY(config) # dummy automizer

# Transacations
aodFileChecker(args.aod)
oneToMultiDepsChecker(args.mixing, "eventMixing", analysisCfg, analysisArgName)
oneToMultiDepsChecker(args.process, "sameEventPairing", analysisCfg, analysisArgName)
depsChecker(config, sepDeps, sepKey)
depsChecker(config, mixingDeps, mixingKey)

# Write the updated configuration file into a temporary file
updatedConfigFileName = "tempConfigTableReader.json"

with open(updatedConfigFileName, "w") as outputFile:
    json.dump(config, outputFile, indent = 2)

# commandToRun = taskNameInCommandLine + " --configuration json://" + updatedConfigFileName + " -b"
commandToRun = (taskNameInCommandLine + " --configuration json://" + updatedConfigFileName + " --aod-writer-json " + args.writer + " -b")

if args.writer == "false":
    commandToRun = (taskNameInCommandLine + " --configuration json://" + updatedConfigFileName + " -b")

print("====================================================================================================================")
logging.info("Command to run:")
logging.info(commandToRun)
print("====================================================================================================================")
dispArgs(allArgs) # Display all args
os.system(commandToRun) # Execute O2 generated commands
runPycacheRemover() # Run pycacheRemover
