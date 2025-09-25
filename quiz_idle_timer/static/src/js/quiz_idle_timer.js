/** @odoo-module **/
console.log("/** @odoo-module **/")
var timeout = 5,// Timeout in seconds
//var timer = 0,
interval = 1000,//interval time in milliseconds ,1 sec=1000 milliseconds
my_time=0;
//submit = $(".btn-primary['value=start']")
    function mouseHasMoved(e){
        my_time=0
        document.onmousemove = null;
        document.onkeydown = null;
        console.log("mouseHasMoved",my_time)
    }
    setInterval(function(){
        my_time=my_time+1
//        const submit = $(".btn-primary['value=start']")

        const submit = document.querySelector('.btn-primary');
        const secondary_submit = document.querySelector('.btn-secondary');
        if (my_time==timeout){
        my_time=0
//        if(btn-primary){
                submit.click()
                if(secondary_submit){
                secondary_submit.click()
                }
//
//        }
//      console.log("===")
//        {
//            trigger: 'button.btn-primary:contains("Manufacture")',
//            run: "click",
//        },

        }
        console.log('idle',my_time)

        document.onmousemove = function(e){
            mouseHasMoved(e);
        }
        document.onkeydown=function(e){
            mouseHasMoved(e);
        }
    }, interval);

















/** @odoo-module **/
//import { registry } from "@web/core/registry";
//import { FieldChar } from "@web/views/fields/char/char_field";
//
//export class QuizIdleTimer extends FieldChar {
//    setup() {
//        super.setup();
//        this.updateInterval = null;
//        this.remainingSeconds = 0;
//    }
//
//    mounted() {
//        super.mounted();
//        this.startCountdown();
//    }
//
//    willUnmount() {
//        super.willUnmount();
//        this.stopCountdown();
//    }
//
//    startCountdown() {
//        this.stopCountdown();
//
//        // Get the value from the field, which is in minutes (e.g., 0.16)
//        const minutesFloat = this.props.record.data.idle_time_limit;
//
//        // Convert minutes to seconds
//        this.remainingSeconds = Math.floor(minutesFloat * 60);
//
//        if (this.remainingSeconds <= 0) {
//            this.state.value = "EXPIRED";
//            return;
//        }
//
//        this.updateInterval = setInterval(() => {
//            if (this.remainingSeconds <= 0) {
//                this.state.value = "EXPIRED";
//                this.stopCountdown();
//                return;
//            }
//
//            const minutes = Math.floor(this.remainingSeconds / 60);
//            const seconds = this.remainingSeconds % 60;
//
//            const formattedMinutes = String(minutes).padStart(2, '0');
//            const formattedSeconds = String(seconds).padStart(2, '0');
//
//            this.state.value = `${formattedMinutes}:${formattedSeconds}`;
//            this.remainingSeconds--;
//            this.render();
//        }, 1000);
//    }
//
//    stopCountdown() {
//        if (this.updateInterval) {
//            clearInterval(this.updateInterval);
//        }
//    }
//}
//QuizIdleTimer.template = "quiz_idle_timer.QuizIdleTimerTemplate";
//registry.category("fields").add("quiz_idle_timer", QuizIdleTimer);







