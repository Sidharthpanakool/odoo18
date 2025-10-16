from odoo import models,api ,fields

class ProductProduct(models.Model):
    _inherit = "product.product"

    approval_needed = fields.Boolean(string="Approval needed")

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if not self.env.user.has_group('product_manager_approval.group_product_create_manager'):
                vals['approval_needed'] = True
                vals['active'] = False
        return super().create(vals_list)

    def action_approve_product(self):
        self.approval_needed = False
        self.active = True















    # @api.model_create_multi
    # def create(self, vals_list):
    #     print("aaaa")
    #     if  self.env.user.has_group('product_manager_approval.group_product_create_user'):
    #         print("Hiii")
    #         vals=vals_list[0]
    #         print(vals)
    #         self.env['product.creation.request'].create([{
    #             'name':vals.get('name'),
    #             'sales_price':vals.get('lst_price'),
    #             'cost_price':vals.get('standard_price'),
    #         }])
    #     elif  self.env.user.has_group('product_manager_approval.group_product_create_manager'):
    #         print("Manager")
    #
    #     return super().create(vals_list)

        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'New Record',
        #     'res_model': 'product.creation.request',
        #     'view_mode': 'form',
        #     'view_id': self.env.ref('product_manager_approval.action_product_creation_request').id,
        #     'target': 'current',
        # }

    # @api.model_create_multi
    # def create(self, vals_list):
    #     if  self.env.user.has_group('product.group_product_manager'):
    #         vals = vals_list[0]
    #         req = self.env['product.manager.approval'].create({
    #             'name': vals.get('name'),
    #             # 'default_code': vals.get('default_code'),
    #             # 'categ_id': vals.get('categ_id'),
    #             # 'uom_id': vals.get('uom_id'),
    #         })
    #         action = self.env.ref('product_manager_approval.action_product_creation_request_form_view').id
    #         msg = "You are not allowed to create products directly. Please submit this New Item Request for approval."
    #         raise RedirectWarning(msg, action, 'Go to Request')
    #     return super().create(vals_list)

        # @api.model_create_multi
    # def create(self, vals_list):
    #     if any(val.get('snoozed_until', False) and val.get('trigger',
    #                                                        self.default_get(['trigger'])['trigger']) == 'auto' for
    #            val in vals_list):
    #         raise UserError(_("You can not create a snoozed orderpoint that is not manually triggered."))
    #     return super().create(vals_list)







        # return {
        #     'name': 'service customer',
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'res.partner',
        #     'view_id': self.env.ref('vehicle_repair_management.action_service_customer_form_view').id,
        #     'target': 'current',
        #     'context': {'create': False,
        #                 'default_name': self.name,
        #                 'default_phone': self.phone,
        #                 'default_image_1920': self.image_1920
        #                 }
        # }
        # print("Hi")
        # res = super(ProductProduct, self).create(values)
        # # if self.env.user.has_group('product.group_product_manager'):

        # self.env.ref('product_manager_approval.action_product_creation_request_form_view')
        # print()




        # group_product_manager


        # return res

    # def action_product_creation_request_form_view(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'New Record',
    #         'res_model': '', # Replace with your model
    #         'view_mode': 'form',
    #         'target': 'new',
    #     }