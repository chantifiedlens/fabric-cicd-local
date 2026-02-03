# Log in with Azure CLI (az login) prior to execution

# Below are suggested variables, modify as needed
# $ProdWorkspace = "YOUR WORKSPACE ID HERE"
# $Environment = "Prod"
# $RepositoryDirectory = "workspace"
# $ItemsInScope = "Report,SemanticModel"
# # Syntax to run 'python .\auth_local_variables.py --WorkspaceId $ProdWorkspace --Environment $Environment --RepositoryDirectory $RepositoryDirectory --ItemsInScope  $ItemsInScope'

# from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items
import argparse

# Include parsed arguments
parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('--WorkspaceId', type=str)
parser.add_argument('--Environment', type=str)
parser.add_argument('--RepositoryDirectory', type=str)
parser.add_argument('--ItemsInScope', type=str)
args = parser.parse_args()

# Convert item_type_in_scope into a list
allitems = args.ItemsInScope
item_type_in_scope=allitems.split(",")

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id= args.WorkspaceId,
    environment=args.Environment,
    repository_directory=args.RepositoryDirectory,
    item_type_in_scope=item_type_in_scope,    
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)
