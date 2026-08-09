# Teams Membership Management

Power Automate solution for managing Microsoft Teams memberships using predefined Team Sets.

This solution allows administrators to manage complex Teams memberships through business-oriented Role Sets (Team Sets) instead of manually adding and removing users from multiple Teams.

---

# Overview

Managing Microsoft Teams memberships manually becomes difficult as organizations grow.

Typical challenges include:

- Employees forgetting to join required Teams after a department transfer
- Users remaining in Teams they no longer need access to
- New employees requiring membership in multiple Teams
- Managers spending time maintaining memberships manually
- Team owners manually adding and removing members

To solve these challenges, this solution introduces the concept of a **Team Set**.

A Team Set represents a business role and contains one or more Microsoft 365 Groups.

Example:

```text
Tokyo Sales Representative
├─ Tokyo Office
├─ Sales Department
└─ IT Support
```

When a user is assigned to the Team Set, the solution automatically synchronizes Microsoft 365 Group memberships.

---

# Solution Components

The solution contains two Power Automate flows and several environment variables.

../screenshots/solution-overview.png

### Flow 1

**Bulk Add Members to Teams Groups by Team Set**

Batch processing flow that reads users and Team Sets from Excel.

### Flow 2

**Bulk Add Members to Teams Groups from Forms Responses**

Self-service enrollment flow using SharePoint Forms.

---

# Architecture

```text
User
   ↓
Excel / SharePoint Form
   ↓
Power Automate
   ↓
Team Set Definition
   ↓
Microsoft 365 Groups
   ↓
Microsoft Teams
   ↓
Engage / Planner
```

---

# Features

- Team Set based membership management
- Bulk add users to Teams
- Bulk remove users from Teams
- Microsoft Forms integration
- SharePoint integration
- Excel integration
- Microsoft Graph integration
- Automatic membership synchronization
- Environment Variable support
- Solution-based deployment

---

# Self-Service Enrollment

Users can select a Team Set by using a simple SharePoint Form.

../screenshots/forms-role-selection.png

Example Team Sets:

```text
NewEmployees_Tokyo
NewEmployees_Osaka
Tokyo_Sales
Osaka_Sales
Tokyo_SalesManager
```

After submission, memberships are automatically synchronized.

---

# Excel Batch Processing

The Excel version allows administrators to perform bulk membership updates.

../screenshots/excel-teamset-table.png

Required columns:

```text
Name
Mail
Select a Role Set
```

The selected Team Set determines which Microsoft 365 Groups the user should belong to.

---

# Team Set Examples

| Team Set | Included Groups |
|-----------|----------------|
| NewEmployees_Tokyo | Tokyo Office, New Employees, Training Participants, IT Support |
| NewEmployees_Osaka | Osaka Office, New Employees, Training Participants, IT Support |
| Tokyo_Sales | Tokyo Office, Sales Department, IT Support |
| Osaka_Sales | Osaka Office, Sales Department, IT Support |
| Tokyo_SalesManager | Tokyo Office, Sales Department, Managers Communication, IT Support |

---

# Flow Design

## Excel-Based Flow

../screenshots/excel-membership-sync-flow.png

Processing steps:

1. Initialize Team Set configuration
2. Load Group IDs
3. Read Excel rows
4. Retrieve current memberships
5. Determine required memberships
6. Add missing groups
7. Remove unnecessary groups

---

## Forms-Based Flow

../screenshots/forms-membership-sync-flow.png

Processing steps:

1. SharePoint item is created or modified
2. Load Team Set configuration
3. Retrieve current memberships
4. Determine required memberships
5. Add missing groups
6. Remove unnecessary groups

---

# Environment Variables

The solution uses Environment Variables to separate configuration from business logic.

../screenshots/environment-variables.png

Examples:

```text
ListSiteURL
SPOListID
TargetGroupID_1
TargetGroupID_2
TargetGroupID_3
...
```

This makes deployment across Development, Test, and Production environments easier.

---

# SharePoint Configuration

The Forms version uses a SharePoint Form to collect Role Set selections.

../screenshots/sharepoint-form-creation.png

Recommended form name:

```text
SelectRoleSet
```

Recommended field:

```text
Select Teams Role Set
```

The available choices should match the Team Set names configured in the solution.

---

# Related Qiita Articles

## TeamsやEngageの登録を効率化！チームセットによる一括登録の仕組み

This article explains:

- Team Set architecture
- Group membership synchronization
- Microsoft Graph integration
- Team Set JSON configuration

https://qiita.com/DaddyDaddy/items/886990cf4f88cba3c85f

---

## Formsで役割を選択したら適切なチームに自動参加できる仕組みを作ってみた

This article explains:

- Microsoft Forms integration
- SharePoint List integration
- Self-service enrollment
- Dynamic Team Set selection

https://qiita.com/DaddyDaddy/items/f43ed39074a34b12df6b

---

# Folder Structure

```text
TeamsMembershipManagement
│
├─ docs
│   ├─ install-guide.md
│   ├─ setup-guide.md
│   └─ release-notes.md
│
├─ screenshots
│
├─ samples
│
└─ solution
    ├─ managed
    └─ unmanaged
```

---

# Installation

See:

```text
docs/install-guide.md
```

---

# Technical Design

See:

```text
docs/setup-guide.md
```

---

# Roadmap

Future enhancements may include:

- SharePoint managed Team Sets
- Power Apps administration console
- Approval workflows
- Entra ID integration
- GitHub Actions deployment
- Power Platform Pipelines deployment

---

# Requirements

- Microsoft 365
- Microsoft Teams
- Power Automate
- SharePoint Online
- Microsoft Entra ID

Premium licenses are not required for the basic implementation.

---

# Disclaimer

This solution is provided as-is.

Always test in a non-production environment before deploying to production.

---

# Author

GitHub

https://github.com/daddydaddy

Qiita

https://qiita.com/DaddyDaddy