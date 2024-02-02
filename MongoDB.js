const fetch = require('node-fetch');
const apiKey = 599a424f-6dc1-4b2d-bb73-60b997aac973;
const databaseName = OSKIF;

const { MongoClient } = require('mongodb');

// Replace with your MongoDB Atlas connection string
const uri = 'mongodb+srv://<admin>:<Vtenkhf0X5MGCcaJ>@cluster0.mongodb.net/test?retryWrites=true&w=majority';

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function connectToMongoDB() {
    try {
        await client.connect();
        console.log('Connected to MongoDB');
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
    }
}

// Call the connectToMongoDB function to establish the connection
connectToMongoDB();

// Function to connect to MongoDB
async function connectToMongoDB() {
    try {
        const response = await fetch(`https://api.mongodb.com/v3.6/groups/${apiKey}/clusters/${databaseName}/connect`);
        const data = await response.json();
        console.log('Connected to MongoDB');
        console.log('Connection String:', data.connectionString);
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
    }
}
// Call the connectToMongoDB function to establish the connection
connectToMongoDB();
