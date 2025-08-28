/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

console.log("Product Owner js")

patch(PosStore.prototype, {
    async _processData(loadedData) {
        await super._processData(...arguments);
        this.product_temp=loadedData['product.product']
    }
});
