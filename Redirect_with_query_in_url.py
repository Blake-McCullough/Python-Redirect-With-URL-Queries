#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com




#URL FOR ANDROID VM IS 10.0.2.2:8000
from flask import Flask, request
app = Flask(import_name=__name__)

@app.route("/")
def echo():

    to_echo = request.args.get("code", "")

    response = "{}".format(to_echo)

    response =  "foobar://success?code="+response 
    print(response)

#HTML SHIT
    return f'''<HTML>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Grant Access to Flutter</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    html, body {{ margin: 0; padding: 0; }}

    main {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
    }}

    #icon {{
      font-size: 96pt;
    }}

    #text {{
      padding: 2em;
      max-width: 260px;
      text-align: center;
    }}

    #button a {{
      display: inline-block;
      padding: 6px 12px;
      color: white;
      border: 1px solid rgba(27,31,35,.2);
      border-radius: 3px;
      background-image: linear-gradient(-180deg, #34d058 0%, #22863a 90%);
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
    }}

    #button a:active {{
      background-color: #279f43;
      background-image: none;
    }}
  </style>
</head>
<body>
  <main>
    <div id="icon">&#x1F3C7;</div>
    <div id="text">Press the button below to sign in using your Localtest.me account.</div>
    <div id="button"><a href="{response}">Sign in</a></div>
  </main>
</body>
</html>
'''
if __name__ == "__main__":
    app.run(port=8000)