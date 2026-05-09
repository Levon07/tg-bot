import time
from signal_engine import generate_signal


def run_bot():
    while True:
        try:
            signal = generate_signal()

            print("\n=== SIGNAL UPDATE ===")
            print(signal)

            # later we will send this to Telegram here

        except Exception as e:
            print("ERROR:", e)

        # run every 5 minutes
        time.sleep(300)


if __name__ == "__main__":
    run_bot()