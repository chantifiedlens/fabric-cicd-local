# Install Python 3.12 and Azure CLI apps locally
# Install the fabric-cicd library (via 'pip install fabric-cicd')
# Log in with Azure CLI (az login) prior to execution
# First test login as yourself, and then as a service principal (az login --service-principal -u <app-id> -p <password-or-cert> --tenant <tenant-id>)

# Syntax to run 'python .\1-auth_local_hard_coded.py'

# from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items

# Sample values for FabricWorkspace  object parameters
workspace_id = "00000000-0000-0000-0000-000000000000" # Your target workspace Id goes here
environment = "Prod"
repository_directory = ("workspace")
item_type_in_scope = ["Report","SemanticModel"]

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)