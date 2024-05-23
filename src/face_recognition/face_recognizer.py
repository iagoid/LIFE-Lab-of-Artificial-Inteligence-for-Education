#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append("../constants")
import pickle
from collections import Counter
from pathlib import Path
from cv2.typing import MatLike
import cv2
import src.constants.constants as constants

import face_recognition


class FaceRecognizer:
    def __init__(self, encodings_location: Path):
        """
        Given an unknown image, get the locations and encodings of any faces and
        compares them against the known encodings to find potential matches.
        """
        with encodings_location.open(mode="rb") as f:
            self.loaded_encodings = pickle.load(f)

    def recognize_faces(
        self,
        img: MatLike | str,
        model: str = "hog",
    ) -> str:

        # reconhecimento de imagens salva os captadas
        if type(img) is str:
            img = face_recognition.load_image_file(img)

        # redimensiona a imagem para melhorar a velocidade
        small_img = cv2.resize(img, None, fx=0.5, fy=0.5)
        input_face_locations = face_recognition.face_locations(small_img, model=model)
        input_face_encodings = face_recognition.face_encodings(
            small_img, input_face_locations
        )

        for _, unknown_encoding in zip(input_face_locations, input_face_encodings):
            name = self._recognize_face(unknown_encoding)
            if not name:
                name = constants.NAME_UNKNOWN_PLAYER
            return name

    def _recognize_face(self, unknown_encoding):
        """
        Given an unknown encoding and all known encodings, find the known
        encoding with the most matches.
        """
        boolean_matches = face_recognition.compare_faces(
            self.loaded_encodings["encodings"], unknown_encoding
        )
        votes = Counter(
            name
            for match, name in zip(boolean_matches, self.loaded_encodings["names"])
            if match
        )
        if votes:
            return votes.most_common(1)[0][0]
