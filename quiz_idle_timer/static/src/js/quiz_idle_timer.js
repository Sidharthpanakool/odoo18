///* @odoo-module */
//import { Component, useState } from "@odoo/owl";
//import { rpc } from "@web/core/network/rpc";
//import { registry } from "@web/core/registry";
//import { session } from "@web/session";
//import { useService } from "@web/core/utils/hooks";
//import { _t } from "@web/core/l10n/translation";
//const { onMounted, mount } = owl
//class TimerSystrayItem extends Component{
//    static template="auto_logout_idle_user_odoo.TimerSystray"
//    setup(){
//        super.setup();
//        this.get_idle_time();
//        this.state = useState({
//           idle_time: null,
//        })
//    }
//    get_idle_time() {
//        var self = this
//        var now = new Date().getTime();
//        rpc('/get_idle_time/timer', {
//        }).then((data) => {
//            if (data) {
//                self.minutes = data
//                self.idle_timer()
//            }
//         });
//    }
//    /**
//    passing values of the countdown to the xml
//    */
//    idle_timer() {
//        var self = this
//        var nowt = new Date().getTime();
//        var date = new Date(nowt);
//        date.setMinutes(date.getMinutes() + self.minutes);
//        var updatedTimestamp = date.getTime();
//        /** Running the count down using setInterval function */
//        var idle = setInterval(function() {
//            var now = new Date().getTime();
//            var distance = updatedTimestamp - now;
//            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
//            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//            var seconds = Math.floor((distance % (1000 * 60)) / 1000);
//            if (hours && days) {
//                self.state.idle_time = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
//            } else if (hours) {
//                self.state.idle_time = hours + "h " + minutes + "m " + seconds + "s ";
//            } else {
//                self.state.idle_time = minutes + "m " + seconds + "s ";
//            }
//            /** if the countdown is zero the link is redirect to the login page*/
//            if (distance < 0) {
//                clearInterval(idle);
//                self.state.idle_time = "EXPIRED";
//                location.replace("/web/session/logout")
//            }
//        }, 1000);
//        /**
//        checking if the onmouse-move event is occur
//        */
//        document.onmousemove = () => {
//            var nowt = new Date().getTime();
//            var date = new Date(nowt);
//            date.setMinutes(date.getMinutes() + self.minutes);
//            updatedTimestamp = date.getTime();
//        };
//         /**
//        checking if the onkeypress event is occur
//        */
//        document.onkeypress = () => {
//            var nowt = new Date().getTime();
//            var date = new Date(nowt);
//            date.setMinutes(date.getMinutes() + self.minutes);
//            updatedTimestamp = date.getTime();
//        };
//        /**
//        checking if the onclick event is occur
//        */
//        document.onclick = () => {
//            var nowt = new Date().getTime();
//            var date = new Date(nowt);
//            date.setMinutes(date.getMinutes() + self.minutes);
//            updatedTimestamp = date.getTime();
//        };
//        /**
//        checking if the ontouchstart event is occur
//        */
//        document.ontouchstart = () => {
//            var nowt = new Date().getTime();
//            var date = new Date(nowt);
//            date.setMinutes(date.getMinutes() + self.minutes);
//            updatedTimestamp = date.getTime();
//        }
//        /**
//        checking if the onmousedown event is occur
//        */
//        document.onmousedown = () => {
//            var nowt = new Date().getTime();
//            var date = new Date(nowt);
//            date.setMinutes(date.getMinutes() + self.minutes);
//            updatedTimestamp = date.getTime();
//        }
//        /**
//        checking if the onload event is occur
//        */
//        document.onload = () => {
//            var nowt = new Date().getTime();
//            var date = new Date(nowt);
//            date.setMinutes(date.getMinutes() + self.minutes);
//            updatedTimestamp = date.getTime();
//        }
//    }
//}
//export const systrayItem = {
//    Component: TimerSystrayItem
//};
//registry.category("systray").add("auto_logout_idle_user_odoo.TimerSystray",systrayItem, {sequence:25});







/** @odoo-module **/

