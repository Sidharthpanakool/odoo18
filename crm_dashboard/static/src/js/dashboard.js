/** @odoo-module **/
import { registry } from "@web/core/registry";
//import { Component } from "@odoo/owl";
import { Component, onMounted, useState ,onWillStart, useRef} from "@odoo/owl";

import { useService } from "@web/core/utils/hooks";
//import { loadJS } "@web/core/assets";
//import Chart from 'chart.js/auto';


const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
  setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_data();
        this.action = useService("action");

//        onWillStart(async ()=>{
//            await loadJS("https://cdn.jsdelivr.net/npm/chart.js")
//        })


//        console.log("a",this)
//        this.Chart = null;

//        this.state = useState({chartData: null,});
//        onMounted(() => this.loadCharts());

  }

//  async _fetch_data(){
//     let result = await this.orm.call("crm.lead", "get_tiles_data", [], {});
//     document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
//     document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
//     document.getElementById('exp_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
//     document.getElementById('revenue').innerHTML = `<span>${result.currency}${result.invoice_amt_sum}</span>`;
//     document.getElementById('won').innerHTML = `<span>${result.won}</span>`;
//     document.getElementById('loss').innerHTML = `<span>${result.loss}</span>`;
//
//  }

  async _fetch_data(filter='year'){
    let result = await this.orm.call("crm.lead", "get_tiles_data", [], {context: {filter}});

    console.log("ree",result)
//    this.updateTiles(result);
//}
//
//updateTiles(result){
    document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
    document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
    document.getElementById('exp_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
    document.getElementById('revenue').innerHTML = `<span>${result.currency}${result.invoice_amt_sum}</span>`;
    document.getElementById('won').innerHTML = `<span>${result.won}</span>`;
    document.getElementById('loss').innerHTML = `<span>${result.loss}</span>`;
}

onFilterChange(ev){
    const filter = ev.target.value;
    this._fetch_data(filter);
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


//    async loadCharts() {
//    console.log("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
//        const data = await this.orm.call("crm.lead", "get_chart_data", ["year"]);
//
////        console.log("D",data)
////        this.state.chartData = data;
////        this.renderCharts(data);
////    }
////
////    renderCharts(data) {
//
//        // Lost vs Won
//        new Chart(document.getElementById("lost_lead_chart"), {
//            type: "bar",
//            data: {
//                labels: ["Won", "Lost"],
//                datasets: [{
//                    label: "Opportunities",
//                    data: [data.lost_vs_won.Won, data.lost_vs_won.Lost],
//                    backgroundColor: ["#4CAF50", "#F44336"],
//                }],
//            },
//        });
//
////        // Activity Pie
////        new Chart(document.getElementById("activity_pie"), {
////            type: "pie",
////            data: {
////                labels: Object.keys(data.activity),
////                datasets: [{
////                    data: Object.values(data.activity),
////                }],
////            },
////        });
////
////        // Leads by Month Table
////        const tbody = document.querySelector("#leads_month_table tbody");
////        tbody.innerHTML = "";
////        data.leads_by_month.forEach((r) => {
////            const row = `<tr><td>${r.month}</td><td>${r.count}</td></tr>`;
////            tbody.insertAdjacentHTML("beforeend", row);
////        });
////
////        // Leads by Medium Donut
////        new Chart(document.getElementById("leads_medium_donut"), {
////            type: "doughnut",
////            data: {
////                labels: Object.keys(data.leads_by_medium),
////                datasets: [{
////                    data: Object.values(data.leads_by_medium),
////                }],
////            },
////        });
////
////        // Leads by Campaign
////        new Chart(document.getElementById("leads_campaign_chart"), {
////            type: "bar",
////            data: {
////                labels: Object.keys(data.leads_by_campaign),
////                datasets: [{
////                    data: Object.values(data.leads_by_campaign),
////                    backgroundColor: "#42A5F5",
////                }],
////            },
////        });
//    }



}

//export class OwlCrmDashboard extends Component {}
//
//OwlCrmDashboard.template= "crm_dashboard.CrmDashboard";
//
//OwlCrmDashboard.component =  { KpiCard}
//
//registry.category("actions").add("crm_dashboard.CrmDashboard",OwlCrmDashboard)


CrmDashboard.template = "crm_dashboard.CrmDashboard";
// Register the component with the action tag
actionRegistry.add("crm_dashboard_tag", CrmDashboard);




///** @odoo-module **/
//
//import { registry } from "@web/core/registry";
//import { Component, onMounted, useState } from "@odoo/owl";
//import { useService } from "@web/core/utils/hooks";
//
//class CRMDashboard extends Component {
//    setup() {
//        this.orm = useService("orm");
//        this.state = useState({
//            chartData: null,
//        });
//        onMounted(() => this.loadCharts());
//    }
//
//    async loadCharts() {
//        const data = await this.orm.call("crm.dashboard", "get_chart_data", ["year"]);
//        this.state.chartData = data;
//        this.renderCharts(data);
//    }
//
//    renderCharts(data) {
//        // Lost vs Won
//        new Chart(document.getElementById("lost_lead_chart"), {
//            type: "bar",
//            data: {
//                labels: ["Won", "Lost"],
//                datasets: [{
//                    label: "Opportunities",
//                    data: [data.lost_vs_won.Won, data.lost_vs_won.Lost],
//                    backgroundColor: ["#4CAF50", "#F44336"],
//                }],
//            },
//        });
//
//        // Activity Pie
//        new Chart(document.getElementById("activity_pie"), {
//            type: "pie",
//            data: {
//                labels: Object.keys(data.activity),
//                datasets: [{
//                    data: Object.values(data.activity),
//                }],
//            },
//        });
//
//        // Leads by Month Table
//        const tbody = document.querySelector("#leads_month_table tbody");
//        tbody.innerHTML = "";
//        data.leads_by_month.forEach((r) => {
//            const row = `<tr><td>${r.month}</td><td>${r.count}</td></tr>`;
//            tbody.insertAdjacentHTML("beforeend", row);
//        });
//
//        // Leads by Medium Donut
//        new Chart(document.getElementById("leads_medium_donut"), {
//            type: "doughnut",
//            data: {
//                labels: Object.keys(data.leads_by_medium),
//                datasets: [{
//                    data: Object.values(data.leads_by_medium),
//                }],
//            },
//        });
//
//        // Leads by Campaign
//        new Chart(document.getElementById("leads_campaign_chart"), {
//            type: "bar",
//            data: {
//                labels: Object.keys(data.leads_by_campaign),
//                datasets: [{
//                    data: Object.values(data.leads_by_campaign),
//                    backgroundColor: "#42A5F5",
//                }],
//            },
//        });
//    }
//}
//
//registry.category("actions").add("crm_dashboard_tag", CRMDashboard);


