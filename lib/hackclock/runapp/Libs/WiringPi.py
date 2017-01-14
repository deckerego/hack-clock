import wiringpi

class WiringPiSingleton:
    already_setup = None

    def setup(self):
        if not WiringPiSingleton.already_setup:
            WiringPiSingleton.already_setup = True
            wiringpi.wiringPiSetupSys()
