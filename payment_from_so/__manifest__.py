{
 'name': 'payment from sale order',
 'version': '18.0.1.0.0',
 'license': "LGPL-3",
 'category': 'Sales',
 'sequence': 1,
 'summary': 'L o L',
 'description': "Payment from saleo rder",
 'author': "cybro",
 'data': ["views/sale_order_views_inherit.xml"
 ],
 'assets': {
 'web.assets_backend': [

 ],
 'web.assets_frontend': [

 ]
 },

 'depends': ['base','sale','sale_management'],
 'application': True,
 'auto_install': True,
 'installable': True,
}