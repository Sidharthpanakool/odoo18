/** @odoo-module **/
console.log("aaa")
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
class SystrayIcon extends Component {
   setup() {
       super.setup();
       this.notification = useService("notification");
       console.log(this)
   }
//   showNotification() {
//       this.notification.add("Hello! This is a notification", {
//           title: "Systray Notification",
//           type: "info",
//           sticky: false,
//       });
//   }
}
SystrayIcon.template = "systray_icon";
export const systrayItem = {
   Component: SystrayIcon,
};
registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 1 });


///** @odoo-module */
//
//import { useService } from '@web/core/utils/hooks';
//import { Component } from '@odoo/owl';
//import { registry } from "@web/core/registry";
//
//export class LocationUpdater extends Component {
//    static template = "odoo_live_location.location_updater_template";
//
//    setup() {
//        console.log("setup");
//        this.rpc = useService("rpc");
//        this.getAndUpdateLocation(1);
//    }
//
//    async updateLocationOnServer(latitude, longitude, recordId) {
//        console.log("Updating location on server...");
//        const response = await this.rpc({
//            model: 'location.info',
//            method: 'update_location',
//            args: [[recordId], {
//                'partner_latitude': latitude,
//                'partner_longitude': longitude,
//            }],
//        });
//        console.log("Location updated:", response);
//    }
//
//    async getAndUpdateLocation(recordId) {
//        console.log("Fetching location...");
//        if (navigator.geolocation) {
//            navigator.geolocation.getCurrentPosition(async (position) => {
//                const latitude = position.coords.latitude;
//                const longitude = position.coords.longitude;
//                await this.updateLocationOnServer(latitude, longitude, recordId);
//                console.log('Location updated successfully!');
//            }, (error) => {
//                console.error("Error fetching location:", error);
//            });
//        } else {
//            console.error("Geolocation is not supported by this browser.");
//        }
//    }
//}
//
//registry.category("actions").add("LocationUpdater", LocationUpdater);
