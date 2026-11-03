# Installation Guide

[日本語](./install-guide.md) | English

This guide explains how to import the Dataverse Bulk Operations solution into a Power Platform environment.

## Prerequisites

- A Power Platform environment with a Dataverse database
- An environment role that allows solution imports, such as Environment Administrator or System Administrator
- A user who can create connections for Dataverse, Microsoft Entra ID, and HTTP with Microsoft Entra ID connectors used by the flows
- The licenses required by the connectors and permission to use them in your tenant

This is an unmanaged solution. Import it into a development or test environment first.

## Before Importing

1. Download the [solution ZIP](../solution/OnboardingTraining_1_0_0_1.zip).
2. Confirm that the target is not a production environment.
3. Ensure that the person assigning connections in the import wizard has the permissions required to authenticate each connector.

The unique solution name and ZIP filename use `OnboardingTraining`; the solution display name is `DataverseBulkOperations`.

## Import the Solution

1. Open [Power Apps](https://make.powerapps.com/) and select the target environment.
2. Open **Solutions** and select **Import solution**.
3. Select the downloaded `OnboardingTraining_1_0_0_1.zip`.
4. If the wizard asks you to configure connection references, assign connections for the target environment. Check the connector type for each reference shown:
   - Microsoft Dataverse
   - Microsoft Entra ID
   - HTTP with Microsoft Entra ID (preauthorized)
5. Start the import and wait for it to complete. If it fails, review the details, resolve any connection or environment permission issues, and retry.

## After Import

1. Open the imported `DataverseBulkOperations` solution.
2. Confirm that all connection references are assigned to valid connections.
3. Open the flows and verify that their connections point to the target environment.
4. Follow the setup guide to review the environment URL, create data, and update target IDs in `create_and_update_multiple_sampleAction`.
5. Inspect the delete flow without running it. It deletes all rows in its target table; do not enable or run it until setup and deletion targets have been reviewed.
6. Follow the [Setup Guide](./setup-guide.en.md) to test in a dedicated test environment with test data.

## Notes

- Importing the solution does not authenticate connections or complete environment-specific configuration.
- For manually triggered flows, also review run permissions and configure run-only users' connections if applicable.
- Components in an unmanaged solution can be edited in the target environment. Decide how changes will be managed before operating it.
