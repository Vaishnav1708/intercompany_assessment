import frappe
from frappe import _


def validate_intercompany_sales_invoice(doc, method=None):
    if doc.company != "Ecofinit Dubai":
        return

    if doc.customer != "Metal Green Saudi Arabia - Internal Customer":
        return

    if not doc.custom_sales_value_confirmation:
        frappe.throw(
            _("An approved Sales Value Confirmation is required before creating this intercompany Sales Invoice.")
        )

    confirmation = frappe.get_doc(
        "Sales Value Confirmation",
        doc.custom_sales_value_confirmation,
    )

    if confirmation.workflow_state != "Approved":
        frappe.throw(
            _("The selected Sales Value Confirmation must be Approved.")
        )

    if confirmation.company != doc.company:
        frappe.throw(_("Company must match the Sales Value Confirmation."))

    if confirmation.customer != doc.customer:
        frappe.throw(_("Customer must match the Sales Value Confirmation."))

    invoice_qty = sum(
        item.qty for item in doc.items if item.item_code == confirmation.item
    )

    if invoice_qty > confirmation.quantity:
        frappe.throw(
            _("Invoice quantity cannot exceed the approved quantity.")
        )