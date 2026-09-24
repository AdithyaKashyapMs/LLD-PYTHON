from transport_mode import TransportMode


class WalkMode(TransportMode):
    def eta(self):
        print("Walking will take 30 minutes")

    def directions(self):
        print("Go to left and take right")