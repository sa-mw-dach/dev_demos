# Demo 12 - Run the CPU-based LLM TinyLLama inside Red Hat OpenShift AI

Based on work done in the AI quickstart [llm-cpu-serving](https://github.com/rh-ai-quickstart/llm-cpu-serving).

- In OpenShift AI, create a data science project 'tinyllama'
- Open the 'tinyllama' project and under 'Models' click on 'Select single-model'
- Create the ServingRuntime:
    - In the OpenShift console, press the Plus-symbol in the bar at the top and select 'Import YAML'. 
    - Ensure that the project 'tinyllama' is selected at the top
    - Paste the content from the file [servingruntime.yaml](servingruntime.yaml) and click 'create'.
- Create the InferenceService:
    - In the OpenShift console, press the Plus-symbol in the bar at the top and select 'Import YAML'. 
    - Ensure that the project 'tinyllama' is selected at the top
    - Paste the content from the file [inferenceservice.yaml](inferenceservice.yaml) and click 'create'.
- Testing the deployed model
    - In OpenShift AI, go to the 'tinyllama' project and under 'Models' observe the newly created model 'tinyllama-1b-cpu' until its status indicated ready.
    - Then, in project 'tinyllama', create a new workbench based on code-server.
    - Open a terminal and call the model via 
        ```yaml
        curl -X POST -H "Content-Type: application/json" -d '{"model":"tinyllama" ,"prompt": "Hello, how are you?"}' http://tinyllama-1b-cpu-predictor.tinyllama.svc.cluster.local:8080/v1/completions | jq
        ```
