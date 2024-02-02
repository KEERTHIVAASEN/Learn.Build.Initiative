const { MongoClient } = require('mongodb');

// Replace YOUR_CONNECTION_STRING with your actual connection string
const uri = 'YOUR_CONNECTION_STRING';

// Create a new MongoClient
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

// Function to connect to MongoDB
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
