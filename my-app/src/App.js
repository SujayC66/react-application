import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get('https://app1213-fnesatgja9gxccav.canadacentral-01.azurewebsites.net/api/data')
            .then(response => {
                setData(response.data.message);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, []);

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>React and Flask Integration</h1>
            <p>{data || "Loading..."}</p>
        </div>
    );
}

export default App;
