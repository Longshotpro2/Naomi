# -*- coding: utf-8 -*-
import random
from naomi import plugin


class MeaningOfLifePlugin(plugin.SpeechHandlerPlugin):
    def intents(self):
        return {
            'MeaningOfLifeIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            "WHAT IS THE MEANING OF LIFE",
                            "WHAT IS THE ULTIMATE ANSWER TO THE ULTIMATE QUESTION OF LIFE THE UNIVERSE AND EVERYTHING"
                        ]
                    },
                    'fr-FR': {
                        'templates': [
                            "QUEL EST LE SENS DE LA VIE",
                            "QUELLE EST LA RÉPONSE ULTIME À LA QUESTION ULTIME DE VIE L'UNIVERS ET TOUT"
                        ]
                    },
                    'de-DE': {
                        'templates': [
                            "WAS IST DER SINN DES LEBENS",
                            "WAS IST DIE ULTIMATIVE ANTWORT AUF DIE ULTIMATIVE FRAGE DES LEBENS DES UNIVERSUMS UND ALLES"
                        ]
                    }
                },
                'action': self.handle
            }
        }

    def handle(self, intent, mic):
        """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        """
        _ = self.gettext
        text = intent['input']
        if("ULTIMATE" in text or "EVERYTHING" in text):
            message = self.gettext("Fourty two")
        else:
            message = random.choice([  # nosec
                _("It's nothing very complicated. Try and be nice to people, avoid eating carbohydrates, read a good book every now and then, get some walking in, and try and live together in peace and harmony with people of all creeds and nations."),
                _("Life. Don't talk to me about life.")
            ])

        mic.say(message)
