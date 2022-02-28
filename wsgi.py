from app.main import app
from flask_apscheduler import APScheduler
from app.main import remove_qr_codes
scheduler = APScheduler()

if __name__ == "__main__":
        scheduler.add_job(
                id="Delete qr codes", func=remove_qr_codes, trigger="interval", seconds=5
        )
        scheduler.start()
        app.run()