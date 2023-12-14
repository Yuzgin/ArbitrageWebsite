const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json());

app.post('/submit', (req, res) => {
    const { email, url } = req.body;

    // Validate that email, url, and recipients are present before proceeding
    if (!email || !url ) {
        return res.status(400).json({ error: 'Email and URL are required.' });
    }

    // Use the received URL and recipients in the command
    const smtp_server = 'smtp.gmail.com';
    const smtp_port = 587;
    const sender_email = 'andycodenotifications@gmail.com';
    const sender_password = 'gcnh ifil midb rqvc';

    // Convert recipients array to a string
    const recipient_email = email;

    const command = `python PPSoT.py "${url}" "${smtp_server}" "${smtp_port}" "${sender_email}" "${sender_password}" ${recipient_email}`;

    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            return res.status(500).json({ error: 'Internal server error.' });
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return res.status(500).json({ error: 'Internal server error.' });
        }

        console.log(`Python script output: ${stdout}`);
        res.status(200).json({ message: 'Python script executed successfully.' });
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
