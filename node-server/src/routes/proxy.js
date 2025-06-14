const express = require('express');
const router = express.Router();
const axios = require('axios');

const PYTHON_SERVER_URL = process.env.PYTHON_SERVER_URL || 'http://localhost:5001';

// Proxy all chatbot requests to Python server
router.post('/', async (req, res) => {
    try {
        const response = await axios.post(`${PYTHON_SERVER_URL}/api/chat`, req.body);
        res.json(response.data);
    } catch (error) {
        console.error('Python server error:', error);
        res.status(500).json({
            error: 'Failed to communicate with AI server',
            details: error.response?.data || error.message
        });
    }
});

module.exports = router;
