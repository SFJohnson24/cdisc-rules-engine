from typing import List, Type

from cdisc_rules_engine.config import ConfigService
from cdisc_rules_engine.dummy_models.dummy_dataset import DummyDataset
from cdisc_rules_engine.services.cache import CacheServiceInterface
from cdisc_rules_engine.services.factory_interface import FactoryInterface

from . import BaseDataService, DummyDataService, LocalDataService


class DataServiceFactory(FactoryInterface):
    _service_map = {"local": LocalDataService, "dummy": DummyDataService}

    def __init__(self, config: ConfigService, cache_service: CacheServiceInterface):
        self.config = config
        self.cache_service = cache_service

    def get_data_service(self) -> BaseDataService:
        """Get local data service"""
        return self.get_service("local", cache_service=self.cache_service)

    def get_dummy_data_service(self, data: List[DummyDataset]) -> BaseDataService:
        return self.get_service("dummy", data=data)

    @classmethod
    def register_service(cls, name: str, service: Type[BaseDataService]) -> None:
        """
        Save mapping of service name and it's implementation
        """
        if not name:
            raise ValueError("Service name must not be empty!")
        if not issubclass(service, BaseDataService):
            raise TypeError("Implementation of BaseDataService required!")
        cls._service_map[name] = service

    def get_service(self, name: str, **kwargs) -> BaseDataService:
        """Get instance of service that matches searched implementation"""
        if name in self._service_map:
            return self._service_map.get(name)(**kwargs)
        raise ValueError(f"Service name must be in  {list(self._service_map.keys())}")
