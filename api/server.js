const express = require("express");
const bcrypt = require("bcrypt");
const fs = require('fs');

const app = express();
app.use(express.json())

const project = "k4rb1ne";

const port = 85;

const AccessKey = "puturaccesskeyidc";  // used to delete and create keys
const getAuthsUrl = `/keys/${project}`;
const createAuthUrl = `/create/${project}`;
const checkAuthUrl = `/verify/${project}`;
const delAuthUrl = `/kill/${project}`;

const filePath = 'db/db.json';

const readFile = (filePath) => {
    try {
        const data = fs.readFileSync(filePath, 'utf-8');
        return JSON.parse(data);
    } catch (error) {
        console.error('Error reading file:', error.message);
        return {};
    }
};

const users = readFile(filePath);

const saveToFile = (filePath, data) => {
    try {
        const jsonData = JSON.stringify(data, null, 2);
        fs.writeFileSync(filePath, jsonData, 'utf-8');
        console.log('Changes saved to file.');
    } catch (error) {
        console.error('Error writing to file:', error.message);
    }
};

const addUser = (username, authKey, duration, creationDate) => {
    users[username] = {
        authKey,
        duration,
        creationDate
    };
    saveToFile(filePath, users);
};

const removeUser = (username) => {
    delete users[username];
    saveToFile(filePath, users);
};

const getUser = (username) => {
    return users[username] || null;
};

const doTimeShitFRFR = (filePath) => {  // deletes when user time runs out
    const currentDate = new Date();
    for (const discordid in users) {
        const user = users[discordid];
        const creationDate = new Date(user.creationDate);

        //const StimeDifference = (currentDate - creationDate) / 1000; // seconds
        const DtimeDifference = (currentDate - creationDate) / (1000 * 60 * 60 * 24); // days

        if (user.duration != "-1") { // dont check lifetime keys
            if (parseInt(user.duration) <= DtimeDifference) {  // duration is amnt of days
                removeUser(discordid);
                saveToFile(filePath, users);
                console.log(`User '${discordid}' removed after ${user.duration} seconds.`);
            }
        }
    }
};

const getAllUsers = () => {
    return Object.keys(users).map(username => ({
        username,
        ...users[username]
    }));
};

// Get All Keys
app.get(getAuthsUrl, (req, res) => {
    res.send("Kill urself fag");
});

app.post(getAuthsUrl, (req, res) => {
	if (req.body.accessKey == AccessKey) {
		res.send(getAllUsers());
	} else {
		return res.status(500).send("Erm, you dont have any privilege sir. Try being white... (because that makes sense)");
	}
});


// Create Key
app.get(createAuthUrl, (req, res) => { 
    res.send("you thought nigga");
});

app.post(createAuthUrl, async (req, res) => {
    try {
        if (!getUser(req.body.discordid)) {
            if (req.body.accessKey == AccessKey) {
                const salt = await bcrypt.genSalt();
                const hashedKey = await bcrypt.hash(req.body.authKey, salt);

                // Get the current date in ISO format
                const creationDate = new Date().toISOString();

                const user = {
                    discordid: req.body.discordid,
                    duration: req.body.duration,
                    authKey: hashedKey
                };

                addUser(user.discordid, user.authKey, user.duration, creationDate);
                res.status(201).send(`${user.authKey}`);
                //res.status(201).send(`Created a user with Discord ID ${req.body.discordid}`);
            } else {
                return res.status(500).send("Sir, where's your trump card?");
            }
        } else {
            res.send("User already exists pooron.");
        }
    } catch (error) {
        console.error('Error:', error.message);
        res.status(500).send("Something went wrong, cuh");
    }
});

// Delete Key
app.get(delAuthUrl, (req, res) => { 
    res.send("YOU ARE LIKE SPED NIGGA LMFAOOOO");
});

// Delete Key
app.post(delAuthUrl, async (req, res) => {
    const user = getUser(req.body.discordid);
    if (user == null) {
        return res.status(400).send("User not found farthead"); // user not valid
    } else {
        if (req.body.accessKey == AccessKey) { // prevent random people from deleting keys
            removeUser(req.body.discordid);
            return res.status(201).send(`commited a "george floyd" against user ${req.body.discordid}`);
        } else {
            return res.status(500).send("you ain gyatt dat white privilege my boi");
        }
    }
});

// Check Key
app.get(checkAuthUrl, (req, res) => {
    res.send("nice fiddler / wireshark");
});

app.post(checkAuthUrl, async (req, res) => {
    const user = getUser(req.body.discordid);
    if (user == null) {
        return res.status(500).send("User and or Key not valid!"); // user not valid
    }
    try {
        if (await bcrypt.compare(req.body.authKey, user.authKey)) {
            return res.status(201).send("Success");
        } else {
            return res.status(500).send("User and or Key not valid!"); // key not valid
        }
    } catch {
        res.status(500).send("somf went wrong cuh: verify page");
    }
})

// Check every minute
setInterval(() => {
    doTimeShitFRFR(filePath);
}, 60000);

app.listen(port); // Port 85

console.log(`Server started at: http://localhost:${port}/`);
console.log(`Access Key:\t${AccessKey}`)