from flask import Flask, request, render_template_string
import mimetypes

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Stream Video</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f0f0;
      padding: 20px;
      text-align: center;
    }
    .container {
      background: white;
      padding: 20px;
      max-width: 600px;
      margin: auto;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    input[type="text"] {
      width: 90%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      padding: 10px 20px;
      border: none;
      background: #007BFF;
      color: white;
      font-size: 16px;
      border-radius: 5px;
      cursor: pointer;
    }
    video {
      width: 100%;
      margin-top: 20px;
      border-radius: 10px;
      background: black;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>🎥 Enter Video URL to Stream</h2>
    <form method="POST">
      <input type="text" name="video_url" placeholder="Paste video URL (.mp4, .m4v, .webm, .ogg)" required value="{{ url or '' }}">
      <br>
      <button type="submit">▶️ Play</button>
    </form>
    {% if url %}
    <video controls autoplay preload="none">
      <source src="{{ url }}" type="{{ mime }}">
      Your browser does not support the video tag.
    </video>
    {% endif %}
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    url, mime = None, "video/mp4"
    if request.method == 'POST':
        url = request.form.get('video_url')
        mime = mimetypes.guess_type(url)[0] or "video/mp4"
    return render_template_string(HTML_TEMPLATE, url=url, mime=mime)

if __name__ == '__main__':
    # Render gives us a PORT env variable
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
