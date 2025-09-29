/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.SurveyIdleTimer = publicWidget.Widget.extend({
    selector: ".o_survey_form",
    start: async function () {

        this._super.apply(this,arguments);
        this.orm=this.bindService('orm')
        this.options=this.$('form').data()

        const survey_data=await this.orm.searchRead('survey.survey', [['access_token','=',this.options.surveyToken]],
        ['quiz_idle_time','idle_time_limit']);

        if(survey_data){
            const idle_time_enabled = survey_data[0].quiz_idle_time;
            const idle_time =  survey_data[0].idle_time_limit;

            if(idle_time_enabled && idle_time>0){
                this.bindIdleTimeLimit(idle_time);
                document.getElementById("time_limit").innerHTML = idle_time;
            }
        }
        },
        bindIdleTimeLimit: function (idle_time){
            let timeout=0;
            const interval=1000;

            function mouseHasMoved(e){
                timeout=0;
                document.onmousemove = null;
                document.onkeydown = null;
            }
            setInterval(function (){


            document.getElementById("timer").innerHTML = timeout;
            timeout++;

            if (timeout == idle_time){
                timeout=0;
                const start = document.querySelector('.btn-primary[value="start"]');
                const next = document.querySelector('.btn-primary[value="next"]');
                const finish = document.querySelector('.btn-secondary[value="finish"]');
                const next_skipped = document.querySelector('.btn-primary[value="next-skipped"]')

                if(start){
                        start.click()
                }else if(next){
                        next.click()
                }else if(finish){
                        finish.click()
                }else if(next_skipped){
                        next_skipped.click()
                }
                }
                document.onmousemove = function(e){
                    mouseHasMoved(e);
                }
                document.onkeydown=function(e){
                    mouseHasMoved(e);
                }
            }, interval);
    },
});
export default publicWidget.registry.SurveyIdleTimer;