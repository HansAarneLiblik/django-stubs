from typing import TypeVar, Optional, Any, Type, Dict, Union, overload, List, Iterator, Tuple, Iterable, Sized, Sequence

from django.db.models.base import Model

from django.db import models
from django.db.models import Manager
from django.db.models.sql.query import Query, RawQuery

_T = TypeVar("_T", bound=models.Model, covariant=True)

class QuerySet(Iterable[_T], Sized):
    def __init__(
        self,
        model: Optional[Type[models.Model]] = ...,
        query: Optional[Query] = ...,
        using: Optional[str] = ...,
        hints: Optional[Dict[str, models.Model]] = ...,
    ) -> None: ...
    @classmethod
    def as_manager(cls) -> Manager[Any]: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __bool__(self) -> bool: ...
    def __class_getitem__(cls, item: Type[_T]):
        pass
    @overload
    def __getitem__(self, k: int) -> _T: ...
    @overload
    def __getitem__(self, k: str) -> Any: ...
    @overload
    def __getitem__(self, k: slice) -> QuerySet[_T]: ...
    def __and__(self, other: QuerySet) -> QuerySet: ...
    def __or__(self, other: QuerySet) -> QuerySet: ...
    def iterator(self, chunk_size: int = ...) -> Iterator[_T]: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> Dict[str, Any]: ...
    def get(self, *args: Any, **kwargs: Any) -> _T: ...
    def create(self, **kwargs: Any) -> _T: ...
    def bulk_create(self, objs: Sequence[Model], batch_size: Optional[int] = ...) -> List[_T]: ...
    def get_or_create(self, defaults: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> Tuple[_T, bool]: ...
    def update_or_create(self, defaults: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> Tuple[_T, bool]: ...
    def earliest(self, *fields: Any, field_name: Optional[Any] = ...) -> _T: ...
    def latest(self, *fields: Any, field_name: Optional[Any] = ...) -> _T: ...
    def first(self) -> Optional[_T]: ...
    def last(self) -> Optional[_T]: ...
    def in_bulk(
        self, id_list: Any = ..., *, field_name: str = ...
    ) -> Union[Dict[int, models.Model], Dict[str, models.Model]]: ...
    def delete(self) -> Tuple[int, Dict[str, int]]: ...
    def update(self, **kwargs: Any) -> int: ...
    def exists(self) -> bool: ...
    def explain(self, *, format: Optional[Any] = ..., **options: Any) -> str: ...
    def raw(
        self, raw_query: str, params: Any = ..., translations: Optional[Dict[str, str]] = ..., using: None = ...
    ) -> RawQuerySet: ...
    def values(self, *fields: Any, **expressions: Any) -> QuerySet: ...
    def values_list(self, *fields: Any, flat: bool = ..., named: bool = ...) -> List[Any]: ...
    def dates(self, field_name: str, kind: str, order: str = ...) -> QuerySet: ...
    def datetimes(self, field_name: str, kind: str, order: str = ..., tzinfo: None = ...) -> QuerySet: ...
    def none(self) -> QuerySet[_T]: ...
    def all(self) -> QuerySet[_T]: ...
    def filter(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def complex_filter(self, filter_obj: Any) -> QuerySet[_T]: ...
    def count(self) -> int: ...
    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet[_T]: ...
    def intersection(self, *other_qs: Any) -> QuerySet[_T]: ...
    def difference(self, *other_qs: Any) -> QuerySet[_T]: ...
    def select_for_update(self, nowait: bool = ..., skip_locked: bool = ..., of: Tuple = ...) -> QuerySet: ...
    def select_related(self, *fields: Any) -> QuerySet[_T]: ...
    def prefetch_related(self, *lookups: Any) -> QuerySet[_T]: ...
    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def order_by(self, *field_names: Any) -> QuerySet[_T]: ...
    def distinct(self, *field_names: Any) -> QuerySet[_T]: ...
    def extra(
        self,
        select: Optional[Dict[str, Any]] = ...,
        where: Optional[List[str]] = ...,
        params: Optional[List[Any]] = ...,
        tables: Optional[List[str]] = ...,
        order_by: Optional[Sequence[str]] = ...,
        select_params: Optional[Sequence[Any]] = ...,
    ) -> QuerySet[_T]: ...
    def reverse(self) -> QuerySet[_T]: ...
    def defer(self, *fields: Any) -> QuerySet[_T]: ...
    def only(self, *fields: Any) -> QuerySet[_T]: ...
    def using(self, alias: Optional[str]) -> QuerySet[_T]: ...
    @property
    def ordered(self) -> bool: ...
    @property
    def db(self) -> str: ...
    def resolve_expression(self, *args: Any, **kwargs: Any) -> Any: ...
    # TODO: remove when django adds __class_getitem__ methods
    def __getattr__(self, item: str) -> Any: ...

class RawQuerySet(Iterable[_T], Sized):
    def __init__(
        self,
        raw_query: RawQuery,
        model: Optional[Type[models.Model]] = ...,
        query: Optional[Query] = ...,
        params: Tuple[Any] = ...,
        translations: Optional[Dict[str, str]] = ...,
        using: str = ...,
        hints: Optional[Dict[str, models.Model]] = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __bool__(self) -> bool: ...
    @overload
    def __getitem__(self, k: int) -> _T: ...
    @overload
    def __getitem__(self, k: str) -> Any: ...
    @overload
    def __getitem__(self, k: slice) -> QuerySet[_T]: ...
    @property
    def columns(self) -> List[str]: ...
    @property
    def db(self) -> str: ...
    def iterator(self) -> Iterator[_T]: ...
    @property
    def model_fields(self) -> Dict[str, str]: ...
    def prefetch_related(self, *lookups: Any) -> RawQuerySet[_T]: ...
    def resolve_model_init_order(self) -> Tuple[List[str], List[int], List[Tuple[str, int]]]: ...
    def using(self, alias: Optional[str]) -> RawQuerySet[_T]: ...
