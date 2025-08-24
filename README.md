AI Research Assistant 🔍
A powerful Streamlit web application that leverages Google's Gemini AI model and the Portia agent framework to perform automated research on any topic. This tool combines AI-powered content generation with web search capabilities to deliver comprehensive research reports with sources.

✨ Features
Intuitive Web Interface: Clean Streamlit UI for easy interaction

AI-Powered Research: Utilizes Google's Gemini model for intelligent content generation

Automated Web Search: Integrates with Tavily search API to gather current information

Environment Validation: Automatically checks API key configuration

Real-time Results: Displays formatted research reports with proper sources

Sidebar Status Panel: Quick overview of API configuration status

🚀 Quick Start
Prerequisites
Python 3.8 or higher

API keys for:

Google Generative AI (Gemini)

Tavily Search API

Portia API

Installation
Clone or download the application files

Install required dependencies:

bash
pip install streamlit python-dotenv google-generativeai portia
Create a .env file in the same directory with your API keys:

text
GOOGLE_API_KEY=your_actual_google_api_key_here
TAVILY_API_KEY=your_actual_tavily_api_key_here
PORTIA_API_KEY=your_actual_portia_api_key_here
PORTIA_MODEL=gemini-1.5-pro
Getting API Keys
Google API Key
Visit https://aistudio.google.com/

Create an account or sign in

Generate an API key for the Generative Language API

Enable the API in Google Cloud Console if needed

Tavily API Key
Sign up at https://tavily.com/

Obtain your API key from the dashboard

Portia API Key
Visit the Portia website or repository for access information

Obtain your API key

Running the Application
Start the application:

bash
streamlit run app_gemini_portia_docs.py
Open your browser to the provided local URL (typically http://localhost:8501)

Check the sidebar to verify your API keys are properly configured

Enter your research topic in the text input field

Click "Start Research" to begin the analysis

View the generated research report with sources

🏗️ How It Works
API Validation: The application validates your Google API key on startup

Agent Initialization: When you submit a research topic, it initializes a Portia agent

Web Search: The agent uses the Tavily search tool to gather current information

Content Generation: Gemini processes the information and generates a structured report

Result Display: The results are displayed in a formatted markdown output

📁 Project Structure
text
app_gemini_portia_docs.py  # Main application file
.env                       # Environment variables (not included in repo)
requirements.txt           # Python dependencies
⚙️ Configuration
The application can be configured through the .env file:

Variable	Description	Default
GOOGLE_API_KEY	Your Google Generative AI API key	Required
TAVILY_API_KEY	Your Tavily search API key	Required
PORTIA_API_KEY	Your Portia API key	Required
PORTIA_MODEL	The Gemini model to use	gemini-1.5-pro
🔧 Troubleshooting
Common Issues
API Key Errors:

Verify all API keys are correctly set in your .env file

Ensure billing is enabled for Google Cloud services if required

Module Not Found Errors:

Ensure all dependencies are installed: pip install -r requirements.txt

Search Functionality Not Working:

Verify your Tavily API key is valid and has sufficient credits

Environment Setup Verification
The application includes built-in validation that checks:

Presence of all required API keys

Validity of the Google API key

Proper configuration of the Portia agent

📊 Example Usage
Launch the application

Enter a research topic like "Future of AI in healthcare"

Click "Start Research"

Wait a few moments while the AI gathers and processes information

Review the comprehensive report with sources

🛠️ Customization
You can modify the application by:

Changing the default research model in the .env file

Adjusting the research prompt in the run_research() function

Modifying the UI elements in the render_ui() function

⚠️ Limitations
Research quality depends on the available web sources

API usage may incur costs depending on your plan

Results are generated automatically and should be verified for critical applications

📝 License
This application uses various APIs and services subject to their respective terms of service. Please ensure compliance with all API usage policies.

🤝 Support
For issues related to:

Google API: Consult Google Cloud support

Tavily API: Visit https://tavily.com/support

Portia Framework: Check the Portia documentation

Application-specific issues: Review the code comments or check for updates

Note: This application is for demonstration purposes. Always verify important information from multiple sources before making decisions based on AI-generated content.
