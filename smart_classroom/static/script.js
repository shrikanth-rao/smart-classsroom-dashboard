function fetchData() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            // Attendance
            let list = document.getElementById('attendance-list');
            list.innerHTML = '';
            data.attendance.forEach(item => {
                let li = document.createElement('li');
                li.textContent = `${item.usn}: ${item.status}`;
                list.appendChild(li);
            });

            // Sensor
            document.getElementById('temperature').textContent = data.sensors.temperature;
            document.getElementById('light').textContent = data.sensors.light;
        });
}

// Fetch every 15 seconds (for prototyping)
setInterval(fetchData, 15000);
fetchData();
