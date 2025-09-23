/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState, onMounted } from "@odoo/owl";
import { Dropdown } from "@web/core/dropdown/dropdown";

class SystrayWeatherDropdown extends Component {
    setup() {
        this.state = useState({
            date: "--",
            temp: "--",
            condition: "--",
            description: "Fetching weather...",
            city: "--",
            last_update: "--"
        });
        onMounted(() => {
            this.fetchWeather();
        });
    }
    async fetchWeather() {
        const apiKey = "94195601549010db471631e5033a379f";
        if (!navigator.geolocation) {
            this.state.description = "Geolocation not supported";
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

                this.state.date = new Date().toLocaleDateString();
                this.state.temp = data.main?.temp ?? "--";
                this.state.condition = data.weather?.[0]?.main ?? "--";
                this.state.description = data.weather?.[0]?.description ?? "--";
                this.state.city = data.name ?? "--";
                this.state.last_update = new Date().toLocaleString();
                this.state.icon=data.weather?.[0]?.icon ?? "--";
                this.state.temp_min=data.main?.temp_min ?? "--";
                this.state.temp_max=data.main?.temp_max ?? "--";

            } catch (e) {
                this.state.description = "Weather fetch failed";
            }
        }, () => {
            this.state.description = "Location access denied";
        });
    }
}

SystrayWeatherDropdown.template = "weather_systray_dropdown";
SystrayWeatherDropdown.components = { Dropdown};

export const systrayItem = {
    Component: SystrayWeatherDropdown,
};
registry.category("systray").add("SystrayWeatherDropdown", systrayItem, { sequence: 100 });