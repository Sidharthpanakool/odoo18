///** @odoo-module */
////import { renderToElement } from "@web/core/utils/render";
////import publicWidget from "@web/legacy/js/public/public_widget";
////import { rpc } from "@web/core/network/rpc";
//console.log("Snippet")
//odoo.define('vehicle_repair_management.snippet', function(require) {
//'use strict';
//var PublicWidget = require('web.public.widget');
//var rpc = require('web.rpc');
//var core = require('web.core');
//var qweb = core.qweb;
//var Dynamic = PublicWidget.Widget.extend({
//    selector : '.categories_section',
//    willStart:async function() {
//    var self=this;
//    await rpc.query({
//    route:'/get_top_vehicles',}).then((data)=>
//    {
//    this.data=data;
//    });
//    },
//    start:function(){
//    var chunks=_.chunk(this.data,4)
//    chunks[0].is_active=true
//    this.$el.find('#top_products_carousel').html(
//    qweb.render('vehicle_repair_management.category_data',{chunks
//    })
//    )
//    },
//    });
//    PublicWidget.registry.categories_section = Dynamic;``
//    return Dynamic;
//    });


/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
console.log("Snippet")
publicWidget.registry.get_product_tab = publicWidget.Widget.extend({
    selector : '.categories_section',
    willStart:async function() {
        console.log("KKKKKK")
        const result = await rpc('/get_top_vehicles', {});
            if(result){
            this.$target.empty().html(renderToElement('vehicle_repair_management.category_data', {result: result}))
        }
    },
});
