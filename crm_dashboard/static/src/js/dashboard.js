/** @odoo-module **/
import {
	registry
} from "@web/core/registry";
import {
	Component,
	useState
} from "@odoo/owl";
import {
	useService
} from "@web/core/utils/hooks";

const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
	setup() {
		super.setup();
		this.orm = useService('orm');
		this._fetch_data();
		this.action = useService("action");
		this.loadCharts();

		this.state = useState({
			leads_by_month: [],
		});

	}

	async _fetch_data(filter = 'year') {
		let result = await this.orm.call("crm.lead", "get_tiles_data", [], {
			context: {
				filter
			}
		});

		document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
		document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
		document.getElementById('exp_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
		document.getElementById('revenue').innerHTML = `<span>${result.currency}${result.invoice_amt_sum}</span>`;
		document.getElementById('won').innerHTML = `<span>${result.won}</span>`;
		document.getElementById('loss').innerHTML = `<span>${result.loss}</span>`;
	}


	async loadCharts(filter = 'year') {

		if (this._charts) {
			this._charts.forEach(chart => chart.destroy());
		}

		const data = await this.orm.call("crm.lead", "get_chart_data", [], {
			context: {
				filter
			}
		});
		this.state.leads_by_month = data.leads_by_month;


		const chart1 = new Chart(document.getElementById("lost_lead_chart"), {
			type: "bar",
			data: {
				labels: ["Won", "Lost"],
				datasets: [{
					label: "Opportunities",
					data: [data.lost_vs_won.Won, data.lost_vs_won.Lost],
				}],
			},
		});

		const chart2 = new Chart(document.getElementById("activity_pie"), {
			type: "pie",
			data: {
				labels: Object.keys(data.activity),
				datasets: [{
					data: Object.values(data.activity),
				}],
			},
		});

		const chart3 = new Chart(document.getElementById("leads_medium_donut"), {
			type: "doughnut",
			data: {
				labels: Object.keys(data.leads_by_medium),
				datasets: [{
					data: Object.values(data.leads_by_medium),
				}],
			},
		});

    		const chart4 = new Chart(document.getElementById("leads_campaign_chart"), {
			type: "bar",
			data: {
				labels: Object.keys(data.leads_by_campaign),
				datasets: [{
					label: "Leads",
					data: Object.values(data.leads_by_campaign),
					backgroundColor: "#42A5F5",
				}],
			},
		});

		this._charts = [chart1, chart2, chart3, chart4];
		this.state.leads_by_month = data.leads_by_month;
	}

	onFilterChange(ev) {
		const filter = ev.target.value;

		this.currentFilter = parseInt(ev.target.value);

		this._fetch_data(filter);
		this.loadCharts(filter);
	}



	async redirect_to_leads() {

		const filter = document.getElementById("crm_filter").value;
		let result = await this.orm.call("crm.lead", "get_tiles_data", [], {
			context: {
				filter
			}
		});
		this.action.doAction({
			type: 'ir.actions.act_window',
			target: 'current',
			res_model: 'crm.lead',
			views: [
				[false, 'list'],
				[false, 'form']
			],
			domain: [
				['id', 'in', result.my_leads]
			],
		});
	}

	async redirect_to_opportunity() {
		const filter = document.getElementById("crm_filter").value;
		let result = await this.orm.call("crm.lead", "get_tiles_data", [], {
			context: {
				filter
			}
		});
		this.action.doAction({
			type: 'ir.actions.act_window',
			target: 'current',
			res_model: 'crm.lead',
			views: [
				[false, 'list'],
				[false, "form"]
			],
			domain: [
				['id', 'in', result.my_opportunity]
			],
		});
	}

}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);