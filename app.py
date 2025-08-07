# Create header with Cadence logo using Streamlit components
            header_col1, header_col2 = st.columns([1, 6])
            
            with header_col1:
                try:
                    st.image("CADENCE.png", width=80)
                except:
                    st.markdown("🏈")  # Fallback football emoji
                    
            with header_col2:
                st.markdown("### Fantasy Analysis")            # Create header with Cadence logo using base64
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #1a1a1a 0%, #6b46c1 100%); 
                        padding: 1rem; border-radius: 15px; margin: 1rem 0; 
                        border-left: 4px solid #8b5cf6; display: flex; align-items: center; gap: 1rem;">
                <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcwAAAHMCAYAAABY25rOAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3QecFOXZ//H7yjlhOVvOHnccIEhQEVtiiS2aqLElMRr7YxKNJk9i8qdEY+xRsXcTu7Fg7w0bNsQGFhQU9jjOtrcccDnIWZ7/8dz37PsmdyDHO7uzs/vMZ97v7Ozszvd7ZnZ+893beebH3EREABEBJK/vGpCqS+NhiEgkgYJIXOJrQbC3Iv4PGRLfzCIiEhEJKxKJRCKy/yt7RM+GJP8b+dF/F8S4ZJo+/p1IJKIiEu+jIH6NIhKOGNnFl4v8s8T/d3GJvV/i/5O/rf2+7uDlJfZeY5Rj/VYlf5/xf4h/77HLNqITzF//8T9bBn9vGSp/b5zGUVy9Q/5u7VL1adrQgU5EREREJKJBhYHORETG/3EJBjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCmCgExERpQAGOhERUQpgoBMREaUABjoREVEKYKATERGlAAY6ERFRCsg2XQARkVki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 streamlit as st
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
            # Create header with Cadence logo using Streamlit components
            col1, col2 = st.columns([1, 8])
            
            with col1:
                try:
                    st.image("CADENCE.png", width=60)
                except:
                    st.markdown("🏈")  # Fallback if logo doesn't load
                    
            with col2:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #1a1a1a 0%, #6b46c1 100%); 
                            padding: 1rem; border-radius: 15px; margin: 1rem 0; 
                            border-left: 4px solid #8b5cf6;">
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
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": question})
                
                # Trigger analysis immediately
                with st.spinner("🔍 Searching for latest NFL data and analyzing..."):
                    # Create a progress bar to show thinking process
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Step 1: Extract search terms
                    status_text.text("🔍 Extracting key player information...")
                    progress_bar.progress(20)
                    search_query = st.session_state.analyst.extract_search_terms(question)
                    
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
                    analysis = st.session_state.analyst.analyze_fantasy_question(question)
                    
                    # Step 5: Complete
                    status_text.text("✅ Analysis complete!")
                    progress_bar.progress(100)
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    # Display the analysis
                    st.session_state.analyst.format_analysis_response(analysis)
                    
                    # Add to chat history
                    simple_response = f"{analysis.get('recommendation', 'Analysis complete')}\n\nConfidence: {analysis.get('confidence', 'Medium')}"
                    st.session_state.messages.append({"role": "assistant", "content": simple_response})
                    
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