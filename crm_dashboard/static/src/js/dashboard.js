/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, onMounted, useState ,onWillStart, useRef} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
  setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_data();
        this.action = useService("action");
        this.loadCharts();

        console.log(this)
        }

  async _fetch_data(filter='year'){
    let result = await this.orm.call("crm.lead", "get_tiles_data", [], {context: {filter}});

    console.log("ree",result)

    document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
    document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
    document.getElementById('exp_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
    document.getElementById('revenue').innerHTML = `<span>${result.currency}${result.invoice_amt_sum}</span>`;
    document.getElementById('won').innerHTML = `<span>${result.won}</span>`;
    document.getElementById('loss').innerHTML = `<span>${result.loss}</span>`;
  }

    async loadCharts() {

        console.log('this',this)

        const data = await this.orm.call("crm.lead", "get_chart_data", ['year']);
        console.log("d",data)
        console.log("leads_by_month",data.leads_by_month)
//        console.log("month",data.leads_by_month[{month}]);
//        console.log("count",data.leads_by_month{count});

           data.leads_by_month.forEach(item => {

            document.getElementById('month').innerHTML = `<span>${item.month}</span>`;
            document.getElementById('lead_count').innerHTML = `<span>${item.count}</span>`;

            console.log(`Month: ${item.month}, Count: ${item.count}`);
           });


//        document.getElementById('month').innerHTML = `<span>${data.leads_by_month}</span>`;
//        document.getElementById('lead_count').innerHTML = `<span>${data.leads_by_month}</span>`;

        // Lost vs Won (Bar)
        const chart1 = new Chart(document.getElementById("lost_lead_chart"), {
            type: "bar",
            data: {
                labels: ["Won", "Lost"],
                datasets: [{
                    label: "Opportunities",
                    data: [data.lost_vs_won.Won, data.lost_vs_won.Lost],
//                    backgroundColor: ["#4CAF50", "#F44336"],
                }],
            },
        });

        // Activity Pie
        const chart2 = new Chart(document.getElementById("activity_pie"), {
            type: "pie",
            data: {
                labels: Object.keys(data.activity),
                datasets: [{
                    data: Object.values(data.activity),
//                    backgroundColor: ["#2196F3", "#FFC107", "#FF5722", "#9C27B0"],
                }],
            },
        });

        // Leads by Medium (Doughnut)
        const chart3 = new Chart(document.getElementById("leads_medium_donut"), {
            type: "doughnut",
            data: {
                labels: Object.keys(data.leads_by_medium),
                datasets: [{
                    data: Object.values(data.leads_by_medium),
//                    backgroundColor: ["#03A9F4", "#E91E63", "#8BC34A", "#FF9800"],
                }],
            },
        });

        // Leads by Campaign (Bar)
        const chart4 = new Chart(document.getElementById("leads_campaign_chart"), {
            type: "bar",
            data: {
                labels: Object.keys(data.leads_by_campaign),
                datasets: [{
                    label: "Leads",
                    data: Object.values(data.leads_by_campaign),
//                    backgroundColor: "#42A5F5",
                }],
            },
        });

        this._charts = [chart1, chart2, chart3, chart4];
    }

    onFilterChange(ev){
    const filter = ev.target.value;
    this._fetch_data(filter);
    this.loadCharts();
}


  async redirect_to_leads() {
//  console.log("crmDaaaaaaaaaaaa",this)
       let result = await this.orm.call("crm.lead", "get_tiles_data", [], {});
            console.log('re',result)
            console.log(typeof(result.user))

            const my_lead_list= result.my_leads
            const regex = /\((.*?)\)/;
            const matches= my_lead_list.match(regex);
            if (matches && matches[1]) {

                const numbersAsString = matches[1].split(',');
                const numbers = numbersAsString.map(Number);

                console.log("matches",matches)
                console.log("matches[1]",matches[1])
                console.log('numbersAsString',numbersAsString)
                console.log('numbers',numbers);
                console.log('type_my_leads',typeof(result.my_leads))
                console.log('type_of_numbers',typeof(numbers))

                this.action.doAction({
                type: 'ir.actions.act_window',
                target: 'current',
                res_model: 'crm.lead',
                views: [[false, 'list'], [false, "form"]],
                domain: [['id','in',numbers]],
            });
            }
            }
    async redirect_to_opportunity(){
        let result = await this.orm.call("crm.lead", "get_tiles_data", [], {});
        console.log(result)

        const my_opportunity= result.my_opportunity
        const regex = /\((.*?)\)/;
        const matches= my_opportunity.match(regex);
        if (matches && matches[1]) {

            const numbersAsString = matches[1].split(',');
            const numbers = numbersAsString.map(Number);

            console.log("matches",matches)
            console.log("matches[1]",matches[1])
            console.log('numbersAsString',numbersAsString)
            console.log('numbers',numbers);
            console.log('type_my_leads',typeof(result.my_opportunity))
            console.log('type_of_numbers',typeof(numbers))

            this.action.doAction({
            type: 'ir.actions.act_window',
            target: 'current',
            res_model: 'crm.lead',
            views: [[false, 'list'], [false, "form"]],
            domain: [['id','in',numbers]],
        });
        }

    }

}

CrmDashboard.template = "crm_dashboard.CrmDashboard";
// Register the component with the action tag
actionRegistry.add("crm_dashboard_tag", CrmDashboard);
