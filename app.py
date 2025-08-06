import streamlit as st
import requests
import json
from datetime import datetime
from typing import Dict, List, Any
import os
import anthropic
from dotenv import load_dotenv
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🏈 Cadence Fantasy Analyst",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #000000 0%, #2d1b69 50%, #6b46c1 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(107, 70, 193, 0.3);
        border: 2px solid #6b46c1;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        margin: 0;
    }
    
    .main-header p {
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
        color: #e5e7eb;
    }
    
    /* Chat interface styling */
    .stChatMessage {
        background: rgba(107, 70, 193, 0.1) !important;
        border: 1px solid #6b46c1 !important;
        border-radius: 15px !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a1a 0%, #000000 100%);
    }
    
    /* Text colors */
    .stMarkdown, .stText {
        color: white !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #6b46c1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);
        transform: translateY(-2px);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #6b46c1, #8b5cf6, #a78bfa);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(0, 0, 0, 0.8);
        color: white;
        border: 2px solid #6b46c1;
        border-radius: 10px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6;
        box-shadow: 0 0 20px rgba(107, 70, 193, 0.3);
    }
    
    /* Success/Info/Error boxes with theme colors */
    .stAlert {
        background: rgba(107, 70, 193, 0.2);
        border: 1px solid #6b46c1;
        border-radius: 15px;
        color: white;
    }
    
    /* Spinner */
    .stSpinner {
        color: #8b5cf6 !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    
    /* Footer styling */
    .footer-text {
        color: #9ca3af;
        text-align: center;
        font-size: 0.9rem;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #374151;
    }
</style>
""", unsafe_allow_html=True)

class CadenceFantasyAnalyst:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.system_prompt = """
        You are an elite NFL Fantasy Football Analyst with deep expertise in player evaluation, matchup analysis, and fantasy strategy. You have access to web search capabilities and use them extensively to gather the most current information before making any recommendations.

        Your core responsibilities:
        - Conduct thorough web research on players, teams, matchups, and NFL news before providing analysis
        - Provide data-driven start/sit recommendations based on matchups, target share, red zone usage, and game script predictions
        - Evaluate fantasy trades by analyzing player values, positional scarcity, schedule strength, and injury risk
        - Deliver comprehensive player analysis incorporating recent performance trends, usage patterns, and upcoming opportunities
        - Stay current on injury reports, depth chart changes, coaching decisions, and weather conditions that impact fantasy performance

        Your analytical framework:
        1. Always search for the most recent news and data on relevant players/teams before making recommendations
        2. Consider multiple factors: matchup difficulty, target/carry volume, red zone opportunities, game script, weather, and injury status
        3. Provide specific reasoning for each recommendation with supporting data points
        4. Include confidence levels (high/medium/low) for your recommendations
        5. Mention key risks or variables that could change your analysis
        6. Compare players directly when evaluating trades or start/sit decisions
        7. Analyse coaching staff and if relevant, say what their fantasy impact is for fantasy players.

        Your communication style:
        - Lead with your recommendation, then provide supporting analysis
        - Use specific statistics and recent performance data to support conclusions
        - Acknowledge uncertainty when data is limited or conflicting
        - Provide actionable insights that directly impact fantasy decisions
        - Include relevant context about upcoming matchups or schedule considerations

        Before making any fantasy recommendation, you must search for current information on the relevant players, teams, matchups, and any breaking news that could impact your analysis. Base all recommendations on the most up-to-date data available.
        """
    
    def search_web(self, query: str) -> str:
        """Search the web for NFL fantasy information"""
        try:
            search_url = "https://serpapi.com/search"
            params = {
                "q": f"{query} NFL fantasy football 2024",
                "api_key": os.getenv("SERPAPI_KEY"),
                "engine": "google",
                "num": 5
            }
            
            response = requests.get(search_url, params=params)
            if response.status_code == 200:
                results = response.json()
                search_results = ""
                if "organic_results" in results:
                    for result in results["organic_results"][:3]:
                        search_results += f"Title: {result.get('title', '')}\n"
                        search_results += f"Snippet: {result.get('snippet', '')}\n\n"
                return search_results
            else:
                return "Unable to fetch current data. Please try again."
                
        except Exception as e:
            return f"Search temporarily unavailable: {str(e)}"
    
    def analyze_fantasy_question(self, question: str) -> Dict[str, Any]:
        """Analyze fantasy question using web search and Claude AI"""
        
        try:
            # First, search for relevant information
            search_query = self.extract_search_terms(question)
            search_results = self.search_web(search_query)
            
            # Create the full prompt for Claude
            full_prompt = f"""
            User Question: {question}
            
            Current NFL Information Found:
            {search_results}
            
            Based on the current information above and your fantasy football expertise, provide a comprehensive analysis that includes:
            
            1. Your specific recommendation (accept/decline the trade, start/sit decision, etc.)
            2. Your confidence level (High/Medium/Low) 
            3. Detailed reasoning with specific data points
            4. Key risk factors to monitor
            5. Additional context or timing considerations
            
            Be specific and actionable. If this involves player comparisons, directly compare their situations, ages, targets, team contexts, etc.
            """
            
            # Call Claude API
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1500,
                system=self.system_prompt,
                messages=[
                    {"role": "user", "content": full_prompt}
                ]
            )
            
            # Parse Claude's response
            claude_analysis = response.content[0].text
            
            # Try to extract structured data from Claude's response
            confidence = "Medium"  # Default
            if "high confidence" in claude_analysis.lower() or "highly confident" in claude_analysis.lower():
                confidence = "High"
            elif "low confidence" in claude_analysis.lower() or "not confident" in claude_analysis.lower():
                confidence = "Low"
            
            return {
                "recommendation": claude_analysis,
                "confidence": confidence,
                "analysis": search_results,
                "risks": "See detailed analysis above",
                "context": "Based on current market data and trends"
            }
            
        except Exception as e:
            return {
                "recommendation": f"Analysis temporarily unavailable: {str(e)}",
                "confidence": "Low",
                "analysis": search_results if 'search_results' in locals() else "Search data available",
                "risks": "Unable to provide full analysis at this time",
                "context": "Please try again or check your API configuration"
            }
    
    def extract_search_terms(self, question: str) -> str:
        """Extract key terms for web search"""
        key_terms = []
        
        words = question.split()
        for i, word in enumerate(words):
            if word.lower() in ['start', 'sit', 'trade', 'vs', 'versus']:
                if i > 0:
                    key_terms.append(words[i-1])
                if i < len(words) - 1:
                    key_terms.append(words[i+1])
        
        return " ".join(key_terms) if key_terms else question
    
    def format_analysis_response(self, analysis: Dict[str, Any]) -> None:
        """Display the analysis response with Cadence brand styling using Streamlit components"""
        recommendation = analysis.get('recommendation', 'Analysis in progress...')
        confidence = analysis.get('confidence', 'Medium')
        
        # Extract key components from the recommendation if it's detailed
        if len(recommendation) > 100:  # If we have a detailed analysis
            # Try to identify if it's a trade decision
            is_trade = any(word in recommendation.lower() for word in ['trade', 'accept', 'decline', 'keep', 'sell'])
            is_start_sit = any(word in recommendation.lower() for word in ['start', 'sit', 'bench', 'lineup'])
            
            if is_trade:
                decision_emoji = "🤝" if "accept" in recommendation.lower() or "yes" in recommendation.lower() else "❌"
            elif is_start_sit:
                decision_emoji = "✅" if "start" in recommendation.lower() else "🔄"
            else:
                decision_emoji = "📊"
        else:
            decision_emoji = "🎯"
            
        # Confidence emoji and values
        confidence_emoji = {"High": "🔥", "Medium": "⚡", "Low": "⚠️"}.get(confidence, "⚡")
        confidence_value = {"High": 0.85, "Medium": 0.60, "Low": 0.35}.get(confidence, 0.60)
        
        # Use Streamlit's built-in styling components with Cadence theme
        with st.container():
            # Create header with Cadence logo
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #1a1a1a 0%, #6b46c1 100%); 
                        padding: 1rem; border-radius: 15px; margin: 1rem 0; 
                        border-left: 4px solid #8b5cf6; display: flex; align-items: center; gap: 1rem;">
                <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA0NjAgNDYwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZWxsaXBzZSBjeD0iMjMwIiBjeT0iMjMwIiByeD0iMjI1IiByeT0iMTM1IiBmaWxsPSIjMDAwMDAwIi8+CjxyZWN0IHg9IjM2IiB5PSIyNDAiIHdpZHRoPSIzODgiIGhlaWdodD0iNDAiIGZpbGw9IiMwMDAwMDAiLz4KPGxpbmUgeDE9IjE4MCIgeTE9IjE3NSIgeDI9IjE4MCIgeTI9IjIwNSIgc3Ryb2tlPSIjNkI0NkMxIiBzdHJva2Utd2lkdGg9IjgiLz4KPGxpbmUgeDE9IjIwMCIgeTE9IjE3NSIgeDI9IjIwMCIgeTI9IjIwNSIgc3Ryb2tlPSIjNkI0NkMxIiBzdHJva2Utd2lkdGg9IjgiLz4KPGxpbmUgeDE9IjIyMCIgeTE9IjE3NSIgeDI9IjIyMCIgeTI9IjIwNSIgc3Ryb2tlPSIjNkI0NkMxIiBzdHJva2Utd2lkdGg9IjgiLz4KPGxpbmUgeDE9IjI0MCIgeTE9IjE3NSIgeDI9IjI0MCIgeTI9IjIwNSIgc3Ryb2tlPSIjNkI0NkMxIiBzdHJva2Utd2lkdGg9IjgiLz4KPGxpbmUgeDE9IjI2MCIgeTE9IjE3NSIgeDI9IjI2MCIgeTI9IjIwNSIgc3Ryb2tlPSIjNkI0NkMxIiBzdHJva2Utd2lkdGg9IjgiLz4KPGxpbmUgeDE9IjI4MCIgeTE9IjE3NSIgeDI9IjI4MCIgeTI9IjIwNSIgc3Ryb2tlPSIjNkI0NkMxIiBzdHJva2Utd2lkdGg9IjgiLz4KPHRleHQgeD0iMjMwIiB5PSIzMDAiIGZpbGw9IiM2QjQ2QzEiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0OCIgZm9udC13ZWlnaHQ9ImJvbGQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkNBREVOQ0U8L3RleHQ+Cjwvc3ZnPgo=" 
                     style="width: 40px; height: 40px;" alt="Cadence Logo"/>
                <h3 style="color: white; margin: 0;">Fantasy Analysis</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Create two columns - one for analysis, one for confidence
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Create recommendation box with softer themed colors
                if "accept" in recommendation.lower():
                    bg_color = "linear-gradient(135deg, #374151 0%, #4b5563 100%)"
                    accent_color = "#10b981"
                    recommendation_label = "✅ RECOMMENDATION"
                elif "decline" in recommendation.lower():
                    bg_color = "linear-gradient(135deg, #374151 0%, #4b5563 100%)"
                    accent_color = "#f59e0b"
                    recommendation_label = "❌ RECOMMENDATION"
                else:
                    bg_color = "linear-gradient(135deg, #374151 0%, #6b46c1 100%)"
                    accent_color = "#8b5cf6"
                    recommendation_label = "📊 ANALYSIS"
                
                st.markdown(f"""
                <div style="background: {bg_color}; 
                            color: white; padding: 1.5rem; border-radius: 12px; margin: 1rem 0;
                            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
                            border-left: 4px solid {accent_color};">
                    <strong>{recommendation_label}:</strong><br><br>{recommendation}
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Create simple confidence display using Streamlit components
                st.markdown(f"### {confidence_emoji}")
                st.markdown("**CONFIDENCE**")
                
                # Use Streamlit's progress bar
                progress_color = {"High": "green", "Medium": "normal", "Low": "red"}.get(confidence, "normal")
                st.progress(confidence_value)
                
                # Add confidence text
                if confidence == "High":
                    st.success(f"**{confidence}**")
                elif confidence == "Medium":
                    st.info(f"**{confidence}**")
                else:
                    st.warning(f"**{confidence}**")

def main():
    # Header with Cadence branding
    st.markdown("""
    <div class="main-header">
        <h1>🏈 CADENCE Fantasy Analyst</h1>
        <p>Elite fantasy football analysis powered by real-time NFL data & AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize the analyst
    if "analyst" not in st.session_state:
        st.session_state.analyst = CadenceFantasyAnalyst()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar with examples and info
    with st.sidebar:
        st.header("⚡ Quick Analysis")
        st.write("**🔥 Popular Questions:**")
        example_questions = [
            "Should I start Tyreek Hill or Davante Adams this week?",
            "Is Josh Allen worth trading Lamar Jackson and Tony Pollard?",
            "What's the outlook for Christian McCaffrey this week?",
            "Who should I pick up from waivers at RB?",
            "What's the weather impact for this week's games?"
        ]
        
        for question in example_questions:
            if st.button(f"💭 {question[:35]}...", key=question):
                st.session_state.messages.append({"role": "user", "content": question})
                st.rerun()
        
        st.markdown("---")
        st.write("**🎯 Features:**")
        st.write("🔍 Real-time NFL data search")
        st.write("⚡ Start/sit recommendations") 
        st.write("🤝 Trade analysis")
        st.write("🏥 Injury report updates")
        st.write("📊 Matchup analysis")
        st.write("🌦️ Weather considerations")
        st.write("🤖 AI-powered insights")
    
    # Main chat interface
    st.header("💬 Ask Your Fantasy Question")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                st.markdown(message["content"], unsafe_allow_html=True)
            else:
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("💭 Ask me about your fantasy lineup, trades, or player analysis..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching for latest NFL data and analyzing..."):
                # Create a progress bar to show thinking process
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Step 1: Extract search terms
                status_text.text("🔍 Extracting key player information...")
                progress_bar.progress(20)
                search_query = st.session_state.analyst.extract_search_terms(prompt)
                
                # Step 2: Search web
                status_text.text("🌐 Searching for latest NFL data...")
                progress_bar.progress(40)
                search_results = st.session_state.analyst.search_web(search_query)
                
                # Step 3: Analyze with AI
                status_text.text("🤖 AI analyzing data and generating insights...")
                progress_bar.progress(70)
                
                # Step 4: Get full analysis
                status_text.text("📊 Finalizing fantasy recommendations...")
                progress_bar.progress(90)
                analysis = st.session_state.analyst.analyze_fantasy_question(prompt)
                
                # Step 5: Complete
                status_text.text("✅ Analysis complete!")
                progress_bar.progress(100)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Use the new formatting method
                st.session_state.analyst.format_analysis_response(analysis)
        
        # Add assistant response to chat history (simplified for chat history)
        simple_response = f"{analysis.get('recommendation', 'Analysis complete')}\n\nConfidence: {analysis.get('confidence', 'Medium')}"
        st.session_state.messages.append({"role": "assistant", "content": simple_response})
    
    # Footer with Cadence branding
    st.markdown("---")
    st.markdown(f"""
    <div class="footer-text">
        ⏰ Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 🏈 Powered by <strong>CADENCE AI</strong><br>
        <strong>⚠️ Disclaimer:</strong> This analysis is for entertainment purposes. Always do your own research!
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()