from __future__ import annotations

from typing import Any, Dict, Optional


class PaginationQuery:
    def __init__(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        include: Optional[str] = None,
    ) -> None:
        self.limit = limit
        self.before = before
        self.after = after
        self.include = include

    def to_params(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.before:
            params["before"] = self.before
        if self.after:
            params["after"] = self.after
        if self.include:
            params["include"] = self.include
        return params


def expand_metadata_filters(params: Dict[str, Any], metadata: Optional[Dict[str, Any]]) -> None:
    if not metadata:
        return
    for k, v in metadata.items():
        params[f"metadata[{k}]"] = v
