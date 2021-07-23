from typing import Dict, List
from typing_extensions import TypedDict

import ckan.plugins.toolkit as tk

from ckanext.search_autocomplete.utils import (
    autocomplete_datasets,
    autocomplete_categories,
    Suggestion,
)


class AutocompleteDict(TypedDict):
    datasets: List[Suggestion]
    categories: List[Suggestion]


@tk.side_effect_free
def search_autocomplete(context, data_dict) -> AutocompleteDict:
    q = tk.get_or_bust(data_dict, "q")
    words = q.lower().split()

    if not words:
        return {
            "datasets": [],
            "categories": [],
        }

    # use only first two words. Otherwise we'll mess with
    # distributions of relevant suggestions per word
    datasets = autocomplete_datasets(words)
    categories = autocomplete_categories(words)

    return {
        "datasets": datasets,
        "categories": categories,
    }
