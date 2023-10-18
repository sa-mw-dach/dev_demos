# Demo 05 - Personal AI Assistant for Application Development

## Introduction
- AI Assistent for Application Development
- OpenShift Dev Spaces
- Continue
- Private: on-prem & air-gapped
- Enriching AI assistent with own information, e.g. company coding guidelines provided as PDF to the model as additional source
- ...


## Requirements
In order to be able to run the demo, the following requirements need to be fullfilled:
* Red Hat OpenShift (tested on version 4.12)
* Red Hat OpenShift Dev Spaces (tested on version 3.8)
* Continue VS Code extension (tested on version 0.1.28)
* Optional when using GPUs: NVIDIA GPU Operator (tested on version 23.6.1) & NFD (tested on version 4.11.0) 


## Installation of Continue
Continue(XXX) describes itself as "an open-source autopilot for software development". It is an IDE Extension and brings the power of ChatGPT and other Larga-Language Models (LLM) to VS Code. In this section, Continue is installed in OpenShift Dev Spaces in a way that supports on-prem air-gapped usage.

Basically the instructions for installing Continue in an on-prem air-gapped environment are followed, as can be found [here](https://continue.dev/docs/walkthroughs/running-continue-without-internet). 

1) Open OpenShift Dev Spaces & create an "Empty Workspace" (this will use the Universal Developer Image, UDI)

1) Download the VS Code extension [here](https://open-vsx.org/extension/Continue/continue) (download "Linux x64") and use it directly in OpenShift Dev Spaces, if internet connection is available, or store it in your artifact store of choice, from which you have access in OpenShift.

1) In OpenShift Dev Spaces, go to the extensions menu at the left, click on the three dots at the top of the "Extensions" page and select "Install from VSIX". Now select the previously downloaded Continue VSIX file (e.g. `Continue.continue-0.1.28@linux-x64.vsix`) and hit "ok".









Note that the installation of VS code extensions can be automated using devfiles (XXX).


1) Inside the newly created workspace, open a terminal and clone the following git repo: `https://github.com/sa-mw-dach/dev_demos.git`

