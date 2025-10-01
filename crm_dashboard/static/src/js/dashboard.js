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
     document.getElementById('won').innerHTML = `<span>${result.won}</span>`;
     document.getElementById('loss').innerHTML = `<span>${result.loss}</span>`;



  }
  redirect_to_leads(group, filter="all") {
               console.log("aaa")

//
////        this.dropdown.close();
////        const context = {
////            // Necessary because activity_ids of mail.activity.mixin has auto_join
////            // So, duplicates are faking the count and "Load more" doesn't show up
////            force_search_count: 1,
////        };
//
//        if (group.model === "account.move") {
//            this.action.doAction("account.view_invoice_form_l10n_sg", {
//                additionalContext: {
////                    active_ids: group.activity_ids,
//                    active_model: "account.move",
//                },
//            });
//            return;
//        }
////        this.action.doAction(
////            {
//////                context,
//////                domain,
////                name: group.name,
////                res_model: account.move,
////                search_view_id: [false],
////                type: "ir.actions.act_window",
////                views,
////            },
////            {
////                clearBreadcrumbs: true,
////                viewType: group.view_type,
////            }
////        );
//            this.action.doAction({
//            type: 'ir.actions.act_window',
//            name: _t('crm.lead.form'),
//            target: 'current',
//            res_id: activity.res_id,
//            res_model: 'crm.lead',
//            views: [[false, 'form']],
//            });

////        if (filter === "all") {
////            context["search_default_activities_overdue"] = 1;
////            context["search_default_activities_today"] = 1;
////        }
////        else if (filter === "overdue") {
////            context["search_default_activities_overdue"] = 1;
////        }
////        else if (filter === "today") {
////            context["search_default_activities_today"] = 1;
////        }
////        else if (filter === "upcoming_all") {
////            context["search_default_activities_upcoming_all"] = 1;
////        }
//
////        let domain = [["activity_user_id", "=", this.userId]];
////        if (group.domain) {
////            domain = Domain.and([domain, group.domain]).toList();
////        }
////        const views = this.availableViews(group);
////    }
    }

//  redirect_to_leads(group, filter = "all") {
//        // fetch the data from the button otherwise fetch the ones from the parent (.o_ActivityMenuView_activityGroup).
//        const context = {};
//        if (group.model === "crm.lead") {
//            this.dropdown.close();
//            if (filter === "my") {
//                context["search_default_activities_overdue"] = 1;
//                context["search_default_activities_today"] = 1;
//            } else {
//                context["search_default_activities_" + filter] = 1;
//            }
//            // Necessary because activity_ids of mail.activity.mixin has auto_join
//            // So, duplicates are faking the count and "Load more" doesn't show up
//            context["force_search_count"] = 1;
//            context["active_test"] = 0; // to show lost leads in the activity
//            this.action.doAction("crm.crm_lead_action_my_activities", {
//                additionalContext: context,
//                clearBreadcrumbs: true,
//            });
//        } else {
//            return super.openActivityGroup(group, filter);
//        }
//    }




}
CrmDashboard.template = "crm_dashboard.CrmDashboard";
// Register the component with the action tag
actionRegistry.add("crm_dashboard_tag", CrmDashboard);
