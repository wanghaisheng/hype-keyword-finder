To retrieve keyword data, including suggestions and metrics, using the Google Ads API (formerly AdWords API), you can leverage the **Keyword Planner**. Below is a step-by-step guide:

---

### Step 1: Set Up Google Ads API
1. **Create a Google Cloud Project**:
   - Enable the Google Ads API.
   - Set up OAuth2 credentials.

2. **Link Google Ads Account**:
   - Use a Google Ads Manager account.

3. **Install the Client Library**:
   - Install the Google Ads API client library for your preferred programming language. For Node.js:
     ```bash
     npm install google-ads-api
     ```

---

### Step 2: Authenticate
Authenticate with your Google Ads account using OAuth2. Here's an example configuration for Node.js:

#### Configuration (`googleads.config.json`)
```json
{
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "refresh_token": "YOUR_REFRESH_TOKEN",
  "developer_token": "YOUR_DEVELOPER_TOKEN",
  "login_customer_id": "YOUR_MANAGER_ACCOUNT_ID"
}
```

---

### Step 3: Fetch Keyword Ideas
Use the `KeywordPlanIdeaService` to fetch keyword suggestions.

#### Example Script (Node.js)
```javascript
import { GoogleAdsApi } from 'google-ads-api';
import fs from 'fs';

// Load configuration
const config = JSON.parse(fs.readFileSync('googleads.config.json', 'utf8'));

// Initialize API client
const client = new GoogleAdsApi({
    client_id: config.client_id,
    client_secret: config.client_secret,
    developer_token: config.developer_token
});

// Define customer ID
const customerId = config.login_customer_id;

// Function to fetch keyword ideas
async function fetchKeywordIdeas(keyword) {
    const service = client.KeywordPlanIdeaService;

    try {
        const request = {
            customer_id: customerId,
            keyword_plan_network: 'GOOGLE_SEARCH',
            language: { language_constant: '1000' }, // English
            geo_target_constants: [{ geo_target_constant: '2840' }], // US
            keyword_seed: { keywords: [keyword] }
        };

        const response = await service.generateKeywordIdeas(request);

        // Parse results
        response.results.forEach(result => {
            console.log(`Keyword: ${result.text}`);
            console.log(`Avg Monthly Searches: ${result.keyword_idea_metrics.avg_monthly_searches}`);
            console.log(`Competition: ${result.keyword_idea_metrics.competition}`);
        });

    } catch (error) {
        console.error('Error fetching keyword ideas:', error.message);
    }
}

// Call function with a keyword
fetchKeywordIdeas('example keyword');
```

---

### Step 4: Key Parameters
- **`geo_target_constants`**: Specify geographic targeting (e.g., `2840` for the U.S.).
- **`language`**: Specify language targeting (e.g., `1000` for English).
- **`keyword_seed`**: Input your keyword(s).

---

### Expected Output
Running this script will output keyword suggestions, average monthly searches, and competition metrics for the given keyword.

---

### Step 5: Testing & Refinement
- Test the script with multiple keywords.
- Explore additional parameters (e.g., `historical_metrics_options`) in the [Google Ads API documentation](https://developers.google.com/google-ads/api).

---

Let me know if you need help with customization or further details!
