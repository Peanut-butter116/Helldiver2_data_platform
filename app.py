import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Helldivers 2 China Growth Intelligence Platform",
    page_icon="🎮",
    layout="wide",
)

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #1b1f4b 0%, #0a0d1f 35%, #070910 100%);
        color: #f7f9ff;
    }
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0d1f 0%, #13183a 100%);
        border-right: 1px solid rgba(98, 188, 255, 0.25);
    }
    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #e8ecff;
        line-height: 1.3;
        margin-bottom: 0.2rem;
    }
    .sidebar-subtitle {
        font-size: 0.88rem;
        color: #9eb6ff;
        margin-bottom: 1rem;
    }
    .sidebar-note {
        font-size: 0.8rem;
        color: #9aa5ce;
        border-left: 3px solid #52d3ff;
        padding-left: 0.6rem;
        margin-top: 0.8rem;
    }
    .card {
        background: linear-gradient(180deg, rgba(20, 26, 58, 0.95), rgba(13, 17, 40, 0.95));
        border: 1px solid rgba(108, 194, 255, 0.28);
        border-radius: 14px;
        padding: 16px 18px;
        box-shadow: 0 0 0 1px rgba(136, 90, 255, 0.08), 0 10px 30px rgba(0, 0, 0, 0.25);
        margin-bottom: 12px;
    }
    .metric-label { color: #9db3ff; font-size: 0.86rem; }
    .metric-value { color: #ffffff; font-size: 1.7rem; font-weight: 700; margin-top: 2px; }
    .metric-sub { color: #7fd3ff; font-size: 0.76rem; margin-top: 2px; }
    .section-title {
        color: #e9ecff;
        font-size: 1.08rem;
        font-weight: 700;
        margin: 0.2rem 0 0.7rem 0;
    }
    .recommend-box {
        background: rgba(82, 211, 255, 0.08);
        border: 1px solid rgba(82, 211, 255, 0.35);
        border-radius: 12px;
        padding: 12px 14px;
        color: #dff7ff;
        margin-top: 0.6rem;
    }
    .viral-box {
        background: rgba(163, 117, 255, 0.12);
        border: 1px solid rgba(196, 149, 255, 0.45);
        border-radius: 12px;
        padding: 12px 14px;
        color: #f0e4ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def metric_card(label: str, value: str, sub: str = ""):
    st.markdown(
        f"""
        <div class='card'>
            <div class='metric-label'>{label}</div>
            <div class='metric-value'>{value}</div>
            <div class='metric-sub'>{sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_card(title: str):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)


plotly_template = "plotly_dark"

# ---------- Sidebar ----------
st.sidebar.markdown("<div class='sidebar-title'>HELLDIVERS 2</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-subtitle'>China Growth Intelligence Platform</div>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Behavior Insights",
        "Experiments & Automation",
        "Community Signals",
        "Model Outputs",
        "Case Study",
    ],
)

st.sidebar.markdown(
    "<div class='sidebar-note'>Demo data only — created for product assessment.</div>",
    unsafe_allow_html=True,
)

# ---------- Shared Mock Data ----------
china_share = 8.2
target_share = 15.0
new_players_today = 1234
retention_7d = 28

trend_df = pd.DataFrame(
    {
        "date": pd.to_datetime(
            [
                "2025-05-04",
                "2025-05-05",
                "2025-05-06",
                "2025-05-07",
                "2025-05-08",
                "2025-05-09",
                "2025-05-10",
            ]
        ),
        "china_share": [7.1, 7.3, 7.6, 7.8, 8.0, 8.1, 8.2],
    }
)

# ---------- Page 1 ----------
if page == "Overview":
    st.title("Chinese Player Growth Command Center")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Current China Player Share", "8.2%")
    with c2:
        metric_card("Target", "15%")
    with c3:
        metric_card("New Chinese Players Today", f"{new_players_today:,}")
    with c4:
        metric_card("7-Day Retention", "28%")

    section_card("Progress to China Share Target")
    st.progress(china_share / target_share)
    st.caption(f"Current progress: {china_share:.1f}% of total players toward {target_share:.0f}% target.")

    col_l, col_r = st.columns([1.2, 1])
    with col_l:
        section_card("China Player Share Trend (7 Days)")
        fig_trend = px.line(trend_df, x="date", y="china_share", markers=True, template=plotly_template)
        fig_trend.update_traces(line_color="#52d3ff", marker_color="#be8bff", line_width=3)
        fig_trend.update_layout(yaxis_title="China Share (%)", xaxis_title="Date", height=320)
        st.plotly_chart(fig_trend, use_container_width=True)

    with col_r:
        section_card("Top Churn Barriers")
        churn_df = pd.DataFrame(
            {
                "barrier": [
                    "Network latency / disconnects",
                    "Early mission difficulty",
                    "Language / localisation",
                ],
                "share": [42, 28, 18],
            }
        )
        fig_churn = px.bar(
            churn_df,
            x="share",
            y="barrier",
            orientation="h",
            template=plotly_template,
            color="share",
            color_continuous_scale="Blues",
        )
        fig_churn.update_layout(coloraxis_showscale=False, height=320, xaxis_title="Share (%)", yaxis_title="")
        st.plotly_chart(fig_churn, use_container_width=True)

    section_card("High-Potential Channel Snapshot")
    channels_df = pd.DataFrame(
        {
            "Rank": [1, 2, 3],
            "Channel": ["Bilibili creator XX", "Douyin livestream YY", "Friend referral"],
            "CAC": ["¥8", "¥15", "¥0"],
            "7D Retention": ["35%", "18%", "45%"],
            "ROI Score": ["High", "Medium", "Very High"],
        }
    )
    st.dataframe(channels_df, use_container_width=True)
    st.markdown(
        "<div class='recommend-box'><b>Recommendation:</b> Increase Bilibili creator budget, optimise Douyin creative, and strengthen friend referral incentives.</div>",
        unsafe_allow_html=True,
    )

# ---------- Page 2 ----------
elif page == "Behavior Insights":
    st.title("Chinese Player Behavior Insights")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Average Session Length", "42m")
    with c2:
        metric_card("Prime-Time Activity Share", "47%")
    with c3:
        metric_card("Squad Match Rate", "31%")
    with c4:
        metric_card("Returning Player Rate", "38%")

    hours = list(range(24))
    activity = [5, 4, 4, 3, 2, 2, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 20, 24, 28, 33, 35, 32, 26, 16]
    activity_df = pd.DataFrame({"hour": hours, "activity": activity})

    col_l, col_r = st.columns([1.2, 1])
    with col_l:
        section_card("Active Time Pattern (Beijing Time)")
        fig_activity = px.line(activity_df, x="hour", y="activity", template=plotly_template, markers=True)
        fig_activity.update_traces(line_color="#5be5ff", line_width=3)
        fig_activity.update_layout(xaxis_title="Hour (00:00-23:00)", yaxis_title="Activity Index", height=330)
        st.plotly_chart(fig_activity, use_container_width=True)

    with col_r:
        section_card("Preferred Weapons")
        weapon_df = pd.DataFrame(
            {
                "weapon": ["Shotgun", "Machine Gun", "Orbital Cannon", "Grenade Launcher", "Laser Weapon"],
                "pref": [46, 32, 21, 15, 11],
            }
        )
        fig_weapon = px.bar(weapon_df, x="pref", y="weapon", orientation="h", template=plotly_template, color="pref")
        fig_weapon.update_layout(coloraxis_showscale=False, xaxis_title="Preference (%)", yaxis_title="", height=330)
        st.plotly_chart(fig_weapon, use_container_width=True)

    section_card("Top Drop-off Missions")
    drop_df = pd.DataFrame(
        {
            "Mission": ["First Extraction", "Bug Queen", "High-Pressure Defense"],
            "Failure Rate": ["58%", "43%", "37%"],
        }
    )
    st.dataframe(drop_df, use_container_width=True)

    st.markdown("### Social Behaviour Snapshot")
    st.markdown(
        "- Average friends: **2.1**  \n- Squad rate: **31%**  \n- Referral conversion: **12%**  \n- Most-used emotes: **👍 🇨🇳**"
    )
    st.markdown("<div class='recommend-box'>Schedule server maintenance in low periods and launch events during peak hours.</div>", unsafe_allow_html=True)
    st.markdown("<div class='recommend-box'>Show Chinese strategy guide pop-ups for high-failure missions.</div>", unsafe_allow_html=True)
    st.markdown("<div class='recommend-box'>Launch a dedicated Chinese squad channel and strengthen co-op features.</div>", unsafe_allow_html=True)

elif page == "Experiments & Automation":
    st.title("China Growth Experiments & Automation")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Active Experiments", "3")
    with c2:
        metric_card("Live Rules", "4")
    with c3:
        metric_card("Win Rate", "67%")
    with c4:
        metric_card("Estimated 7D Impact", "+5.4pp")

    section_card("Active Experiments")
    exp_df = pd.DataFrame(
        {
            "Experiment": [
                "Add Chinese voice prompt to tutorial step 3",
                "Change invite reward to limited China Dragon skin",
                "Bilibili creative: challenge -> 4-player co-op excitement",
            ],
            "Status": ["Running", "Collecting data", "Completed"],
            "Result": ["Completion rate +9% (p < 0.05)", "No significant change yet", "Landing-page CTR +14%, 7D retention +6%"],
            "Action": ["Roll out to all", "Extend test", "View report"],
        }
    )
    st.dataframe(exp_df, use_container_width=True)

    section_card("Live Automation Rules")
    st.markdown(
        """
        - If China-player latency > 150ms for 3 minutes → show **“Consider enabling a game accelerator.”**
        - If a China player fails 2 missions in a row → push Chinese **“Support Guide.”**
        - If first payment fails → suggest alternative payment option / resolution flow.
        - If invite sent but friend does not complete first match → notify inviter: **“Your squadmate needs support.”**
        """
    )

    col1, col2 = st.columns([1.1, 1])
    with col1:
        section_card("Experiment Funnel")
        funnel_df = pd.DataFrame(
            {
                "stage": ["Impressions", "Clicks", "Install", "Tutorial Complete", "Day 7 Retention", "Payer Conversion"],
                "count": [4_320_000, 312_000, 76_100, 43_200, 17_600, 2_110],
            }
        )
        fig_funnel = go.Figure(go.Funnel(y=funnel_df["stage"], x=funnel_df["count"], marker={"color": ["#53d2ff", "#63beff", "#739fff", "#8b85ff", "#a56fff", "#c85fff"]}))
        fig_funnel.update_layout(template=plotly_template, height=360)
        st.plotly_chart(fig_funnel, use_container_width=True)

    with col2:
        section_card("Estimated 7D Impact Trend")
        impact_df = pd.DataFrame({"day": [1, 2, 3, 4, 5, 6, 7], "impact_pp": [0.8, 1.4, 2.1, 3.2, 4.0, 4.8, 5.4]})
        fig_impact = px.line(impact_df, x="day", y="impact_pp", markers=True, template=plotly_template)
        fig_impact.update_traces(line_color="#b58aff", line_width=3)
        fig_impact.update_layout(yaxis_title="Impact (+pp)", xaxis_title="Day", height=360)
        st.plotly_chart(fig_impact, use_container_width=True)

elif page == "Community Signals":
    st.title("Chinese Community Signals")
    st.write(
        "Tencent can turn Chinese comments from Tencent Video, WeChat Channels, QQ communities and monitored platforms such as Bilibili, NGA, 小黑盒 and Tieba into structured growth signals."
    )

    signals_df = pd.DataFrame(
        {
            "Signal type": ["Download intent", "Squad seeking", "Technical concern", "Price / monetisation concern", "Viral cultural signal"],
            "Example Chinese keywords/comments": [
                "在哪下载, 我也想玩, PS5能玩吗, Steam叫什么",
                "有人一起开黑吗, 求队友, 带带我",
                "国内会不会卡, 掉线, 延迟高, 匹配不到人",
                "多少钱, 等打折, 战债值不值, 超级币贵吗",
                "赛博淞沪会战, 上海保卫战, 超级地球, 太燃了",
            ],
            "Business meaning": [
                "Potential new player",
                "Good target for referral / squad campaign",
                "Network barrier before purchase",
                "Pricing or Warbond concern",
                "Community event or campaign opportunity",
            ],
        }
    )
    st.dataframe(signals_df, use_container_width=True)

    rng = np.random.default_rng(42)
    platforms = ["Bilibili", "NGA", "小黑盒", "Tieba", "WeChat Channels", "QQ Group"]
    intents = ["Download intent", "Squad seeking", "Technical concern", "Price concern", "Viral signal"]
    sentiments = ["Positive", "Neutral", "Negative"]
    keywords = ["在哪下载", "求队友", "延迟高", "太燃了", "等打折", "上海保卫战"]
    mock_comments = pd.DataFrame(
        {
            "comment_text": rng.choice(["我也想玩", "求队友一起", "会不会卡", "太燃了", "等打折再买", "上海保卫战冲!"], 180),
            "source_platform": rng.choice(platforms, 180),
            "keyword_tag": rng.choice(keywords, 180),
            "intent_label": rng.choice(intents, 180),
            "sentiment": rng.choice(sentiments, 180, p=[0.45, 0.35, 0.2]),
            "engagement_score": rng.integers(10, 1000, 180),
        }
    )

    c1, c2 = st.columns(2)
    with c1:
        platform_filter = st.selectbox("source_platform", ["All"] + platforms)
    with c2:
        intent_filter = st.selectbox("intent_label", ["All"] + intents)

    filtered = mock_comments.copy()
    if platform_filter != "All":
        filtered = filtered[filtered["source_platform"] == platform_filter]
    if intent_filter != "All":
        filtered = filtered[filtered["intent_label"] == intent_filter]

    x1, x2, x3 = st.columns(3)
    with x1:
        fig_intent = px.histogram(filtered, x="intent_label", template=plotly_template, color="intent_label")
        fig_intent.update_layout(showlegend=False, height=280)
        st.plotly_chart(fig_intent, use_container_width=True)
    with x2:
        fig_sent = px.histogram(filtered, x="sentiment", template=plotly_template, color="sentiment")
        fig_sent.update_layout(showlegend=False, height=280)
        st.plotly_chart(fig_sent, use_container_width=True)
    with x3:
        top_kw = filtered.groupby("keyword_tag", as_index=False)["engagement_score"].sum().sort_values("engagement_score", ascending=False)
        fig_kw = px.bar(top_kw.head(6), x="keyword_tag", y="engagement_score", template=plotly_template, color="engagement_score")
        fig_kw.update_layout(coloraxis_showscale=False, height=280)
        st.plotly_chart(fig_kw, use_container_width=True)

    st.markdown("<div class='viral-box'><b>Viral Alert:</b> Spike detected: ‘Cyber Shanghai Defence’ mentions +340% in 24h.</div>", unsafe_allow_html=True)
    st.markdown("<div class='recommend-box'>The platform should go beyond sentiment analysis and identify who wants to play, who needs teammates, what blocks conversion, and which cultural moments can be amplified.</div>", unsafe_allow_html=True)
    st.dataframe(filtered.head(30), use_container_width=True)

elif page == "Model Outputs":
    st.title("Model Outputs")
    tab_a, tab_b, tab_c, tab_d = st.tabs(["Churn Attribution", "Player Preference Clustering", "Channel Attribution", "Social Referral Analysis"])
    with tab_a:
        st.markdown("**Inputs:** technical logs, mission failure, localisation signals, social media complaints")
        st.markdown("**Methods:** topic modelling, gradient boosting/XGBoost churn risk scoring, multi-class churn reason classifier")
        c1, c2, c3 = st.columns(3)
        c1.metric("High-risk CN players", "18.4%")
        c2.metric("Top reason", "Network")
        c3.metric("7D churn uplift", "+9pp")
        reason_df = pd.DataFrame({"reason": ["Network", "Difficulty", "Social", "Localisation"], "mix": [42, 28, 18, 10]})
        st.plotly_chart(px.bar(reason_df, x="reason", y="mix", template=plotly_template, color="mix"), use_container_width=True)

    with tab_b:
        st.markdown("**Inputs:** squad size, difficulty, mission style, weapon/stratagem use, playtime, referrals")
        st.markdown("**Methods:** feature engineering + K-means/GMM, PCA/UMAP visualisation, cluster profiling")
        st.markdown("**Segments:** Hardcore co-op, Casual solo, Social referral, Content explorers, Churn-prone learners")
        c1, c2, c3 = st.columns(3)
        c1.metric("Largest segment", "Casual Solo")
        c2.metric("Best retention", "Hardcore Co-op")
        c3.metric("Best referral", "Social Seed")
        rng = np.random.default_rng(7)
        cluster_names = ["Hardcore co-op", "Casual solo", "Social referral", "Content explorers", "Churn-prone learners"]
        pts = []
        for i, name in enumerate(cluster_names):
            cx, cy = rng.uniform(-4, 4), rng.uniform(-4, 4)
            for _ in range(55):
                pts.append((rng.normal(cx, 0.6), rng.normal(cy, 0.6), name))
        cluster_df = pd.DataFrame(pts, columns=["x", "y", "cluster"])
        st.plotly_chart(px.scatter(cluster_df, x="x", y="y", color="cluster", template=plotly_template), use_container_width=True)

    with tab_c:
        st.markdown("**Inputs:** source channel, KOL, tags, click, install, retention, Warbond spend")
        st.markdown("**Methods:** first-touch + multi-touch attribution, ROI by cohort, incrementality/MMM")
        c1, c2, c3 = st.columns(3)
        c1.metric("Best ROI", "Bilibili")
        c2.metric("Most installs", "Douyin")
        c3.metric("Best D30", "Referral")
        attr_df = pd.DataFrame(
            {
                "channel": ["Bilibili/KOL", "Douyin", "Steam discount", "PS Store feature", "Social referral"],
                "installs": [22100, 28400, 14300, 9800, 11700],
                "CAC": [8, 15, 12, 10, 0],
                "D7 retention": [35, 18, 24, 27, 45],
                "D30 retention": [20, 11, 14, 16, 29],
                "Warbond conversion": [8.2, 4.1, 5.0, 6.2, 7.4],
                "ROI score": [92, 61, 69, 75, 98],
            }
        )
        st.dataframe(attr_df, use_container_width=True)

    with tab_d:
        st.markdown("**Inputs:** referral code, WeChat/QQ share, invite clicks, first squad play, accepted invite, D7 retention")
        st.markdown("**Methods:** referral graph, seed scoring, invite chain path analysis, funnel drop-off analysis")
        c1, c2, c3 = st.columns(3)
        c1.metric("Top seed", "Squad host")
        c2.metric("Best step", "Install")
        c3.metric("Weakest step", "First squad")
        ref_funnel = pd.DataFrame({"stage": ["Invite Sent", "Invite Click", "Install", "First Squad", "D7 Retained"], "count": [18000, 9100, 4200, 1700, 760]})
        st.plotly_chart(go.Figure(go.Funnel(y=ref_funnel["stage"], x=ref_funnel["count"], marker={"color": ["#5bd0ff", "#71b5ff", "#8f98ff", "#aa7eff", "#ca66ff"]})).update_layout(template=plotly_template, height=350), use_container_width=True)
        chain_df = pd.DataFrame({"seed_player": ["A102", "B773", "C559", "D098"], "invite_chain_len": [5, 4, 3, 3], "squad_conversion": [0.42, 0.37, 0.29, 0.26]})
        st.dataframe(chain_df, use_container_width=True)

else:
    st.title("Case Study: Cyber Shanghai Defence")
    st.subheader("1) What happened?")
    st.write(
        "In Helldivers 2’s 2025 virtual Earth defence event, Shanghai became a key final stronghold. Chinese players rallied around defending it, while global players joined across time zones, turning the mission into a viral community moment."
    )

    st.subheader("2) Why it matters")
    cols = st.columns(3)
    bullets = [
        "Player-generated campaign",
        "Cultural resonance",
        "Global unity / 世界大团结",
        "China–US player cooperation",
        "Social sharing effect",
        "Growth potential",
    ]
    for i, b in enumerate(bullets):
        cols[i % 3].markdown(f"<div class='card'>{b}</div>", unsafe_allow_html=True)

    st.subheader("3) How the platform captures it")
    st.markdown(
        """
        - Detect keyword spikes: “赛博淞沪会战”, “上海保卫战”, “Equality-on-Sea”
        - Track content reactions: “我也想玩”, “在哪下载”, “有人一起开黑吗”
        - Measure returning players, squad formation, referral links, and D7 retention
        - Identify which channels amplified the event
        - Recommend creator content, China-time events, or commemorative rewards
        """
    )

    st.subheader("4) From one-off event to long-term growth")
    st.markdown("### Detect → Diagnose → Amplify → Convert → Repeat")
    st.markdown(
        """
        **Detect:** Track keyword spikes, creator engagement, shares, comments, and download-intent signals.

        **Diagnose:** Identify why the event resonates: cultural meaning, co-op gameplay, global unity, China–US cooperation, and social sharing.

        **Amplify:** Launch creator recaps, China-time missions, squad-up challenges, commemorative rewards, and WeChat/QQ referral campaigns.

        **Convert:** Guide interested users from viral content to PS/Steam store pages, squad-finder, beginner guides, and first-mission support.

        **Repeat:** Measure new players, returning players, referral chains, D7 retention, and revenue, then turn successful patterns into a future China live-ops playbook.
        """
    )

    strategy_df = pd.DataFrame(
        {
            "Strategy": [
                "City-defence live events",
                "Creator recap campaigns",
                "Cultural reward design",
                "Cross-time-zone cooperation",
                "New-player conversion flow",
            ],
            "Example campaign idea": [
                "China-time ‘Defend Super Earth’ weekend missions linked to symbolic cities",
                "Tencent Video / WeChat Channels creators summarise heroic player moments",
                "Limited titles, capes, banners or emotes inspired by community moments",
                "Global relay defence events with prime-time regional protection",
                "Viral video → landing page → PS/Steam link → squad-finder → beginner guide",
            ],
        }
    )
    st.dataframe(strategy_df, use_container_width=True)
