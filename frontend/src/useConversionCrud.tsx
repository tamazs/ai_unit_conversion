import { useState } from 'react';

export function useConverter() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const convert = async (prompt: unknown) => {
        setLoading(true);
        setError(null);
        try {
            const res = await fetch('http://localhost:8000/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ request: prompt }),
            });
            const data = await res.json();
            return data.response;
        } catch (e) {
            setError("Something went wrong.");
            return null;
        } finally {
            setLoading(false);
        }
    };

    return { convert, loading, error };
}