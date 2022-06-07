#Steps to setup2
oc new-project pipelines-demo
oc apply -f setup/workspace-pvc.yaml
oc apply -f pipeline/licenseplate-pipeline.yaml 
