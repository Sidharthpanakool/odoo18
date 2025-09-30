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

        console.log(this)
  }
  async _fetch_data(){
     let result = await this.orm.call("crm.lead", "get_tiles_data", [], {});
     document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
     document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
     document.getElementById('exp_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
     document.getElementById('revenue').innerHTML = `<span>${result.currency}${result.invoice_amt_sum}</span>`;
  }

}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
// Register the component with the action tag
actionRegistry.add("crm_dashboard_tag", CrmDashboard);
