# Log in with Azure CLI (az login) prior to execution
# Syntax to run 'python .\auth_local_hard_coded.py'

from pathlib import Path

# from azure.identity import AzureCliCredential
from fabric_cicd import deploy_with_config,append_feature_flag

append_feature_flag("enable_experimental_features")
append_feature_flag("enable_config_deploy")

# Deploy using a config file
deploy_with_config(
    config_file_path="workspace/config.yml",
    environment="test"
)