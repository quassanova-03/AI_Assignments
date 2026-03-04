import random
import string
from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

captcha_text = ""

def generate_captcha():
    global captcha_text

    # Generate random text
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    width = 260
    height = 100

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 42)
    except:
        font = ImageFont.load_default()

    x = 20

    for char in captcha_text:

        y = random.randint(10, 40)

        # create rotated character
        char_img = Image.new("RGBA", (60, 80), (255,255,255,0))
        char_draw = ImageDraw.Draw(char_img)

        char_draw.text((10,10), char, font=font, fill="black")

        char_img = char_img.rotate(random.randint(-30,30), expand=1)

        image.paste(char_img, (x,y), char_img)

        x += random.randint(35,45)

    # Add noise lines
    for _ in range(6):
        x1 = random.randint(0,width)
        y1 = random.randint(0,height)
        x2 = random.randint(0,width)
        y2 = random.randint(0,height)

        draw.line((x1,y1,x2,y2), fill="gray", width=2)

    # Add noise dots
    for _ in range(300):
        x = random.randint(0,width)
        y = random.randint(0,height)

        draw.point((x,y), fill="black")

    image.save("static/captcha.png")


@app.route("/", methods=["GET","POST"])
def index():

    global captcha_text

    message = ""

    if request.method == "POST":

        user = request.form["captcha"]

        if user == captcha_text:
            message = "✅ Access Granted!"
        else:
            message = "❌ Incorrect CAPTCHA. Try again."

    generate_captcha()

    return render_template("Captcha.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)