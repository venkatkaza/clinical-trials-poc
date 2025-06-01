import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import json
import time

# Configure the page
st.set_page_config(
    page_title="Clinical Trial Intelligence Platform",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        background-color: #1e40af;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #1e3a8a;
        transform: translateY(-2px);
        box-shadow: 0 5px 10px rgba(0,0,0,0.2);
    }
    .metric-card {
        background-color: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .success-box {
        background-color: #10b981;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #f59e0b;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'selected_sites' not in st.session_state:
    st.session_state.selected_sites = []

# Mock data generator functions
def generate_mock_trials(n=100):
    """Generate realistic clinical trial data"""
    trials = []
    indications = ['NSCLC', 'Breast Cancer', 'Colorectal Cancer', 'Melanoma', 'Prostate Cancer']
    phases = ['Phase I', 'Phase II', 'Phase III', 'Phase II/III']
    statuses = ['Completed', 'Terminated', 'Withdrawn', 'Active']
    
    for i in range(n):
        trial = {
            'trial_id': f'NCT{random.randint(10000000, 99999999)}',
            'title': f'{random.choice(indications)} Study {i+1}',
            'indication': random.choice(indications),
            'phase': random.choice(phases),
            'status': random.choice(statuses),
            'enrollment': random.randint(50, 500),
            'duration_months': random.randint(12, 48),
            'success_rate': random.uniform(0.1, 0.9),
            'year': random.randint(2018, 2024),
            'primary_endpoint': random.choice(['PFS', 'OS', 'ORR', 'CR']),
            'sites': random.randint(10, 100)
        }
        trials.append(trial)
    
    return pd.DataFrame(trials)

def generate_mock_sites(n=50):
    """Generate realistic site data"""
    sites = []
    countries = ['USA', 'Germany', 'UK', 'Japan', 'Canada', 'France', 'Spain', 'Italy']
    cities = {
        'USA': ['Boston', 'New York', 'Houston', 'Los Angeles', 'Chicago'],
        'Germany': ['Berlin', 'Munich', 'Hamburg', 'Frankfurt'],
        'UK': ['London', 'Manchester', 'Edinburgh', 'Birmingham'],
        'Japan': ['Tokyo', 'Osaka', 'Kyoto', 'Nagoya'],
        'Canada': ['Toronto', 'Vancouver', 'Montreal'],
        'France': ['Paris', 'Lyon', 'Marseille'],
        'Spain': ['Madrid', 'Barcelona', 'Valencia'],
        'Italy': ['Rome', 'Milan', 'Naples']
    }
    
    for i in range(n):
        country = random.choice(countries)
        site = {
            'site_id': f'SITE{i+1:04d}',
            'name': f'{random.choice(cities[country])} Medical Center',
            'country': country,
            'city': random.choice(cities[country]),
            'enrollment_rate': round(random.uniform(0.5, 5.0), 1),
            'screen_failure_rate': round(random.uniform(0.1, 0.4), 2),
            'deviation_rate': round(random.uniform(0.01, 0.1), 2),
            'cost_per_patient': random.randint(15000, 50000),
            'startup_time_days': random.randint(30, 120),
            'pi_experience': random.randint(5, 30),
            'quality_score': round(random.uniform(0.6, 0.95), 2),
            'genetic_testing': random.choice(['Yes', 'No']),
            'phase_experience': random.choice(['I/II/III', 'II/III', 'III only'])
        }
        sites.append(site)
    
    return pd.DataFrame(sites)

# Load or generate data
@st.cache_data
def load_data():
    trials_df = generate_mock_trials(100)
    sites_df = generate_mock_sites(50)
    return trials_df, sites_df

trials_df, sites_df = load_data()

# Header
st.markdown("# 🧬 Clinical Trial Intelligence Platform")
st.markdown("### AI-Powered Protocol Optimization & Site Selection")

# Sidebar inputs
with st.sidebar:
    st.markdown("## Trial Parameters")
    
    indication = st.selectbox(
        "Indication",
        ["NSCLC", "Breast Cancer", "Colorectal Cancer", "Melanoma", "Prostate Cancer"]
    )
    
    mutation = st.text_input("Target Mutation", "EGFR L858R")
    
    phase = st.radio(
        "Phase",
        ["Phase II", "Phase III", "Phase II/III"]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        target_enrollment = st.number_input(
            "Target Enrollment",
            min_value=50,
            max_value=1000,
            value=150,
            step=10
        )
    
    with col2:
        timeline_months = st.number_input(
            "Timeline (months)",
            min_value=12,
            max_value=60,
            value=24,
            step=6
        )
    
    st.markdown("### Geographic Preferences")
    countries = st.multiselect(
        "Select Countries",
        ["USA", "Germany", "UK", "Japan", "Canada", "France", "Spain", "Italy"],
        default=["USA", "Germany", "Japan"]
    )
    
    st.markdown("### Analysis Options")
    include_cost_analysis = st.checkbox("Include Cost Analysis", value=True)
    include_risk_assessment = st.checkbox("Include Risk Assessment", value=True)
    
    analyze_button = st.button("🚀 Run Analysis", use_container_width=True)

# Main content area
if not st.session_state.analysis_complete:
    # Welcome screen
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Historical Trials Analyzed", "10,847")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Success Pattern Identified", "2,341")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Avg. Time Saved", "4.5 months")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Features overview
    st.markdown("### How It Works")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("#### 1️⃣ Input Parameters")
        st.markdown("Define your trial requirements and constraints")
    
    with col2:
        st.markdown("#### 2️⃣ AI Analysis")
        st.markdown("Our AI analyzes thousands of similar trials")
    
    with col3:
        st.markdown("#### 3️⃣ Optimization")
        st.markdown("Generate optimized protocol and site list")
    
    with col4:
        st.markdown("#### 4️⃣ Implementation")
        st.markdown("Export ready-to-use recommendations")

# Run analysis when button clicked
if analyze_button:
    st.session_state.analysis_complete = True
    
    # Show progress
    progress_container = st.container()
    with progress_container:
        st.markdown("### 🔄 Analysis in Progress...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            ("Retrieving historical trial data...", 0.2),
            ("Analyzing success patterns...", 0.4),
            ("Optimizing protocol design...", 0.6),
            ("Selecting optimal sites...", 0.8),
            ("Generating recommendations...", 1.0)
        ]
        
        for step_text, progress_value in steps:
            status_text.text(step_text)
            progress_bar.progress(progress_value)
            time.sleep(0.5)  # Simulate processing
        
        progress_container.empty()

# Show results if analysis is complete
if st.session_state.analysis_complete:
    # Results tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Executive Summary",
        "📋 Protocol Optimization", 
        "🏥 Site Selection",
        "💰 Cost Analysis",
        "📈 Risk Assessment"
    ])
    
    with tab1:
        st.markdown("## Executive Summary")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.markdown("### ✅ Analysis Complete")
            st.markdown(f"""
            Based on analysis of **{len(trials_df[trials_df['indication'] == indication])}** similar {indication} trials,
            we've identified an optimized protocol design and selected **{len(countries) * 5}** optimal sites
            across {len(countries)} countries.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Key recommendations
            st.markdown("### 🎯 Key Recommendations")
            
            recommendations = [
                f"**Primary Endpoint**: Progression-Free Survival (PFS) - 87% correlation with approval",
                f"**Sample Size**: {target_enrollment} patients with 90% power calculation",
                f"**Duration**: {timeline_months} months with adaptive design option",
                f"**Sites**: Top {len(countries) * 5} sites selected from {len(sites_df)} evaluated",
                f"**Projected Success Rate**: 73% (vs. industry average 42%)"
            ]
            
            for rec in recommendations:
                st.markdown(f"- {rec}")
        
        with col2:
            # Success probability gauge
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=73,
                title={'text': "Success Probability"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#10b981"},
                    'steps': [
                        {'range': [0, 50], 'color': "#fee2e2"},
                        {'range': [50, 70], 'color': "#fef3c7"},
                        {'range': [70, 100], 'color': "#d1fae5"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 42
                    }
                }
            ))
            fig_gauge.update_layout(height=300)
            st.plotly_chart(fig_gauge, use_container_width=True)
            
            # Time savings
            st.metric("Time to First Patient", "3.5 months", "-2.5 months")
            st.metric("Total Cost Estimate", f"${target_enrollment * 35000:,}", "-23%")
    
    with tab2:
        st.markdown("## Protocol Optimization")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Recommended Design Elements")
            
            design_elements = {
                "Primary Endpoint": "Progression-Free Survival (PFS)",
                "Secondary Endpoints": "Overall Survival, Overall Response Rate, Duration of Response",
                "Stratification Factors": "Mutation subtype, Prior therapy, Performance status",
                "Randomization": "2:1 (Experimental:Control)",
                "Interim Analysis": "At 50% enrollment with adaptive design",
                "Safety Run-in": "First 20 patients with DSMB review"
            }
            
            for key, value in design_elements.items():
                st.markdown(f"**{key}**: {value}")
        
        with col2:
            # Historical success rates by endpoint
            endpoints_df = pd.DataFrame({
                'Endpoint': ['PFS', 'OS', 'ORR', 'CR', 'DOR'],
                'Success_Rate': [0.73, 0.65, 0.58, 0.42, 0.61],
                'Trials': [342, 289, 198, 87, 156]
            })
            
            fig_endpoints = px.bar(
                endpoints_df,
                x='Endpoint',
                y='Success_Rate',
                title='Historical Success Rates by Primary Endpoint',
                labels={'Success_Rate': 'Success Rate', 'Endpoint': 'Primary Endpoint'},
                color='Success_Rate',
                color_continuous_scale='Viridis'
            )
            fig_endpoints.update_layout(showlegend=False)
            st.plotly_chart(fig_endpoints, use_container_width=True)
        
        st.markdown("### 📝 Inclusion/Exclusion Criteria")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### ✅ Key Inclusion Criteria")
            inclusion = [
                "Confirmed EGFR L858R mutation",
                "Stage IIIB/IV NSCLC",
                "ECOG PS 0-2",
                "Adequate organ function",
                "No prior EGFR-targeted therapy"
            ]
            for item in inclusion:
                st.markdown(f"- {item}")
        
        with col2:
            st.markdown("#### ❌ Key Exclusion Criteria")
            exclusion = [
                "Brain metastases (unless treated)",
                "Prior checkpoint inhibitor < 28 days",
                "Active autoimmune disease",
                "Concurrent malignancy",
                "Pregnancy or nursing"
            ]
            for item in exclusion:
                st.markdown(f"- {item}")
    
    with tab3:
        st.markdown("## Site Selection Results")
        
        # Filter sites by selected countries
        filtered_sites = sites_df[sites_df['country'].isin(countries)].copy()
        
        # Calculate composite score
        filtered_sites['composite_score'] = (
            filtered_sites['quality_score'] * 0.3 +
            (filtered_sites['enrollment_rate'] / 5.0) * 0.3 +
            (1 - filtered_sites['deviation_rate']) * 0.2 +
            (1 - filtered_sites['screen_failure_rate']) * 0.2
        )
        
        # Sort by composite score
        top_sites = filtered_sites.nlargest(15, 'composite_score')
        st.session_state.selected_sites = top_sites
        
        # Display map
        st.markdown("### 🗺️ Geographic Distribution")
        
        # Create map visualization
        country_counts = top_sites['country'].value_counts()
        
        col1, col2, col3 = st.columns(3)
        for i, (country, count) in enumerate(country_counts.items()):
            with [col1, col2, col3][i % 3]:
                st.metric(country, f"{count} sites")
        
        # Site rankings table
        st.markdown("### 🏆 Top Recommended Sites")
        
        display_cols = ['site_id', 'name', 'country', 'enrollment_rate', 
                       'quality_score', 'cost_per_patient', 'composite_score']
        
        st.dataframe(
            top_sites[display_cols].style.format({
                'enrollment_rate': '{:.1f} pts/mo',
                'quality_score': '{:.2%}',
                'cost_per_patient': '${:,.0f}',
                'composite_score': '{:.3f}'
            }).background_gradient(subset=['composite_score'], cmap='Greens'),
            use_container_width=True
        )
        
        # Site metrics visualization
        col1, col2 = st.columns(2)
        
        with col1:
            fig_enrollment = px.bar(
                top_sites.head(10),
                x='name',
                y='enrollment_rate',
                title='Enrollment Rates by Site',
                labels={'enrollment_rate': 'Patients/Month', 'name': 'Site'},
                color='enrollment_rate',
                color_continuous_scale='Blues'
            )
            fig_enrollment.update_xaxis(tickangle=-45)
            st.plotly_chart(fig_enrollment, use_container_width=True)
        
        with col2:
            fig_quality = px.scatter(
                top_sites,
                x='cost_per_patient',
                y='quality_score',
                size='enrollment_rate',
                color='country',
                title='Cost vs Quality Analysis',
                labels={'cost_per_patient': 'Cost per Patient ($)', 
                       'quality_score': 'Quality Score'}
            )
            st.plotly_chart(fig_quality, use_container_width=True)
    
    with tab4:
        if include_cost_analysis:
            st.markdown("## Cost Analysis")
            
            # Calculate costs
            selected_sites_df = st.session_state.selected_sites
            total_site_costs = selected_sites_df['cost_per_patient'].sum() * (target_enrollment / len(selected_sites_df))
            
            # Cost breakdown
            cost_breakdown = {
                'Site Costs': total_site_costs,
                'Drug Supply': target_enrollment * 15000,
                'Monitoring': target_enrollment * 5000,
                'Data Management': target_enrollment * 3000,
                'Regulatory': 250000,
                'Other': target_enrollment * 2000
            }
            
            total_cost = sum(cost_breakdown.values())
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Cost breakdown pie chart
                fig_pie = px.pie(
                    values=list(cost_breakdown.values()),
                    names=list(cost_breakdown.keys()),
                    title='Cost Breakdown by Category'
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            
            with col2:
                st.metric("Total Estimated Cost", f"${total_cost:,.0f}")
                st.metric("Cost per Patient", f"${total_cost/target_enrollment:,.0f}")
                st.metric("vs. Industry Average", "-23%", delta_color="inverse")
            
            # Country cost comparison
            st.markdown("### Cost by Country")
            
            country_costs = selected_sites_df.groupby('country')['cost_per_patient'].mean()
            
            fig_country_costs = px.bar(
                x=country_costs.index,
                y=country_costs.values,
                title='Average Cost per Patient by Country',
                labels={'x': 'Country', 'y': 'Cost per Patient ($)'}
            )
            st.plotly_chart(fig_country_costs, use_container_width=True)
        else:
            st.info("Cost analysis not included. Enable in the sidebar to view.")
    
    with tab5:
        if include_risk_assessment:
            st.markdown("## Risk Assessment")
            
            # Risk matrix
            risks = [
                {"Risk": "Slow enrollment", "Probability": "Medium", "Impact": "High", 
                 "Mitigation": "Selected high-performing sites, backup sites identified"},
                {"Risk": "Protocol amendments", "Probability": "Low", "Impact": "Medium",
                 "Mitigation": "Comprehensive protocol based on 342 similar trials"},
                {"Risk": "Site quality issues", "Probability": "Low", "Impact": "Medium",
                 "Mitigation": "Only selected sites with >85% quality scores"},
                {"Risk": "Regulatory delays", "Probability": "Medium", "Impact": "Medium",
                 "Mitigation": "Parallel submissions, experienced regulatory sites"},
                {"Risk": "Safety signals", "Probability": "Low", "Impact": "High",
                 "Mitigation": "Safety run-in, enhanced monitoring plan"}
            ]
            
            risk_df = pd.DataFrame(risks)
            
            # Risk heatmap
            risk_matrix = {
                ("Low", "Low"): 1, ("Low", "Medium"): 2, ("Low", "High"): 3,
                ("Medium", "Low"): 2, ("Medium", "Medium"): 4, ("Medium", "High"): 6,
                ("High", "Low"): 3, ("High", "Medium"): 6, ("High", "High"): 9
            }
            
            risk_df['Risk_Score'] = risk_df.apply(
                lambda x: risk_matrix[(x['Probability'], x['Impact'])], axis=1
            )
            
            # Display risk table
            st.dataframe(
                risk_df.style.background_gradient(
                    subset=['Risk_Score'], 
                    cmap='RdYlGn_r'
                ),
                use_container_width=True,
                hide_index=True
            )
            
            # Risk mitigation timeline
            st.markdown("### Risk Mitigation Timeline")
            
            timeline_data = [
                {"Phase": "Site Selection", "Month": 0, "Action": "Quality screening completed"},
                {"Phase": "Site Initiation", "Month": 1, "Action": "Training and certification"},
                {"Phase": "First Patient", "Month": 3, "Action": "Safety run-in begins"},
                {"Phase": "25% Enrolled", "Month": 6, "Action": "First DSMB review"},
                {"Phase": "50% Enrolled", "Month": 12, "Action": "Interim analysis"},
                {"Phase": "100% Enrolled", "Month": 18, "Action": "Enrollment complete"},
                {"Phase": "Database Lock", "Month": 24, "Action": "Final analysis"}
            ]
            
            timeline_df = pd.DataFrame(timeline_data)
            
            fig_timeline = px.scatter(
                timeline_df,
                x='Month',
                y='Phase',
                text='Action',
                title='Study Milestones & Risk Checkpoints'
            )
            fig_timeline.update_traces(textposition='top center', marker=dict(size=15))
            fig_timeline.update_layout(height=400)
            st.plotly_chart(fig_timeline, use_container_width=True)
        else:
            st.info("Risk assessment not included. Enable in the sidebar to view.")
    
    # Export section
    st.markdown("---")
    st.markdown("### 📥 Export Options")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📄 Generate PDF Report", use_container_width=True):
            st.success("PDF report generation initiated...")
            # In real implementation, generate actual PDF
    
    with col2:
        if st.button("📊 Export to Excel", use_container_width=True):
            st.success("Excel export initiated...")
            # In real implementation, create Excel file
    
    with col3:
        if st.button("🔗 Share Results", use_container_width=True):
            st.info("Shareable link: https://clinicaltrialai.app/results/demo123")
    
    with col4:
        if st.button("💾 Save Analysis", use_container_width=True):
            st.success("Analysis saved to your workspace")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #6b7280; font-size: 0.875rem;'>
    Clinical Trial Intelligence Platform v1.0 | Powered by Advanced AI
    </div>
    """,
    unsafe_allow_html=True
)