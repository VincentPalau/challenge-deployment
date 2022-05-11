from typing import Literal
from pydantic import BaseModel, Field, PositiveInt, Optional

class Property(BaseModel):
    area: PositiveInt
    property_type: Literal["APARTMENT", "HOUSE", "OTHERS"] = Field(..., alias="property-type")
    rooms_number: PositiveInt  = Field(..., alias="rooms-number")
    zip_code: PositiveInt  = Field(..., alias="zip-code")
    land_area: Optional[PositiveInt]  = Field(..., alias="land-area")
    garden: Optional[bool]
    garden_area: Optional[PositiveInt]  = Field(..., alias="garden-area")
    equipped_kitchen: Optional[bool] = Field(..., alias="equipped-kitchen")
    full_address: Optional[str] = Field(..., alias="full-address")
    swimming_pool: Optional[bool] = Field(..., alias="swimming-pool")
    furnished: Optional[bool]
    open_fire: Optional[bool] = Field(..., alias="open-fire")
    terrace: Optional[bool]
    terrace_area: Optional[PositiveInt] = Field(..., alias="terrace-area")
    facades_number: Optional[PositiveInt] = Field(..., alias="facades-number")
    building_state: Optional[Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]] = Field(..., alias="building-state")
