from nicegui import ui

# === Logic
def send_message():
    msg = message_box.value.strip()
    if msg:
        print(f"[User] {msg}")
        message_box.value = ""

# === Styles
ui.add_head_html("""
<link href="https://fonts.googleapis.com/css2?family=Fira+Code&display=swap" rel="stylesheet">
<style>
  html, body {
    margin: 0; padding: 0;
    font-family: 'Fira Code', monospace;
    background-color: #0d0d0d;
    color: #e5e7eb;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    box-sizing: border-box;
  }

  .container {
    display: flex;
    height: 100vh;
    width: 100vw;
  }

  .sidebar {
    position: absolute;
    top: 0; left: 0;
    width: 220px;
    height: 100vh;
    background-color: #000;
    display: flex;
    flex-direction: column;
    padding-top: 12px;
  }

  .sidebar-btn {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 16px;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.3s ease;
    width: 100%;
  }

  .sidebar-btn:hover, .sidebar-btn.active {
    background-color: #1f1f1f;
    border-left: 4px solid #3B82F6;
  }

  .sidebar-icon {
    font-size: 20px;
    color: #3B82F6;
  }

  .main {
    margin-left: 220px;
    width: calc(100vw - 220px);
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 48px;
    padding: 0 16px;
    border-bottom: 1px solid #1f1f1f;
    width: 100%;
    box-sizing: border-box;
    position: relative;
  }

  .brand-container {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .brand {
    font-size: 20px;
    color: #3B82F6;
    font-weight: bold;
  }

  .intro-box {
    background-color: #1f1f1f;
    border-radius: 8px;
    padding: 12px;
    font-size: 14px;
    max-width: 400px;
    color: #cbd5e1;
    white-space: pre-line;
    position: absolute;
    top: 52px;
    left: 16px;
    z-index: 10;
    display: none;
  }

  .show {
    display: block !important;
  }

  .console-stack {
    font-size: 24px;
    line-height: 1.8;
    text-align: center;
    margin-top: 40px;
  }

  .code-blue {
    color: #3B82F6;
    font-weight: 600;
  }

  #logicLine {
    border-right: 2px solid #3B82F6;
    white-space: nowrap;
    overflow: hidden;
    display: inline-block;
    animation: blinkCursor 0.8s step-end infinite;
  }

  @keyframes blinkCursor {
    0%, 100% { border-color: transparent; }
    50% { border-color: #3B82F6; }
  }

  .input-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 24px;
  }

  .input-bar {
    background: linear-gradient(to right, #1a1a1a, #111827);
    border-radius: 12px;
    padding: 12px 16px;
    display: flex;
    gap: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    width: 80%;
    max-width: 700px;
  }

  .input-bar input {
    flex-grow: 1;
    border: none;
    color: #f3f4f6;
    font-size: 16px;
    outline: none;
    padding: 10px 12px;
    border-radius: 8px;
    background-color: transparent;
  }

  .input-bar button {
    background: none;
    border: none;
    color: #3B82F6;
    font-size: 22px;
    cursor: pointer;
  }

  .input-bar button:hover {
    color: #60a5fa;
  }

  @media (max-width: 768px) {
    .sidebar {
      display: none;
    }
    .main {
      margin-left: 0;
      width: 100vw;
    }
    .console-stack {
      font-size: 20px;
      margin-top: 24px;
    }
    .input-bar {
      flex-direction: column;
      gap: 8px;
      width: 90%;
    }
  }
</style>
""")

# === Layout
with ui.element('div').classes('container'):

    # Sidebar
    with ui.column().classes('sidebar'):
        ui.label('TM').classes('text-[#3B82F6] text-lg font-bold px-4 pb-2')
        for icon, label, active in [('home', 'Home', True), ('folder', 'Projects', False), ('send', 'Contact', False)]:
            classes = 'sidebar-btn active' if active else 'sidebar-btn'
            with ui.element('div').classes(classes):
                ui.icon(icon).classes('sidebar-icon')
                ui.label(label).classes('text-sm')

    # Main Column
    with ui.column().classes('main'):

        # Header
        ui.html('''
        <div class="top-bar">
            <div class="brand-container">
                <div class="brand">TebogoGPT</div>
                <i id="toggleIntro" class="material-icons" style="cursor:pointer;color:#3B82F6;">expand_more</i>
            </div>
            <button class="resume-btn" style="margin-left:auto; border:1px solid #3B82F6; background:none; color:#3B82F6; padding:6px 12px; border-radius:6px;">Download Resume</button>
            <div id="introBox" class="intro-box">
Hey there! I’m your personal AI introducing Tebogo Monamodi’s work. 🚀

Skill: Building fast real-time apps with Python & FastAPI.
Project: Try the Voice Transcriber App for starters.

Curious to download the resume or view some projects?
            </div>
        </div>
        ''')

        # Console Message
        ui.html('''
        <div class="console-stack">
          <div><span class="code-blue">print</span>("Hello, World")</div>
          <div>&lt;<span class="code-blue">AI meets Software Craftsmanship</span> /&gt;</div>
          <div id="logicLine">|</div>
        </div>
        ''')

        # Input Bar
        with ui.element('div').classes('input-wrapper'):
            with ui.element('div').classes('input-bar'):
                message_box = ui.input(placeholder='Send a message...').classes(
                    'w-full bg-transparent text-white px-4 py-2 rounded-md text-[15px] font-normal'
                )
                ui.button('', icon='arrow_upward', on_click=lambda: send_message()).classes(
                    'text-[#3B82F6] text-[22px] hover:text-[#60a5fa]'
                )

# JS Logic
ui.add_body_html("""
<script>
  const text = 'Where creativity meets logic...';
  let index = 0;
  const el = document.getElementById('logicLine');

  function typeLogic() {
    if (index <= text.length) {
      el.textContent = text.substring(0, index++);
      setTimeout(typeLogic, 70);
    }
  }

  typeLogic();

  document.getElementById('toggleIntro').addEventListener('click', () => {
    document.getElementById('introBox').classList.toggle('show');
  });
</script>
""")

# Run App
ui.run(title='TebogoGPT Console', dark=True)

