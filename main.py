import os
import logging
from pathlib import Path
from datetime import datetime
from src import generate_qr, generate_uuid


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        uuid = generate_uuid()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        uuid_dir = os.path.join(base_dir, "assets", str(uuid))

        Path(uuid_dir).mkdir(parents=True, exist_ok=False)
        logging.info("Directory created: %s", uuid_dir)

        qr_file = os.path.join(uuid_dir, f"{uuid}.png")
        data_file = os.path.join(uuid_dir, "data.txt")

        generate_qr(uuid, qr_file)
        logging.info("QR code saved: %s", qr_file)

        with open(data_file, "w") as file:
            file.write(f"{uuid}\n{datetime.now()}")
        logging.info("Data file saved")

    except FileExistsError:
        logging.error("Directory already exists")

    except Exception as e:
        logging.error("An error occurred: %s", e)


if __name__ == "__main__":
    main()
