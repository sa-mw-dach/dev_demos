# Demo 01 - Licence plate recognition

## Introduction
The first demo of this series is based on the "Red Hat OpenShift Data Science Workshop - Licence plate recognition"[^license_plate_desc] and shows the usage of Red Hat CodeReady Workspaces (CRW) running on Red Hat Openshift to create a develeopment environment for an Artifical Intelligence (AI) workload, which can be executed from within CRW using CPU and GPU. 

## Requirements
In order to be able to create the CodeReady Workspace and run the sample AI workload as described below, the following requirements need to be fullfilled:
* Red Hat OpenShift (tested on version 4.8.17)
* Red Hat CodeReady Workspaces (tested on version 2.12.1)
* Optional: NVIDIA GPU Operator (tested on version 1.8.2)

## Usage
**Creating the CodeReady workspace:**
1) Open CodeReady Workspaces (CRW) and click on "Create Workspace"
1) Click "Custom Workspace" and in section "DevFile" paste the devfile URL for GPU or CPU execution in the field "Enter devfile URL":
    + CPU execution: https://raw.githubusercontent.com/sa-mw-dach/demo_crw_ai/main/infra/workspace_ai_cpu.yml
    + GPU execution: https://raw.githubusercontent.com/sa-mw-dach/demo_crw_ai/main/infra/workspace_ai_gpu.yml

    Then click "Load Devfile", adapt the settings in the yaml editor, if needed, and finally click "Create & Open". The first time you run the devfile it may take some minutes to create the workspace (e.g. due to downloading the proper container image).
1) After the workspace has been created, you are asked if you trust the authors of the demo repo[^demo_repo]. Click "Yes, I trust" and the demo repo's content is automatically being synced to your workspace (accessible on the left under "CHE (Workspace)").

**Starting the webserver hosting the AI workload**
1) Go to the menu bar and select "Terminal" and "Run Task". Then click on "01_license_plate__Run server" at the top of the page. A command window is opening at the bottom of the page, where you can see the webserver for the AI workload being started. The first time you execute this task inside the workspace, the prerequistes are installed via Python's PyPi, which may take some minutes.
1) After the AI webserver has been started successfully, a new window tells you that a new process is listening on port 5000, which is the desired AI webserver listener. You are asked if you want to create a redirect for this port, which you answer with "yes".
1) Subsequently a new window pops up telling you that the redirect is enabled now and provides the URL to the webserver, which you can open by clicking "Open In New Tab". The new browser window should simply show the JSON string `{ "status": "ok"}`, which means that the webserver and the AI workload are working properly. Please note that it may take some seconds until the redirect is working properly.

**Testing the AI model**

Go to the menu bar and select "Terminal" and "Run Task". Then click on "01_license_plate__Test AI model" at the top of the page. The number plate of picture "demo_crw_ai_repo/external/dataset/images/Cars374.png" is being analyzed by the AI model and the result should be the JSON String `{'prediction': 'S7JDV'}`. You can now play around with this AI model and test the reckognition of different number plates by opening the Python file "demo_crw_ai_repo/demos/01_license_plate/test_ai_model.py" in the CRW editor (under "CHE (WORKSPACE)" on the left side of the screen). Simply uncomment one of the examples provided and comment the other two. For example:
```python
#response = requests.post('http://127.0.0.1:5000/predictions', '{"data": "Cars374.png"')
#response = requests.post('http://127.0.0.1:5000/predictions', '{"data": "Cars387.png"')
response = requests.post('http://127.0.0.1:5000/predictions', '{"data": "Cars18.png"}')
```
You can also add your own pictures to "demo_crw_ai_repo/external/dataset/images/" in the CRW editor and use them to test the AI model by replacing the string "Cars374.png" with the name of the newly uploaded file and executing the task "01_license_plate__Test AI model" as described above.


**Testing the GPU computation**

Go to the menu bar and select "Terminal" and "Run Task". Then click on "01_license_plate__Test GPU computation" at the top of the page. A new command window opens at the bottom of the screen, displaying the result of a simple matrix calculation as given in "demo_crw_ai_repo/demos/01_license_plate/test_gpu.py", which should be
`[[22. 28.][49. 64.]]`. Additionally, the available GPUs are displayed. If `[]` is shown, no GPU could be found and the calculations have been done using the CPU.

You can play around with the file "test_gpu.py" and use `with tf.device('/CPU:0'):` or `with tf.device('/GPU:0'):` in front of the computations in order to run the workload with CPU or GPU, respectively. After running this file via task "01_license_plate__Test GPU computation" as described above, in the terminal output it will be clearly stated for each computation if a CPU or GPU has been used.


## Note regarding external resources
The "Red Hat OpenShift Data Science Workshop - Licence plate recognition" repo[^license_plate_repo] has been included in this repo using `git subtree` as
```
git subtree add --prefix external/licence-plate-workshop https://github.com/rh-aiservices-bu/licence-plate-workshop.git main --squash
```
Starting from the original code's commit id 4ebb74326cdd70eedf861225f6604fef0d0e3194 changes regarding the PyPi packages in file `external/licence-plate-workshop/requirements.txt` have been done to fit to the environment at hand.

[^license_plate_desc]: https://rh-aiservices-bu.github.io/licence-plate-workshop/
[^license_plate_repo]: https://github.com/rh-aiservices-bu/licence-plate-workshop.git
[^demo_repo]: https://github.com/sa-mw-dach/demo_crw_ai.git