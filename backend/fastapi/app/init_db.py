from database import engine
import models


def main():
    models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
