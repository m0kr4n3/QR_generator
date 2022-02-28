#!/usr/bin/python3

from flask import Flask, request, render_template, redirect, url_for
from flask_apscheduler import APScheduler
import os, qrcode, uuid

app = Flask(__name__)

scheduler = APScheduler()



def remove_qr_codes():
    for f in os.listdir("app/static/qr_codes"):
        os.remove(os.path.join("app/static/qr_codes", f))


@app.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        return redirect(url_for("generate_qr"))


@app.route("/generate_qr", methods=["GET", "POST"])
def generate_qr():
    if request.method == "GET":
        return render_template("./generate_qr.html")
    elif request.method == "POST":
        text = request.form.get("text")

        try:
            QR = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            QR.add_data(text)
            img = QR.make_image(fill_color="black", back_color="white")
            qr_path = f"static/qr_codes/{uuid.uuid4().hex}.png"
            img.save(f"app/{qr_path}")

            result = "Here's your QR code"
        except Exception as e:
            print(e)
            result = "something is going wrong"
            qr_path = None
        finally:
            return render_template(
                "./generate_qr.html", result=result, qr_path=qr_path
            )


if __name__ == "__main__":
    scheduler.add_job(
        id="Delete qr codes", func=remove_qr_codes, trigger="interval", seconds=5
    )
    scheduler.start()
    app.run(debug=True)
