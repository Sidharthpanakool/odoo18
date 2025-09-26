/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

console.log("console")

publicWidget.registry.SurveyIdleTimer = publicWidget.Widget.extend({
 selector: ".o_survey_form",
 start: function () {
//                this.orm = this.bindService("orm");
//                console.log("bind",this.orm)
//                const searchRead= this.orm.searchRead('survey.survey',[],[])
//                console.log('searchRead',searchRead)
//                console.log("this",this)

    var timeout = 5,// Timeout in seconds
    //var timer = 0,
    interval = 1000,//interval time in milliseconds ,1 sec=1000 milliseconds
    my_time=0;
        function mouseHasMoved(e){
            my_time=0
            document.onmousemove = null;
            document.onkeydown = null;
            console.log("mouseHasMoved",my_time)
        }
        setInterval(function(){
            my_time=my_time+1
            const start = document.querySelector('.btn-primary[value="start"]');
            const next = document.querySelector('.btn-primary[value="next"]');
            const finish = document.querySelector('.btn-secondary[value="finish"]');
            const next_skipped = document.querySelector('.btn-primary[value="next-skipped"]')

            if (my_time==timeout){
                my_time=0
                if(start){
                        start.click()
                        console.log('start')
                }else if(next){
                        next.click()
                        console.log("next")
                }else if(finish){
                        finish.click()
                        console.log('Finish')
                }else if(next_skipped){
                        next_skipped.click()
                        console.log('next_skipped')
                }
            }
            console.log('idle',my_time)

            document.onmousemove = function(e){
                mouseHasMoved(e);
            }
            document.onkeydown=function(e){
                mouseHasMoved(e);
            }
        }, interval);
    }
})