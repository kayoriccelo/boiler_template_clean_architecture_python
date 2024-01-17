
from src.core.exceptions import UseCaseRuleException


class BaseRules:
    _exception = True
    _can = True
    _kwargs = {}

    def _get_value_in_kwargs(self, name, required=True):
        value = self._kwargs.get(value, None)

        if not value and required:
            raise Exception(f'{name} not found in {type(self).__name__}')
        
        return value

    def execute_exception(self, message):
        if self._exception:
            raise UseCaseRuleException('', message)

        return True

    def execute_callback(self, callback):
        if not self._can:
            self._can = callback()
            
        else:
            callback()
