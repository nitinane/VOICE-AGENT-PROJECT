
async function testLanguageLock() {
  const baseUrl = 'http://localhost:3000/api';
  
  const testCases = [
    {
      name: 'Kiosk Brain: English Request with Hindi Lock',
      url: `${baseUrl}/kiosk-brain`,
      body: {
        transcript: 'I want to withdraw 5000 rupees',
        language: 'hi-IN'
      },
      expectedLanguage: 'hi' // Should contain Hindi script
    },
    {
      name: 'Groq API: English Request with Kannada Lock',
      url: `${baseUrl}/groq`,
      body: {
        transcript: 'Show me my balance',
        language: 'kn-IN',
        mode: 'CALL'
      },
      expectedLanguage: 'kn' // Should contain Kannada script
    }
  ];

  console.log('--- Starting Language Lock Verification ---');

  for (const test of testCases) {
    console.log(`\nTesting: ${test.name}`);
    try {
      const response = await fetch(test.url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(test.body)
      });
      
      const data = await response.json();
      const speakText = data.speak || data.response_text;
      
      console.log(`Response Speech: ${speakText}`);
      
      // Simple script detection: check for non-ASCII characters as a proxy for regional scripts
      const isRegional = /[^\x00-\x7F]/.test(speakText);
      
      if (isRegional) {
        console.log('✅ PASS: Regional script detected in response.');
      } else {
        console.log('❌ FAIL: Only ASCII/English detected in response.');
      }
    } catch (err) {
      console.error(`❌ ERROR: ${err.message}`);
    }
  }
}

testLanguageLock();
