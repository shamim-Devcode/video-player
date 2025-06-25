from flask import Flask, request, render_template_string

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
      <input type="text" name="video_url" placeholder="Paste .mp4 video URL" required value="{{ url or '' }}">
      <br>
      <button type="submit">▶️ Play</button>
    </form>
    {% if url %}
    <video controls autoplay preload="none">
      <source src="{{ url }}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    {% endif %}
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    if request.method == 'POST':
        url = request.form.get('video_url')
    return render_template_string(HTML_TEMPLATE, url=url)

if __name__ == '__main__':
    app.run(debug=True)
