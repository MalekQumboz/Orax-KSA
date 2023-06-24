from __future__ import unicode_literals
import frappe
from frappe import _

import frappe.defaults


def rm_Custom_DocLetterHead():
    print("remove Custom DocLetterHead")
    # frappe.delete_doc('Letter Head', 'main_sar')


def after_uninstall():
    pass
    
def before_uninstall():
    rm_Custom_DocLetterHead()