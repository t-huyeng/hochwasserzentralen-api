import typing_extensions
from deutschland.hochwasserzentralen.apis.tags import TagValues
from deutschland.hochwasserzentralen.apis.tags.bundesland_api import BundeslandApi
from deutschland.hochwasserzentralen.apis.tags.pegel_api import PegelApi

TagToApi = typing_extensions.TypedDict(
    "TagToApi",
    {
        TagValues.PEGEL: PegelApi,
        TagValues.BUNDESLAND: BundeslandApi,
    },
)

tag_to_api = TagToApi(
    {
        TagValues.PEGEL: PegelApi,
        TagValues.BUNDESLAND: BundeslandApi,
    }
)
