# Teams Membership Management

Power Automate solution for managing Microsoft Teams, Microsoft 365 Groups, Engage Communities, and Planner memberships using predefined Team Sets.

---

# Overview

Managing Microsoft Teams memberships manually becomes difficult as organizations grow.

Typical challenges include:

- Employees forgetting to join required Teams after a department transfer
- Users remaining in Teams they no longer need access to
- New employees requiring membership in multiple Teams
- Managers spending time maintaining memberships manually
- Team owners manually adding and removing members

This solution introduces the concept of a **Team Set**.

Instead of assigning users to individual Teams one by one, administrators define a Team Set that represents a business role.

Example:

```text
Tokyo Sales Representative
├─ Tokyo Office
├─ Sales Department
└─ IT Support
```

When a user is assigned to the Team Set, the solution automatically:

- Adds the user to required Microsoft 365 Groups
- Removes the user from unnecessary groups
- Synchronizes Teams membership
- Synchronizes Engage community membership
- Synchronizes Planner membership

---

# Important Notice

## Test with Dedicated Microsoft 365 Groups First

Before using real Microsoft 365 Groups or production Teams, it is strongly recommended that you create dedicated test Teams and test Microsoft 365 Groups specifically for validation purposes.

Do not use production Group IDs during initial testing.

Recommended approach:

1. Create several test Teams.
2. Obtain the Microsoft 365 Group IDs associated with those Teams.
3. Configure the environment variables using the test Group IDs.
4. Validate the synchronization behavior.
5. Replace the test Group IDs with production Group IDs only after successful validation.

---

## Risk of Membership Changes

This solution automatically adds and removes group memberships.

Incorrect Team Set definitions, Group IDs, flow modifications, or configuration mistakes may result in unintended behavior, including:

- Users being removed from Teams unexpectedly
- Users being added to incorrect Teams
- Users losing access to related Microsoft 365 resources
- Unintended changes to Engage communities
- Unintended changes to Planner membership

Always validate the solution in a non-production environment before using it in production.

---

## Recommendation During Initial Testing

During early testing phases, it is recommended that membership update actions are disabled.

For example:

```text
AddGroups
RemoveGroups
```

should not execute actual membership changes until the synchronization logic has been fully validated.

Recommended approach:

```text
Load Team Set
↓
Determine Required Groups
↓
Calculate AddGroups
↓
Calculate RemoveGroups
↓
Review Results
```

Only after confirming that the calculated results are correct should the following actions be enabled:

```text
Add member to group
Remove member from group
```

This allows administrators to verify the expected behavior without making actual changes to Microsoft 365 Groups.

---

## No Warranty

This solution is provided as-is.

The author makes no guarantees regarding suitability, reliability, security, or fitness for a particular purpose.

The author cannot be held responsible for any direct or indirect consequences resulting from the use of this solution.

Use this solution at your own risk.

---

# Architecture

```text
User
   ↓
Microsoft Forms / SharePoint List / Excel
   ↓
Power Automate
   ↓
Team Set Definition
   ↓
Microsoft 365 Groups
   ↓
Teams / Engage / Planner
```

---

# Features

- Team Set based membership management
- Bulk add users to Teams
- Bulk remove users from Teams
- Microsoft Forms integration
- SharePoint List integration
- Excel integration
- Microsoft Graph integration
- Automatic membership synchronization
- Environment Variable support
- Solution deployment support

---

# Team Set Example

| Team Set | Included Groups |
|-----------|----------------|
| New Employee (Tokyo) | All Employees, Tokyo Office, New Employees, Training Participants, IT Support |
| Tokyo Sales Representative | All Employees, Tokyo Office, Sales Department, IT Support |
| Osaka Sales Representative | All Employees, Osaka Office, Sales Department, IT Support |
| Tokyo Developer | All Employees, Tokyo Office, Development Department, IT Support |
| Tokyo Sales Manager | All Employees, Tokyo Office, Sales 