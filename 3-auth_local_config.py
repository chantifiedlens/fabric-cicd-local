# Log in with Azure CLI (az login) prior to execution
# Syntax to run 'python .\3-auth_local_config.py'

from pathlib import Path

from fabric_cicd import deploy_with_config,append_feature_flag

append_feature_flag("enable_experimental_features")
# Commented out as no longer required from fabric-cicd v0.2.0 onwards for configuration based deployments
# append_feature_flag("enable_config_deploy")

# Deploy using a config file
deploy_with_config(
    config_file_path="workspace/config.yml",
    environment="test"
)