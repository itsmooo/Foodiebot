const express = require("express");
const router = express.Router();
const axios = require("axios");

// Hormuud Payment API endpoint
const HORMUUD_API_URL = "https://api.waafipay.net/asm";

// Payment route for Hormuud
router.post("/hormuud", async (req, res) => {
  try {
    const { phone, amount } = req.body;
    console.log("are they exist", phone, amount);
    

    const paymentData = {
      schemaVersion: "1.0",
      requestId: Date.now().toString(),
      timestamp: new Date().toISOString(),
      channelName: "WEB",
      serviceName: "API_PURCHASE",
      serviceParams: {
        merchantUid: process.env.HORMUUD_MERCHANT_UID,
        apiUserId: process.env.HORMUUD_API_USER_ID,
        apiKey: process.env.HORMUUD_API_KEY,
        paymentMethod: "mwallet_account",
        payerInfo: {
          accountNo: phone,
        },
        transactionInfo: {
          referenceId: "referenceId",
          invoiceId: "invoiceId",
          amount: amount,
          currency: "USD",
          description: "description",
        },
      },
    };

    const response = await axios.post(HORMUUD_API_URL, paymentData, {
      headers: {
        "Content-Type": "application/json",
      },
    });

    res.json(response.data);
  } catch (error) {
    console.error("Payment error:", error);
    res.status(500).json({
      error: "Payment processing failed",
      details: error.response?.data || error.message,
    });
  }
});

module.exports = router;
