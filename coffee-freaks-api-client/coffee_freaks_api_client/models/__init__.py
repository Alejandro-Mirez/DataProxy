""" Contains all the data models used in inputs/outputs """

from .add_coffee_file import AddCoffeeFile
from .add_roaster_file import AddRoasterFile
from .bad_request import BadRequest
from .beans import Beans
from .beans_kind import BeansKind
from .brewing_method import BrewingMethod
from .change_password_request import ChangePasswordRequest
from .coffee_kind import CoffeeKind
from .coffee_request_entity import CoffeeRequestEntity
from .coffee_result import CoffeeResult
from .coffee_result_with_roaster import CoffeeResultWithRoaster
from .data_ordering import DataOrdering
from .email_content_type import EmailContentType
from .email_result import EmailResult
from .email_status import EmailStatus
from .email_template_result import EmailTemplateResult
from .email_template_type import EmailTemplateType
from .failure_result import FailureResult
from .get_all_coffee_parameters import GetAllCoffeeParameters
from .get_all_coffee_result import GetAllCoffeeResult
from .get_all_emails_parameters import GetAllEmailsParameters
from .get_all_roaster_parameters import GetAllRoasterParameters
from .get_all_roaster_results import GetAllRoasterResults
from .get_emails_response import GetEmailsResponse
from .get_roaster_coffee_parameters import GetRoasterCoffeeParameters
from .get_roaster_coffee_result import GetRoasterCoffeeResult
from .grammage import Grammage
from .image_info_response import ImageInfoResponse
from .image_metadata import ImageMetadata
from .image_result import ImageResult
from .image_tag import ImageTag
from .invalid_field import InvalidField
from .invalid_input import InvalidInput
from .invalid_token import InvalidToken
from .login_request import LoginRequest
from .map_string import MapString
from .not_found import NotFound
from .patch_coffee_request import PatchCoffeeRequest
from .patch_roaster_request import PatchRoasterRequest
from .patch_template_request import PatchTemplateRequest
from .preview_result import PreviewResult
from .preview_template_request import PreviewTemplateRequest
from .processing import Processing
from .registration_request import RegistrationRequest
from .registration_resend_request import RegistrationResendRequest
from .replace_file import ReplaceFile
from .reset_password_input import ResetPasswordInput
from .roaster_request_entity import RoasterRequestEntity
from .roaster_result import RoasterResult
from .server_error import ServerError
from .simple_result_status import SimpleResultStatus
from .success_result import SuccessResult
from .token_result import TokenResult
from .unauthorized import Unauthorized
from .unit_type import UnitType
from .valid_token_result import ValidTokenResult

__all__ = (
    "AddCoffeeFile",
    "AddRoasterFile",
    "BadRequest",
    "Beans",
    "BeansKind",
    "BrewingMethod",
    "ChangePasswordRequest",
    "CoffeeKind",
    "CoffeeRequestEntity",
    "CoffeeResult",
    "CoffeeResultWithRoaster",
    "DataOrdering",
    "EmailContentType",
    "EmailResult",
    "EmailStatus",
    "EmailTemplateResult",
    "EmailTemplateType",
    "FailureResult",
    "GetAllCoffeeParameters",
    "GetAllCoffeeResult",
    "GetAllEmailsParameters",
    "GetAllRoasterParameters",
    "GetAllRoasterResults",
    "GetEmailsResponse",
    "GetRoasterCoffeeParameters",
    "GetRoasterCoffeeResult",
    "Grammage",
    "ImageInfoResponse",
    "ImageMetadata",
    "ImageResult",
    "ImageTag",
    "InvalidField",
    "InvalidInput",
    "InvalidToken",
    "LoginRequest",
    "MapString",
    "NotFound",
    "PatchCoffeeRequest",
    "PatchRoasterRequest",
    "PatchTemplateRequest",
    "PreviewResult",
    "PreviewTemplateRequest",
    "Processing",
    "RegistrationRequest",
    "RegistrationResendRequest",
    "ReplaceFile",
    "ResetPasswordInput",
    "RoasterRequestEntity",
    "RoasterResult",
    "ServerError",
    "SimpleResultStatus",
    "SuccessResult",
    "TokenResult",
    "Unauthorized",
    "UnitType",
    "ValidTokenResult",
)
