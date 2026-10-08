## Demo App

Custom ERPNext/Frappe app for the Ecofinit Dubai ↔ Metal Green Saudi Arabia intercompany assessment.

## Versions

- ERPNext: 15.43.3
- Frappe: 15.47.2
- Ubuntu: 24.04 LTS (update this to your actual version)

## Features

- Sales Value Confirmation custom approval flow
- Validation that blocks Ecofinit intercompany Sales Invoice without approved confirmation
- Intercompany Transaction Tracker report
- Fixtures for custom field, workflow, workflow states, and roles

## App installation

From the bench folder:

```bash
cd ~/demo-bench
bench get-app <your-github-repo-url>
bench --site demo.com install-app intercompany_assessment
bench --site demo.com migrate
bench --site demo.com clear-cache
```

If the app is already present locally:

```bash
cd ~/demo-bench
bench --site demo.com install-app intercompany_assessment
bench --site demo.com migrate
```

## Setup steps

1. Enable developer mode if needed.
2. Install the app on the target site.
3. Run migrations.
4. Import/export fixtures through app hooks.
5. Verify Workflow, Workflow State, Role, and Custom Field records are present.

## Fixtures and migrations

After changing fixtures or hooks:

```bash
cd ~/demo-bench
bench --site demo.com export-fixtures --app intercompany_assessment
bench --site demo.com migrate
bench --site demo.com clear-cache
```

## Site configuration

- Site Name: `demo.com`
- Time Zone: `Asia/Riyadh`
- Assessment tax templates use 0% as a demo assumption
- Intercompany SAR price list is used for the internal transaction scenario

## Report

Report name:

- `Intercompany Transaction Tracker`

Open from Desk and verify it shows:
- Ecofinit Sales Invoice
- Metal Green Purchase Invoice
- Item
- Quantity
- Value
- Status

## Tests

Recommended checks:
- Sales Invoice creation blocked without approved Sales Value Confirmation
- Sales Value Confirmation workflow transitions work correctly
- Partial GRNs update stock and PO status correctly
- Intercompany tracker report shows completed document linkage

## Notes

- Do not store passwords, tokens, or database credentials in this repository.
- Keep all assessment customization inside this app only.
