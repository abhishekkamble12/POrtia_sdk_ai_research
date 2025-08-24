# app_gemini_portia_docs.py

import os
import json
import datetime as dt
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


from portia import Config, Portia, Step, StorageClass, LLMProvider

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

APP_TITLE = "AI Research Assistant"
DEFAULT_MODEL = os.getenv("PORTIA_MODEL", "gemini-1.5-pro")  

# -------------------------
# API Key Validation
# -------------------------
def validate_google_api_key():
    """Validate the Google API key"""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        return False, "❌ GOOGLE_API_KEY not found"
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Test", safety_settings={'HARASSMENT':'block_none'})
        return True, "✅ Google API key is valid"
    except Exception as e:
        error_msg = str(e)
        return False, f"❌ Google API error: {error_msg}"

# -------------------------
# Portia Setup
# -------------------------
@st.cache_resource(show_spinner=False)
def build_agent() -> Portia:
    is_valid, message = validate_google_api_key()
    if not is_valid:
        st.error(message)
        return None
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    config = Config(
        project_name="ai-research-gemini",
        storage_class=StorageClass.MEMORY,
        model=DEFAULT_MODEL,
        llm_provider=LLMProvider.GOOGLE,
        google_api_key=api_key
    )
    
    try:
        agent = Portia(config=config)
        return agent
    except Exception as e:
        st.error(f"❌ Failed to initialize Portia: {str(e)}")
        return None

def run_research(agent: Portia, topic: str) -> dict:
    if agent is None:
        return {"error": "Agent not initialized"}
    
    today = dt.date.today().isoformat()
    step_prompt = f"Research: {topic}. Provide summary with sources. Date: {today}."

    step = Step(
        name="research",
        task=step_prompt,
        tools=["portia:tavily::search"],
        output="text"
    )

    try:
        result = agent.run(step)
        output = getattr(result, "output", "")
        return {"markdown": output}
    except Exception as e:
        return {"error": str(e)}

# -------------------------
# Streamlit UI
# -------------------------
def render_ui():
    st.set_page_config(page_title=APP_TITLE, page_icon="🔍", layout="wide")
    st.title(APP_TITLE)
    
    # Display current environment status
    st.sidebar.header("Environment Status")
    
    google_key = os.getenv("GOOGLE_API_KEY", "NOT FOUND")
    tavily_key = os.getenv("TAVILY_API_KEY", "NOT FOUND")
    portia_key = os.getenv("PORTIA_API_KEY", "NOT FOUND")
    
    st.sidebar.code(f"GOOGLE_API_KEY: {google_key[:15]}...")
    st.sidebar.code(f"TAVILY_API_KEY: {tavily_key[:15]}...")
    st.sidebar.code(f"PORTIA_API_KEY: {portia_key[:15]}...")
    
    # Validate Google API key
    is_valid, message = validate_google_api_key()
    if is_valid:
        st.sidebar.success(message)
    else:
        st.sidebar.error(message)
        st.error("""
        ## 🔧 Google API Configuration Required
        
        **Your Google API key is invalid or not configured properly:**
        
        1. **Get a new API key:** https://aistudio.google.com/
        2. **Enable the API:** https://console.cloud.google.com/
           - Search for "Generative Language API"
           - Click "Enable"
        3. **Set up billing** (if required)
        4. **Update your .env file** with the new key
        
        **Current .env file should look like:**
        ```
        GOOGLE_API_KEY=your_actual_key_here
        TAVILY_API_KEY=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
        PORTIA_API_KEY=prt-IIvN7lat.smpAwTu3qcdMAFqVUi0tddWoBILCxAvP
        PORTIA_MODEL=gemini-1.5-pro
        ```
        """)
        return
    
    # Only show research UI if Google API is valid
    st.success("✅ Google API key is valid!")
    
    topic = st.text_input("Research Topic:", "Future of AI")
    if st.button("Start Research"):
        agent = build_agent()
        if agent:
            with st.spinner("Researching..."):
                result = run_research(agent, topic)
                
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                st.markdown(result["markdown"])
                st.success("Research completed!")

if __name__ == "__main__":
    render_ui()