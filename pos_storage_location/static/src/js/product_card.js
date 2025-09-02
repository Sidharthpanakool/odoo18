//import { Component } from "@odoo/owl";
//
//export class ProductCard extends Component {
//    static template = "my_pos_event_.Product_Qty";
//    static props = {
//        class: { String, optional: true },
//        name: String,
//        product: Object,
//        productId: Number | String,
//        comboExtraPrice: { String, optional: true },
//        color: { type: [Number, undefined], optional: true },
//        imageUrl: [String, Boolean],
//        productInfo: { Boolean, optional: true },
//        onClick: { type: Function, optional: true },
//        onProductInfoClick: { type: Function, optional: true },
//        showWarning: { type: Boolean, optional: true },
//        productCartQty: { type: [Number, undefined], optional: true },
//    };
//    static defaultProps = {
//        onClick: () => {},
//        onProductInfoClick: () => {},
//        class: "",
//        showWarning: false,
//    };


//// Part of Odoo. See LICENSE file for full copyright and licensing details.
//import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
//import { patch } from "@web/core/utils/patch";
//
//patch(ProductCard.prototype, {
//    get displayRemainingSeats() {
//        return Boolean(this.props.product.event_id) && this.props.product.event_id.seats_limited;
//    },
//});

//
//
//import { _t } from '@web/core/l10n/translation';
//import { patch } from '@web/core/utils/patch';
//import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
//
//patch(ProductCard, {
//    props: {
//        ...ProductCard.props,
//        quantity: { type: Number, optional: true },
//    },
//});
//
//patch(ProductCard.prototype, {
//    setup() {
//        super.setup(...arguments);
//        this.allQuantitySelectedTooltip = _t("All available quantity selected");
//    },
//});



///** @odoo-module **/
//import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
//import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
//import { patch } from "@web/core/utils/patch";
//
//
//import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
//
//
//patch(PosOrderline. prototype, {
//    setup() {
//       console.log(this)
//           this.product_owner_id = this.product_id.product_owner_id.name || "";
//            return super.setup(...arguments);
//    },
//    getDisplayData() {
//        return {
//            ...super.getDisplayData(),
//            product_owner_id: this.get_product().product_owner_id.name || "",
//            };
//    },
//
//    prepareBaseLineForTaxesComputationExtraValues(customValues = {}) {
//        const extraValues = super.prepareBaseLineForTaxesComputationExtraValues(customValues);
//        extraValues.product_owner_id = this.product_id.product_owner_id;
//        return extraValues;
//    },
//});
//patch(Orderline, {
//    props: {
//        ...Orderline.props,
//        line: {
//            ...Orderline.props.line,
//            shape: {
//                ...Orderline.props.line.shape,
//                product_owner_id: { type: String, optional: true },
//            },
//        },
//    },
//});