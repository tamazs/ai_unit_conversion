import { useState } from 'react';
import { Outlet, useNavigate } from "react-router-dom";
import '../App.css';

export default function TopPanel() {
    const [activeTab, setActiveTab] = useState(null);
    const navigate = useNavigate();

    return (
        <div className="app-container">
            <header className="tab-bar">
                <button
                    className={`tab-button ${activeTab === 'kmh-mih' ? 'active' : ''}`}
                    onClick={() => { setActiveTab('kmh-mih'); navigate('/kmh_mih')}}
                >
                    Km/h ↔ mi/h
                </button>

                <button
                    className={`tab-button ${activeTab === 'c-f' ? 'active' : ''}`}
                    onClick={() => {setActiveTab('c-f'); navigate('/celsius_fahrenheit')}}
                >
                    °C ↔ °F
                </button>

                <button
                    className={`tab-button ${activeTab === 'kg-lbs' ? 'active' : ''}`}
                    onClick={() => { setActiveTab('kg-lbs'); navigate('/kg_lbs')}}
                >
                    kg ↔ lbs
                </button>
            </header>

            <Outlet/>
        </div>
    );
}