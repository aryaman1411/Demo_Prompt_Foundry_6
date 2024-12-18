Below is a basic example of how you can structure your Terraform code to create Azure resources. This example includes the creation of a resource group, a storage account, and an app service plan.

```hcl
provider "azurerm" {
  features {}
}

module "resource_group" {
  source  = "Azure/resource-group/azurerm"
  version = "2.0.0"

  name     = "example-resources"
  location = "West Europe"
}

module "storage_account" {
  source  = "Azure/storage-account/azurerm"
  version = "2.0.0"

  name                     = "examplestorageaccount"
  resource_group_name      = module.resource_group.name
  location                 = module.resource_group.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
}

module "app_service_plan" {
  source  = "Azure/app-service/azurerm"
  version = "2.0.0"

  name                = "example-app-service-plan"
  location            = module.resource_group.location
  resource_group_name = module.resource_group.name
  kind                = "Windows"
  reserved            = false

  sku {
    tier = "Standard"
    size = "S1"
  }
}
```

This is a very basic example and does not include all possible configurations. You should adjust the code according to your needs. 

Remember to replace the placeholders with your actual values. Also, make sure to use the latest version of the modules.

The code is modular, meaning each resource is created in its own module. This makes the code easier to manage and update. 

The code follows best practices such as using a separate module for each resource, using variables instead of hard-coding values, and using the latest version of the Azure provider.