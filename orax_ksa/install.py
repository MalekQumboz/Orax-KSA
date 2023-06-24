from __future__ import unicode_literals
import frappe
from frappe import _

import frappe.defaults


def add_records(records):
    # from erpnext/setup/setup_wizard/install_fixtures.py
    # this should be added as a function in frappe like frappe.add_records(records)
    # from frappe.modules import scrub
    for r in records:
        doc = frappe.new_doc(r.get("doctype"))
        doc.update(r)
        doc.insert(ignore_permissions=True)
        frappe.reload_doctype(r.get("doctype"))
        frappe.db.sql(
            """
            update `tabLetter Head` set source=%(html)s where name=%(name)s
            """,
            {"html": "HTML", "name": "main_sar"}
        )


def add_Custom_DocLetterHead():

    records = [
        {
            "doctype": "Letter Head",
            "creation": "2023-05-03 21:35:54.561379",
            "modified": "2023-05-04 23:07:11.951991",
            "modified_by": "Administrator",
            "owner": "Administrator",
            "idx": 0,
            "docstatus": 0,
            "name": "main_sar",
            "letter_head_name": "main_sar",
            "source": "HTML",
            "footer_source": "HTML",
            "disabled": 0,
            "is_default": 1,
            "content": "<meta charset='UTF-8'><meta content='IE=edge'><meta content='width=device-width, initial-scale=1.0' name='viewport'><title>Header The page</title><style> section{width: 100%;border: 3px solid black;border-radius: 10px;display: flex;justify-content: space-between;font-weight: bold;padding: 15px;}.midelPage{    display: flex;    align-items:center;    width: 210px;       	height: 130px;}.rightPage{    text-align: right;}.leftPage{text-align: left;} img{display: block;margin: 0 auto;width: 100%;height: 100%;}</style><section><div class='rightPage'><p> شركة الحلول الذهبية لتقنية نظم المعلومات <br> برامج محاسبية - شبكات -مواقع ومتاجر الكترونية <br>السجل التجاري: 4030365478 <br> الجوال: 0552661598 - 0565627769</p></div><div class='midelPage'><img alt='imageMid' src='/files/WhatsApp Image 2023-04-12 at 12.49.35.jpeg'></div><div class='leftPage'><p>Golden Solutions Information System Tech <br>Accounting programs - networks <br>- websites and electronic stores<br>C.R: 4030365478<br>Mobile : 0552661598 - 0565627769</p></div></section>",
             "footer": "<footer><div class='company-info'> <h5>المركز الرئيسي - جدة - شارع خالد بن الوليد - جوال: +9665627769</h5>    <h5>Head Office - Jeddah - Khalid Bin Al Waleed Street - Mobile: +9665627769</h5>    <h5>www.oraxsoft.com</h5>  </div>  </footer><style>  footer {    display: flex;    justify-content: space-between;    align-items: center;    padding: 20px;    font-size: 14px;  }     .company-info {       align-items: center;   }  .company-info h3 {    margin-top: 0;      }    .company-info p {    margin: 5px 0;  }   </style>",
            "_user_tags": "",
            "_comments": "",
            "_assign": "",
            "_liked_by": ""
        }
    ]
    print("Adding Custom DocLetterHead")
    check_head = frappe.db.sql(
		""" SELECT
			name
		FROM
			`tabLetter Head` 
		WHERE
			name ='main_sar'
			"""
	)
    if not check_head:
        add_records(records)
    
    
    # source of all existing letter heads must be HTML
    # frappe.db.sql('update `tabLetter Head` set content=`<h1>تجربة راس الفاتورة</h1>` where name=`main_sar``)
    # frappe.db.sql('update "tabLetter Head" set content="Desk" where name="main_sar"')




def before_install():
    add_Custom_DocLetterHead()

# def after_install():
#     pass
