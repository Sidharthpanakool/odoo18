from email.policy import default

from odoo import fields,models,api

class ProductAssembly(models.Model):
    _name = "product.assembly"

    name = fields.Char(string="Product Name",  required=True ,)
    assembly_id = fields.Char(string="Product id",
                              required=True ,
                              readonly=True,
                              default='New',
                              copy=False,
                              tracking=True)

    consumed_parts_ids = fields.One2many('consumed.parts', 'consumed_product_id', "Consumed product")

    @api.model
    def write(self, vals):
        # self.env['product.product'].create([{
        #     'name': self.name,
        #     'active': False
        # }])

        if vals.get('assembly_id', 'New') == 'New':
            vals['assembly_id'] = self.env['ir.sequence'].next_by_code('product.assembly.code') or 'New'
        return super(ProductAssembly, self).create(vals)



    # @api.model_create_multi
    # def create(self,vals_list):
    #     self.env['product.product'].create([{
    #         'name': self.name,
    #         'active': False,
    #         'sale_ok':True,
    #         'purchase_ok':True,
    #
    #     }])




