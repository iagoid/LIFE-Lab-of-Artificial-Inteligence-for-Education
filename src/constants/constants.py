import os

DEVELOP_MODE = True
NUM_IMAGES_USE_TRAINING = 5

HARCASCADEPATH = "models" + os.sep + "haarcascade_frontalface_default.xml"
DIRECTORY_IMAGE_PLAYER = "PlayerImages"
DIRECTORY_AUDIO_PLAYER = "PlayerAudio"
DIRECTORY_LOGS_IMAGE = "LogsImages"
DIRECTORY_CAPTURES = "Captures"
DIRECTORY_CSV_PLAYERS = DIRECTORY_IMAGE_PLAYER + os.sep + "players.csv"

DIRECTORY_LOG_FACE_REC = "LogFaceRec"

NAME_UNKNOWN_PLAYER = "UNKNOWN"

INITIAL_NUMBER_MOVEMENTS = 3

NUMBER_CONFETTI_PARTICLES = 1000

NUMBERS_MAX_ATTEMPS_IDENTIFY_PLAYER = 5

START_MESSAGES = ["Preparar...", "Memorize!"]
