# User Python Based Interface

\tableofcontents

[![doxygen](https://img.shields.io/badge/doxygen-documentation-blue.svg)](https://dquserinterfaceoop.github.io/docs/html/)

This project includes python based user interface development for PWG-DQ Workflows based on nightly-20221025. You can follow the instructions and you can find tutorials in table of contents (For prerequisites, Installation guide for argcomplete and Some Informations good to know).

## Contact
Ionut Cristian Arsene (Owner of [`O2DQWorkflows`](https://github.com/iarsene/O2DQworkflows))

Cevat Batuhan Tolon (Author Of Interface)

## Important

Since the interface is constantly updated for stability, it is recommended to update it with `git pull --rebase` command

## Table Of Contents
- [Python Scripts And JSON Configs](doc/1_ScriptsAndConfigs.md)
  - [Main Python Scripts](doc/1_ScriptsAndConfigs.md#main-python-scripts)
  - [Config Files](doc/1_ScriptsAndConfigs.md#config-files)
  - [DQ Interface Scripts](doc/1_ScriptsAndConfigs.md#dq-interface-scripts)
  - [Common Deps Interface Scripts](doc/1_ScriptsAndConfigs.md#common-deps-interface-scripts)
  - [Extra Modules](doc/1_ScriptsAndConfigs.md#extra-modules)
- [Prerequisites!!!](doc/2_Prerequisites.md)
  - [Cloning repository](doc/2_Prerequisites.md#cloning-repository)
  - [argcomplete - Bash tab completion for argparse](doc/2_Prerequisites.md#argcomplete---bash-tab-completion-for-argparse)
  - [Instalation Guide For argcomplete](doc/2_Prerequisites.md#instalation-guide-for-argcomplete)
    - [Prerequisites Before Installation argcomplete Package For Linux Based Systems and LXPLUS](doc/2_Prerequisites.md#prerequisites-before-installation-argcomplete-package-for-linux-based-systems-and-lxplus)
    - [Local Instalation (Not Need For O2)](doc/2_Prerequisites.md#local-instalation-not-need-for-o2)
    - [O2 Installation](doc/2_Prerequisites.md#o2-installation)
    - [Prerequisites Before Installation argcomplete Package For MacOS Based Systems](doc/2_Prerequisites.md#prerequisites-before-installation-argcomplete-package-for-macos-based-systems)
    - [Local Instalation (Not Need For O2)](doc/2_Prerequisites.md#local-instalation-not-need-for-o2-1)
    - [O2 Installation](doc/2_Prerequisites.md#o2-installation-1)
- [Instructions for TAB Autocomplete](doc/3_InstructionsforTABAutocomplete.md)
- [Technical Informations](doc/4_TechincalInformations.md)
  - [Helper Command Functionality](doc/4_TechincalInformations.md#helper-command-functionality)
  - [Some Things You Should Be Careful For Using and Development](doc/4_TechincalInformations.md#some-things-you-should-be-careful-for-using-and-development)
  - [Some Notes Before The Instructions](doc/4_TechincalInformations.md#some-notes-before-the-instructions)
  - [Interface Modes: JSON Overrider and JSON Additional](doc/4_TechincalInformations.md#interface-modes-json-overrider-and-json-additional)
- [Instructions for Python Scripts](doc/5_InstructionsForPythonScripts.md)
  - [Download CutsLibrary, MCSignalLibrary, MixingLibrary From Github](doc/5_InstructionsForPythonScripts.md#download-cutslibrary-mcsignallibrary-mixinglibrary-from-github)
  - [Get CutsLibrary, MCSignalLibrary, MixingLibrary From Local Machine](doc/5_InstructionsForPythonScripts.md#get-cutslibrary-mcsignallibrary-mixinglibrary-from-local-machine)
  - [Available configs in DownloadLibs.py Interface](doc/5_InstructionsForPythonScripts.md#available-configs-in-downloadlibspy-interface)
- [Instructions for runTableMaker/runTableMakerMC.py](doc/5_InstructionsForPythonScripts.md#instructions-for-runtablemakerruntablemakermcpy)
  - [Available configs in runTableMaker Interface](doc/5_InstructionsForPythonScripts.md#available-configs-in-runtablemakerruntablemakermc-interface)
- [Instructions for runTableReader.py](doc/5_InstructionsForPythonScripts.md#instructions-for-runtablereaderpy)
  - [Available configs in runTableReader Interface](doc/5_InstructionsForPythonScripts.md#available-configs-in-runtablereader-interface)
- [Instructions for runDQEfficiency.py](doc/5_InstructionsForPythonScripts.md#instructions-for-rundqefficiencypy)
  - [Available configs in runDQEfficiency Interface](doc/5_InstructionsForPythonScripts.md#available-configs-in-rundqefficiency-interface)
- [Instructions for runFilterPP.py](doc/5_InstructionsForPythonScripts.md#instructions-for-runfilterpppy)
  - [Available configs in runFilterPP Interface](doc/5_InstructionsForPythonScripts.md#available-configs-in-runfilterpp-interface)
- [Instructions for runDQFlow.py](doc/5_InstructionsForPythonScripts.md#instructions-for-rundqflowpy)
  - [Available configs in runDQFlow Interface](doc/5_InstructionsForPythonScripts.md#available-configs-in-rundqflow-interface)
- [Tutorial Part](doc/6_Tutorials.md)
  - [Download Datas For Tutorials](doc/6_Tutorials.md#download-datas-for-tutorials)
    - [Workflows In Tutorials](doc/6_Tutorials.md#workflows-in-tutorials)
    - [Skimmed Datas In Tutorials](doc/6_Tutorials.md#skimmed-datas-in-tutorials)
    - [Pre-Made JSON configuration Files In Tutorials](doc/6_Tutorials.md#pre-made-json-configuration-files-in-tutorials)
  - [MC Part](doc/6_Tutorials.md#mc-part)
    - [Run tableMakerMC on LHC21i3d2 (jpsi to MuMu pp Run3Simulation)](doc/6_Tutorials.md#run-tablemakermc-on-lhc21i3d2-jpsi-to-mumu-pp-run3simulation)
    - [Run dqEfficiency on MC (LHC21i3d2 pp Run3Simulation)](doc/6_Tutorials.md#run-dqefficiency-on-mc-lhc21i3d2-pp-run3simulation)
    - [Run tablemakerMC on LHC21i3b (Prompt jpsi to dielectron pp Run3Simulation)](doc/6_Tutorials.md#run-tablemakermc-on-lhc21i3b-prompt-jpsi-to-dielectron-pp-run3simulation)
    - [Run dqEfficiency on MC (LHC21i3b pp Run3Simulation)](doc/6_Tutorials.md#run-dqefficiency-on-mc-lhc21i3b-pp-run3simulation)
    - [Run tablemakerMC on LHC21i3f2 (Non-Prompt jpsi to dielectron pp Run3Simulation)](doc/6_Tutorials.md#run-tablemakermc-on-lhc21i3f2-non-prompt-jpsi-to-dielectron-pp-run3simulation)
    - [Run dqEfficiency on LHC21i3f2 (LHC21i3f2 pp Run3Simulation)](doc/6_Tutorials.md#run-dqefficiency-on-lhc21i3f2-lhc21i3f2-pp-run3simulation)
  - [Data Part](doc/6_Tutorials.md#data-part)
    - [Run tableMaker on LHC15o (LHC15o PbPb Run2Data)](doc/6_Tutorials.md#run-tablemaker-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run tableReader on LHC15o (LHC15o PbPb Run2Data)](doc/6_Tutorials.md#run-tablereader-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run tableMaker on LHC15o With Generic Flow Analysis (LHC15o PbPb Run2Data)](doc/6_Tutorials.md#run-tablemaker-on-lhc15o-with-generic-flow-analysis-lhc15o-pbpb-run2data)
    - [Run tableReader on LHC15o with Generic Flow Analysis (LHC15o PbPb Run2Data)](doc/6_Tutorials.md#run-tablereader-on-lhc15o-with-generic-flow-analysis-lhc15o-pbpb-run2data)
    - [Run dqFlow on LHC15o (LHC15o PbPb Run2Data)](doc/6_Tutorials.md#run-dqflow-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run v0Selector on LHC15o (LHC15o PbPb Run2Data)](doc/6_Tutorials.md#run-v0selector-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run tableMaker on LHC22c (LHC22c pp Run3Data)](doc/6_Tutorials.md#run-tablemaker-on-lhc22c-lhc22c-pp-run3data)
    - [Run tableReader on Data (LHC22c pp Run3Data)](doc/6_Tutorials.md#run-tablereader-on-data-lhc22c-pp-run3data)
    - [Run filterPP on fwdprompt(fwdprompt pp Run3Data)](doc/6_Tutorials.md#run-filterpp-on-fwdpromptfrom-hands-on-session-ii)
  - [Special Part : Dilepton Analysis For Non-Standart Existing Workflows in DQ](doc/6_Tutorials.md#special-part--dilepton-analysis-for-non-standart-existing-workflows-in-dq)
    - [MC : Dilepton Track Analysis (On Bc Simulation)](doc/6_Tutorials.md#mc--dilepton-track-analysis-on-bc-simulation)
    - [Data : Dilepton Hadron Analysis (On PbPb Data LHC15o)](doc/6_Tutorials.md#data--dilepton-hadron-analysis-on-pbpb-data-lhc15o)
- [Developer Guide](doc/7_DeveloperGuide.md)
  - [Naming Conventions](doc/7_DeveloperGuide.md#naming-conventions)
- [TroubleshootingTreeNotFound](doc/8_TroubleshootingTreeNotFound.md)
  - [Converters](doc/8_TroubleshootingTreeNotFound.md#converters-special-additional-tasks-for-workflows)
  - [add_track_prop](doc/8_TroubleshootingTreeNotFound.md#addtrackprop)


## TODO LIST

- Add developer guide (for contributing) chapter
- Maintaince need for available configs part (v0selector is missing)
- Needed to explain O2-DQ Data Model and Workflow