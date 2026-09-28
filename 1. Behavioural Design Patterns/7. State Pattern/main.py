from bike_mode import BikeMode
from transport_service import TransportService
from walk_mode import WalkMode

transport_service = TransportService(BikeMode())
transport_service.eta()
transport_service.directions()

transport_service.set_mode(WalkMode())
transport_service.eta()
transport_service.directions()