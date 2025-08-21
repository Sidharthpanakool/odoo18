/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
console.log("Snippet")
publicWidget.registry.get_product_tab = publicWidget.Widget.extend({
    selector : '.categories_section',
    async willStart() {
        console.log("KKKKKK")
        const result = await rpc('/get_top_vehicles', {});
        if(result){
            this.$target.empty().html(renderToElement('vehicle_repair_management.category_data', {result: result}))
        }
    },
});

