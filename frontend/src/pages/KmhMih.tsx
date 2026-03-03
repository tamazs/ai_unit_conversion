import { useState } from 'react';
import { useConverter } from '../useConversionCrud';
import '../App.css';

export default function KmhMih() {
    const [value, setValue] = useState('');
    const [unit, setUnit] = useState('km/h');
    const [result, setResult] = useState(null);
    const { convert, loading, error } = useConverter();

    const toggleUnit = () => {
        setUnit(prev => prev === 'km/h' ? 'mi/h' : 'km/h');
        setResult(null);
    };

    const handleConvert = async () => {
        if (!value) return;
        const prompt = `Convert ${value} ${unit === 'km/h' ? 'km/h to mi/h' : 'mi/h to km/h'}`;
        const response = await convert(prompt);
        if (response) setResult(response);
    };

    return (
        <div className="converter-page">
            <div className="converter-card">
                <h2 className="converter-title">Speed Converter</h2>

                <div className="input-row">
                    <input
                        className="converter-input"
                        type="number"
                        placeholder={`Enter ${unit}`}
                        value={value}
                        onChange={e => { setValue(e.target.value); setResult(null); }}
                        onKeyDown={e => e.key === 'Enter' && handleConvert()}
                    />
                    <button className="unit-toggle" onClick={toggleUnit}>
                        {unit === 'km/h' ? 'km/h → mi/h' : 'mi/h → km/h'}
                    </button>
                </div>

                <button className="convert-btn" onClick={handleConvert} disabled={loading}>
                    {loading ? 'Converting...' : 'Convert'}
                </button>

                {error && <p style={{ color: 'red', fontSize: '0.9rem' }}>{error}</p>}

                {result && (
                    <div className="result-box">
                        <span className="result-value">{result}</span>
                    </div>
                )}
            </div>
        </div>
    );
}