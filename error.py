from typing import Literal, Optional
from pydantic import BaseModel, Field, PositiveInt, ValidationError

class Property(BaseModel):
    area: int
    property_type: Optional[Literal["APARTMENT", "HOUSE", "OTHERS"]] = Field(default=None, alias="property-type")
    rooms_number: Optional[int] = Field(default=None, alias="rooms-number")
    zip_code: Optional[int] = Field(default=None, alias="zip-code")
    land_area: Optional[int] = Field(default=None, alias="land-area")
    garden: Optional[bool] = None
    garden_area: Optional[int] = Field(default=None, alias="garden-area")
    equipped_kitchen: Optional[bool] = Field(default=None, alias="equipped-kitchen")
    full_address: Optional[str] = Field(default=None, alias="full-address")
    swimming_pool: Optional[bool] = Field(default=None, alias="swimming-pool")
    furnished: Optional[bool] = None
    open_fire: Optional[bool] = Field(default=None, alias="open-fire")
    terrace: Optional[bool] = None
    terrace_area: Optional[int] = Field(default=None, alias="terrace-area")
    facades_number: Optional[int] = Field(default=None, alias="facades-number")
    building_state: Optional[Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]] = Field(default=None, alias="building-state")