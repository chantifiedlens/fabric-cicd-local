# Fabric CICD Local Deployment Example

This repository demonstrates the first steps of a **fabric-cicd** deployment workflow from a local machine. It provides practical examples of authenticating with Microsoft Fabric and deploying items to your Fabric workspace.

## About This Repository

This example is based on the [fabric-cicd library](https://microsoft.github.io/fabric-cicd/latest/), an open-source tool that simplifies the CI/CD workflow for Microsoft Fabric projects. This repository was created to accompany the post “[First Fabric CI/CD Deployment Steps](https://chantifiedlens.com/2026/02/04/first-fabric-cicd-deployment-steps/)” and demonstrates how the library can be applied in a real-world scenario.

### Workspace Contents

The `workspace/` folder contains Microsoft Fabric items created by the Git integration feature in Microsoft Fabric. These items include:

- **Reports** - Power BI reports (.pbir format)
- **Semantic Models** - Data models for reports
- **Notebooks** - Jupyter notebooks for data processing
- **Data Pipelines** - Orchestration workflows
- **Dataflows** - Data transformation pipelines
- **Lakehouses** - Data lake storage with metadata
- **Warehouses** - SQL analytics data warehouses
- **Databases** - SQL databases and mirrored databases
- **Environments** - Python/Spark execution environments
- **Copy Jobs** - Data ingestion jobs
- **Apache Airflow Jobs** - Distributed scheduling
- **Event Streams** - Real-time data streaming
- **KQL Dashboards** - Real-time analytics dashboards
- **GraphQL APIs** - Custom API definitions
- **Variable Libraries** - Shared configuration variables
- **And more...**

All items follow the Fabric Git integration structure with metadata and definition files included.

## Prerequisites

Before running the authentication scripts, ensure you have:

1. **Python 3.12** or later installed
2. **Azure CLI** installed on your local machine
3. **fabric-cicd library** installed via pip
4. **Azure authentication** configured on your machine

### Setup Instructions

1. Install Python 3.12 from [python.org](https://www.python.org/downloads/)

2. Install Azure CLI from [Microsoft Docs](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows)

3. Install the required dependencies:
   ```bash
   pip install -r workspace/requirements.txt
   ```

4. Authenticate with Azure:
   ```bash
   az login
   ```
   
   For service principal authentication:
   ```bash
   az login --service-principal -u <app-id> -p <password-or-cert> --tenant <tenant-id>
   ```

## Running the Authentication Scripts

This repository includes three progressive authentication examples, each demonstrating a different approach to configuring Fabric CICD deployments:

### 1. Hard-Coded Authentication (`1-auth_local_hard_coded.py`)

**Use Case:** Quick testing and local development

This script uses hard-coded configuration values to authenticate and deploy items.

**Steps to Run:**

1. Open the script and update the configuration values:
   ```python
   workspace_id = "YOUR-WORKSPACE-ID"  # Replace with your actual workspace ID
   environment = "Prod"
   repository_directory = "workspace"
   item_type_in_scope = ["Report", "SemanticModel"]  # Customize which item types to deploy
   ```

2. Ensure you're logged in with Azure CLI:
   ```bash
   az login
   ```

3. Run the script:
   ```bash
   python .\1-auth_local_hard_coded.py
   ```

**Output:** The script will deploy all Report and SemanticModel items from the workspace folder to your target workspace.

---

### 2. Command-Line Variables Authentication (`2-auth_local_variables.py`)

**Use Case:** Flexible deployments with different configurations without code changes

This script accepts parameters via command-line arguments, making it ideal for CI/CD pipelines and repeated deployments with different settings.

**Steps to Run:**

1. Ensure you're logged in with Azure CLI:
   ```bash
   az login
   ```

2. Run the script with your desired parameters:
   ```bash
   python .\2-auth_local_variables.py --WorkspaceId "YOUR-WORKSPACE-ID" --Environment "Prod" --RepositoryDirectory "workspace" --ItemsInScope "Report,SemanticModel"
   ```

**Parameter Details:**

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--WorkspaceId` | Target workspace ID in Microsoft Fabric | `00000000-0000-0000-0000-000000000000` |
| `--Environment` | Environment name for tagging | `Prod` or `Dev` |
| `--RepositoryDirectory` | Path to workspace items | `workspace` |
| `--ItemsInScope` | Comma-separated list of item types to deploy | `Report,SemanticModel,Notebook` |

**PowerShell Example:**
```powershell
$WorkspaceId = "YOUR-WORKSPACE-ID"
$Environment = "Prod"
$RepositoryDirectory = "workspace"
$ItemsInScope = "Report,SemanticModel"
python .\2-auth_local_variables.py --WorkspaceId $WorkspaceId --Environment $Environment --RepositoryDirectory $RepositoryDirectory --ItemsInScope $ItemsInScope
```

---

### 3. Configuration File Authentication (`3-auth_local_config.py`)

**Use Case:** Production deployments with complex configurations and feature flags

This script uses a YAML configuration file (`workspace/config.yml`) for all settings, providing the most flexible and maintainable approach for production environments.

**Steps to Run:**

1. Update the configuration file:
   - Edit `workspace/config.yml`
   - Update workspace names or IDs for your environments:
     ```yaml
     workspace:
       test: your-test-workspace-name
       prod: your-prod-workspace-name
     ```
   - Customize `item_types_in_scope` to specify which Fabric items to deploy
   - (Optional) Link a parameter file for dynamic values

2. Ensure you're logged in with Azure CLI:
   ```bash
   az login
   ```

3. Run the script:
   ```bash
   python .\3-auth_local_config.py
   ```

**Configuration File Details:**

The `workspace/config.yml` file controls:
- **Workspace Selection:** Define target workspaces by environment name or ID
- **Item Types:** Specify which Fabric items to deploy (Reports, Notebooks, Dataflows, etc.)
- **Parameters:** Reference external parameter files for dynamic configuration
- **Publish Settings:** Configure additional publish options (optional section)

**Advanced Features:**

The script enables experimental features for advanced deployments:
- `enable_experimental_features` - Enables preview capabilities
- `enable_config_deploy` - Activates configuration-based deployment

---

## Choosing the Right Approach

| Use Case | Script | Advantages |
|----------|--------|-----------|
| **Local Testing** | `1-auth_local_hard_coded.py` | Simple, quick to set up, good for learning |
| **CI/CD Pipelines** | `2-auth_local_variables.py` | Flexible, parameterized, reusable in automation |
| **Production** | `3-auth_local_config.py` | Comprehensive, file-based, best for complex scenarios |

---

## Troubleshooting

### Azure Login Issues
- Ensure Azure CLI is installed: `az --version`
- Log in again: `az login` or `az login --use-device-code`
- For service principal issues, verify your credentials and tenant ID

### Module Not Found Errors
- Reinstall fabric-cicd: `pip install --upgrade fabric-cicd`
- Verify installation: `pip list | findstr fabric-cicd`

### Workspace Not Found
- Verify the workspace ID/name exists in your Fabric tenant
- Ensure you have the appropriate permissions in the workspace

### Permission Denied
- Check your Fabric workspace permissions
- Verify your Azure account has the necessary roles

---

## Additional Resources

- [fabric-cicd Documentation](https://microsoft.github.io/fabric-cicd/latest/)
- [Microsoft Fabric Overview](https://learn.microsoft.com/en-us/fabric/get-started/fabric-home)
- [Azure CLI Documentation](https://learn.microsoft.com/en-us/cli/azure/)
- [Operationalize fabric-cicd to work with Microsoft Fabric and YAML Pipelines](https://chantifiedlens.com/2025/03/18/operationalize-fabric-cicd-to-work-with-microsoft-fabric-and-yaml-pipelines/)
- [Operationalize fabric-cicd to work with Microsoft Fabric and GitHub Actions](https://chantifiedlens.com/2025/04/11/operationalize-fabric-cicd-to-work-with-microsoft-fabric-and-github-actions/)

---

## License

This example repository demonstrates usage of the fabric-cicd library. Refer to the fabric-cicd repository for license details.
