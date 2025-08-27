/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

export function chunk(array, size) {
	const result = [];
	for (let i = 0; i < array.length; i += size) {
		result.push(array.slice(i, i + size));
	}
	return result;
}
publicWidget.registry.get_product_tab = publicWidget.Widget.extend({
	selector: '.categories_section',
	willStart: async function() {
		var self = this;
		await rpc('/get_top_vehicles', {}).then((data) => {
			this.data = data;
		});
	},
	start: function() {
		var chunks = chunk(this.data, 4)
		this.$el.find("#latest_cars").html(
			renderToElement('vehicle_repair_management.category_data', {
				chunks
			}))
	},
});



