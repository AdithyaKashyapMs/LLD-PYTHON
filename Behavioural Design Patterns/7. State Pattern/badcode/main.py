from without_pattern import TransportService, TransportMode

# Here we are using the TransportService class to get the ETA and directions for different transport modes.
# The TransportService class is tightly coupled with the TransportMode enum and it is not easy to

transport_service = TransportService(TransportMode.WALKING)
transport_service.eta()
transport_service.directions()

transport_service.set_mode(TransportMode.BIKE)
transport_service.eta()
transport_service.directions()