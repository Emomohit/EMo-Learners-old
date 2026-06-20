export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  // Google Apps Script Web App URL
  const scriptURL = process.env.GOOGLE_SCRIPT_URL || 'https://script.google.com/macros/s/AKfycbz-fB-IFTVnLb9XZnZGyHglOtmXT7qOq35xiwarfudzXBDD9jHBTp04iKCWQaLMrgqLVw/exec';

  if (!scriptURL) {
    return res.status(500).json({ error: 'Server misconfiguration: GOOGLE_SCRIPT_URL is missing.' });
  }

  try {
    const { Email } = req.body;

    if (!Email) {
      return res.status(400).json({ error: 'Email is required.' });
    }

    // Google Apps Script expects x-www-form-urlencoded format
    const formData = new URLSearchParams();
    formData.append('Email', Email);

    // Make the request to Google Apps Script from the backend
    const response = await fetch(scriptURL, {
      method: 'POST',
      body: formData,
    });
    
    const data = await response.json();

    if (data.result === 'success') {
      return res.status(200).json({ success: true, message: 'Saved successfully' });
    } else {
      return res.status(500).json({ success: false, error: data.error });
    }
  } catch (error) {
    return res.status(500).json({ success: false, error: error.message });
  }
}
