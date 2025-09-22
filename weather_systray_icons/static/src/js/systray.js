/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";

/**
 * Systray Weather Icon
 */
class SystrayWeatherIcon extends Component {

    setup() {
        this.dialog = useService("dialog");
        console.log("aca",this)

        // Default weather data
        this.weather = {
            date: "--",
            temp: "--",
            condition: "--",
            description: "Fetching weather...",
            city: "--",
            last_update: "--"
//            icon:"--"
        };

        this.fetchWeather();
    }

    async fetchWeather() {
        const apiKey = "94195601549010db471631e5033a379f";

        if (!navigator.geolocation) {
            this.weather.description = "Geolocation not supported";
            return;
        }

        navigator.geolocation.getCurrentPosition(async (pos) => {
            try {
                const lat = pos.coords.latitude;
                const lon = pos.coords.longitude;
                const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
                const res = await fetch(url);
                const data = await res.json();
                console.log('data',data)

                this.weather = {
                    date: new Date().toLocaleDateString(),
                    temp: data.main?.temp ?? "--",
                    condition: data.weather?.[0]?.main ?? "--",
                    description: data.weather?.[0]?.description ?? "--",
                    city: data.name ?? "--",
                    last_update: new Date().toLocaleString(),
                    icon: data.weather?.[0]?.icon ?? "--",
                    temp_min:data.main?.temp_min ?? "--",
                    temp_max:data.main?.temp_max ?? "--",
                };
                this.render();
            } catch (e) {
                this.weather.description = "Weather fetch failed";
                this.render();
            }
        }, () => {
            this.weather.description = "Location access denied";
            this.render();
        });
    }

    openPopup() {
        console.log("Opening Weather Popup…", this.weather); // ✅ Debug

        this.dialog.add(WeatherPopup, {
            props: { weather: this.weather },
            title: "Weather Info",
        });
    }
}

/**
 * Popup Component
 */
class WeatherPopup extends Component {
    setup(){
    console.log("WeatherPopup",this)
    }
    static components = { Dialog };
    static template = "weather_systray_icons.WeatherPopup";
    static props = { weather: { type: Object, optional: true } };

}


SystrayWeatherIcon.template = "weather_systray_icons.SystrayWeatherIcon";

// Register in systray
registry.category("systray").add("SystrayWeatherIcon", {
    Component: SystrayWeatherIcon,
}, { sequence: 1 });










/////** @odoo-module **/
//
//import { registry } from "@web/core/registry";
//import { useService } from "@web/core/utils/hooks";
//import { Component } from "@odoo/owl";
//import { Dropdown } from "@web/core/dropdown/dropdown";
//import { DropdownItem } from "@web/core/dropdown/dropdown_item";
//
///**
// * Systray Weather Icon
// */
//class SystrayWeatherIcon extends Component {
//
//    setup() {
//        this.dialog = useService("dialog");
//        console.log("aca",this)
//
////        // Default weather data
////        this.weather = {
////            date: "--",
////            temp: "--",
////            condition: "--",
////            description: "Fetching weather...",
////            city: "--",
////            last_update: "--"
//////            icon:"--"
////        };
//
//        this.fetchWeather();
//    }
//
//    async fetchWeather() {
//        const apiKey = "94195601549010db471631e5033a379f";
//
////        if (!navigator.geolocation) {
////            this.weather.description = "Geolocation not supported";
////            return;
////        }
//
//        navigator.geolocation.getCurrentPosition(async (pos) => {
//            try {
//                const lat = pos.coords.latitude;
//                const lon = pos.coords.longitude;
//                const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
//                const res = await fetch(url);
//                const data = await res.json();
//                console.log('data',data)
//
//                this.weather = {
//                    date: new Date().toLocaleDateString(),
//                    temp: data.main?.temp ?? "--",
//                    condition: data.weather?.[0]?.main ?? "--",
//                    description: data.weather?.[0]?.description ?? "--",
//                    city: data.name ?? "--",
//                    last_update: new Date().toLocaleString(),
//                    icon: data.weather?.[0]?.icon ?? "--",
//                    temp_min:data.main?.temp_min ?? "--",
//                    temp_max:data.main?.temp_max ?? "--",
//                };
//                this.render();
//            } catch (e) {
//                this.weather.description = "Weather fetch failed";
//                this.render();
//            }
//        }, () => {
//            this.weather.description = "Location access denied";
//            this.render();
//        });
//    }
//
//    openPopup() {
//        console.log("Opening Weather Popup…", this); // ✅ Debug
//        this.dialog.add(SystrayWeatherIcon, {
//            props: { weather: this.weather },
//            title: "Weather Info",
//        });
//    }
//}
//
///**
// * Popup Component
//// */
////class WeatherPopup extends Component {
////    setup(){
////    console.log("WeatherPopup",this)
////    }
//////    static components = { Dialog };
////    static template = "weather_systray_icons.WeatherPopup";
////    static props = { weather: { type: Object, optional: true } };
////
////}
//
//SystrayWeatherIcon.template = "weather_systray_icons.SystrayWeatherIcon";
//SystrayWeatherIcon.components = {Dropdown};
//
//// Register in systray
//registry.category("systray").add("SystrayWeatherIcon", {
//    Component: SystrayWeatherIcon,
//}, { sequence: 1 });