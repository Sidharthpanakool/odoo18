from email.policy import default

from odoo import fields,models,api

class ProductAssembly(models.Model):
    _name = "product.assembly"
    _rec_name = 'product_id'


    product_id = fields.Many2one('product.template', string="Product")
    consumed_parts_ids = fields.One2many('consumed.parts', 'consumed_product_id', "Consumed product")
    quantity = fields.Float(string="Quantity")




    #
    #         name = fields.Char(string="Reference", required=True, default='New')
    #         product_id = fields.Many2one('product.product', string="Product", required=True)
    #         component_line_ids = fields.One2many('consumed.products', 'bom_id', string="Components")







    # @api.model_create_multi
    # def create(self,vals_list):
    #     self.env['product.product'].create([{
    #         'name': self.name,
    #         'active': False,
    #         'sale_ok':True,
    #         'purchase_ok':True,
    #
    #     }])






#
#     < odoo >
#     < !-- Menu -->
#     < menuitem
#     id = "menu_simple_prod_root"
#     name = "Simple Production"
#     sequence = "10" / >
# 
#     < !-- BoM -->
#     < record
#     id = "view_product_bom_tree"
#     model = "ir.ui.view" >
#     < field
#     name = "name" > product.bom.tree < / field >
#     < field
#     name = "model" > product.bom < / field >
#     < field
#     name = "arch"
#     type = "xml" >
#     < tree >
#     < field
#     name = "name" / >
#     < field
#     name = "product_id" / >
# 
# < / tree >
# < / field >
# < / record >
# 
# < record
# id = "view_product_bom_form"
# model = "ir.ui.view" >
# < field
# name = "name" > product.bom.form < / field >
# < field
# name = "model" > product.bom < / field >
# < field
# name = "arch"
# type = "xml" >
# < form
# string = "Product BoM" >
# < sheet >
# < group >
# < field
# name = "name" / >
# < field
# name = "product_id" / >
# < / group >
# < field
# name = "component_line_ids" >
# < tree
# editable = "bottom" >
# < field
# name = "product_id" / >
# < field
# name = "quantity" / >
# < / tree >
# < / field >
# < / sheet >
# < / form >
# < / field >
# < / record >
# 
# < record
# id = "action_product_bom"
# model = "ir.actions.act_window" >
# < field
# name = "name" > Product
# BoMs < / field >
# < field
# name = "res_model" > product.bom < / field >
# < field
# name = "view_mode" > tree, form < / field >
# < / record >
# 
# < menuitem
# id = "menu_bom"
# name = "BoMs"
# parent = "menu_simple_prod_root"
# action = "action_product_bom" / >
# 
# < !-- Product
# Creation -->
# < record
# id = "view_product_creation_tree"
# model = "ir.ui.view" >
# < field
# name = "name" > product.creation.tree < / field >
# < field
# name = "model" > product.creation < / field >
# < field
# name = "arch"
# type = "xml" >
# < tree >
# < field
# name = "name" / >
# < field
# name = "product_id" / >
# < field
# name = "quantity" / >
# < field
# name = "state" / >
# < / tree >
# < / field >
# < / record >
# 
# < record
# id = "view_product_creation_form"
# model = "ir.ui.view" >
# < field
# name = "name" > product.creation.form < / field >
# < field
# name = "model" > product.creation < / field >
# < field
# name = "arch"
# type = "xml" >
# < form
# string = "Product Creation" >
# < header >
# < button
# name = "action_confirm_creation"
# string = "Confirm"
# type = "object"
# states = "draft"
# 
# 
# class ="btn-primary" / >
# 
# < field
# name = "state"
# widget = "statusbar"
# statusbar_visible = "draft,done" / >
# < / header >
# < sheet >
# < group >
# < field
# name = "name" / >
# < field
# name = "bom_id" / >
# < field
# name = "product_id"
# readonly = "1" / >
# < field
# name = "quantity" / >
# < / group >
# < / sheet >
# < / form >
# < / field >
# < / record >
# 
# < record
# id = "action_product_creation"
# model = "ir.actions.act_window" >
# < field
# name = "name" > Product
# Creations < / field >
# < field
# name = "res_model" > product.creation < / field >
# < field
# name = "view_mode" > tree, form < / field >
# < / record >
# 
# < menuitem
# id = "menu_product_creation"
# name = "Product Creation"
# parent = "menu_simple_prod_root"
# action = "action_product_creation" / >
# < / odoo >
# 
# < odoo >
# < record
# id = "seq_product_creation"
# model = "ir.sequence" >
# < field
# name = "name" > Product
# Creation < / field >
# < field
# name = "code" > product.creation < / field >
# < field
# name = "prefix" > PC / < / field >
# < field
# name = "padding" > 4 < / field >
# < / record >
# < / odoo >
# 
# 'data': [
#     'data/ir_sequence_data.xml',
#     'views/product_creation_views.xml',
# ],