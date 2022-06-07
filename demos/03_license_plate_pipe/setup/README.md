#Steps to setup3
oc new-project pipelines-demo
oc apply -f setup/workspace-pvc.yaml
oc apply -f pipeline/licenseplate-pipeline.yaml 
