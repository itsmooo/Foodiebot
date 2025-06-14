const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const paymentRoutes = require('./routes/payment');
const proxyRoutes = require('./routes/proxy');
const authRoutes = require('./routes/auth');
const orderRoutes = require('./routes/order');
dotenv.config();
const app = express();

// Configure CORS
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3001',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));

app.use(express.json());

// Connect MongoDB
connectDB();

// Routes
app.use('/api/payment', paymentRoutes);
app.use('/api/auth',  authRoutes);
app.use('/api/orders',  orderRoutes);

// Proxy routes to Python server for AI/ML functionality
app.use('/api/chatbot', proxyRoutes);

const PORT = process.env.NODE_PORT || 3000;
app.listen(PORT, () => console.log(`Node.js server running on port ${PORT}`));
