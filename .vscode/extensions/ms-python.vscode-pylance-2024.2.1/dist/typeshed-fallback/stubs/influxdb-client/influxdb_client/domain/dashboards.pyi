from _typeshed import Incomplete

class Dashboards:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, links: Incomplete | None = None, dashboards: Incomplete | None = None) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    @property
    def dashboards(self): ...
    @dashboards.setter
    def dashboards(self, dashboards) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
