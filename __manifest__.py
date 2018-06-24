# -*- coding: utf-8 -*-
{
    'name': "Cost Benefit Analysis",
    'summary': """
        This Module is useful for small business like coffee shop of analysis cost and benefit""",

    'description': """
        Feture
		- Compute cost of goods
		- Record Daily Benefit
		- Record Daily Expenses
    """,

    'author': "Popboon (Air) Mahachanawong for Caramel Cafe",
    'website': "http://www.caramelcafe.co.th",

    # for the full list
    'category': 'Accounting & Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
    	'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
}
