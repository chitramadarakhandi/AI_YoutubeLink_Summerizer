import gradio as gr
from transformers import pipeline
import yt_dlp

# MODEL LOADING (Your logic intact)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1
)

def get_video_text(url: str) -> str:
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "forcejson": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    title = info.get("title", "")
    description = info.get("description", "")

    return f"{title}. {description}".strip()

def summarize_youtube(video_url: str) -> str:
    try:
        text = get_video_text(video_url)

        if not text:
            return "❌ No text available to summarize."

        chunks = [text[i:i+800] for i in range(0, len(text), 800)]

        summaries = []
        for chunk in chunks[:3]:
            result = summarizer(
                chunk,
                max_length=120,
                min_length=40,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])

        return "🤖 " + " ".join(summaries)

    except Exception as e:
        return f"❌ Error: {e}"

# DUMMY AUTH (UI ONLY)
def login(user, pwd):
    if user and pwd:
        return "✅ Login successful!"
    return "❌ Enter valid credentials"

def register(user, pwd):
    if user and pwd:
        return "✅ Registered successfully!"
    return "❌ Fill all fields"

# UI STARTS HERE
with gr.Blocks(css="""
body {
    background: #0f172a;
}
.navbar {
    background: linear-gradient(90deg, #6366f1, #9333ea);
    padding: 15px;
    font-size: 20px;
    font-weight: bold;
    color: white;
    text-align: center;
}
.tech-box {
    background: #1e293b;
    border-radius: 12px;
    padding: 15px;
    color: white;
    text-align: center;
    font-weight: bold;
}
.chat-box {
    background: #020617;
    border-radius: 15px;
    padding: 20px;
}
""") as demo:

    # ---------------- NAVBAR ----------------
    gr.HTML("""
    <div class="navbar">
        🔐 Login | 📝 Register | 🤖 Summarizer AI | 🛠 Tech Stack
    </div>
    """)

    with gr.Tabs():

        # ---------------- LOGIN TAB ----------------
        with gr.Tab("🔐 Login"):
            gr.Markdown("## Login to Your Account")
            login_user = gr.Textbox(label="Username")
            login_pwd = gr.Textbox(label="Password", type="password")
            login_btn = gr.Button("Login", variant="primary")
            login_out = gr.Textbox(label="Status")

            login_btn.click(login, [login_user, login_pwd], login_out)

        # ---------------- REGISTER TAB ----------------
        with gr.Tab("📝 Register"):
            gr.Markdown("## Create New Account")
            reg_user = gr.Textbox(label="Username")
            reg_pwd = gr.Textbox(label="Password", type="password")
            reg_btn = gr.Button("Register", variant="primary")
            reg_out = gr.Textbox(label="Status")

            reg_btn.click(register, [reg_user, reg_pwd], reg_out)

        # ---------------- SUMMARIZER AI ----------------
        with gr.Tab("🤖 Summarizer AI"):
            gr.Markdown("## 💬 Chat with YouTube Summarizer AI")

            with gr.Row():
                gr.Markdown("🤖 **AI Bot Ready**")

            with gr.Column(elem_classes="chat-box"):
                yt_link = gr.Textbox(
                    placeholder="Paste YouTube video link here...",
                    label="YouTube URL"
                )
                summarize_btn = gr.Button("🚀 Summarize")
                summary_output = gr.Textbox(
                    label="AI Response",
                    lines=8
                )

            summarize_btn.click(
                summarize_youtube,
                inputs=yt_link,
                outputs=summary_output
            )

        # ---------------- TECH STACK ----------------
        with gr.Tab("🛠 Tech Stack"):
            gr.Markdown("## Technologies Used")

            with gr.Row():
                gr.HTML('<div class="tech-box">🐍 Python</div>')
                gr.HTML('<div class="tech-box">🤗 Transformers</div>')
                gr.HTML('<div class="tech-box">🧠 BART-Large-CNN</div>')

            with gr.Row():
                gr.HTML('<div class="tech-box">🎥 yt-dlp</div>')
                gr.HTML('<div class="tech-box">🎨 Gradio</div>')
                gr.HTML('<div class="tech-box">💻 VS Code</div>')

            gr.Markdown("""
            ### Project Highlights
            - AI-powered YouTube summarization  
            - Chatbot-style interface  
            - Modular UI with authentication pages  
            - CPU-safe transformer model  
            """)

# -------------------------------
# LAUNCH
# -------------------------------
# demo.launch() # for local testing
demo.launch(share=True) # to get public link

