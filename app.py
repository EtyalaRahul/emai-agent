import streamlit as st
import traceback

from graph import graph
from nodes import (
    evaluate_email,
    improve_email
)

st.set_page_config(
    page_title="AI Email Writing Trainer",
    page_icon="📧",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );
}

.block-container {
    padding-top: 1rem;
}

.hero-title {
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:white;
    margin-bottom:5px;
}

.hero-sub {
    text-align:center;
    color:#cbd5e1;
    margin-bottom:25px;
}

.glass-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(16px);
    border:1px solid rgba(255,255,255,0.12);
    padding:20px;
    border-radius:20px;
    margin-bottom:15px;
}

.metric-card {
    background: rgba(255,255,255,0.08);
    border-radius:15px;
    padding:15px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
}

.metric-value {
    font-size:30px;
    font-weight:bold;
    color:#22c55e;
}

.metric-label {
    color:white;
}

.footer {
    text-align:center;
    color:#94a3b8;
    margin-top:40px;
    font-size:14px;
}

.phrase-box {
    background:#1e293b;
    padding:8px;
    border-radius:10px;
    margin-bottom:8px;
    color:#e2e8f0;
}

.big-textarea textarea {
    min-height:450px !important;
    font-size:16px !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

if "question" not in st.session_state:
    st.session_state.question = None

if "evaluation" not in st.session_state:
    st.session_state.evaluation = None

if "improved_email" not in st.session_state:
    st.session_state.improved_email = None

# -----------------------------
# GEMINI KEY SCREEN
# -----------------------------

if not st.session_state.api_key:

    st.markdown(
        """
        <div class='hero-title'>
        📧 AI Email Writing Trainer
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='hero-sub'>
        Practice TCS-style Email Writing with AI Evaluation
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='glass-card'>",
        unsafe_allow_html=True
    )

    st.subheader("🔑 Enter Gemini API Key")

    key = st.text_input(
        "Gemini API Key",
        type="password"
    )

    if st.button("Start Practice", use_container_width=True):

        if key.strip():

            st.session_state.api_key = key
            st.rerun()

        else:
            st.error("Please enter a Gemini API Key")

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    """
    <div class='hero-title'>
    📧 AI Email Writing Trainer
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='hero-sub'>
    Generate Unlimited TCS-Style Email Writing Questions
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TOP BUTTONS
# -----------------------------

col_btn1, col_btn2, col_btn3 = st.columns([1,1,5])

with col_btn1:

    if st.button(
        "🎯 New Question",
        use_container_width=True
    ):

        try:

            result = graph.invoke(
                {
                    "api_key": st.session_state.api_key,
                    "action": "generate"
                }

            )

            st.session_state.question = (
                result["question"]
            )

            st.session_state.evaluation = None
            st.session_state.improved_email = None

            st.rerun()

        except Exception as e:

            st.error(str(e))

with col_btn2:

    if st.button(
        "🔄 Reset",
        use_container_width=True
    ):

        st.session_state.question = None
        st.session_state.evaluation = None
        st.session_state.improved_email = None

        st.rerun()

# -----------------------------
# NO QUESTION
# -----------------------------

if not st.session_state.question:

    st.info(
        "Click 'New Question' to generate a practice email."
    )

    st.stop()

question = st.session_state.question

# -----------------------------
# MAIN LAYOUT
# -----------------------------

left, right = st.columns([1,1])

# -----------------------------
# LEFT PANEL
# -----------------------------

with left:

    st.markdown(
        """
        <div class='glass-card'>
        <h2>🤖 AI Coach</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class='glass-card'>
        <h3>Scenario</h3>
        <p>{question['scenario']}</p>

        <hr>

        <b>Role:</b> {question['role']}<br>
        <b>Recipient:</b> {question['recipient']}<br>
        <b>Minimum Words:</b> {question['min_words']}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Mandatory Phrases")

    for phrase in question["phrases"]:

        st.markdown(
            f"""
            <div class='phrase-box'>
            ✅ {phrase}
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.session_state.evaluation:

        ev = st.session_state.evaluation

        st.markdown("## 📊 Evaluation")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Grammar",
                ev["grammar"]
            )

            st.metric(
                "Tone",
                ev["tone"]
            )

            st.metric(
                "Clarity",
                ev["clarity"]
            )

        with c2:

            st.metric(
                "Structure",
                ev["structure"]
            )

            st.metric(
                "Phrases",
                ev["phrases"]
            )

            st.metric(
                "Total",
                ev["total"]
            )

        st.markdown("### Missing Phrases")

        missing = ev.get(
            "missing_phrases",
            []
        )

        if missing:

            for item in missing:
                st.error(item)

        else:
            st.success(
                "All mandatory phrases used."
            )

        st.markdown("### Suggestions")

        for item in ev["suggestions"]:
            st.info(item)

# -----------------------------
# RIGHT PANEL
# -----------------------------

with right:

    st.markdown(
        """
        <div class='glass-card'>
        <h2>✍ Email Editor</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    email_text = st.text_area(
        "Write your email here",
        height=500,
        key="email_editor"
    )

    if st.button(
        "🚀 Evaluate Email",
        use_container_width=True
    ):

        if not email_text.strip():

            st.warning(
                "Please write an email first."
            )

        else:

            try:

                eval_result = evaluate_email(
                    {
                        "api_key":
                        st.session_state.api_key,

                        "question":
                        question,

                        "email":
                        email_text
                    }
                )

                st.session_state.evaluation = (
                    eval_result["evaluation"]
                )

                improved = improve_email(
                    {
                        "api_key":
                        st.session_state.api_key,

                        "question":
                        question,

                        "email":
                        email_text
                    }
                )

                st.session_state.improved_email = (
                    improved[
                        "improved_email"
                    ]
                )

                st.rerun()

            except Exception:

                st.error(
                    traceback.format_exc()
                )

    if st.session_state.improved_email:

        st.markdown("## 🌟 Improved Version")

        st.code(
            st.session_state.improved_email,
            language="text"
        )

# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
    """
    <hr>
    <div class='footer'>
        🚀 Developed by <b>Etyala Rahul</b>
    </div>
    """,
    unsafe_allow_html=True
)