# Demonstration of OpenShift Pipelines
This is a very specific and absolutely not production-ready demo of deploying Typo3 via a pipeline.

## Usage
1) Clone repo in CodeReady Workspaces
```
git clone https://github.com/sa-mw-dach/dev_demos.git
cd dev_demos/demos/02_pipelines_typo3/
```

2) Add pipeline to OpenShift cluster:
```
oc new-project pipelines-typo3
oc apply -f pipeline.yaml
```

3) Run pipeline to deploy Typo3:
```
tkn pipeline start clone-and-run-manifest -w name=shared-workspace,claimName=source-pvc -p git-url=https://github.com/sa-mw-dach/dev_demos.git -p git-revision=feature/pipelines -p manifest_dir=demos/02_pipelines_typo3/k8s --showlog
```

4) Open Typo3 Web UI and provide db credentials `typo3 / yourothersupersecretpassword`
