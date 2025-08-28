/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { Order,Orderline } from "@point_of_sale/app/store/models";

patch(Orderline.prototype, {
    getDisplayData(){
    console.log(this)
    return{
        ...super.getDisplayData(),


        product_owner_id: this.get_product().product_owner_id,

    };
    }
    });