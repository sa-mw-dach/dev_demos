# How to deploy the pipeline

First of all, you need to create a new project for your pipeline

`oc new-project pipelines-demo`

Because our pipeline constitutes several task we must assure that all task can access the workspace where we checked out the project from git. Since each task is run in its own pod, we must provide persisten storage. Hence, we need to create a PersistentVolumeClaim that we can use when we run the pipeline.

`oc apply -f setup/workspace-pvc.yaml`

Finally, we create the new pipeline in our new project.

`oc apply -n pipelines-demo -f pipeline/licenseplate-pipeline.yaml` 

To run the pipeline you can either create a PielineRun resource, use the tkn cli or the OpenShift admin console.
