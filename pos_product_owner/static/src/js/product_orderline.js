/** @odoo-module **/
import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

patch(PosOrderline. prototype, {
    setup() {
       console.log(this)
           this.product_owner_id = this.product_id.product_owner_id.name || "";
            return super.setup(...arguments);
    },
    getDisplayData() {
        return {
            ...super.getDisplayData(),
            product_owner_id: this.get_product().product_owner_id.name || "",
            };
    },

    prepareBaseLineForTaxesComputationExtraValues(customValues = {}) {
        const extraValues = super.prepareBaseLineForTaxesComputationExtraValues(customValues);
        extraValues.product_owner_id = this.product_id.product_owner_id;
        return extraValues;
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