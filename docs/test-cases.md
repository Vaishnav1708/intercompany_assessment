# Test Cases

## TC-01
Create Ecofinit PO for 100 units of AL-DROSS-001 at SAR 2,000.
Expected: PO submits successfully.

## TC-02
Create GRN 1 for 30.
Expected: Stock increases by 30; PO pending = 70.

## TC-03
Create GRN 2 for 40.
Expected: Stock increases to 70 cumulative; PO pending = 30.

## TC-04
Create GRN 3 for 30.
Expected: Stock increases to 100 cumulative; PO pending = 0.

## TC-05
Create Sales Value Confirmation as Ecofinit Sales User.
Expected: Can save and send for approval.

## TC-06
Try approval as Ecofinit Sales User.
Expected: Approval not allowed.

## TC-07
Approve as Sales Value Approver.
Expected: Workflow state = Approved.

## TC-08
Create Ecofinit Sales Invoice without approved confirmation.
Expected: Validation error.

## TC-09
Create Ecofinit Sales Invoice with approved confirmation.
Expected: Invoice saves/submits.

## TC-10
Generate Metal Green intercompany Purchase Invoice.
Expected: Linked Purchase Invoice created.

## TC-11
Run Intercompany Transaction Tracker.
Expected: Completed transaction row is visible.
