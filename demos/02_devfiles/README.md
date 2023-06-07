# Demo 02 - Dev Spaces Devfiles

## Introduction
Some devfiles for testing Dev Spaces functionality.

## Simple devfile
A simple devfile for creating a Dev Spaces workspace is given in devfile_udi.yaml.

It uses the Red Hat Universal Developer Image (UDI) from quay.io/devfile/universal-developer-image:ubi8-latest. The content of the container iamage can be found here: https://github.com/devfile/developer-images.

Just open the Dev Spaces Dashboard, paste the link to the raw-formatted devfile in the "Git Repo URL" field and press "Create & Open". It is important to use the raw format, e.g. https://raw.githubusercontent.com/sa-mw-dach/dev_demos/main/demos/02_devfiles/devfile_udi.yaml.


## Private image repos
When using private image repos, the Dev Spaces workspace needs to have the proper credentials for the respective image registry.

As can be seen in devfile_udi_private.yaml, the container image being used within the Workspace is taken from a private repo, where credentials are needed for accessing it. If one tries to create a workspace based on this devfile (like explained in section "Simple devfile") then you will get an access denied error message.

To resolve this, one option is to create a Kubernetes secret within the user namespace in OpenShift and label it properly so that Dev Spaces injects it into the workspace. Following https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.6/html/user_guide/using-credentials-and-configurations-in-workspaces#creating-image-pull-secrets-creating-an-image-pull-secret-with-cli, one needs to:

1) Go to the Dev Spaces user namespace, for example "user1-devspaces"
   ```
   oc project <devspaces-user-namespace>
   ```
2) Create image pull secret
   ```
   oc create secret docker-registry <secret_name> \
    --docker-server=<registry_server> \
    --docker-username=<username> \
    --docker-password=<password> \
    --docker-email=<email_address>
   ```
3) Add Dev Spaces labels to image pull secret
   ```
   oc label secret <secret_name> controller.devfile.io/devworkspace_pullsecret=true controller.devfile.io/watch-secret=true
   ```

Now one can open the Dev Spaces Dashboard, paste the link to the raw-formatted devfile in the "Git Repo URL" field and press "Create & Open". It is important to use the raw format, e.g. https://raw.githubusercontent.com/sa-mw-dach/dev_demos/main/demos/02_devfiles/devfile_udi_private.yaml.

