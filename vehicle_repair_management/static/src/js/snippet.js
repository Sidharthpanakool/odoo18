///** @odoo-module */
//import { renderToElement } from "@web/core/utils/render";
//import publicWidget from "@web/legacy/js/public/public_widget";
//import { rpc } from "@web/core/network/rpc";
//
//console.log("Snippet")
//
//publicWidget.registry.get_product_tab = publicWidget.Widget.extend({
//    selector : '.categories_section',
//    async willStart(){
//        var self=this
//        console.log("Kkkkk")
//        const result = await rpc('/get_top_vehicles', {});
//        console.log(result)
//        rpc('/get_top_vehicles').then(function(result){
//            self.$el.find('#latest_cars').html(renderToElement('vehicle_repair_management.category_data', {result:result}))
//        });
//    },
//});


/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

console.log("Snippet")

publicWidget.registry.get_product_tab = publicWidget.Widget.extend({
    selector : '.categories_section',
    willStart: async function(){
        var self=this;
        console.log("Kkkkk")
        const result = await rpc('/get_top_vehicles', {});
        console.log(result)
        rpc('/get_top_vehicles').then(function(result){
            self.$el.find('#latest_cars').html(renderToElement('vehicle_repair_management.category_data', {result}))
        });
    },
});


