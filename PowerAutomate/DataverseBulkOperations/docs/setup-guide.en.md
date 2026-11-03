# Setup Guide

[日本語](./setup-guide.md) | English

This guide covers connections, environment-specific values, and testing for Dataverse Bulk Operations. Complete these steps after importing the solution and before running any flows.

## Solution Components

The solution includes samples for Dataverse bulk create/update, deletion, FetchXML retrieval, and Microsoft Entra ID group membership checks, as well as a canvas app and tables for testing.

| Flow | Main connections | Values to review |
|---|---|---|
| `create_and_update_multiple_sampleAction` | HTTP with Microsoft Entra ID (preauthorized) | Dataverse environment URL, records to create, and row IDs to update |
| `deleteMultiple_sampleAction` | Microsoft Dataverse, HTTP with Microsoft Entra ID (preauthorized) | The `dd_employees` table and the rows to delete |
| `tmp_FetchXML` | Microsoft Dataverse | Table and column names in the FetchXML |
| `tmp_search_in_group` | Microsoft Entra ID | User and group ID to check |

The flows use manual triggers. Verify their connection references and run permissions. If other users will run them, also configure the run-only users' connections.

## Dataverse Web API Endpoint

The `baseURL` Compose action in `create_and_update_multiple_sampleAction` contains the sample value `https://example.crm.dynamics.com`. Replace it with the URL of the target environment before running the flow. Do not include a trailing `/`.

```text
https://<your-environment-organization-url>
```

Find the URL in the Power Platform admin center or the environment details. Confirm that the HTTP with Microsoft Entra ID connection used for the request is authenticated and has access to that environment.

## Sample Values in the Create/Update Flow

In addition to the environment URL, this flow contains test values in its definition. Review the relevant actions before running it.

- `createMultiple` creates three fixed records in `dd_employees`. Change the email addresses and other values to test data for your environment.
- The `Create_Records_in_Bulk` scope creates records from a range whose upper value is currently `100`, generating sample rows numbered 1 through 99. Adjust the number to the amount you need to test.
- `updateMultiple` updates three fixed row IDs. Confirm that those IDs exist in the target environment and replace them with test record IDs if necessary.
- The create and update actions run during the same manual flow run. Start with a small amount of test data and compare the run history with the records in Dataverse.

The table logical name is `dd_employee`, and its collection name is `dd_employees`. If you change column names or data types, update both the request JSON and the table definition accordingly.

## Important Warning About the Delete Flow

`deleteMultiple_sampleAction` retrieves rows from `dd_employees` without a filter, up to 1,000 at a time, and repeatedly sends DELETE requests using the Web API `$batch` endpoint. It continues until the table is empty, so running it deletes all data in that table.

Despite its name, this flow does not use the Dataverse `DeleteMultiple` message. Do not assume it is safe just because you reviewed a filter or target table.

- Do not run this flow in production.
- Test it only in a dedicated, disposable environment.
- Immediately before running it, verify that the table contains no data that must be retained.
- Keep the flow disabled if deletion is not authorized.

## Other Flows

### `tmp_FetchXML`

This FetchXML sample links `dd_employee` and `dd_onboardingtraining` by email address and retrieves employees without a related onboarding training record. If you change the tables or columns, also update the FetchXML `entity`, `attribute`, and `link-entity` settings.

### `tmp_search_in_group`

This flow uses the Microsoft Entra ID connector to check membership for the user and group ID in its definition. Replace the user UPN and group ID with test values from your tenant before running it.

## Test Procedure

1. Create test employee records in a development or test environment.
2. Verify the connection references and the target environment for each flow.
3. Configure the create/update flow's environment URL, create data, and update target IDs for testing.
4. Manually run `create_and_update_multiple_sampleAction` and review the run history and Dataverse records.
5. Configure the target tables, user, and group for `tmp_FetchXML` and `tmp_search_in_group`, then run each flow individually.
6. If you need to test deletion, use a dedicated disposable environment only, and confirm that all rows in the target table can be deleted before running the flow.

## Troubleshooting

- **Connection reference error**: Confirm that each solution connection reference is assigned to an authenticated connection in the target environment.
- **HTTP 401/403**: Check the HTTP with Microsoft Entra ID connection's authentication, access to the target environment, and tenant connector policies.
- **HTTP 404**: Verify the environment URL, API path, and table collection name (for example, `dd_employees`).
- **Create/update errors**: Check column logical names, data types, required fields, target row IDs, and request data.
- **FetchXML errors**: Confirm that table and column logical names and link conditions match the schema in the target environment.

Check the Dataverse Web API version, request format, and support for bulk operations on each table against the specifications for your environment.
