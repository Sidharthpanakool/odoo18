/** @odoo-module **/
import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

console.log("product orderline js")

patch(PosOrderline.prototype, {
    setup(vals) {
        console.log(this)
        this.product_owner_id = this.product_id.product_owner_id || "";
        return super.setup(...arguments);
    },
    getDisplayData() {
        return {
            ...super.getDisplayData(),
            product_owner_id: this.get_product().product_owner_id || "",
        };
    },

    // EXTENDS 'point_of_sale'
    prepareBaseLineForTaxesComputationExtraValues(customValues = {}) {
        const extraValues = super.prepareBaseLineForTaxesComputationExtraValues(customValues);
        extraValues.product_owner_id = this.product_id.product_owner_id;
        return extraValues;
        console.log("Extra",extraValues)
    },
});

patch(Orderline, {
    props: {
        ...Orderline.props,
        line: {
            ...Orderline.props.line,
            shape: {
                ...Orderline.props.line.shape,
                product_owner_id: { type: String, optional: true },
            },
        },
    },
});




















//import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
//import { patch } from "@web/core/utils/patch";
//
//console.log("product orderline js")
//
//patch(Orderline.prototype, {
//    setup(){
//    console.log(this)
//    },
//    getDisplayData() {
//    console,log("hello")
//    return {
//        ...super.getDisplayData(),
//        product_owner_id: this.get_product().product_owner_id,
//    };
//    }
//    });




///** @odoo-module **/
//import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
//import { patch } from "@web/core/utils/patch";
//
//console.log("product orderline js")
//
//patch(Orderline.prototype, {
//    setup(){
//    console.log(this)
//    },
//    getDisplayData() {
//    console,log("hello")
//    return {
//        ...super.getDisplayData(),
//        product_owner_id: this.get_product().product_owner_id,
//    };
//    }
//    }););