//import { deserializeDateTime } from "@web/core/l10n/dates";
//import publicWidget from "@web/legacy/js/public/public_widget";
//const { DateTime } = luxon;
//import { useIdleTimer } from "./utils/use_idle_timer";


//publicWidget.registry.SurveyTimerWidget = publicWidget.Widget.extend({
//    //--------------------------------------------------------------------------
//    // Widget
//    //--------------------------------------------------------------------------
//
//    /**
//     * @override
//     */
//    init: function (parent, params) {
//        this._super.apply(this, arguments);
//        this.timer = params.timer;
//        this.timeLimitMinutes = params.timeLimitMinutes;
//        this.surveyTimerInterval = null;
//        this.timeDifference = null;
//        if (params.serverTime) {
//            this.timeDifference = DateTime.utc().diff(
//                deserializeDateTime(params.serverTime)
//            ).milliseconds;
//        }
//    },
//
//
//    /**
//    * Two responsabilities : Validate that time limit is not exceeded and Run timer otherwise.
//    * If end-user's clock OR the system clock  is de-synchronized before the survey is started, we apply the
//    * difference in timer (if time difference is more than 5 seconds) so that we can
//    * display the 'absolute' counter
//    *
//    * @override
//    */
//    start: function () {
//        var self = this;
//        return this._super.apply(this, arguments).then(function () {
//            self.countDownDate = DateTime.fromISO(self.timer, { zone: "utc" }).plus({
//                minutes: self.timeLimitMinutes,
//            });
//            if (Math.abs(self.timeDifference) >= 5000) {
//                self.countDownDate = self.countDownDate.plus({ milliseconds: self.timeDifference });
//            }
//            if (self.timeLimitMinutes <= 0 || self.countDownDate.diff(DateTime.utc()).seconds < 0) {
//                self.trigger_up('time_up');
//            } else {
//                self._updateTimer();
//                self.surveyTimerInterval = setInterval(self._updateTimer.bind(self), 1000);
//            }
//        });
//    },
//
//    // -------------------------------------------------------------------------
//    // Private
//    // -------------------------------------------------------------------------
//
//    _formatTime: function (time) {
//        return time > 9 ? time : '0' + time;
//    },
//
//    /**
//    * This function is responsible for the visual update of the timer DOM every second.
//    * When the time runs out, it triggers a 'time_up' event to notify the parent widget.
//    *
//    * We use a diff in millis and not a second, that we round to the nearest second.
//    * Indeed, a difference of 999 millis is interpreted as 0 second by moment, which is problematic
//    * for our use case.
//    */
//    _updateTimer: function () {
//        var timeLeft = Math.round(this.countDownDate.diff(DateTime.utc()).milliseconds / 1000);
//
//        if (timeLeft >= 0) {
//            var timeLeftMinutes = parseInt(timeLeft / 60);
//            var timeLeftSeconds = timeLeft - (timeLeftMinutes * 60);
//            this.$el.text(this._formatTime(timeLeftMinutes) + ':' + this._formatTime(timeLeftSeconds));
//        } else {
//            clearInterval(this.surveyTimerInterval);
//            this.trigger_up('time_up');
//        }
//    },
//});
//
//export default publicWidget.registry.SurveyTimerWidget;



// Timeout in seconds
var timeout = 10; // 10 seconds

// You don't have to change anything below this line, except maybe
// the alert('Welcome back!') :-)
// ----------------------------------------------------------------
var pos = '', prevpos = '', timer = 0, interval = timeout / 5 * 1000;
timeout = timeout * 1000 - interval;

function mouseHasMoved(e){

    console.log("mouseHasMoved")

    document.onmousemove = null;
    prevpos = pos;
    pos = e.pageX + '+' + e.pageY;
    if(timer > timeout){
        timer = 0;
//        alert('Welcome back!');

    }
}

setInterval(function(){
    console.log("idle")


    if(pos == prevpos){
//        alert('Time is running!');
        timer += interval;
    }else{
        timer = 0;
        prevpos = pos;
    }
    document.onmousemove = function(e){
        mouseHasMoved(e);
    }
}, interval);