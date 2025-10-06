/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
  setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_data();
        this.action = useService("action");

//        console.log(this)
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

}



CrmDashboard.template = "crm_dashboard.CrmDashboard";
// Register the component with the action tag
actionRegistry.add("crm_dashboard_tag", CrmDashboard);


