
import streamlit as st

from prompt_analyzer import analyze_prompt
from prompt_improver import improve_prompt, generate_response


st.set_page_config(
    page_title="AI Prompt Analyzer & Improver",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Prompt Analyzer & Improver")
st.write(
    "Analyze your prompt, understand its prompting techniques, "
    "and improve it automatically using a local AI model."
)

st.info(
    "Enter a prompt below. The application will analyze it first. "
    "You can review the analysis before improving the prompt."
)

# Keep results between Streamlit reruns.
if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "original_prompt" not in st.session_state:
    st.session_state.original_prompt = ""

if "original_output" not in st.session_state:
    st.session_state.original_output = ""

if "improved_prompt" not in st.session_state:
    st.session_state.improved_prompt = ""

if "improved_output" not in st.session_state:
    st.session_state.improved_output = ""


# STEP 1: User enters a prompt.
with st.form("prompt_form"):
    user_prompt = st.text_area(
        "Enter your prompt",
        placeholder="Example: Explain deadlock",
        height=130
    )

    analyze_button = st.form_submit_button(
        "🔍 Analyze Prompt",
        type="primary"
    )


# STEP 2: Analyze and generate the original output.
if analyze_button:
    if not user_prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Analyzing your prompt..."):
            analysis = analyze_prompt(user_prompt)

        st.session_state.analysis = analysis
        st.session_state.original_prompt = user_prompt
        st.session_state.original_output = ""
        st.session_state.improved_prompt = ""
        st.session_state.improved_output = ""

        with st.spinner("Generating the original response..."):
            original_output = generate_response(user_prompt)

        st.session_state.original_output = original_output


# STEP 3: Display analysis for review.
if st.session_state.analysis is not None:
    st.divider()
    st.header("1. Prompt Analysis")

    st.write("**Original prompt:**")
    st.code(st.session_state.original_prompt, language=None)

    st.write("**Detected prompting techniques:**")

    techniques = st.session_state.analysis["techniques"]

    if techniques:
        for technique in techniques:
            st.success(technique)
    else:
        st.warning("No techniques detected.")

    st.write("**Reasoning:**")
    st.write(st.session_state.analysis["explanation"])

    st.divider()
    st.header("2. Original Prompt Output")
    st.markdown(st.session_state.original_output)

    # STEP 4: Wait for the user's decision.
    st.divider()
    st.header("3. Review and Improve")

    st.write(
        "Review the classification and original response. "
        "When you're ready, click the button to improve your prompt."
    )

    if st.button("✨ Improve Prompt", type="primary"):
        with st.spinner("Improving your prompt..."):
            improved = improve_prompt(
                st.session_state.original_prompt
            )

        if improved.startswith("Unable to generate a response."):
            st.error(improved)
        else:
            st.session_state.improved_prompt = improved

            with st.spinner("Generating the improved response..."):
                st.session_state.improved_output = (
                    generate_response(improved)
                )

            st.rerun()


# STEP 5: Display the improved prompt and comparison.
if st.session_state.improved_prompt:
    st.divider()
    st.header("4. Improved Prompt")

    st.write(
        "You can edit the improved prompt before generating "
        "its final response."
    )

    edited_prompt = st.text_area(
        "Edit improved prompt",
        value=st.session_state.improved_prompt,
        height=180,
        key="edited_prompt"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Generate Updated Output"):
            if edited_prompt.strip():
                with st.spinner("Generating updated response..."):
                    st.session_state.improved_prompt = edited_prompt
                    st.session_state.improved_output = (
                        generate_response(edited_prompt)
                    )
                st.rerun()
            else:
                st.warning("The improved prompt cannot be empty.")

    with col2:
        st.download_button(
            "⬇️ Download Improved Prompt",
            data=st.session_state.improved_prompt,
            file_name="improved_prompt.txt",
            mime="text/plain"
        )

    st.divider()
    st.header("5. Compare Outputs")

    original_col, improved_col = st.columns(2)

    with original_col:
        st.subheader("Original Output")
        st.markdown(st.session_state.original_output)

    with improved_col:
        st.subheader("Improved Output")
        st.markdown(st.session_state.improved_output)

    st.caption(
        "The improved response may differ in detail, clarity, "
        "structure, and relevance. Better results are not guaranteed "
        "for every prompt."
    )

st.divider()
st.caption("Powered by Python, Streamlit, and Ollama")
