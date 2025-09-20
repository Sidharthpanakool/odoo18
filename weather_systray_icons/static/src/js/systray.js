/** @odoo-module **/
console.log("aaa")
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
class SystrayIcon extends Component {
   setup() {
       super.setup();
       this.notification = useService("notification");
   }
   showNotification() {
       this.notification.add("Hello! This is a notification", {
           title: "Systray Notification",
           type: "info",
           sticky: false,
       });
   }
}
SystrayIcon.template = "systray_icon";
export const systrayItem = {
   Component: SystrayIcon,
};
registry.category("systray").add("systray_icon", systrayItem, { sequence: 1 });


